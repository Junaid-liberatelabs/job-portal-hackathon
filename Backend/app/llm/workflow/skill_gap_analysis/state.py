from pydantic import BaseModel
from typing import Optional

class SkillGapAnalysisState(BaseModel):
    user_profile_data: dict

    user_applied_job_data: list[dict]

    gap_analysis_report: Optional[str] = None



