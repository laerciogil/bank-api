from _typeshed import Incomplete

from bank_api.schemas.auth import LoginRequest as LoginRequest
from bank_api.security import sign_jwt as sign_jwt
from bank_api.views.auth import LoginResponse as LoginResponse

router: Incomplete

async def login(data: LoginRequest) -> LoginResponse: ...
