from pathlib import Path
from app.rag.ingestion.pipeline import run_embedding_pipeline

UPLOAD_DIR = Path("data/raw")

def save_document(file):
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    path = UPLOAD_DIR / file.filename

    with open(path, "wb") as f:
        f.write(file.file.read())

    # Re-Index after upload
    run_embedding_pipeline()

    return {"filename": file.filename}