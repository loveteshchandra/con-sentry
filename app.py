"""
FastAPI wrapper for Constitutional AI Compliance System.
Provides HTTP endpoints for health checks and evaluation.
"""
from typing import List, Tuple
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.constitution import Constitution, SimpleRetriever, DEFAULT_PRINCIPLES
from src.judge import ConstitutionalJudge
from src.metrics import calculate_compliance_score
from src.red_team import RedTeamer

app = FastAPI(
    title="Constitutional AI Compliance System",
    description="Evaluate LLM interactions against a constitutional safety framework",
    version="1.0.0"
)

# Initialize components on startup
constitution = Constitution(DEFAULT_PRINCIPLES)
retriever = SimpleRetriever(constitution)
judge = ConstitutionalJudge(retriever)
red_teamer = RedTeamer()


# Request/Response Models
class Interaction(BaseModel):
    prompt: str
    response: str


class EvaluationRequest(BaseModel):
    interactions: List[Interaction]


class VerdictResponse(BaseModel):
    prompt: str
    response: str
    score: int
    label: str
    reasoning: str


class EvaluationResponse(BaseModel):
    verdicts: List[VerdictResponse]
    compliance_score: float


class RedTeamResponse(BaseModel):
    adversarial_prompts: List[str]


# Endpoints
@app.get("/health")
async def health_check():
    """Health check endpoint for ECS."""
    return {"status": "healthy"}


@app.post("/evaluate", response_model=EvaluationResponse)
async def evaluate_interactions(request: EvaluationRequest):
    """
    Evaluate a list of prompt/response interactions against the constitution.
    Returns individual verdicts and an overall compliance score.
    """
    if not request.interactions:
        raise HTTPException(status_code=400, detail="No interactions provided")
    
    traces = []
    verdicts = []
    
    for interaction in request.interactions:
        trace = judge.evaluate(interaction.prompt, interaction.response)
        traces.append(trace)
        verdicts.append(VerdictResponse(
            prompt=interaction.prompt,
            response=interaction.response,
            score=trace.verdict.score,
            label=trace.verdict.label,
            reasoning=trace.verdict.reasoning
        ))
    
    score = calculate_compliance_score(traces)
    
    return EvaluationResponse(
        verdicts=verdicts,
        compliance_score=score
    )


@app.get("/red-team", response_model=RedTeamResponse)
async def generate_red_team_prompts():
    """Generate adversarial prompts for red teaming."""
    attacks = red_teamer.generate_attacks()
    return RedTeamResponse(adversarial_prompts=attacks)


@app.get("/")
async def root():
    """Root endpoint with API info."""
    return {
        "name": "Constitutional AI Compliance System",
        "version": "1.0.0",
        "endpoints": {
            "/health": "Health check",
            "/evaluate": "Evaluate interactions (POST)",
            "/red-team": "Generate adversarial prompts"
        }
    }
