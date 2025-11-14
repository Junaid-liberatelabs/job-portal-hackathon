from pydantic import BaseModel
from typing import List

class AnalysisOutput(BaseModel):
    key_skills: List[str]
    tools_and_technologies: List[str]
    relevant_roles: List[str]

class SkillsExtractionState(BaseModel):
    file_data: str
    analysis_output: AnalysisOutput

