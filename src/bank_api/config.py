import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "DEV")
    database_url: str = os.getenv("DATABASE_URL", "")
    auth_secrete_key: str = os.getenv("AUTH_SECRETE_KEY", "")

    def __init__(self, model_config: SettingsConfigDict) -> None:
        super().__init__(model_config=model_config)


settings = Settings(
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="forbid",
        env_file_encoding="utf-8",
    ),
)
