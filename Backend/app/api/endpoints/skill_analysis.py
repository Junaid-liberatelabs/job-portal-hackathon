from fastapi import APIRouter
from app.services.pdf_extraction import extract_pdf
from app.api.schemas.skill_analysis import SkillAnalysisResponse
from fastapi import HTTPException
from app.llm.workflow.skills_extraction.graph import skill_extraction_graph
from fastapi import UploadFile, File
router = APIRouter()
from app.core.logging_config import get_logger
logger = get_logger(__name__)

@router.post("/analyze")
async def analyze_skills(file: UploadFile = File(...)):

    #if both cv_content and file are not provided, raise an error
    # if not request:
    #     raise HTTPException(status_code=400, detail="File must be provided")

    cv_text = extract_pdf(file)

    try:
        graph = skill_extraction_graph.compile()
        input_data = {
            "file_data": cv_text,
            "additional_cv_content": None
        }
        result = graph.invoke(input_data)
        return SkillAnalysisResponse(analysis_output=result.analysis_output)
    except Exception as e:
        logger.error(f"Error analyzing skills: {e}")
        raise HTTPException(status_code=500, detail=str(e))

