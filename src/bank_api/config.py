import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "DEV")
    database_url: str = os.getenv("DATABASE_URL", "")
    auth_secret_key: str = os.getenv("AUTH_SECRET_KEY", "")
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="forbid",
        env_file_encoding="utf-8",
    )


settings = Settings()

