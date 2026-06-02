import FleetScannerDemo from "./components/FleetScannerDemo"
import InvestigatorDemo from "./components/InvestigatorDemo"

function App() {
  return (
    <div style={{ maxWidth: 760, margin: "0 auto", padding: 24, fontFamily: "sans-serif" }}>
      <h1 style={{ marginBottom: 4 }}>DriftdetectionAI</h1>
      <p style={{ color: "#666", marginBottom: 32 }}>Failure intelligence for AI systems</p>
      <h2 style={{ marginBottom: 16 }}>Agent Demos</h2>
      <InvestigatorDemo />
      <FleetScannerDemo />
    </div>
  )
}

export default App
