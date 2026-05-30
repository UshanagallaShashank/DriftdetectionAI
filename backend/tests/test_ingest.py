import os
import sys

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.api.dependencies import get_db
from app.core.database import Base
from main import app

TEST_DB_URL = os.environ["TEST_DATABASE_URL"]


@pytest.fixture
async def client():
    engine = create_async_engine(TEST_DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    factory = async_sessionmaker(engine, expire_on_commit=False)

    async def override():
        async with factory() as session:
            yield session

    app.dependency_overrides[get_db] = override
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()
    await engine.dispose()


@pytest.mark.asyncio
async def test_ingest_behavior_success(client):
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


@pytest.mark.asyncio
async def test_ingest_with_optional_fields(client):
    r = await client.post("/api/v1/behaviors/ingest", json={
        "system_id": "agent-2",
        "session_id": "sess-abc",
        "action_type": "tool_call",
        "input_data": {"tool": "search"},
        "output_data": {"results": []},
        "metadata": {"latency_ms": 120},
    })
    assert r.status_code == 200
