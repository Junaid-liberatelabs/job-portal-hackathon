from pydantic import BaseModel


class CareerRoadmapRequest(BaseModel):
    timeframe: str
    available_learning_time: str

class CareerRoadmapResponse(BaseModel):
    career_roadmap_report: str