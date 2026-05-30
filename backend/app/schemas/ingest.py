from typing import Any, Optional
from pydantic import BaseModel

# Payload accepted by the POST /behaviors/ingest endpoint
class IngestRequest(BaseModel):
    system_id: str
    session_id: Optional[str] = None
    action_type: str
    input_data: dict[str, Any]
    output_data: dict[str, Any]
    metadata: Optional[dict[str, Any]] = None

# Confirmation returned after a behavior record is successfully stored
class IngestResponse(BaseModel):
    behavior_id: str
    status: str = "ingested"
