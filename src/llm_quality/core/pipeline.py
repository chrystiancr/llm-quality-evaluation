from llm_quality.core.evaluator import BaseEvaluator
from llm_quality.core.report import EvaluationReport


class EvaluationPipeline:
    """Execute multiple evaluators and generate a consolidated report."""

    def __init__(self, evaluators: list[BaseEvaluator]):
        self.evaluators = evaluators

    def run(self, response: str) -> EvaluationReport:
        results = [
            evaluator.evaluate(response)
            for evaluator in self.evaluators
        ]

        return EvaluationReport(results=results)
