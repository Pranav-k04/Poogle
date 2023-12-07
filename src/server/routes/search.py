from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/search")
async def search():
    return {
        "hello": "there"
    }