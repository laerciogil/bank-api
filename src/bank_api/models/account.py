import sqlalchemy as sa

from bank_api.database import metadata

accounts = sa.Table(
    "account",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id"), nullable=False),
    sa.Column("balance", sa.Numeric(10, 2), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)
