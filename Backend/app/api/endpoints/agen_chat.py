from fastapi import APIRouter, Body, Depends, Request
from app.api.schemas.agent_chat import AgentInitResponse, AgentChatMessageRequest, AgentChatMessageResponse
from app.db.session import get_db
from app.auth.dependencies import get_current_user
from app.core.logging_config import get_logger
from sqlalchemy.orm import Session
from app.db.model.user import User
import uuid
from typing import Annotated
from app.core.config import settings
from langchain_core.messages import HumanMessage
router = APIRouter()
logger = get_logger(__name__)

@router.post("/agent-chat/init", response_model=AgentInitResponse)
def init_agent(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    thread_id = str(uuid.uuid4())
    # create_agent_chat_thread(db, current_user.id, thread_id)
    return AgentInitResponse(thread_id=thread_id)


@router.post("/agent-chat/message", response_model=AgentChatMessageResponse)
def agent_chat_message(
    http_request: Request,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    request: AgentChatMessageRequest = Body(...),
):
    compiled_graph = http_request.app.state.agent_chat_graph
    
    config = {
        "configurable": {
            'user_id': current_user.id,
            'thread_id': request.thread_id
        }
    }
    input_data = {
        "messages": [HumanMessage(content=request.user_message)]
    }
    response = compiled_graph.invoke(input_data, config=config)
    return AgentChatMessageResponse(response=response["messages"][-1].content)