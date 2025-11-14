from pydantic import BaseModel
from typing import Optional
from app.api.schemas.career_roadmap import CareerRoadmapGraphData

class CareerRoadmapState(BaseModel):
    user_profile_data: dict
    user_applied_job_data: list[dict]
    timeframe: str
    available_learning_time: str
    career_roadmap_report: Optional[str] = None
    graph_data: Optional[CareerRoadmapGraphData] = None