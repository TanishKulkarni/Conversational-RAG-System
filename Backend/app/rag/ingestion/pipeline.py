# app/rag/ingestion/pipeline.py

from pathlib import Path
from app.rag.ingestion.loaders.universal_loader import load_documents


BASE_DIR = Path(__file__).resolve().parents[3]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"


def run_text_extraction():

    print("Looking for documents in:", RAW_DATA_DIR)

    documents = load_documents(str(RAW_DATA_DIR))

    print(f"\nLoaded {len(documents)} documents/pages.")

    if documents:
        print("\nSample content:")
        print(documents[0].page_content[:500])
        print("\nMetadata:", documents[0].metadata)

    return documents


if __name__ == "__main__":
    run_text_extraction()