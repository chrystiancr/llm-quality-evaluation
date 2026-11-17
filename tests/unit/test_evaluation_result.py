from llm_quality.core.results import EvaluationResult


def test_evaluation_result_creates_valid_instance():
    result = EvaluationResult(
        evaluator_name="response_length",
        passed=True,
        score=1.0,
        details={"actual_length": 50},
    )

    assert result.evaluator_name == "response_length"
    assert result.passed is True
    assert result.score == 1.0
    assert result.details == {"actual_length": 50}


def test_evaluation_result_uses_empty_details_by_default():
    result = EvaluationResult(
        evaluator_name="response_length",
        passed=True,
        score=1.0,
    )

    assert result.details == {}


def test_evaluation_results_do_not_share_details():
    first = EvaluationResult(
        evaluator_name="first",
        passed=True,
        score=1.0,
    )

    second = EvaluationResult(
        evaluator_name="second",
        passed=True,
        score=0.8,
    )

    first.details["message"] = "First result"

    assert "message" not in second.details
