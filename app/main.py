from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title = "MindMap+ Node Service",
    description = "API for managing nodes in the MindMap+ application",
    version = "0.1.0"
)

app.include_router(router)