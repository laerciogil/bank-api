import sqlalchemy as sa

from bank_api.database import metadata

users = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(100), nullable=False),
    sa.Column("email", sa.String(100), nullable=False),
    sa.Column("password", sa.String(50), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)
