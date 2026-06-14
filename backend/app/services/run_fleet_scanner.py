from langchain_core.messages import ToolMessage
from langgraph.prebuilt import create_react_agent
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.llm import get_llm
from app.prompts.fleet_scanner import fleet_scanner_system_prompt
from app.tools.get_action_breakdown_tool import make_get_action_breakdown_tool
from app.tools.get_behaviors_tool import make_get_behaviors_tool
from app.tools.list_systems_tool import make_list_systems_tool


async def run_fleet_scanner(db: AsyncSession) -> dict:
    tools = [
        make_list_systems_tool(db),
        make_get_action_breakdown_tool(db),
        make_get_behaviors_tool(db),
    ]
    agent = create_react_agent(get_llm(), tools, prompt=fleet_scanner_system_prompt())
    result = await agent.ainvoke({"messages": [("human", "Scan the entire fleet and produce a health report.")]})
    msgs = result["messages"]
    steps = [
        {"tool": m.name, "input": str(msgs[i - 1].tool_calls[0]["args"]) if hasattr(msgs[i - 1], "tool_calls") else "", "output": str(m.content)}
        for i, m in enumerate(msgs) if isinstance(m, ToolMessage)
    ]
    return {"output": msgs[-1].content, "steps": steps}
