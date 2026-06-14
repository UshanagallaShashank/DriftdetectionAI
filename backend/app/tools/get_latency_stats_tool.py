from langchain_core.tools import tool
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.behavior_record import BehaviorRecord


def make_get_latency_stats_tool(db: AsyncSession):
    @tool
    async def get_latency_stats(system_id: str) -> str:
        """Read latency_ms from behavior metadata to detect slow or degraded calls."""
        result = await db.execute(
            select(BehaviorRecord.action_type, BehaviorRecord.extra)
            .where(BehaviorRecord.system_id == system_id)
            .where(BehaviorRecord.extra.isnot(None))
        )
        pairs = [(r.action_type, r.extra.get("latency_ms")) for r in result.fetchall() if r.extra]
        values = [(t, v) for t, v in pairs if v is not None]
        if not values:
            return f"No latency data in metadata for '{system_id}'"
        nums = [v for _, v in values]
        avg, mx = sum(nums) / len(nums), max(nums)
        slow = [(t, v) for t, v in values if v > 2000]
        out = f"'{system_id}' latency — avg={avg:.0f}ms, max={mx}ms over {len(nums)} calls"
        if slow:
            out += f" | SLOW (>2s): {', '.join(f'{t}={v}ms' for t,v in slow)}"
        return out

    return get_latency_stats
