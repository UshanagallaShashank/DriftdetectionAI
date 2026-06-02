import { useEffect, useState } from "react"
import { listBehaviors } from "../api/client"
import type { BehaviorRecord } from "../types"

export default function BehaviorList({ systemId }: { systemId: string }) {
  const [items, setItems] = useState<BehaviorRecord[]>([])
  const [total, setTotal] = useState(0)

  useEffect(() => {
    listBehaviors(systemId || undefined).then((d) => {
      setItems(d.items ?? [])
      setTotal(d.total ?? 0)
    })
  }, [systemId])

  return (
    <div style={{ marginBottom: 24 }}>
      <h2>Behaviors ({total})</h2>
      {items.map((b) => (
        <div key={b.id} style={{ border: "1px solid #eee", padding: 8, marginBottom: 6, fontFamily: "monospace" }}>
          <strong>{b.system_id}</strong> · {b.action_type} · {new Date(b.timestamp).toLocaleString()}
        </div>
      ))}
      {total === 0 && <p style={{ color: "#888" }}>No behaviors yet. Ingest one above.</p>}
    </div>
  )
}
