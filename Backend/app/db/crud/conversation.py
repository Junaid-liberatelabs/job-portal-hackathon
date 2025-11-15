from app.db.model.conversation import Conversation
from app.db.model.conversation_message import ConversationMessage
from sqlalchemy.orm import Session
from typing import List


def create_conversation(db: Session, user_id: str, thread_id: str):
    conversation = Conversation(user_id=user_id, thread_id=thread_id)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation


def get_user_all_conversations_thread_ids(db: Session, user_id: str):
    #return only the thread_id as a list of strings
    results = db.query(Conversation).filter(Conversation.user_id == user_id).with_entities(Conversation.thread_id).all()
    return [thread_id[0] for thread_id in results]

def get_conversation_by_thread_id(db: Session, thread_id: str):
    return db.query(Conversation).filter(Conversation.thread_id == thread_id).first()

def verify_thread_ownership(db: Session, thread_id: str, user_id: str) -> bool:
    conversation = db.query(Conversation).filter(
        Conversation.thread_id == thread_id,
        Conversation.user_id == user_id
    ).first()
    return conversation is not None

def delete_conversation_by_thread_id(db: Session, thread_id: str):
    db.query(Conversation).filter(Conversation.thread_id == thread_id).delete()
    db.commit()
    return True

def create_conversation_message(db: Session, thread_id: str, user_id: str, role: str, content: str):
    message = ConversationMessage(
        thread_id=thread_id,
        user_id=user_id,
        role=role,
        content=content
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_conversation_messages_by_thread_id(db: Session, thread_id: str) -> List[ConversationMessage]:
    return db.query(ConversationMessage).filter(
        ConversationMessage.thread_id == thread_id
    ).order_by(ConversationMessage.created_at.asc()).all()
