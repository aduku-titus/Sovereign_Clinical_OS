import operator
from typing import TypedDict, Annotated, List, Union


# The "Chart" that is passed between agents
class AgentState(TypedDict):
    patient_id: str
    vitals: dict  # The Geriatric 9 from Project 1
    triage_level: str  # Calculated by Triage Agent
    safety_flags: List[str]  # From Project 3 Shield

    # The Drafts
    draft_summary: str

    # The Legal 'Stop' Sign
    nurse_approved: bool

    # Chat History (Append-only)
    messages: Annotated[List[str], operator.add]
