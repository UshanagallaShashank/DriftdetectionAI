import { useState } from "react"
import { scanFleet } from "../api/agents"
import type { AgentRunResponse } from "../types/agent"
import AgentSteps from "./AgentSteps"

const card = { border: "1px solid #ddd", borderRadius: 8, padding: 20, marginBottom: 16 }

export default function FleetScannerDemo() {
  const [result, setResult] = useState<AgentRunResponse | null>(null)
  const [loading, setLoading] = useState(false)

  const run = async () => {
    setLoading(true)
    setResult(await scanFleet())
    setLoading(false)
  }

  return (
    <div style={card}>
      <h3 style={{ marginTop: 0 }}>🛡️ Demo 2 — Fleet Health Scanner</h3>
      <p style={{ color: "#666", fontSize: 13 }}>Agent discovers all active systems, checks each one, then ranks them by health.</p>
      <button onClick={run} disabled={loading} style={{ padding: "6px 16px", background: "#1a1a1a", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer", marginBottom: 12 }}>
        {loading ? "Scanning fleet…" : "Scan All Systems"}
      </button>
      <AgentSteps steps={result?.steps ?? []} />
      {result && <div style={{ background: "#efe", borderRadius: 6, padding: 12, marginTop: 8, fontSize: 14 }}><strong>Fleet Report:</strong> {result.output}</div>}
    </div>
  )
}
