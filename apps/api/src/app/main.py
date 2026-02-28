from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.pipeline import router as pipeline_router

app = FastAPI(title="Medical AI Agent (Dental RU-only MVP)")

app.include_router(health_router)
app.include_router(pipeline_router, prefix="/api")
