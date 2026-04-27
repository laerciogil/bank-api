from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .controllers import account, auth, root, transaction
from .database import database, engine, metadata
from .exceptions import AccountNotFoundError, BusinessError

if TYPE_CHECKING:
    from collections.abc import AsyncIterator


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await database.connect()
    metadata.create_all(engine)
    print(app.title, app.version, "started")
    yield
    await database.disconnect()


app = FastAPI(
    title="Bank API",
    version="0.1.0",
    description="API to manage bank accounts",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(auth.router)
app.include_router(account.router)
app.include_router(transaction.router)

@app.exception_handler(AccountNotFoundError)
async def account_not_found_error_handler(
    request: Request, exc: AccountNotFoundError) -> JSONResponse:
    print(request.headers, str(exc))
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Account not found"},
    )

@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError) -> JSONResponse:
    print(request.headers, str(exc))
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": str(exc)},
    )

def run() -> None:
    uvicorn.run(app, port=8000, host="0.0.0.0")  # noqa: S104


if __name__ == "__main__":
    run()
