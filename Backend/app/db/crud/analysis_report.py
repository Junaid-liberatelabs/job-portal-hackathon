from sqlalchemy.orm import Session
from app.db.model.skill_gap_analysis_report import SkillGapAnalysisReport
from datetime import datetime
from app.db.model.career_roadmap_report import CareerRoadmapReport
from app.api.schemas.career_roadmap import CareerRoadmapGraphData
import json

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

#get the most recent skill gap analysis report
def get_most_recent_skill_gap_analysis_report(db: Session):
    return db.query(SkillGapAnalysisReport).order_by(SkillGapAnalysisReport.created_at.desc()).first()


#career roadmap report

def create_career_roadmap_report(db: Session, user_id: str, report: str, graph_data: CareerRoadmapGraphData):
    career_roadmap_report = CareerRoadmapReport(user_id=user_id, career_roadmap_report=report, graph_data=json.dumps(graph_data.model_dump()))
    db.add(career_roadmap_report)
    db.commit()
    db.refresh(career_roadmap_report)
    return career_roadmap_report


def get_most_recent_career_roadmap_report(db: Session, user_id: str):
    return db.query(CareerRoadmapReport).filter(CareerRoadmapReport.user_id == user_id).order_by(CareerRoadmapReport.created_at.desc()).first()
