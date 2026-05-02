from typing import TypedDict

class AgentState(TypedDict):
    query: str
    mode: str
    context: str
    response: str