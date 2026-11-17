from dataclasses import dataclass


@dataclass
class LengthEvaluation:
    passed: bool
    actual_length: int
    min_length: int
    max_length: int


class ResponseLengthEvaluator:
    """Evaluate whether a response respects the configured length limits."""

    def __init__(self, min_length: int = 1, max_length: int = 1000):
        if min_length < 0:
            raise ValueError("Minimum length cannot be negative.")

        if max_length < min_length:
            raise ValueError("Maximum length cannot be less than minimum length.")

        self.min_length = min_length
        self.max_length = max_length

    def evaluate(self, response: str) -> LengthEvaluation:
        if not isinstance(response, str):
            raise TypeError("Response must be a string.")

        actual_length = len(response)

        return LengthEvaluation(
            passed=self.min_length <= actual_length <= self.max_length,
            actual_length=actual_length,
            min_length=self.min_length,
            max_length=self.max_length,
        )
