from langchain_core.tools import tool
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.behavior_record import BehaviorRecord


def make_get_action_breakdown_tool(db: AsyncSession):
    @tool
    async def get_action_breakdown(system_id: str) -> str:
        """Count behaviors by action_type for a system. Shows the distribution and total volume."""
        result = await db.execute(
            select(BehaviorRecord.action_type, func.count().label("n"))
            .where(BehaviorRecord.system_id == system_id)
            .group_by(BehaviorRecord.action_type)
            .order_by(func.count().desc())
        )
        rows = result.fetchall()
        if not rows:
            return f"No behaviors found for '{system_id}'"
        total = sum(r.n for r in rows)
        breakdown = " | ".join(f"{r.action_type}: {r.n}" for r in rows)
        return f"'{system_id}' — {total} total actions → {breakdown}"

    return get_action_breakdown
