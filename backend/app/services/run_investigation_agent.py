from langchain_core.messages import ToolMessage
from langgraph.prebuilt import create_react_agent
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.llm import get_llm
from app.prompts.investigation_agent import investigation_system_prompt
from app.tools.get_action_breakdown_tool import make_get_action_breakdown_tool
from app.tools.get_behaviors_tool import make_get_behaviors_tool
from app.tools.get_latency_stats_tool import make_get_latency_stats_tool


async def run_investigation_agent(db: AsyncSession, system_id: str) -> dict:
    tools = [
        make_get_behaviors_tool(db),
        make_get_action_breakdown_tool(db),
        make_get_latency_stats_tool(db),
    ]
    agent = create_react_agent(get_llm(), tools, prompt=investigation_system_prompt())
    result = await agent.ainvoke({"messages": [("human", f"Investigate system '{system_id}' using all available tools.")]})
    msgs = result["messages"]
    steps = [
        {"tool": m.name, "input": str(msgs[i - 1].tool_calls[0]["args"]) if hasattr(msgs[i - 1], "tool_calls") else "", "output": str(m.content)}
        for i, m in enumerate(msgs) if isinstance(m, ToolMessage)
    ]
    return {"output": msgs[-1].content, "steps": steps}
