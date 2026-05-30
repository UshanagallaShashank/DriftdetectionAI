from fastapi import APIRouter, HTTPException
from app.schemas.ingest import IngestRequest, IngestResponse
from app.services.ingest_service import ingest_behavior

router = APIRouter(prefix="/behaviors", tags=["behaviors"])

# Accepts a raw behavior event from any AI system and records it
@router.post("/ingest", response_model=IngestResponse)
def post_ingest(request: IngestRequest) -> IngestResponse:
    try:
        record = ingest_behavior(request)
        return IngestResponse(behavior_id=str(record.id))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
