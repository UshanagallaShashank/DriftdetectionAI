import { useState } from "react"
import AnalyzePanel from "./components/AnalyzePanel"
import BehaviorList from "./components/BehaviorList"
import IngestForm from "./components/IngestForm"

function App() {
  const [systemId, setSystemId] = useState("my-agent")
  const [tick, setTick] = useState(0)

  return (
    <div style={{ fontFamily: "sans-serif", maxWidth: 860, margin: "0 auto", padding: 24 }}>
      <h1>DriftdetectionAI</h1>
      <p style={{ color: "#555" }}>Failure intelligence for AI systems</p>
      <label>System ID: <input value={systemId} onChange={(e) => setSystemId(e.target.value)} style={{ marginLeft: 8 }} /></label>
      <hr />
      <IngestForm onSuccess={() => setTick((t) => t + 1)} />
      <BehaviorList key={tick} systemId={systemId} />
      <AnalyzePanel systemId={systemId} />
    </div>
  )
}

export default App
