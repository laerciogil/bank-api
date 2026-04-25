from typing import TYPE_CHECKING

from bank_api.database import database
from bank_api.models.account import accounts
from bank_api.views.account import AccountResponse

if TYPE_CHECKING:
    from bank_api.schemas.account import AccountRequest


class AccountService:
    async def read_all(self, limit: int, skip: int = 0) -> list[AccountResponse]:
        query = accounts.select().limit(limit).offset(skip)
        records = await database.fetch_all(query)
        return [
            AccountResponse(**record)  # type: ignore [arg-type]
            for record in records
        ]

    async def create(self, account: AccountRequest) -> AccountResponse:
        command = accounts.insert().values(**account.model_dump())
        account_id = await database.execute(command)

        query = accounts.select().where(accounts.c.id == account_id)
        record = await database.fetch_one(query)
        return AccountResponse(**record)  # type: ignore [arg-type]
