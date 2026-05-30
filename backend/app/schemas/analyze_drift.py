from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class DriftAnalysis(BaseModel):
    drift_detected: bool
    confidence: float
    summary: str
    anomalies: list[str]


class DriftReportResponse(BaseModel):
    id: UUID
    system_id: str
    analyzed_at: datetime
    behavior_count: int
    drift_detected: bool
    confidence: float
    summary: str
    anomalies: list[str]

    model_config = {"from_attributes": True}
