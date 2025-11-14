from sqlalchemy.orm import Session
from app.db.model.skill_gap_analysis_report import SkillGapAnalysisReport
from datetime import datetime

#skill gap analysis report

def create_skill_gap_analysis_report(db: Session, user_id: str, report: str):
    skill_gap_analysis_report = SkillGapAnalysisReport(user_id=user_id, gap_analysis_report=report)
    db.add(skill_gap_analysis_report)
    db.commit()
    db.refresh(skill_gap_analysis_report)
    return skill_gap_analysis_report


def get_skill_gap_analysis_report(db: Session, user_id: str):
    return db.query(SkillGapAnalysisReport).filter(SkillGapAnalysisReport.user_id == user_id).first()


def get_skill_gap_analysis_report_by_date(db: Session, date: datetime):
    return db.query(SkillGapAnalysisReport).filter(SkillGapAnalysisReport.created_at == date).all()

def get_all_skill_gap_analysis_reports(db: Session):
    return db.query(SkillGapAnalysisReport).all()


#career roadmap report