import json

from app.core.llm import get_llm
from app.models.behavior_record import BehaviorRecord
from app.prompts.drift_analysis import drift_analysis_prompt
from app.schemas.analyze_drift import DriftAnalysis


async def run_drift_analysis(behaviors: list[BehaviorRecord]) -> DriftAnalysis:
    structured = get_llm().with_structured_output(DriftAnalysis)
    payload = [
        {"action_type": b.action_type, "input": b.input_data, "output": b.output_data}
        for b in behaviors
    ]
    return await structured.ainvoke(
        drift_analysis_prompt(json.dumps(payload, default=str))
    )
