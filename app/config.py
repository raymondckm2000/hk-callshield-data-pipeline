from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    DB_PATH: str = "./app.db"

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()


settings = get_settings()
