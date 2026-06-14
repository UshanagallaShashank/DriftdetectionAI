from pydantic import BaseModel


class AgentStep(BaseModel):
    tool: str
    input: str
    output: str


class AgentRunResponse(BaseModel):
    output: str
    steps: list[AgentStep]
