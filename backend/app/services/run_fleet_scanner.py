from langgraph.prebuilt import create_react_agent
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.llm import get_llm
from app.tools.get_behaviors_tool import make_get_behaviors_tool
from app.tools.list_systems_tool import make_list_systems_tool

_SYSTEM = (
    "You are a fleet health monitor for AI systems. "
    "First call list_systems to discover all active systems. "
    "Then call get_behaviors for each one. "
    "Finally produce a ranked health report — flag systems that show unusual patterns."
)


async def run_fleet_scanner(db: AsyncSession) -> dict:
    tools = [make_list_systems_tool(db), make_get_behaviors_tool(db)]
    agent = create_react_agent(get_llm(), tools, prompt=_SYSTEM)
    result = await agent.ainvoke({"messages": [("human", "Scan the entire fleet and produce a health report.")]})
    steps = [{"tool": m.name, "input": str(m.content), "output": str(m.content)} for m in result["messages"] if hasattr(m, "name") and m.name]
    return {"output": result["messages"][-1].content, "steps": steps}
