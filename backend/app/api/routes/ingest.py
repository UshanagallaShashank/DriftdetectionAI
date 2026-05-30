from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.schemas.ingest import IngestRequest, IngestResponse
from app.services.save_behavior import save_behavior

router = APIRouter(prefix="/behaviors", tags=["behaviors"])


@router.post("/ingest", response_model=IngestResponse)
async def post_ingest(
    request: IngestRequest, db: AsyncSession = Depends(get_db)
) -> IngestResponse:
    try:
        record = await save_behavior(db, request)
        return IngestResponse(behavior_id=str(record.id))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
