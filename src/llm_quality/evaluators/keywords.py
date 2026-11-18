import re

from llm_quality.core.evaluator import BaseEvaluator
from llm_quality.core.results import EvaluationResult


class KeywordEvaluator(BaseEvaluator):
    """Evaluate whether a response contains the expected keywords."""

    def __init__(self, keywords: list[str]):
        if not keywords:
            raise ValueError("At least one keyword must be provided.")

        if not all(isinstance(keyword, str) for keyword in keywords):
            raise TypeError("All keywords must be strings.")

        normalized_keywords = [keyword.strip() for keyword in keywords]

        if any(not keyword for keyword in normalized_keywords):
            raise ValueError("Keywords cannot be empty.")

        if len(set(keyword.casefold() for keyword in normalized_keywords)) != len(
            normalized_keywords
        ):
            raise ValueError("Keywords must be unique.")

        self.keywords = normalized_keywords

    def evaluate(self, response: str) -> EvaluationResult:
        if not isinstance(response, str):
            raise TypeError("Response must be a string.")

        found_keywords = [
            keyword
            for keyword in self.keywords
            if re.search(
                rf"(?<!\w){re.escape(keyword)}(?!\w)",
                response,
                flags=re.IGNORECASE,
            )
        ]

        missing_keywords = [
            keyword
            for keyword in self.keywords
            if keyword not in found_keywords
        ]

        score = len(found_keywords) / len(self.keywords)

        return EvaluationResult(
            evaluator_name="keyword",
            passed=score == 1.0,
            score=score,
            details={
                "expected_keywords": self.keywords.copy(),
                "found_keywords": found_keywords,
                "missing_keywords": missing_keywords,
            },
        )
