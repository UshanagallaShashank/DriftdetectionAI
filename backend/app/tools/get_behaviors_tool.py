from langchain_core.tools import tool
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.fetch_behaviors import fetch_behaviors


def make_get_behaviors_tool(db: AsyncSession):
    @tool
    async def get_behaviors(system_id: str) -> str:
        """Fetch recent behaviors for an AI system. Returns count, action types, and timestamps."""
        behaviors, total = await fetch_behaviors(db, system_id, 20, 0)
        if not behaviors:
            return f"No behaviors found for system '{system_id}'"
        types = list({b.action_type for b in behaviors})
        latest = behaviors[0].timestamp.strftime("%Y-%m-%d %H:%M")
        return f"System '{system_id}': {total} behaviors. Action types: {types}. Latest: {latest}"

    return get_behaviors
