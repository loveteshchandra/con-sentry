import pytest
from src.schema import Principle, Verdict, EvaluationTrace
from src.constitution import Constitution, SimpleRetriever
from src.judge import ConstitutionalJudge
from src.metrics import calculate_compliance_score

def test_schema_validation():
    p = Principle(id="test", description="desc", weight=0.5)
    assert p.weight == 0.5
    
    v = Verdict(score=5, label="Compliant", reasoning="Good")
    assert v.score == 5

def test_judge_evaluation():
    principles = [Principle(id="safe", description="be safe", weight=1.0)]
    constitution = Constitution(principles)
    retriever = SimpleRetriever(constitution)
    judge = ConstitutionalJudge(retriever)
    
    # Test Compliant
    trace_safe = judge.evaluate("Hello", "Hi there!")
    assert trace_safe.verdict.score == 5
    assert trace_safe.verdict.label == "Compliant"
    
    # Test Violation (Mock heuristic)
    trace_unsafe = judge.evaluate("Bad prompt", "I hate you")
    assert trace_unsafe.verdict.score == 1
    assert trace_unsafe.verdict.label == "Violation"

def test_compliance_score():
    # 2 traces: one 5/5 (1.0), one 1/5 (0.0) -> Avg 0.5
    v1 = Verdict(score=5, label="C", reasoning="R")
    v2 = Verdict(score=1, label="V", reasoning="R")
    
    t1 = EvaluationTrace(input_prompt="a", model_response="b", retrieved_principles=[], verdict=v1)
    t2 = EvaluationTrace(input_prompt="c", model_response="d", retrieved_principles=[], verdict=v2)
    
    score = calculate_compliance_score([t1, t2])
    assert score == 0.5

def test_compliance_score_empty():
    assert calculate_compliance_score([]) == 0.0
