from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from _typeshed import Incomplete
from fastapi import FastAPI

from .controllers import auth as auth
from .controllers import root as root
from .database import database as database
from .database import engine as engine
from .database import metadata as metadata

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]: ...

app: Incomplete

def run() -> None: ...
