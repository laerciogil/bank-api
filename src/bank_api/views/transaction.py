from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    amount: PositiveFloat
    type: str
    created_at: AwareDatetime | NaiveDatetime
