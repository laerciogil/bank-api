from pydantic import AwareDatetime as AwareDatetime
from pydantic import BaseModel
from pydantic import NaiveDatetime as NaiveDatetime

class AccountResponse(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: AwareDatetime | NaiveDatetime
