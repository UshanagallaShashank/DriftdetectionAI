import { useEffect, useState } from "react"
import { listBehaviors } from "../api/client"
import type { BehaviorRecord } from "../types"
import { Badge } from "./ui/badge"
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card"

export default function BehaviorList({ systemId }: { systemId: string }) {
  const [items, setItems] = useState<BehaviorRecord[]>([])
  const [total, setTotal] = useState(0)

  useEffect(() => {
    listBehaviors(systemId || undefined).then((d) => { setItems(d.items ?? []); setTotal(d.total ?? 0) })
  }, [systemId])
  return (
    <Card className="mb-6">
      <CardHeader><CardTitle>Behaviors <Badge variant="secondary">{total}</Badge></CardTitle></CardHeader>
      <CardContent className="space-y-2">
        {items.map((b) => (
          <div key={b.id} className="flex items-center gap-2 text-sm border rounded p-2">
            <Badge>{b.action_type}</Badge>
            <span className="font-mono text-muted-foreground">{b.system_id}</span>
            <span className="ml-auto text-xs text-muted-foreground">{new Date(b.timestamp).toLocaleString()}</span>
          </div>
        ))}
        {total === 0 && <p className="text-sm text-muted-foreground">No behaviors yet.</p>}
      </CardContent>
    </Card>
  )
}
