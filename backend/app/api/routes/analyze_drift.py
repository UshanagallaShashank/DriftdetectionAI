from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.schemas.analyze_drift import DriftReportResponse
from app.services.fetch_behaviors import fetch_behaviors
from app.services.run_drift_analysis import run_drift_analysis
from app.services.save_drift_report import save_drift_report

router = APIRouter(prefix="/behaviors", tags=["behaviors"])


@router.post("/{system_id}/analyze", response_model=DriftReportResponse)
async def post_analyze_drift(
    system_id: str,
    window: int = Query(50, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
) -> DriftReportResponse:
    behaviors, _ = await fetch_behaviors(db, system_id, window, 0)
    if not behaviors:
        raise HTTPException(status_code=404, detail="no behaviors found for this system")
    analysis = await run_drift_analysis(behaviors)
    report = await save_drift_report(db, system_id, len(behaviors), analysis)
    return DriftReportResponse.model_validate(report)
