# app/rag/ingestion/pipeline.py

from pathlib import Path
from app.rag.ingestion.loaders.universal_loader import load_documents
from app.rag.ingestion.processing.chunker import chunk_documents
from app.rag.ingestion.processing.metadata import enrich_metadata


BASE_DIR = Path(__file__).resolve().parents[3]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"


def run_text_extraction():

    print("Looking for documents in:", RAW_DATA_DIR)

    documents = load_documents(str(RAW_DATA_DIR))

    print(f"\nLoaded {len(documents)} documents/pages.")

    # Chunking
    chunked_docs = chunk_documents(documents)
    print(f"Created {len(chunked_docs)} chunks")

    # Metadata enrichment
    chunked_docs = enrich_metadata(chunked_docs)

    if chunked_docs:
        print("\nSample chunk:")
        print(chunked_docs[0].page_content)
        print("\nMetadata:", chunked_docs[0].metadata)

    return chunked_docs


if __name__ == "__main__":
    run_text_extraction()