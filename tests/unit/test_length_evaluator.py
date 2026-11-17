import pytest

from llm_quality.evaluators.length import ResponseLengthEvaluator


def test_evaluator_passes_response_within_limits():
    evaluator = ResponseLengthEvaluator(min_length=5, max_length=20)

    result = evaluator.evaluate("Hello world")

    assert result.passed is True
    assert result.actual_length == 11


def test_evaluator_fails_response_below_minimum():
    evaluator = ResponseLengthEvaluator(min_length=5, max_length=20)

    result = evaluator.evaluate("Hi")

    assert result.passed is False
    assert result.actual_length == 2


def test_evaluator_fails_response_above_maximum():
    evaluator = ResponseLengthEvaluator(min_length=5, max_length=10)

    result = evaluator.evaluate("This is too long")

    assert result.passed is False
    assert result.actual_length == 16


def test_evaluator_rejects_invalid_minimum():
    with pytest.raises(ValueError):
        ResponseLengthEvaluator(min_length=-1, max_length=10)


def test_evaluator_rejects_maximum_below_minimum():
    with pytest.raises(ValueError):
        ResponseLengthEvaluator(min_length=10, max_length=5)


def test_evaluator_rejects_non_string_response():
    evaluator = ResponseLengthEvaluator()

    with pytest.raises(TypeError, match="Response must be a string."):
        evaluator.evaluate(None)
