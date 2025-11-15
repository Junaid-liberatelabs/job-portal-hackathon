from pydantic import BaseModel
from typing import Literal, List

class AgentInitResponse(BaseModel):
    thread_id: str

class AgentChatMessageRequest(BaseModel):
    user_message: str
    thread_id: str

class AgentChatMessageResponse(BaseModel):
    response: str

class routerSchema(BaseModel):
    decided_node: Literal["mentor", "generic"]

class ConversationMessage(BaseModel):
    content: str
    type: str

class ConversationResponse(BaseModel):
    thread_id: str
    messages: List[ConversationMessage]