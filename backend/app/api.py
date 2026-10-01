from fastapi import FastAPI
from pydantic import BaseModel

from services.rag_service import answer_question


app = FastAPI(
    title="Scholar.AI API",
    description="Academic Research Assistant using RAG",
    version="1.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Scholar.AI API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    answer = answer_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }