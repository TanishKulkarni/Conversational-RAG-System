from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_policy_text_splitter():
    """
    Configure splitter optimized for policy documents.
    """

    return RecursiveCharacterTextSplitter(
        chunk_size=1000,        # ~500–1000 tokens
        chunk_overlap=150,      # overlap for context continuity
        separators=[
            "\n\n",             # paragraph
            "\n",               # line break
            ". ",               # sentences
            " ",                # words
            ""
        ]
    )


def chunk_documents(documents: List[Document]) -> List[Document]:
    """
    Split documents into smaller chunks while preserving metadata.
    """

    splitter = get_policy_text_splitter()

    chunked_docs = splitter.split_documents(documents)

    # Add chunk-specific metadata
    for i, doc in enumerate(chunked_docs):
        doc.metadata["chunk_id"] = i

    return chunked_docs