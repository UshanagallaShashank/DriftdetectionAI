import { useState } from "react"
import { ingestBehavior } from "../api/client"

export default function IngestForm({ onSuccess }: { onSuccess: () => void }) {
  const [systemId, setSystemId] = useState("")
  const [actionType, setActionType] = useState("llm_call")
  const [status, setStatus] = useState("")

  const submit = async () => {
    if (!systemId) return
    await ingestBehavior({
      system_id: systemId,
      action_type: actionType,
      input_data: { prompt: "test input" },
      output_data: { response: "test output" },
    })
    setStatus("✓ ingested")
    onSuccess()
  }

  return (
    <div style={{ marginBottom: 24, padding: 16, border: "1px solid #ccc" }}>
      <h2>Ingest Behavior</h2>
      <input placeholder="system_id" value={systemId} onChange={(e) => setSystemId(e.target.value)} style={{ marginRight: 8 }} />
      <input placeholder="action_type" value={actionType} onChange={(e) => setActionType(e.target.value)} style={{ marginRight: 8 }} />
      <button onClick={submit}>Ingest</button>
      {status && <span style={{ marginLeft: 8, color: "green" }}>{status}</span>}
    </div>
  )
}
