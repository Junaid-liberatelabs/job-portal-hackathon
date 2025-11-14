from pydantic import BaseModel

class SkillGapAnalysisReportResponse(BaseModel):
    gap_analysis_report: str

