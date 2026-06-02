import { useState } from "react"
import { ingestBehavior } from "../api/client"
import { Button } from "./ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card"
import { Input } from "./ui/input"

export default function IngestForm({ onSuccess }: { onSuccess: () => void }) {
  const [systemId, setSystemId] = useState("")
  const [actionType, setActionType] = useState("llm_call")
  const [status, setStatus] = useState("")
  const submit = async () => {
    if (!systemId) return
    await ingestBehavior({ system_id: systemId, action_type: actionType, input_data: { prompt: "test" }, output_data: { response: "ok" } })
    setStatus("✓ ingested")
    onSuccess()
  }
  return (
    <Card className="mb-6">
      <CardHeader><CardTitle>Ingest Behavior</CardTitle></CardHeader>
      <CardContent className="flex gap-2 items-center">
        <Input placeholder="system_id" value={systemId} onChange={(e) => setSystemId(e.target.value)} />
        <Input placeholder="action_type" value={actionType} onChange={(e) => setActionType(e.target.value)} />
        <Button onClick={submit}>Ingest</Button>
        {status && <span className="text-green-600 text-sm">{status}</span>}
      </CardContent>
    </Card>
  )
}
