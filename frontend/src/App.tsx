import { useState } from "react"
import AnalyzePanel from "./components/AnalyzePanel"
import BehaviorList from "./components/BehaviorList"
import IngestForm from "./components/IngestForm"
import { Input } from "./components/ui/input"

function App() {
  const [systemId, setSystemId] = useState("my-agent")
  const [tick, setTick] = useState(0)

  return (
    <div className="max-w-3xl mx-auto p-6 space-y-2">
      <h1 className="text-2xl font-bold">DriftdetectionAI</h1>
      <p className="text-muted-foreground text-sm mb-4">Failure intelligence for AI systems</p>
      <div className="flex items-center gap-2 mb-6">
        <span className="text-sm font-medium">System ID</span>
        <Input value={systemId} onChange={(e) => setSystemId(e.target.value)} className="w-48" />
      </div>
      <IngestForm onSuccess={() => setTick((t) => t + 1)} />
      <BehaviorList key={tick} systemId={systemId} />
      <AnalyzePanel systemId={systemId} />
    </div>
  )
}

export default App
