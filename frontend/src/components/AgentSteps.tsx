import type { AgentStep } from "../types/agent"

const s = {
  box: { background: "#f5f5f5", border: "1px solid #ddd", borderRadius: 6, padding: "8px 12px", marginBottom: 6, fontSize: 13 },
  badge: { background: "#1a1a1a", color: "#fff", borderRadius: 4, padding: "2px 8px", fontSize: 11, marginBottom: 4, display: "inline-block" },
  muted: { color: "#666", marginTop: 4, fontFamily: "monospace", fontSize: 12 },
}

export default function AgentSteps({ steps }: { steps: AgentStep[] }) {
  if (!steps.length) return null
  return (
    <div style={{ marginTop: 12 }}>
      <p style={{ fontWeight: 600, marginBottom: 8, fontSize: 13 }}>Tool calls ({steps.length})</p>
      {steps.map((s2, i) => (
        <div key={i} style={s.box}>
          <span style={s.badge}>{s2.tool}</span>
          <p style={s.muted}>{s2.output.slice(0, 200)}{s2.output.length > 200 ? "…" : ""}</p>
        </div>
      ))}
    </div>
  )
}
