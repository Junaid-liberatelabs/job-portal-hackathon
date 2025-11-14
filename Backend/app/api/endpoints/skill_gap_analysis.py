from fastapi import APIRouter
from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.db.model.user import User
from app.llm.workflow.skill_gap_analysis.graph import skill_gap_analysis_graph
from app.core.logging_config import get_logger
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends
from fastapi import HTTPException

from app.api.schemas.skill_gap_analysis import SkillGapAnalysisReportResponse
from app.api.schemas.user import UserResponse
from app.api.schemas.job import JobResponse
from app.db.crud.application import get_applications_by_user
from app.db.crud.job import get_job_by_id
from app.db.crud.analysis_report import create_skill_gap_analysis_report
router = APIRouter()
logger = get_logger(__name__)

@router.post("/skill-gap-analysis")
async def skill_gap_analysis(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):

    try:
        graph = skill_gap_analysis_graph.compile()
        
        # Get all applications for the user
        applications = get_applications_by_user(db, current_user.id)
        
        # Extract job IDs and get job details
        job_ids = [application.job_id for application in applications]
        jobs = [get_job_by_id(db, job_id) for job_id in job_ids]
        
        # Filter out None jobs (in case a job was deleted) and convert to dicts
        user_applied_job_data = [
            JobResponse.model_validate(job).model_dump() 
            for job in jobs 
            if job is not None
        ]
        
        # Convert user model to dict with all available data
        user_profile_data = UserResponse.model_validate(current_user).model_dump()

        print(user_profile_data)
        print(user_applied_job_data)
        
        input_data = {
            "user_profile_data": user_profile_data,
            "user_applied_job_data": user_applied_job_data
        }
        result = graph.invoke(input_data)
        create_skill_gap_analysis_report(db, current_user.id, result["gap_analysis_report"])
        return SkillGapAnalysisReportResponse(gap_analysis_report=result["gap_analysis_report"])
    except Exception as e:
        logger.error(f"Error in skill gap analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    