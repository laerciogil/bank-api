from enum import StrEnum

import sqlalchemy as sa

from bank_api.database import metadata


class TransactionType(StrEnum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"


transactions = sa.Table(
    "transaction",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("account_id", sa.Integer, sa.ForeignKey("account.id"), nullable=False),
    sa.Column("type", sa.Enum(TransactionType), nullable=False),
    sa.Column("amount", sa.Numeric(10, 2), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)
