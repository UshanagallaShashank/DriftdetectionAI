from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.schemas.agent_run import AgentRunResponse, AgentStep
from app.services.run_fleet_scanner import run_fleet_scanner
from app.services.run_investigation_agent import run_investigation_agent

router = APIRouter(prefix="/agents", tags=["agents"])


@router.post("/investigate/{system_id}", response_model=AgentRunResponse)
async def post_investigate(system_id: str, db: AsyncSession = Depends(get_db)) -> AgentRunResponse:
    result = await run_investigation_agent(db, system_id)
    return AgentRunResponse(output=result["output"], steps=[AgentStep(**s) for s in result["steps"]])


@router.post("/scan", response_model=AgentRunResponse)
async def post_scan(db: AsyncSession = Depends(get_db)) -> AgentRunResponse:
    result = await run_fleet_scanner(db)
    return AgentRunResponse(output=result["output"], steps=[AgentStep(**s) for s in result["steps"]])
