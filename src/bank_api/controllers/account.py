from fastapi import APIRouter, Depends, status

from bank_api.schemas.account import AccountRequest
from bank_api.security import login_required
from bank_api.service.account import AccountService
from bank_api.service.transaction import TransactionService
from bank_api.views.account import AccountResponse
from bank_api.views.transaction import TransactionResponse

router = APIRouter(
    prefix="/accounts",
    tags=["Account"],
    dependencies=[Depends(login_required)],
)

account_service = AccountService()
transaction_service = TransactionService()


@router.get("", response_model=list[AccountResponse], status_code=status.HTTP_200_OK)
async def read_accounts(limit: int, skip: int = 0) -> list[AccountResponse]:
    return await account_service.read_all(limit=limit, skip=skip)


@router.post("", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def create_account(account: AccountRequest) -> AccountResponse:
    return await account_service.create(account=account)


@router.get(
    "/{account_id}/transactions",
    response_model=list[TransactionResponse],
    status_code=status.HTTP_200_OK,
)
async def read_account_transactions(
    account_id: int, limit: int, skip: int = 0,
) -> list[TransactionResponse]:
    return await transaction_service.read_all(
        account_id=account_id, limit=limit, skip=skip,
    )
