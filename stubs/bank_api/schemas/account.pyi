from pydantic import BaseModel
from pydantic import PositiveFloat as PositiveFloat

class AccountRequest(BaseModel):
    user_id: int
    balance: PositiveFloat
