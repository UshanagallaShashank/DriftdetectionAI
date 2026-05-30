from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.schemas.query_behaviors import BehaviorSummary, QueryBehaviorsResponse
from app.services.fetch_behaviors import fetch_behaviors

router = APIRouter(prefix="/behaviors", tags=["behaviors"])


@router.get("", response_model=QueryBehaviorsResponse)
async def list_behaviors(
    system_id: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
) -> QueryBehaviorsResponse:
    rows, total = await fetch_behaviors(db, system_id, limit, offset)
    return QueryBehaviorsResponse(
        items=[BehaviorSummary.model_validate(r) for r in rows],
        total=total,
    )
