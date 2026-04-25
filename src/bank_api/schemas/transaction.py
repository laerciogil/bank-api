from enum import StrEnum

from pydantic import BaseModel, PositiveFloat


class TransactionType(StrEnum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"

class TransactionRequest(BaseModel):
    account_id: int
    type: TransactionType
    amount: PositiveFloat

    class Config:
        use_enum_values = True
