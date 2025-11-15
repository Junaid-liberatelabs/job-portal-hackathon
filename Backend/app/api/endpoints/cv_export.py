from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Annotated

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.db.model.user import User
from app.core.logging_config import get_logger
from app.api.schemas.user import UserResponse
from app.api.schemas.job import JobResponse
from app.db.crud.application import get_applications_by_user
from app.db.crud.job import get_job_by_id
from app.llm.workflow.cv_generation.graph import cv_generation_graph

router = APIRouter()
logger = get_logger(__name__)


@router.get("/cv-export", response_class=HTMLResponse)
async def export_cv(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
) -> HTMLResponse:
    """
    Export the authenticated user's profile and job applications as an HTML CV optimized for PDF printing.
    
    Args:
        current_user: The authenticated user (injected by dependency)
        db: Database session (injected by dependency)
        
    Returns:
        HTMLResponse containing the formatted CV ready for PDF printing
        
    Raises:
        HTTPException: 401 if user is not authenticated (handled by dependency)
        HTTPException: 500 if there's an error generating the CV
    """
    try:
        # Compile the graph
        graph = cv_generation_graph.compile()
        
        # Convert user model to dict with all available data
        user_profile_data = UserResponse.model_validate(current_user).model_dump()
        
        # Get all applications for the user
        applications = get_applications_by_user(db, current_user.id)
        
        # Extract job IDs and get job details
        job_ids = [application.job_id for application in applications]
        jobs = [get_job_by_id(db, job_id) for job_id in job_ids]
        
        # Filter out None jobs (in case a job was deleted) and convert to dicts
        user_applied_job_data = [
            JobResponse.model_validate(job).model_dump() 
            for job in jobs 
            if job is not None
        ]
        
        # Prepare input data for the graph
        input_data = {
            "user_profile_data": user_profile_data,
            "user_applied_job_data": user_applied_job_data,
        }
        
        # Invoke the graph to generate HTML CV
        result = graph.invoke(input_data)
        html_cv = result["html_cv"]
        
        # Return HTML response optimized for PDF printing
        return HTMLResponse(content=html_cv, status_code=200)
        
    except SQLAlchemyError as e:
        logger.error(f"Database error in CV export: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail="Database error occurred while generating CV"
        )
    except ValueError as e:
        logger.error(f"Data validation error in CV export: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Incomplete user profile data: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error in CV export: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail=f"Error generating CV: {str(e)}"
        )
