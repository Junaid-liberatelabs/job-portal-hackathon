import uuid

from app.db.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, UniqueConstraint, func


class ApplicationList(Base):
    __tablename__ = "application_list"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    job_id = Column(String, ForeignKey("jobs.id"), nullable=False, index=True)
    
    created_at = Column(DateTime, nullable=False, default=func.now(), server_default=func.now())
    updated_at = Column(
        DateTime, 
        nullable=False, 
        default=func.now(), 
        onupdate=func.now(),
        server_default=func.now()
    )
    
    __table_args__ = (
        UniqueConstraint('user_id', 'job_id', name='uix_user_job_application'),
    )

    def __repr__(self):
        return f"<ApplicationList(id={self.id}, user_id={self.user_id}, job_id={self.job_id})>"