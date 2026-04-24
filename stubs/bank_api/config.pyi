from _typeshed import Incomplete
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    environment: str
    database_url: str
    auth_secrete_key: str
    def __init__(self, model_config: SettingsConfigDict) -> None: ...

settings: Incomplete
