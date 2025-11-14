from fastapi import APIRouter, Depends, UploadFile, File
from app.llm.workflow.skills_extraction.state import SkillsExtractionState
from app.services.pdf_extraction import extract_pdf

router = APIRouter()

@router.post("/analyze")
async def analyze_skills(file: UploadFile = File(...)):
    text = extract_pdf(file)
    return {"text": text}