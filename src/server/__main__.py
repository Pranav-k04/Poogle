import asyncio
import uvicorn
from src.server import app
from src.server.config import PORT
from fastapi.middleware.cors import CORSMiddleware

loop = asyncio.get_event_loop()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def main():
    uvicorn.run(
        "src.server.__main__:app",
        host="0.0.0.0",
        port=PORT,
        reload=True
    )

if __name__ == "__main__":
    loop.run_until_complete(main())