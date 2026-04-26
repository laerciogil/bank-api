from _typeshed import Incomplete

from bank_api.security import login_required as login_required
from bank_api.service.account import AccountService as AccountService
from bank_api.service.transaction import TransactionService as TransactionService
from bank_api.views.account import AccountResponse as AccountResponse
from bank_api.views.transaction import TransactionResponse as TransactionResponse

router: Incomplete
account_service: Incomplete
transaction_service: Incomplete

async def read_accounts(limit: int, skip: int = 0) -> list[AccountResponse]: ...
async def create_account(account: AccountResponse) -> AccountResponse: ...
async def read_account_transactions(
    account_id: int, limit: int, skip: int = 0,
) -> list[TransactionResponse]: ...
