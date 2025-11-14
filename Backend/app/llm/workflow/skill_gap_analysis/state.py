from pydantic import BaseModel

class SkillGapAnalysisState(BaseModel):
    user_profile_data: dict

    user_applied_job_data: list[dict]

    gap_analysis_report: str



