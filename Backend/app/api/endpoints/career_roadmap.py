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
router = APIRouter()
logger = get_logger(__name__)

@router.post("/career-roadmap")
async def career_roadmap(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    request: CareerRoadmapRequest = Body(...),
):
    try:
        user_profile_data = UserResponse.model_validate(current_user).model_dump()

        graph = career_roadmap_graph.compile()
        input_data = {
            "user_profile_data": user_profile_data,
            "timeframe": request.timeframe,
            "available_learning_time": request.available_learning_time,
        }
        result = graph.invoke(input_data)
        return CareerRoadmapResponse(career_roadmap_report=result["career_roadmap_report"])
    except Exception as e:
        logger.error(f"Error in career roadmap: {e}")
        raise HTTPException(status_code=500, detail=str(e))