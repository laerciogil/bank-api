from fastapi import APIRouter

router = APIRouter(tags=["Index"])


@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to the Bank API"}
