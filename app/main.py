from fastapi import FastAPI


app = FastAPI(
    title="BUGHUGE",
    description="Automated Vulnerability Intelligence Engine",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "BUGHUGE",
        "description": "Automated Vulnerability Intelligence Engine",
        "version": "0.1.0",
        "status": "operational",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }