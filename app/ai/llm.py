"""LLM client for OpenAI API."""

from openai import AsyncOpenAI

from app.config import settings

_client: AsyncOpenAI | None = None


def get_openai_client() -> AsyncOpenAI | None:
    """Get OpenAI client if API key is configured."""
    global _client
    if not settings.OPENAI_API_KEY:
        return None
    if _client is None:
        _client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    return _client


async def chat(messages: list[dict[str, str]], model: str | None = None) -> str:
    """
    Send messages to LLM and return response.
    Returns error message if API key is not configured.
    """
    client = get_openai_client()
    if not client:
        return "Ошибка: OPENAI_API_KEY не задан в .env. Добавьте ключ для работы с AI."

    model = model or settings.OPENAI_MODEL
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content or ""

