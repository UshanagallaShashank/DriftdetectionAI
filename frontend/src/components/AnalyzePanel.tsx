import { useState } from "react"
import { analyzeDrift } from "../api/client"
import type { DriftReport } from "../types"

export default function AnalyzePanel({ systemId }: { systemId: string }) {
  const [report, setReport] = useState<DriftReport | null>(null)
  const [loading, setLoading] = useState(false)

  const run = async () => {
    if (!systemId) return
    setLoading(true)
    setReport(await analyzeDrift(systemId))
    setLoading(false)
  }

  return (
    <div style={{ padding: 16, border: "1px solid #ccc" }}>
      <h2>Drift Analysis</h2>
      <button onClick={run} disabled={loading || !systemId}>{loading ? "Analyzing…" : `Analyze "${systemId}"`}</button>
      {report && (
        <div style={{ marginTop: 12 }}>
          <p><strong>Drift:</strong> {report.drift_detected ? "Yes" : "No"} ({Math.round(report.confidence * 100)}% confidence)</p>
          <p><strong>Summary:</strong> {report.summary}</p>
          {report.anomalies.map((a, i) => <p key={i}>⚠ {a}</p>)}
        </div>
      )}
    </div>
  )
}
