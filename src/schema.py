import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class Principle(BaseModel):
    id: str
    description: str
    weight: float = Field(default=1.0, ge=0.0, le=1.0)

class Verdict(BaseModel):
    score: int = Field(..., ge=1, le=5, description="Score from 1 to 5")
    label: str
    reasoning: str

class EvaluationTrace(BaseModel):
    trace_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    input_prompt: str
    model_response: str
    retrieved_principles: List[Principle]
    verdict: Verdict
    metadata: Dict[str, Any] = Field(default_factory=dict)
