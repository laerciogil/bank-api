from _typeshed import Incomplete
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment: str
    database_url: str
    auth_secret_key: str
    model_config: Incomplete

settings: Incomplete
