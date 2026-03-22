from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    answer: str
    citations: list
    confidence: float
    escalation: dict | None = None