from pydantic import AwareDatetime, BaseModel, NaiveDatetime


class AccountResponse(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: AwareDatetime | NaiveDatetime
