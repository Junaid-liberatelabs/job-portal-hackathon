from app.db.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, func
import uuid

class SkillGapAnalysisReport(Base):
    __tablename__ = "skill_gap_analysis_report"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    gap_analysis_report = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now(), server_default=func.now())
    