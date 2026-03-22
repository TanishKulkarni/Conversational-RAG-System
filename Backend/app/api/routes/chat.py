from fastapi import APIRouter
from app.api.schemas.chat import ChatRequest
from app.services.chat_service import process_chat

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("")
def chat_endpoint(request: ChatRequest):
    return process_chat(request.session_id, request.message)