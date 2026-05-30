from sqlalchemy.ext.asyncio import AsyncSession

from app.models.behavior_record import BehaviorRecord
from app.schemas.ingest import IngestRequest
from app.utils.logger import get_logger

logger = get_logger(__name__)


async def save_behavior(db: AsyncSession, request: IngestRequest) -> BehaviorRecord:
    record = BehaviorRecord(
        system_id=request.system_id,
        session_id=request.session_id,
        action_type=request.action_type,
        input_data=request.input_data,
        output_data=request.output_data,
        extra=request.metadata,
    )
    db.add(record)
    await db.commit()
    await db.refresh(record)
    logger.info(f"saved behavior_id={record.id} system={record.system_id}")
    return record
