import { useState } from "react"
import { investigateSystem } from "../api/agents"
import type { AgentRunResponse } from "../types/agent"
import AgentSteps from "./AgentSteps"

const card = { border: "1px solid #ddd", borderRadius: 8, padding: 20, marginBottom: 16 }
const btn = { padding: "6px 16px", background: "#1a1a1a", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }

export default function InvestigatorDemo() {
  const [systemId, setSystemId] = useState("demo-agent")
  const [result, setResult] = useState<AgentRunResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const run = async () => { setLoading(true); setResult(await investigateSystem(systemId)); setLoading(false) }

  return (
    <div style={card}>
      <h3 style={{ marginTop: 0 }}>🔍 Demo 1 — System Investigator</h3>
      <p style={{ color: "#666", fontSize: 13 }}>Agent fetches behaviors for a system and produces an investigation report.</p>
      <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
        <input value={systemId} onChange={(e) => setSystemId(e.target.value)} placeholder="system_id" style={{ padding: "6px 10px", border: "1px solid #ccc", borderRadius: 4, flex: 1 }} />
        <button onClick={run} disabled={loading} style={btn}>
          {loading ? "Investigating…" : "Run Agent"}
        </button>
      </div>
      <AgentSteps steps={result?.steps ?? []} />
      {result && <div style={{ background: "#eef", borderRadius: 6, padding: 12, marginTop: 8, fontSize: 14 }}><strong>Conclusion:</strong> {result.output}</div>}
    </div>
  )
}
