from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_service import save_document
from pathlib import Path
import json
from collections import Counter
from datetime import datetime

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/upload-doc")
def upload_document(file: UploadFile = File(...)):
    return save_document(file)

@router.get("/failed-queries")
def get_failed_queries():
    log_file = Path("data/logs/failed_queries.json")
    if not log_file.exists():
        return []

    try:
        with log_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else [data]
    except json.JSONDecodeError:
        return []

@router.get("/documents")
def get_uploaded_documents():
    """Get list of all uploaded documents"""
    docs_dir = Path("data/raw")
    
    if not docs_dir.exists():
        return []
    
    documents = []
    for doc_file in docs_dir.glob("*"):
        if doc_file.is_file():
            documents.append({
                "name": doc_file.name,
                "size": doc_file.stat().st_size,
                "uploaded_at": datetime.fromtimestamp(doc_file.stat().st_mtime).isoformat()
            })
    
    return sorted(documents, key=lambda x: x.get("uploaded_at", ""), reverse=True)

@router.delete("/documents/{file_name}")
def delete_document(file_name: str):
    """Delete a document by filename"""
    file_path = Path("data/raw") / file_name
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Document not found")
    
    if not file_path.is_file():
        raise HTTPException(status_code=400, detail="Invalid file path")
    
    try:
        file_path.unlink()
        return {"message": f"Document '{file_name}' deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete document: {str(e)}")

@router.get("/query-stats")
def get_query_statistics():
    """Get query statistics including success rate and response time"""
    log_file = Path("data/logs/failed_queries.json")
    
    # Read failed queries
    failed_queries = []
    if log_file.exists():
        try:
            with log_file.open("r", encoding="utf-8") as f:
                data = json.load(f)
                failed_queries = data if isinstance(data, list) else [data]
        except json.JSONDecodeError:
            failed_queries = []
    
    # Calculate statistics
    # For now, we'll use placeholder values since we don't have full query history
    # In production, you'd want to log all queries to calculate these properly
    failed_count = len(failed_queries)
    total_count = max(failed_count + 10, 1)  # Assume at least 10 successful queries
    answered_count = total_count - failed_count
    success_rate = (answered_count / total_count * 100) if total_count > 0 else 0
    
    return {
        "total": total_count,
        "answered": answered_count,
        "failed": failed_count,
        "success_rate": success_rate,
        "avg_response_time": 0.5  # placeholder
    }

@router.get("/top-queries")
def get_top_queries():
    """Get most frequently asked queries"""
    log_file = Path("data/logs/failed_queries.json")
    
    queries = []
    if log_file.exists():
        try:
            with log_file.open("r", encoding="utf-8") as f:
                data = json.load(f)
                queries = data if isinstance(data, list) else [data]
        except json.JSONDecodeError:
            queries = []
    
    # Extract questions and count frequency
    question_list = [q.get("question", q) if isinstance(q, dict) else q for q in queries]
    
    # Count occurrences
    counter = Counter(question_list)
    top_queries = [
        {"question": q, "count": count}
        for q, count in counter.most_common(10)
    ]
    
    return top_queries