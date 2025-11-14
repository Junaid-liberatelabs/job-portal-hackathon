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
from app.db.crud.application import get_applications_by_user
from app.db.crud.job import get_job_by_id

router = APIRouter()
logger = get_logger(__name__)

@router.post("/skill-gap-analysis")
async def skill_gap_analysis(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):

    try:
        graph = skill_gap_analysis_graph.compile()
        user_applied_job_data = get_applications_by_user(db, current_user.id)
        user_applied_job_data = [application.job_id for application in user_applied_job_data]
        user_applied_job_data = [get_job_by_id(db, job_id) for job_id in user_applied_job_data]

        print(user_applied_job_data)
        print(current_user.model_dump())
        input_data = {
            "user_profile_data": current_user.model_dump(),
            "user_applied_job_data": user_applied_job_data
        }
        result = graph.invoke(input_data)
        return SkillGapAnalysisReportResponse(gap_analysis_report=result["gap_analysis_report"])
    except Exception as e:
        logger.error(f"Error in skill gap analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    