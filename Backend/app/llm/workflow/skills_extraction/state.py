from pydantic import BaseModel
from app.api.schemas.skill_analysis import AnalysisOutput
from typing import Optional

class SkillsExtractionState(BaseModel):
    file_data: str
    additional_cv_content: Optional[str] = None
    analysis_output: AnalysisOutput

