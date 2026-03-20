from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.pipeline.conversational_rag import chat

app = FastAPI(title="Conversational Policy Assistant")

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    return chat(request.session_id, request.message)