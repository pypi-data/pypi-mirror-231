from __future__ import annotations

import json
import re
from typing import TYPE_CHECKING, Any, Callable

from .._metrics import bleu
from ..base.eval import BaseEvaluator, BaseOpenAIEvaluator
from ..errors import InvalidParameterError

if TYPE_CHECKING:
    from numbers import Real
    from pathlib import Path

    from .._typing import DataItemType, DatasetFormat, LoggingMode


class QaOpenAIEvaluator(BaseOpenAIEvaluator):
    """Evaluator for question-answering via OpenAI.

    This evaluator utilizes the ability of OpenAI models to tell the quality of a
    response from the following aspects:

    - **Accuracy**: Using the reference answer as the ground truth, does the response
      include factually incorrect information?
    - **Completeness**: Compared with the reference answer, is the response missing
      details?
    - **Clarity**: Is the response well-organized and clearly presented? If accuracy
      and completeness is poor, clarity should also be considered poor.

    Parameters
    ----------
    dataset : str or pathlib.Path
        The absolute path to the evaluation dataset.
    save_path : str or pathlib.Path
        The absolute path to the save location. This path may or may not exist, and if
        it exists, its file contents will be treated as a (partially) written result.
        Whether to overwrite the existing results or to build on them depend on
        ``overwrite`` when using the :meth:`QaOpenAIEvaluator.evaluate` method.
    openai_config : str or pathlib.Path
        The absolute path to the OpenAI configuration file.
    info_func : Callable
        The function that extracts the question, actual answer, and expected answer of
        a data item. The input parameter should be a :class:`pandas.Series`, a list, or
        a dictionary, depending on ``fmt`` and the specific type of each data item. The
        output should be a tuple of three strings, respectively the question, the actual
        answer to that question, and the expected answer of that question. See the notes
        for examples.
    fmt : {"jsonl", "json", "csv"}, default="jsonl"
        The format of ``dataset``.
    domain : str, optional
        The domain of knowledge. ChatGPT will be prompted to know that your question,
        answer, and reference answer are "in {domain}". If ``None``, then this
        information will not be given to ChatGPT.
    aspects : list of str, optional
        The aspects to evaluate. If ``None``, evalute accuracy, completeness, and
        clarity. If there is any string other than "accuracy", "completeness", and
        "clarity", then they have to be specified in ``aspect_descriptions``.
    aspect_descriptions : dict, optional
        An optional dictionary mapping aspects to their descriptions. "accuracy",
        "completeness", and "clarity" have default descriptions but can also be
        overridden by this parameter. Any other aspect, if used in ``aspects``, must
        exist as a key here.
    n_iter : int, default=3
        The number of iterations for each data item. The mean of the scores for each
        data item will be taken as the final score.
    timeout : float, default=60
        The timeout in seconds. This is not the OpenAI timeout, but the timeout for
        cancelling the worker tasks.
    model : str, default="gpt-3.5-turbo"
        The ID of the model to use, must be one of the available OpenAI models that
        support the ChatCompletion API. See also
        https://platform.openai.com/docs/models/model-endpoint-compatibility
    logging_mode : {"all", "failed", "none"}, default="all"
        The logging mode, whether to save the logs of all items, or only of failed
        items, or save no log.
    verbose : int, default=0
        The verbosity level of the processing. For negative levels, only a progress bar
        will be displayed. For level 0, the errored items will also be displayed. For
        positive levels, the all items will be displayed, and the verbosity level
        determines the number of lines to display for the message of each item.

    Notes
    -----
    Here are some examples of ``info_func``:

    Assume that ``dataset`` is in ``.jsonl`` format and each line is of the following
    form: ``{{"instruction": "xxx", "input": "xxx", "output": "xxx", "history": [],
    "response": "xxx"}}``. Then ``info_func`` can be defined as follows:

    .. code-block:: python

        def info_func(data_item: dict) -> tuple[str, str, str]:
            question = data_item["instruction"] + "\\n" + data_item["input"]
            actual = data_item["response"]
            expected = data_item["output"]
            return question, actual, expected

    Now assume that ``dataset`` is in ``.csv`` format with columns "question",
    "answer", and "response". Then ``info_func`` can be defined as follows:

    .. code-block:: python

        def info_func(data_item: pandas.Series) -> tuple[str, str, str]:
            question, answer, response = data_item[["question", "answer", "response"]]
            return question, response, answer
    """

    _pattern = re.compile(r"```[a-z]*\n(.+)\n```")

    def __init__(
        self,
        dataset: str | Path,
        save_path: str | Path,
        openai_config: str | Path,
        info_func: Callable[[DataItemType], tuple[str, str, str]],
        *,
        fmt: DatasetFormat = "jsonl",
        domain: str | None = None,
        aspects: list[str] | None = None,
        aspect_descriptions: dict[str, str] | None = None,
        n_iter: int = 3,
        timeout: float = 60,
        model: str = "gpt-3.5-turbo",
        logging_mode: LoggingMode = "all",
        verbose: int = 0,
    ) -> None:
        self.info_func = info_func
        self.domain = domain

        # Determine the aspects to evaluate on
        avail_aspects: list[str] = ["accuracy", "completeness", "clarity"]
        self.aspects = avail_aspects if aspects is None else aspects
        self.aspect_descriptions = {
            "accuracy": (
                "Using the reference answer as the ground truth, does my answer "
                "include factually incorrect information?"
            ),
            "completeness": (
                "Compared with the reference answer, is my answer missing details?"
            ),
            "clarity": (
                "Is my answer well-organized and clearly presented? If accuracy and "
                "completeness is bad, clarity should also be bad."
            ),
        }
        if aspect_descriptions is not None:
            self.aspect_descriptions.update(aspect_descriptions)

        # Validate the arguments
        if not callable(self.info_func):
            raise InvalidParameterError(
                "info_func", actual=self.info_func, reason="must be a callable"
            )
        if not isinstance(self.aspects, list):
            raise InvalidParameterError(
                "aspects", actual=self.aspects, reason="must be a list"
            )
        if (
            any(subject not in self.aspect_descriptions for subject in self.aspects)
            or len(self.aspects) != len(set(self.aspects))
            or len(self.aspects) == 0
        ):
            raise InvalidParameterError(
                "aspects",
                actual=self.aspects,
                reason=(
                    "must be a list of non-duplicated aspects among "
                    f"{list(self.aspect_descriptions)}"
                ),
            )

        # Set the subject explanations
        self._explanations = [
            f"{subject}: {self.aspect_descriptions[subject]}"
            for subject in self.aspects
        ]
        self._domain = "" if self.domain is None else f" in {self.domain}"

        # Inherit from parent
        super().__init__(
            dataset=dataset,
            save_path=save_path,
            subjects=self.aspects,
            openai_config=openai_config,
            fmt=fmt,
            n_iter=n_iter,
            agg_method="mean",
            timeout=timeout,
            model=model,
            logging_mode=logging_mode,
            verbose=verbose,
        )

    def _prompt(self, data_item: DataItemType) -> tuple[str, str]:
        """:meta private:"""
        question, actual, expected = self.info_func(data_item)
        explanation_expr = "\n".join(
            [
                f"{i + 1}. {explanation}"
                for i, explanation in enumerate(self._explanations)
            ]
        )
        return (
            "You are a professional, impartial, and strict scorer. You will be given "
            "a question, a pending scored answer, and a reference answer "
            f"{self._domain}. Please rate the pending scored answer based on the "
            f"reference answer in the following aspects:\n{explanation_expr}\n\nEach "
            "score should be from 1 to 5. Your rating should be strict enough, and do "
            "not easily give full scores. In your response, you should only include a "
            "JSON object, with keys being the aspects and values being the scores. Do "
            "not include any additional information or explanation.",
            f"### Question\n```\n{question}\n```\n\n### Reference answer\n```\n"
            f"{expected}\n```\n\n### Pending scored answer\n```\n{actual}\n```",
        )

    def _extract_scores(
        self, reply: str, data_item: DataItemType
    ) -> Real | dict[Any, Real]:
        """:meta private:"""
        scores: dict[str, Real]
        try:
            scores = {
                subject.lower(): score for subject, score in json.loads(reply).items()
            }

        # Try to search for a code block in the reply; if errored, leave as is
        except:
            match = re.search(self._pattern, reply)
            assert match is not None, "backup pattern matching failed."
            scores = {
                subject.lower(): score
                for subject, score in json.loads(match.group(1)).items()
            }
        return scores


