"""RAG: simple keyword search + LLM context."""

from app.ai.llm import chat, get_openai_client

# Sample documents about the project
SAMPLE_DOCS = [
    "Portfolio API — REST API на FastAPI с авторизацией JWT и CRUD для задач.",
    "Эндпоинты: POST /api/v1/auth/register, POST /api/v1/auth/login для авторизации.",
    "Задачи: GET, POST, PATCH, DELETE /api/v1/tasks. Требуется JWT токен.",
    "Стек: Python 3.11+, FastAPI, SQLAlchemy, SQLite/PostgreSQL, Docker.",
    "Запуск: uvicorn app.main:app --reload или docker compose up.",
    "Документация API доступна по /docs (Swagger) и /redoc.",
]


def _search_docs(question: str, top_k: int = 3) -> str:
    """Simple keyword-based search (без внешних зависимостей для embeddings)."""
    q_lower = question.lower()
    words = set(w for w in q_lower.split() if len(w) > 2)
    scored = []
    for doc in SAMPLE_DOCS:
        doc_lower = doc.lower()
        score = sum(1 for w in words if w in doc_lower)
        if score > 0:
            scored.append((score, doc))
    scored.sort(key=lambda x: -x[0])
    return "\n".join(d[1] for d in scored[:top_k]) or "\n".join(SAMPLE_DOCS[:2])


async def ask(question: str) -> str:
    """RAG: find relevant docs, then ask LLM with context."""
    if not get_openai_client():
        return "Ошибка: OPENAI_API_KEY не задан в .env."

    try:
        context = _search_docs(question)
        system = """Ты помощник по API проекта Portfolio. Отвечай кратко на основе контекста.
Если в контексте нет ответа — скажи об этом."""
        user = f"Контекст:\n{context}\n\nВопрос: {question}"
        return await chat([
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ])
    except Exception as e:
        return f"Ошибка RAG: {e}"
