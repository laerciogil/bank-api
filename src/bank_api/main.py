from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .controllers import auth, root
from .database import database, engine, metadata

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await database.connect()
    metadata.create_all(engine)
    print(app.title, app.version, "started")
    yield
    await database.disconnect()

app = FastAPI(title="Bank API",
              version="0.1.0",
              description="API to manage bank accounts",
              lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(auth.router)


def run() -> None:
    uvicorn.run(app, port=8000)

if __name__ == "__main__":
    run()
