from abc import ABC, abstractmethod

from llm_quality.core.results import EvaluationResult


class BaseEvaluator(ABC):
    """Base contract for all evaluation components."""

    @abstractmethod
    def evaluate(self, response: str) -> EvaluationResult:
        """Evaluate a model response and return a standardized result."""
        raise NotImplementedError
