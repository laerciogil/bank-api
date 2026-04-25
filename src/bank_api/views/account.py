from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat


class AccountResponse(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: AwareDatetime | NaiveDatetime

class TransactionResponse(BaseModel):
    id: int
    account_id: int
    amount: PositiveFloat
    transaction_type: str
    created_at: AwareDatetime | NaiveDatetime
