from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.pipeline.rag_pipeline import answer_query

app = FastAPI(title="University Policy RAG API")

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    return answer_query(query.question)