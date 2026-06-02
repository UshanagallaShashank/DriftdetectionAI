import { useState } from "react"
import { analyzeDrift } from "../api/client"
import type { DriftReport } from "../types"
import { Badge } from "./ui/badge"
import { Button } from "./ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card"

export default function AnalyzePanel({ systemId }: { systemId: string }) {
  const [report, setReport] = useState<DriftReport | null>(null)
  const [loading, setLoading] = useState(false)
  const run = async () => { if (!systemId) return; setLoading(true); setReport(await analyzeDrift(systemId)); setLoading(false) }
  return (
    <Card>
      <CardHeader><CardTitle>Drift Analysis</CardTitle></CardHeader>
      <CardContent className="space-y-3">
        <Button onClick={run} disabled={loading || !systemId}>{loading ? "Analyzing…" : `Analyze "${systemId}"`}</Button>
        {report && (
          <div className="space-y-2 text-sm">
            <div className="flex gap-2 items-center">
              <Badge variant={report.drift_detected ? "destructive" : "secondary"}>{report.drift_detected ? "Drift detected" : "No drift"}</Badge>
              <span className="text-muted-foreground">{Math.round(report.confidence * 100)}% confidence</span>
            </div>
            <p>{report.summary}</p>
            {report.anomalies.map((a, i) => <p key={i} className="text-amber-600">⚠ {a}</p>)}
          </div>
        )}
      </CardContent>
    </Card>
  )
}
