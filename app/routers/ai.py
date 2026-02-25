from typing import Annotated

from fastapi import APIRouter, Depends

from app.ai.llm import chat as llm_chat
from app.ai.rag import ask as rag_ask
from app.auth import get_current_user
from app.models.user import User
from app.schemas.ai import AskRequest, AskResponse, ChatRequest, ChatResponse

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    request: ChatRequest,
    current_user: Annotated[User, Depends(get_current_user)],
):
    """Простой чат с LLM (требуется OPENAI_API_KEY в .env)."""
    response = await llm_chat([
        {"role": "user", "content": request.message},
    ])
    return ChatResponse(response=response)


@router.post("/ask", response_model=AskResponse)
async def ask_endpoint(
    request: AskRequest,
    current_user: Annotated[User, Depends(get_current_user)],
):
    """RAG: вопрос по документации проекта (требуется OPENAI_API_KEY)."""
    answer = await rag_ask(request.question)
    return AskResponse(answer=answer)
