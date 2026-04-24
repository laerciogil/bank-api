from typing import Annotated

from _typeshed import Incomplete
from fastapi import Depends as Depends
from fastapi import Request as Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

from .config import settings as settings

SECRETE_KEY: Incomplete
ALGORITHM: str
ACCESS_TOKEN_EXPIRE_SECONDS: int

class AccessToken(BaseModel):
    iss: str
    sub: str
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str

class JWTToken(HTTPAuthorizationCredentials):
    scheme: str
    credentials: str
    access_token: AccessToken

def sign_jwt(user_id: str) -> dict[str, str]: ...
async def decode_jwt(token: str) -> JWTToken | None: ...

class JWTBearer(HTTPBearer):
    def __init__(self, *, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> JWTToken | None: ...

async def get_current_user(token: Annotated[JWTToken, None]) -> dict[str, int]: ...
def login_required(current_user: Annotated[dict[str, int], None]) -> dict[str, int]: ...
