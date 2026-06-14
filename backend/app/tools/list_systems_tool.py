from langchain_core.tools import tool
from sqlalchemy import distinct, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.behavior_record import BehaviorRecord


def make_list_systems_tool(db: AsyncSession):
    @tool
    async def list_systems() -> str:
        """List all unique AI system IDs that have been observed and how many behaviors each has."""
        result = await db.execute(select(distinct(BehaviorRecord.system_id)))
        systems = [row[0] for row in result.fetchall()]
        if not systems:
            return "No systems found in the database"
        return f"Active systems ({len(systems)}): {', '.join(systems)}"

    return list_systems
