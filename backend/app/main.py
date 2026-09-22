from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "logsense-backend",
        "environment": settings.environment,
    }