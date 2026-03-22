from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_service import save_document
from pathlib import Path
import json

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/upload-doc")
def upload_document(file: UploadFile = File(...)):
    return save_document(file)

@router.get("/failed-queries")
def get_failed_queries():
    log_file = Path("data/logs/failed_queries.json")
    if not log_file.exists():
        raise HTTPException(status_code=404, detail="failed_queries.json not found")

    try:
        with log_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Invalid JSON in failed_queries.json: {e}")

    return data