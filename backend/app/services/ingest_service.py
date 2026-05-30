from app.models.behavior_record import BehaviorRecord
from app.schemas.ingest import IngestRequest
from app.utils.logger import get_logger

logger = get_logger(__name__)

# Creates a BehaviorRecord from an ingest request and returns it for storage
def ingest_behavior(request: IngestRequest) -> BehaviorRecord:
    record = BehaviorRecord(
        system_id=request.system_id,
        session_id=request.session_id,
        action_type=request.action_type,
        input_data=request.input_data,
        output_data=request.output_data,
        metadata=request.metadata,
    )
    logger.info(f"ingested behavior_id={record.id} system={record.system_id}")
    return record
