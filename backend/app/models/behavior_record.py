import uuid
from datetime import datetime, timezone
from typing import Any, Optional
from pydantic import BaseModel, Field

# Canonical record of a single observed AI system action
class BehaviorRecord(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    system_id: str
    session_id: Optional[str] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    action_type: str
    input_data: dict[str, Any]
    output_data: dict[str, Any]
    metadata: Optional[dict[str, Any]] = None
