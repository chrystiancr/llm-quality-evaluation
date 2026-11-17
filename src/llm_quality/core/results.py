from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvaluationResult:
    """Standardized result returned by an evaluator."""

    evaluator_name: str
    passed: bool
    score: float
    details: dict[str, Any] = field(default_factory=dict)
