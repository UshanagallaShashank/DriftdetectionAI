import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_ingest_behavior_success(client: AsyncClient):
    r = await client.post("/api/v1/behaviors/ingest", json={
        "system_id": "test-agent-1",
        "action_type": "llm_call",
        "input_data": {"prompt": "hello"},
        "output_data": {"response": "world"},
    })
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ingested"
    assert "behavior_id" in body
