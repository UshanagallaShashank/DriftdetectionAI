import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_list_behaviors_empty(client: AsyncClient):
    r = await client.get("/api/v1/behaviors")
    assert r.status_code == 200
    body = r.json()
    assert body["items"] == []
    assert body["total"] == 0
