import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_ingest_with_optional_fields(client: AsyncClient):
    r = await client.post("/api/v1/behaviors/ingest", json={
        "system_id": "agent-2",
        "session_id": "sess-abc",
        "action_type": "tool_call",
        "input_data": {"tool": "search"},
        "output_data": {"results": []},
        "metadata": {"latency_ms": 120},
    })
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ingested"
    assert "behavior_id" in body
