from unittest.mock import AsyncMock, patch

import pytest
from httpx import AsyncClient

from app.schemas.analyze_drift import DriftAnalysis

_MOCK = DriftAnalysis(
    drift_detected=True,
    confidence=0.87,
    summary="Response latency increased significantly across llm_call actions.",
    anomalies=["avg output tokens up 40%", "tool_call frequency dropped"],
)

_INGEST = {
    "system_id": "sys-1",
    "action_type": "llm_call",
    "input_data": {"prompt": "hello"},
    "output_data": {"response": "hi"},
}


@pytest.mark.asyncio
async def test_analyze_drift_returns_report(client: AsyncClient):
    await client.post("/api/v1/behaviors/ingest", json=_INGEST)
    with patch("app.api.routes.analyze_drift.run_drift_analysis", new=AsyncMock(return_value=_MOCK)):
        r = await client.post("/api/v1/behaviors/sys-1/analyze")
    assert r.status_code == 200
    body = r.json()
    assert body["drift_detected"] is True
    assert body["system_id"] == "sys-1"
    assert body["behavior_count"] == 1


@pytest.mark.asyncio
async def test_analyze_drift_404_no_behaviors(client: AsyncClient):
    r = await client.post("/api/v1/behaviors/ghost-system/analyze")
    assert r.status_code == 404