class QaMetricEvaluator(BaseEvaluator):
    """Evaluator for question-answering via common metrics.

    This evaluator supports using the following metric to compare the actual response
    with the reference answer:

    - `BLEU-k <https://en.wikipedia.org/wiki/BLEU>`_ (BiLingual Evaluation Understudy)

    Parameters
    ----------
    dataset : str or pathlib.Path
        The absolute path to the evaluation dataset.
    save_path : str or pathlib.Path
        The absolute path to the save location. This path may or may not exist, and if
        it exists, its file contents will be treated as a (partially) written result.
        Whether to overwrite the existing results or to build on them depend on
        ``overwrite`` when using the :meth:`QaMetricEvaluator.evaluate` method.
    info_func : Callable
        The function that extracts the question, actual answer, and expected answer of
        a data item. The input parameter should be a :class:`pandas.Series`, a list, or
        a dictionary, depending on ``fmt`` and the specific type of each data item. The
        output should be a tuple of three strings, respectively the question, the actual
        answer to that question, and the expected answer of that question. See the notes
        for examples.
    fmt : {"jsonl", "json", "csv"}, default="jsonl"
        The format of ``dataset``.
    bleu_k : list of int or None
        The list of k-values used for BLEU-k. Must be positive. If ``None``, use k-
        values 1 to 4.
    logging_mode : {"all", "failed", "none"}, default="all"
        The logging mode, whether to save the logs of all items, or only of failed
        items, or save no log.
    verbose : int, default=0
        The verbosity level of the processing. For negative levels, only a progress bar
        will be displayed. For level 0, the errored items will also be displayed. For
        positive levels, the all items will be displayed, and the verbosity level
        determines the number of lines to display for the message of each item.

    Notes
    -----
    Here are some examples of ``info_func``:

    Assume that ``dataset`` is in ``.jsonl`` format and each line is of the following
    form: ``{{"instruction": "xxx", "input": "xxx", "output": "xxx", "history": [],
    "response": "xxx"}}``. Then ``info_func`` can be defined as follows:

    .. code-block:: python

        def info_func(data_item: dict) -> tuple[str, str, str]:
            question = data_item["instruction"] + "\\n" + data_item["input"]
            actual = data_item["response"]
            expected = data_item["output"]
            return question, actual, expected

    Now assume that ``dataset`` is in ``.csv`` format with columns "question",
    "answer", and "response". Then ``info_func`` can be defined as follows:

    .. code-block:: python

        def info_func(data_item: pandas.Series) -> tuple[str, str, str]:
            question, answer, response = data_item[["question", "answer", "response"]]
            return question, response, answer
    """

    def __init__(
        self,
        dataset: str | Path,
        save_path: str | Path,
        info_func: Callable[[DataItemType], tuple[str, str, str]],
        *,
        fmt: DatasetFormat = "jsonl",
        bleu_k: list[int] | None = None,
        logging_mode: LoggingMode = "all",
        verbose: int = 0,
    ) -> None:
        self.info_func = info_func
        self.bleu_k = [1, 2, 3, 4] if bleu_k is None else bleu_k

        # Validate the arguments
        if not isinstance(self.bleu_k, list) or any(
            not isinstance(k, int) or k <= 0 for k in self.bleu_k
        ):
            raise InvalidParameterError(
                "bleu_k",
                actual=self.bleu_k,
                reason="must be a list of positive integers",
            )

        # Inherit from parent
        super().__init__(
            dataset=dataset,
            save_path=save_path,
            subjects=[f"BLEU-{k}" for k in self.bleu_k],
            fmt=fmt,
            workers=1,
            n_iter=1,
            agg_method=None,
            logging_mode=logging_mode,
            verbose=verbose,
        )

    def _get_score(self, data_item: DataItemType, **kwargs) -> Real | dict[Any, Real]:
        """:meta private:"""
        _, actual, expected = self.info_func(data_item)
        scores = {}

        # Compute the desired BLEU scores
        for k, bleu_score in zip(self.bleu_k, bleu(actual, expected, self.bleu_k)):
            scores[f"BLEU-{k}"] = bleu_score

        # mypy not working with numbers.Real
        return scores  # type: ignore[return-value]

    async def _aget_score(
        self, data_item: DataItemType, **kwargs
    ) -> Real | dict[Any, Real]:
        """:meta private:"""
        return self._get_score(data_item, **kwargs)
