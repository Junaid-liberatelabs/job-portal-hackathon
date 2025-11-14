from pydantic import BaseModel, Field
from typing import Optional, Any

class SkillGapAnalysisState(BaseModel):
    user_profile_data: dict

    user_applied_job_data: list[dict]

    gap_analysis_report: Optional[str] = None
    
    resource_search_tool: Optional[Any] = Field(default=None, exclude=True)
    
    class Config:
        arbitrary_types_allowed = True



