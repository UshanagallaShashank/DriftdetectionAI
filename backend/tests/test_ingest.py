import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Tests that a well-formed behavior payload is ingested and returns an id
def test_ingest_behavior_success():
    payload = {
        "system_id": "test-agent-1",
        "action_type": "llm_call",
        "input_data": {"prompt": "hello"},
        "output_data": {"response": "world"},
    }
    r = client.post("/api/v1/behaviors/ingest", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ingested"
    assert "behavior_id" in body

# Tests that optional fields (session_id, metadata) are accepted
def test_ingest_with_optional_fields():
    payload = {
        "system_id": "agent-2",
        "session_id": "sess-abc",
        "action_type": "tool_call",
        "input_data": {"tool": "search"},
        "output_data": {"results": []},
        "metadata": {"latency_ms": 120},
    }
    r = client.post("/api/v1/behaviors/ingest", json=payload)
    assert r.status_code == 200
