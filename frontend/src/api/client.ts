const BASE = "http://localhost:8000/api/v1"

export const ingestBehavior = (payload: unknown) =>
  fetch(`${BASE}/behaviors/ingest`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  }).then((r) => r.json())

export const listBehaviors = (systemId?: string) =>
  fetch(`${BASE}/behaviors${systemId ? `?system_id=${systemId}` : ""}`).then(
    (r) => r.json()
  )

export const analyzeDrift = (systemId: string) =>
  fetch(`${BASE}/behaviors/${systemId}/analyze`, { method: "POST" }).then((r) =>
    r.json()
  )
