from fastapi import FastAPI
import logging
from src.server.routes import __all__ as ROUTES
import os

app = FastAPI()
logger = logging.getLogger("uvicorn.info")

# IDF = json.loads(open(f"IDF1.json", "r").read())
# urls = json.loads(open(f"urls.json",'r').read())
# titles = json.loads(open(f"titles.json",'r').read())


for router in ROUTES:
    app.include_router(router)

