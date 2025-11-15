"""State for the chat workflow."""

from typing import Annotated, List, Literal, TypedDict, Optional
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class AgentChatState(TypedDict):
    decided_node: Literal["mentor", "generic"]
    messages: Annotated[List[AnyMessage], add_messages]
    