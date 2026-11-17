from llm_quality.core.evaluator import BaseEvaluator
from llm_quality.core.results import EvaluationResult


class EvaluationPipeline:
    """Execute multiple evaluators against the same response."""

    def __init__(self, evaluators: list[BaseEvaluator]):
        self.evaluators = evaluators

    def run(self, response: str) -> list[EvaluationResult]:
        return [
            evaluator.evaluate(response)
            for evaluator in self.evaluators
        ]
