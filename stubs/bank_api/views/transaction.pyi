from pydantic import AwareDatetime as AwareDatetime
from pydantic import BaseModel
from pydantic import NaiveDatetime as NaiveDatetime
from pydantic import PositiveFloat as PositiveFloat

class TransactionResponse(BaseModel):
    id: int
    account_id: int
    amount: PositiveFloat
    transaction_type: str
    created_at: AwareDatetime | NaiveDatetime
