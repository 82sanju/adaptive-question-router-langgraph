from typing import TypedDict

class AgentState(TypedDict):
    question: str
    needs_search: bool
    answer: str
