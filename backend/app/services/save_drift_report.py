from sqlalchemy.ext.asyncio import AsyncSession

from app.models.drift_report import DriftReport
from app.schemas.analyze_drift import DriftAnalysis


async def save_drift_report(
    db: AsyncSession, system_id: str, behavior_count: int, analysis: DriftAnalysis
) -> DriftReport:
    report = DriftReport(
        system_id=system_id,
        behavior_count=behavior_count,
        drift_detected=analysis.drift_detected,
        confidence=analysis.confidence,
        summary=analysis.summary,
        anomalies=analysis.anomalies,
    )
    db.add(report)
    await db.commit()
    await db.refresh(report)
    return report
