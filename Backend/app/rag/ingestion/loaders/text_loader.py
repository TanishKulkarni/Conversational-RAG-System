from pathlib import Path
from typing import List
from langchain_core.documents import Document


def load_text_file(file_path: str) -> List[Document]:
    """
    Load a plain text file as one Document.
    """
    text = Path(file_path).read_text(encoding="utf-8")

    doc = Document(
        page_content=text,
        metadata={
            "source_file": Path(file_path).name,
            "file_type": "txt"
        }
    )

    return [doc]