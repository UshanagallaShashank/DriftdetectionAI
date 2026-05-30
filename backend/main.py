from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Creates and configures the DriftdetectionAI FastAPI application
app = FastAPI(title="DriftdetectionAI", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "DriftdetectionAI"}
