from typing import TYPE_CHECKING

from bank_api.database import database
from bank_api.exceptions import AccountNotFoundError, InsufficientFundsError
from bank_api.models.account import accounts
from bank_api.models.transaction import transactions
from bank_api.schemas.transaction import TransactionType
from bank_api.views.account import AccountResponse
from bank_api.views.transaction import TransactionResponse

if TYPE_CHECKING:
    from bank_api.schemas.transaction import TransactionRequest


class TransactionService:
    async def read_all(
        self,
        account_id: int,
        limit: int,
        skip: int = 0,
    ) -> list[TransactionResponse]:
        query = (
            transactions.select()
            .where(accounts.c.id == account_id)
            .limit(limit)
            .offset(skip)
        )
        transactions_list = await database.fetch_all(query)
        return [
            TransactionResponse(**transaction)  # type: ignore [arg-type]
            for transaction in transactions_list
        ]

    async def create(self, transaction: TransactionRequest) -> TransactionResponse:
        query = accounts.select().where(accounts.c.id == transaction.account_id)
        account_record = await database.fetch_one(query)
        if not account_record:
            raise AccountNotFoundError
        account = AccountResponse(**account_record)  # type: ignore [arg-type]

        if transaction.type == TransactionType.WITHDRAW:
            balance = float(account.balance) - transaction.amount
            if balance < 0:
                raise InsufficientFundsError(float(account.balance))
        elif transaction.type == TransactionType.DEPOSIT:
            balance = float(account.balance) + transaction.amount

        transaction_id = await self.__register_transaction(transaction)

        await self.__update_account_balance(transaction.account_id, balance)

        query = transactions.select().where(transactions.c.id == transaction_id)
        new_transaction = await database.fetch_one(query)
        return TransactionResponse(**new_transaction)  # type: ignore [arg-type]

    async def __register_transaction(self, transaction: TransactionRequest) -> int:
        command = transactions.insert().values(**transaction.model_dump())
        return await database.execute(command)

    async def __update_account_balance(self, account_id: int, balance: float) -> None:
        command = (
            accounts.update().where(accounts.c.id == account_id)
            .values(balance=balance)
        )
        await database.execute(command)
