from fastapi import APIRouter, Body, Depends, Request, HTTPException
from app.api.schemas.agent_chat import AgentInitResponse, AgentChatMessageRequest, AgentChatMessageResponse, ConversationResponse, ConversationMessage
from app.db.session import get_db
from app.auth.dependencies import get_current_user
from app.core.logging_config import get_logger
from sqlalchemy.orm import Session
from app.db.model.user import User
import uuid
from typing import Annotated
from app.core.config import settings
from langchain_core.messages import HumanMessage
from app.llm.workflow.agent_chat.tools.mentor_tools import user_id_context
from app.db.crud.conversation import (
    get_user_all_conversations_thread_ids, 
    verify_thread_ownership,
    create_conversation,
    create_conversation_message,
    get_conversation_messages_by_thread_id,
    get_conversation_by_thread_id
)
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
    
    # Set user_id in context variable for tools to access
    user_id_context.set(current_user.id)
    
    # Ensure conversation record exists
    existing_conversation = get_conversation_by_thread_id(db, request.thread_id)
    if not existing_conversation:
        create_conversation(db, current_user.id, request.thread_id)
    
    # Save user message
    create_conversation_message(
        db=db,
        thread_id=request.thread_id,
        user_id=current_user.id,
        role="user",
        content=request.user_message
    )
    
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
    agent_response = response["messages"][-1].content
    
    # Save agent response
    create_conversation_message(
        db=db,
        thread_id=request.thread_id,
        user_id=current_user.id,
        role="assistant",
        content=agent_response
    )
    
    return AgentChatMessageResponse(response=agent_response)


@router.post("/agent-chat/conversation", response_model=list[str])
def get_conversation(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    thread_ids = get_user_all_conversations_thread_ids(db, current_user.id)
    return thread_ids

@router.get("/agent-chat/conversation/{thread_id}", response_model=ConversationResponse)
def get_conversation_history(
    thread_id: str,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    # Verify that the thread belongs to the user
    if not verify_thread_ownership(db, thread_id, current_user.id):
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    # Get messages from database
    db_messages = get_conversation_messages_by_thread_id(db, thread_id)
    
    # Convert to response format
    messages = []
    for msg in db_messages:
        messages.append(ConversationMessage(
            content=msg.content,
            type=msg.role
        ))
    
    return ConversationResponse(
        thread_id=thread_id,
        messages=messages
    )
