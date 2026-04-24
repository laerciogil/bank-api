import time
from typing import Annotated
from uuid import uuid4

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

from .config import settings

SECRETE_KEY = settings.auth_secrete_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 3600


class AccessToken(BaseModel):
    iss: str
    sub: str
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str


class JWTToken(HTTPAuthorizationCredentials):
    scheme: str = "Bearer"
    credentials: str
    access_token: AccessToken


def sign_jwt(user_id: str) -> dict[str, str]:
    now = time.time()
    payload = {
        "iss": "bank-api",
        "sub": user_id,
        "aud": "bank-api-users",
        "exp": now + ACCESS_TOKEN_EXPIRE_SECONDS,
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }
    token = jwt.encode(payload, SECRETE_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}


async def decode_jwt(token: str) -> JWTToken | None:
    try:
        payload = jwt.decode(token, SECRETE_KEY, algorithms=[ALGORITHM])
        _token = JWTToken(credentials=token, access_token=AccessToken(**payload))
        return _token if _token.access_token.exp > time.time() else None
    except jwt.PyJWTError as e:
        print(f"Error decoding JWT: {e}")
        return None


class JWTBearer(HTTPBearer):
    def __init__(self, *, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> JWTToken | None:
        authorization = request.headers.get("Authorization", "")
        scheme, _, credentials = authorization.partition(" ")

        if credentials:
            if not scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication scheme",
                )
            payload = await decode_jwt(credentials)
            if not payload:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired token",
                )
            return payload
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization code",
        )


async def get_current_user(
    token: Annotated[JWTToken, Depends(JWTBearer())],
) -> dict[str, int]:
    return {"user_id": int(token.access_token.sub)}


def login_required(
    current_user: Annotated[dict[str, int], Depends(get_current_user)],
) -> dict[str, int]:
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )
    return current_user
