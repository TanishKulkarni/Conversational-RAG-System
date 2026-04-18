from typing import List
from langchain_core.documents import Document

from app.rag.generation.llm import get_llm
from app.rag.generation.prompt import RAG_PROMPT

def format_context(docs: List[Document]) -> str:
    """
    Combine retrieved chunks into a context string with citations.
    """

    context_parts = []

    for doc in docs[:3]:
        source = doc.metadata.get("document_name", "Unknown")
        section = doc.metadata.get("section_title", "Unknown section")
        page = doc.metadata.get("page_number", "N/A")
        content = doc.page_content[:1200]

        context_parts.append(
            f"[Source: {source} | Section: {section} | Page: {page}]\n{content}"
        )
    return "\n\n".join(context_parts)

def generate_answer(question: str, docs: List[Document]) -> str:
    """
    Generate answer using local LLM and retrieved context.
    """
    llm = get_llm()
    context = format_context(docs)
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)
    return response.content