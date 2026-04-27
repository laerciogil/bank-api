from fastapi import APIRouter, Depends, status

from bank_api.schemas.transaction import TransactionRequest
from bank_api.security import login_required
from bank_api.service.transaction import TransactionService
from bank_api.views.transaction import TransactionResponse

router = APIRouter(
    prefix="/transactions",
    tags=["Transaction"],
    dependencies=[Depends(login_required)],
)

transaction_service = TransactionService()

@router.post(
    "",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_transaction(transaction: TransactionRequest) -> TransactionResponse:
    return await transaction_service.create(transaction=transaction)
