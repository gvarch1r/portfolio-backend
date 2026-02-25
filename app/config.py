from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables."""

    APP_NAME: str = "Portfolio API"
    DEBUG: bool = False
    SECRET_KEY: str = "change-me-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite+aiosqlite:///./portfolio.db"

    class Config:
        env_file = ".env"


settings = Settings()
