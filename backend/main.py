from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import analyze_drift, ingest, list_behaviors

# Creates and configures the DriftdetectionAI FastAPI application
app = FastAPI(title="DriftdetectionAI", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router, prefix="/api/v1")
app.include_router(list_behaviors.router, prefix="/api/v1")
app.include_router(analyze_drift.router, prefix="/api/v1")

@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "DriftdetectionAI"}
