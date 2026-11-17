from llm_quality.core.pipeline import EvaluationPipeline
from llm_quality.core.report import EvaluationReport
from llm_quality.evaluators.keywords import KeywordEvaluator
from llm_quality.evaluators.length import ResponseLengthEvaluator


def test_pipeline_runs_single_evaluator():
    pipeline = EvaluationPipeline(
        evaluators=[ResponseLengthEvaluator(min_length=5, max_length=20)]
    )

    report = pipeline.run("Hello world")

    assert isinstance(report, EvaluationReport)
    assert report.total_evaluations == 1
    assert report.passed is True


def test_pipeline_runs_multiple_evaluators():
    pipeline = EvaluationPipeline(
        evaluators=[
            ResponseLengthEvaluator(min_length=5, max_length=20),
            ResponseLengthEvaluator(min_length=15, max_length=30),
        ]
    )

    report = pipeline.run("Hello world")

    assert report.total_evaluations == 2
    assert report.passed_evaluations == 1
    assert report.failed_evaluations == 1
    assert report.passed is False


def test_pipeline_combines_different_evaluators():
    pipeline = EvaluationPipeline(
        evaluators=[
            ResponseLengthEvaluator(min_length=5, max_length=50),
            KeywordEvaluator(keywords=["Python", "AI"]),
        ]
    )

    report = pipeline.run("Python is useful for AI.")

    assert report.total_evaluations == 2
    assert report.passed_evaluations == 2
    assert report.passed is True


def test_pipeline_returns_empty_report_without_evaluators():
    pipeline = EvaluationPipeline(evaluators=[])

    report = pipeline.run("Hello world")

    assert isinstance(report, EvaluationReport)
    assert report.total_evaluations == 0
    assert report.passed is False
