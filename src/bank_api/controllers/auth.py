from fastapi import APIRouter

from bank_api.schemas.auth import LoginRequest
from bank_api.security import sign_jwt
from bank_api.views.auth import LoginResponse

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest) -> LoginResponse:
    response = sign_jwt(user_id=str(data.user_id))
    return LoginResponse(**response)
