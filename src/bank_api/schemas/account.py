from pydantic import BaseModel, PositiveFloat


class AccountRequest(BaseModel):
    user_id: int
    balance: PositiveFloat
