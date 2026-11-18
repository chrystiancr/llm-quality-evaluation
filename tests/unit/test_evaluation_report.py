
import pytest

from llm_quality.core.report import EvaluationReport
from llm_quality.core.results import EvaluationResult


def test_report_calculates_evaluation_totals():
    report = EvaluationReport(
        results=[
            EvaluationResult("length", True, 1.0),
            EvaluationResult("keywords", False, 0.5),
            EvaluationResult("relevance", True, 0.9),
        ]
    )

    assert report.total_evaluations == 3
    assert report.passed_evaluations == 2
    assert report.failed_evaluations == 1


def test_report_calculates_overall_score():
    report = EvaluationReport(
        results=[
            EvaluationResult("length", True, 1.0),
            EvaluationResult("keywords", False, 0.5),
            EvaluationResult("relevance", True, 0.9),
        ]
    )

    assert report.overall_score == pytest.approx(0.8)


def test_report_passes_when_all_evaluations_pass():
    report = EvaluationReport(
        results=[
            EvaluationResult("length", True, 1.0),
            EvaluationResult("keywords", True, 1.0),
        ]
    )

    assert report.passed is True


def test_report_fails_when_any_evaluation_fails():
    report = EvaluationReport(
        results=[
            EvaluationResult("length", True, 1.0),
            EvaluationResult("keywords", False, 0.5),
        ]
    )

    assert report.passed is False


def test_empty_report_has_zero_score_and_does_not_pass():
    report = EvaluationReport()

    assert report.total_evaluations == 0
    assert report.passed_evaluations == 0
    assert report.failed_evaluations == 0
    assert report.overall_score == 0.0
    assert report.passed is False
