from fastapi import APIRouter
from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.db.model.user import User
from app.llm.workflow.career_roadmap.graph import career_roadmap_graph
from app.core.logging_config import get_logger
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends
from app.api.schemas.career_roadmap import CareerRoadmapResponse, CareerRoadmapRequest
from fastapi import HTTPException
from fastapi import Body
from app.db.crud.user import get_user_by_id
from app.api.schemas.user import UserResponse
from app.db.crud.application import get_applications_by_user
from app.db.crud.job import get_job_by_id
from app.db.crud.analysis_report import create_career_roadmap_report, get_most_recent_career_roadmap_report
from app.api.schemas.career_roadmap import CareerRoadmapGraphData
from app.api.schemas.job import JobResponse
router = APIRouter()
logger = get_logger(__name__)

@router.post("/career-roadmap")
def career_roadmap(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    request: CareerRoadmapRequest = Body(...),
):
    try:
        user_profile_data = UserResponse.model_validate(current_user).model_dump()

        applications = get_applications_by_user(db, current_user.id)
        job_ids = [application.job_id for application in applications]
        jobs = [get_job_by_id(db, job_id) for job_id in job_ids]
        user_applied_job_data = [
            JobResponse.model_validate(job).model_dump() 
            for job in jobs 
            if job is not None
        ]

        graph = career_roadmap_graph.compile()
        input_data = {
            "user_applied_job_data": user_applied_job_data,
            "user_profile_data": user_profile_data,
            "timeframe": request.timeframe,
            "available_learning_time": request.available_learning_time,
        }
        result = graph.invoke(input_data)
        create_career_roadmap_report(db, current_user.id, result["career_roadmap_report"], result.get("graph_data"))

        return CareerRoadmapResponse(
            career_roadmap_report=result["career_roadmap_report"],
            graph_data=result.get("graph_data")
        )
    except Exception as e:
        logger.error(f"Error in career roadmap: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/career-roadmap")
def get_career_roadmap(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    report = get_most_recent_career_roadmap_report(db, current_user.id)
    return CareerRoadmapResponse(career_roadmap_report=report.career_roadmap_report, graph_data=CareerRoadmapGraphData.model_validate_json(report.graph_data))  