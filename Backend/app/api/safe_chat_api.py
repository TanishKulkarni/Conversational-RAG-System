from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.pipeline.safe_conversational_rag import safe_chat

app = FastAPI(title="Reliable Policy Assistant")

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    return safe_chat(request.session_id, request.message)