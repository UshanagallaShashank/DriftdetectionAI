import pytest
from httpx import AsyncClient

PAYLOAD = {
    "system_id": "agent-x",
    "action_type": "llm_call",
    "input_data": {"q": "test"},
    "output_data": {"r": "ok"},
}


@pytest.mark.asyncio
async def test_list_behaviors_filter_by_system_id(client: AsyncClient):
    await client.post("/api/v1/behaviors/ingest", json=PAYLOAD)
    await client.post("/api/v1/behaviors/ingest", json={**PAYLOAD, "system_id": "other"})

    r = await client.get("/api/v1/behaviors", params={"system_id": "agent-x"})
    assert r.status_code == 200
    body = r.json()
    assert body["total"] == 1
    assert body["items"][0]["system_id"] == "agent-x"
