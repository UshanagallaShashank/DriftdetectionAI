from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BehaviorSummary(BaseModel):
    id: UUID
    system_id: str
    session_id: Optional[str]
    timestamp: datetime
    action_type: str

    model_config = {"from_attributes": True}


class QueryBehaviorsResponse(BaseModel):
    items: list[BehaviorSummary]
    total: int
