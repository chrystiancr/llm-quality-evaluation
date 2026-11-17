from llm_quality.core.evaluator import BaseEvaluator
from llm_quality.core.results import EvaluationResult


class ResponseLengthEvaluator(BaseEvaluator):
    """Evaluate whether a response respects configured length limits."""

    def __init__(self, min_length: int = 1, max_length: int = 1000):
        if min_length < 0:
            raise ValueError("Minimum length cannot be negative.")

        if max_length < min_length:
            raise ValueError("Maximum length cannot be less than minimum length.")

        self.min_length = min_length
        self.max_length = max_length

    def evaluate(self, response: str) -> EvaluationResult:
        if not isinstance(response, str):
            raise TypeError("Response must be a string.")

        actual_length = len(response)
        passed = self.min_length <= actual_length <= self.max_length

        return EvaluationResult(
            evaluator_name="response_length",
            passed=passed,
            score=1.0 if passed else 0.0,
            details={
                "actual_length": actual_length,
                "min_length": self.min_length,
                "max_length": self.max_length,
            },
        )
