import type { AgentRunResponse } from "../types/agent"

const BASE = "/api/v1/agents"

export const investigateSystem = (systemId: string): Promise<AgentRunResponse> =>
  fetch(`${BASE}/investigate/${systemId}`, { method: "POST" }).then((r) => r.json())

export const scanFleet = (): Promise<AgentRunResponse> =>
  fetch(`${BASE}/scan`, { method: "POST" }).then((r) => r.json())
