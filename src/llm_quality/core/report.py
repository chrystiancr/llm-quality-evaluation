from dataclasses import dataclass, field

from llm_quality.core.results import EvaluationResult


@dataclass
class EvaluationReport:
    """Consolidated report containing multiple evaluation results."""

    results: list[EvaluationResult] = field(default_factory=list)

    @property
    def total_evaluations(self) -> int:
        return len(self.results)

    @property
    def passed_evaluations(self) -> int:
        return sum(result.passed for result in self.results)

    @property
    def failed_evaluations(self) -> int:
        return self.total_evaluations - self.passed_evaluations

    @property
    def overall_score(self) -> float:
        if not self.results:
            return 0.0

        return sum(result.score for result in self.results) / self.total_evaluations

    @property
    def passed(self) -> bool:
        return self.failed_evaluations == 0 and self.total_evaluations > 0
