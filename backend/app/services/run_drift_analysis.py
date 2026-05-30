import json

from app.core.llm import get_llm
from app.models.behavior_record import BehaviorRecord
from app.schemas.analyze_drift import DriftAnalysis

_PROMPT = (
    "You are a drift detector for AI systems. Analyze these behavior records "
    "and identify any drift, anomalies, or unexpected patterns.\n\n"
    "Behaviors (JSON):\n{data}"
)


async def run_drift_analysis(behaviors: list[BehaviorRecord]) -> DriftAnalysis:
    structured = get_llm().with_structured_output(DriftAnalysis)
    payload = [
        {"action_type": b.action_type, "input": b.input_data, "output": b.output_data}
        for b in behaviors
    ]
    return await structured.ainvoke(_PROMPT.format(data=json.dumps(payload, default=str)))
