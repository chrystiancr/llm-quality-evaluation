from llm_quality.core.evaluator import BaseEvaluator
from llm_quality.core.results import EvaluationResult


class KeywordEvaluator(BaseEvaluator):
    """Evaluate whether a response contains the expected keywords."""

    def __init__(self, keywords: list[str]):
        if not keywords:
            raise ValueError("At least one keyword must be provided.")

        if any(not keyword.strip() for keyword in keywords):
            raise ValueError("Keywords cannot be empty.")

        self.keywords = keywords

    def evaluate(self, response: str) -> EvaluationResult:
        if not isinstance(response, str):
            raise TypeError("Response must be a string.")

        normalized_response = response.casefold()

        found_keywords = [
            keyword
            for keyword in self.keywords
            if keyword.casefold() in normalized_response
        ]

        score = len(found_keywords) / len(self.keywords)

        return EvaluationResult(
            evaluator_name="keyword",
            passed=score == 1.0,
            score=score,
            details={
                "expected_keywords": self.keywords,
                "found_keywords": found_keywords,
                "missing_keywords": [
                    keyword
                    for keyword in self.keywords
                    if keyword not in found_keywords
                ],
            },
        )
