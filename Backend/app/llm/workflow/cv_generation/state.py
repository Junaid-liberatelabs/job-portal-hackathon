from pydantic import BaseModel
from typing import Optional


class CVGenerationState(BaseModel):
    user_profile_data: dict
    user_applied_job_data: list[dict]
    html_cv: Optional[str] = None
    
    class Config:
        arbitrary_types_allowed = True
