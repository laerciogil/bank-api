from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="forbid", env_file_encoding="utf-8",
    )

    database_url: str
    environment: str = "PROD"


settings = Settings()
