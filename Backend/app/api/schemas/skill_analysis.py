from pydantic import BaseModel
from fastapi import UploadFile, File
from typing import Optional, List
from pydantic import Field


class SkillAnalysisRequest(BaseModel):
    file: UploadFile = File(...)
    # additional_cv_content: Optional[str] = Field(None, description="Additional CV content to be used for skill analysis")

class AnalysisOutput(BaseModel):
    key_skills: List[str]
    tools_and_technologies: List[str]
    relevant_roles: List[str]

class SkillAnalysisResponse(BaseModel):
    analysis_output: AnalysisOutput