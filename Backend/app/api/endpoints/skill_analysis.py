from fastapi import APIRouter
from app.services.pdf_extraction import extract_pdf
from app.api.schemas.skill_analysis import SkillAnalysisResponse
from fastapi import HTTPException
from app.llm.workflow.skills_extraction.graph import skill_extraction_graph
from fastapi import UploadFile, File
from app.auth.dependencies import get_current_user
from app.db.model.user import User
from app.db.session import get_db
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends
router = APIRouter()
from app.core.logging_config import get_logger
from app.db.crud.user import update_user,add_user_skill
logger = get_logger(__name__)




@router.post("/analyze")
async def analyze_skills(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    file: UploadFile = File(...),
):

    #if both cv_content and file are not provided, raise an error
    # if not request:
    #     raise HTTPException(status_code=400, detail="File must be provided")

    cv_text = extract_pdf(file)
    # print(cv_text)

    try:
        graph = skill_extraction_graph.compile()
        input_data = {
            "file_data": cv_text,
        }
        result = graph.invoke(input_data)
        if result.get("analysis_output") is None:
            raise HTTPException(status_code=500, detail="Failed to extract skills from the document")
        for skill in result["analysis_output"].key_skills:
            add_user_skill(db, current_user.id, skill)

        for tools in result["analysis_output"].tools_and_technologies:
            add_user_skill(db, current_user.id, tools)
        #analysis output is list of strings so we need to join them into a single string
        brief_experience = ", ".join(result["analysis_output"].relevant_roles)
        update_user(db, current_user.id, {"brief_experience": brief_experience})

        return SkillAnalysisResponse(analysis_output=result["analysis_output"])

    except Exception as e:
        logger.error(f"Error analyzing skills: {e}")
        raise HTTPException(status_code=500, detail=str(e))

