export interface AgentStep {
  tool: string
  input: string
  output: string
}

export interface AgentRunResponse {
  output: string
  steps: AgentStep[]
}
