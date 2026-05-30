from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.behavior_record import BehaviorRecord


async def fetch_behaviors(
    db: AsyncSession,
    system_id: Optional[str],
    limit: int,
    offset: int,
) -> tuple[list[BehaviorRecord], int]:
    q = select(BehaviorRecord)
    if system_id:
        q = q.where(BehaviorRecord.system_id == system_id)
    total = await db.scalar(select(func.count()).select_from(q.subquery()))
    rows = await db.scalars(q.order_by(BehaviorRecord.timestamp.desc()).limit(limit).offset(offset))
    return list(rows), total or 0
