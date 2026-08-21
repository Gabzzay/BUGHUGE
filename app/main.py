from fastapi import FastAPI

from app.core.config import settings
from app.models.vulnerability import Vulnerability
from app.services.vulnerability_service import VulnerabilityService


app = FastAPI(
    title=settings.app_name,
    description="Automated Vulnerability Intelligence Engine",
    version=settings.app_version,
)


vulnerability_service = VulnerabilityService()


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


@app.post("/vulnerabilities")
def create_vulnerability(vulnerability: Vulnerability):
    return vulnerability_service.create(vulnerability)