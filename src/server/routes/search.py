from fastapi import APIRouter
from src.server.core.query_processing import process_query

router = APIRouter(prefix="/api")

@router.get("/search")
async def search(q: str = ""):
    if not len(q):
        return {
            "error": "no input"
        }
    return process_query(q)