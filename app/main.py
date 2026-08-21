from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description="Automated Vulnerability Intelligence Engine",
    version=settings.app_version,
)


@app.get("/")
def root():
    return {
        "name": settings.app_name,
        "description": "Automated Vulnerability Intelligence Engine",
        "version": settings.app_version,
        "environment": settings.app_env,
        "status": "operational",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }