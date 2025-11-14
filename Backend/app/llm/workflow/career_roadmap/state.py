from pydantic import BaseModel

class CareerRoadmapState(BaseModel):
    user_profile_data: dict
    timeframe: str
    available_learning_time: str
    career_roadmap_report: str