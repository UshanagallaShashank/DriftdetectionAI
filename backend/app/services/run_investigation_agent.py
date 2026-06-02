from langgraph.prebuilt import create_react_agent
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.llm import get_llm
from app.tools.get_behaviors_tool import make_get_behaviors_tool

_SYSTEM = (
    "You are a behavior drift investigator for AI systems. "
    "Use get_behaviors to fetch the system's actions, then analyze the data "
    "for patterns, anomalies, or drift. Be specific and concise."
)


async def run_investigation_agent(db: AsyncSession, system_id: str) -> dict:
    tools = [make_get_behaviors_tool(db)]
    agent = create_react_agent(get_llm(), tools, prompt=_SYSTEM)
    result = await agent.ainvoke({"messages": [("human", f"Investigate system '{system_id}'. What has it been doing? Any concerns?")]})
    steps = [{"tool": m.name, "input": str(m.content), "output": str(m.content)} for m in result["messages"] if hasattr(m, "name") and m.name]
    return {"output": result["messages"][-1].content, "steps": steps}
