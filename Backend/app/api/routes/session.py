from fastapi import APIRouter
from app.services.session_service import (
    create_session,
    get_session_history,
    delete_session
)

router = APIRouter(prefix="/session", tags=["Session"])

@router.post("")
def create():
    return create_session()

@router.get("/{session_id}")
def history(session_id: str):
    return get_session_history(session_id)

@router.delete("/{session_id}")
def delete(session_id: str):
    return delete_session(session_id)