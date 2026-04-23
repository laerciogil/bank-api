import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="forbid",
        env_file_encoding="utf-8",
    )
    environment: str = "PROD"
    database_url: str = os.getenv("DATABASE_URL", "")
    auth_secrete_key: str = os.getenv(
        "AUTH_SECRETE_KEY", "mysecretkey-with-a-minimum-length-of-32-characters",
    )


settings = Settings()
