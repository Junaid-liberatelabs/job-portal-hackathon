from app.db.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, func
import uuid

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    thread_id = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now(), server_default=func.now())
   