from llm_quality.core.pipeline import EvaluationPipeline
from llm_quality.core.results import EvaluationResult
from llm_quality.evaluators.keywords import KeywordEvaluator
from llm_quality.evaluators.length import ResponseLengthEvaluator


def test_pipeline_runs_single_evaluator():
    pipeline = EvaluationPipeline(
        evaluators=[ResponseLengthEvaluator(min_length=5, max_length=20)]
    )

    results = pipeline.run("Hello world")

    assert len(results) == 1
    assert isinstance(results[0], EvaluationResult)
    assert results[0].passed is True


def test_pipeline_runs_multiple_evaluators():
    pipeline = EvaluationPipeline(
        evaluators=[
            ResponseLengthEvaluator(min_length=5, max_length=20),
            ResponseLengthEvaluator(min_length=15, max_length=30),
        ]
    )

    results = pipeline.run("Hello world")

    assert len(results) == 2
    assert results[0].passed is True
    assert results[1].passed is False


def test_pipeline_combines_different_evaluators():
    pipeline = EvaluationPipeline(
        evaluators=[
            ResponseLengthEvaluator(min_length=5, max_length=50),
            KeywordEvaluator(keywords=["Python", "AI"]),
        ]
    )

    results = pipeline.run("Python is useful for AI.")

    assert len(results) == 2
    assert all(isinstance(result, EvaluationResult) for result in results)
    assert all(result.passed for result in results)


def test_pipeline_returns_empty_list_without_evaluators():
    pipeline = EvaluationPipeline(evaluators=[])

    results = pipeline.run("Hello world")

    assert results == []
