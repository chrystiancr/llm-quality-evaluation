import pytest

from llm_quality.core.results import EvaluationResult
from llm_quality.evaluators.keywords import KeywordEvaluator


def test_keyword_evaluator_passes_when_all_keywords_are_found():
    evaluator = KeywordEvaluator(
        keywords=["Python", "Machine Learning", "AI"]
    )

    result = evaluator.evaluate(
        "Python is widely used in Machine Learning and AI."
    )

    assert isinstance(result, EvaluationResult)
    assert result.passed is True
    assert result.score == 1.0
    assert result.details["missing_keywords"] == []


def test_keyword_evaluator_returns_partial_score():
    evaluator = KeywordEvaluator(
        keywords=["Python", "Java", "AI"]
    )

    result = evaluator.evaluate("Python and AI are useful.")

    assert result.passed is False
    assert result.score == pytest.approx(2 / 3)
    assert result.details["found_keywords"] == ["Python", "AI"]
    assert result.details["missing_keywords"] == ["Java"]


def test_keyword_evaluator_is_case_insensitive():
    evaluator = KeywordEvaluator(keywords=["PYTHON", "AI"])

    result = evaluator.evaluate("Python is useful for ai.")

    assert result.passed is True
    assert result.score == 1.0


def test_keyword_evaluator_does_not_match_partial_words():
    evaluator = KeywordEvaluator(keywords=["AI"])

    result = evaluator.evaluate("Training is important.")

    assert result.passed is False
    assert result.score == 0.0
    assert result.details["found_keywords"] == []
    assert result.details["missing_keywords"] == ["AI"]


def test_keyword_evaluator_matches_keywords_with_punctuation():
    evaluator = KeywordEvaluator(keywords=["AI", "Python"])

    result = evaluator.evaluate("AI, Python, and automation.")

    assert result.passed is True
    assert result.score == 1.0


def test_keyword_evaluator_rejects_empty_keyword_list():
    with pytest.raises(ValueError):
        KeywordEvaluator(keywords=[])


def test_keyword_evaluator_rejects_blank_keywords():
    with pytest.raises(ValueError):
        KeywordEvaluator(keywords=["Python", "   "])


def test_keyword_evaluator_rejects_non_string_response():
    evaluator = KeywordEvaluator(keywords=["Python"])

    with pytest.raises(TypeError, match="Response must be a string."):
        evaluator.evaluate(None)
