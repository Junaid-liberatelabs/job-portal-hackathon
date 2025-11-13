from typing import List, Optional

from app.db.crud.job import (
    create_job as crud_create_job,
    delete_job as crud_delete_job,
    get_job_by_id,
    get_jobs,
    update_job as crud_update_job,
)
from app.db.model.job import ExperienceLevel, JobType
from app.db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.schemas.job import JobCreate, JobResponse, JobUpdate

router = APIRouter()


@router.post("/", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
async def create_job(job: JobCreate, db: Session = Depends(get_db)):
    """
    Create a new job listing.
    
    - **title**: Job title (required)
    - **description**: Job description (required)
    - **company**: Company name (required)
    - **job_type**: Type of job (INTERNSHIP, PART_TIME, FULL_TIME, FREELANCE)
    - **job_location**: Location type (REMOTE, HYBRID, ON_SITE) - optional
    - **required_skills**: List of required skills (at least 1)
    - **recommended_experience_level**: Experience level (STUDENT, ENTRY, JUNIOR)
    - **salary_range_min**: Minimum salary - optional
    - **salary_range_max**: Maximum salary - optional
    """
    try:
        job_data = job.model_dump()
        new_job = crud_create_job(db, job_data)
        return new_job
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create job: {str(e)}",
        )

@router.get("/", response_model=List[JobResponse])
async def list_jobs(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    job_type: Optional[JobType] = Query(None, description="Filter by job type"),
    experience_level: Optional[ExperienceLevel] = Query(None, description="Filter by experience level"),
    skills: Optional[str] = Query(None, description="Comma-separated list of skills to filter by"),
    db: Session = Depends(get_db),
):
    """
    Get a list of jobs with optional filtering.
    
    - **skip**: Number of records to skip (for pagination)
    - **limit**: Maximum number of records to return (default: 100, max: 1000)
    - **job_type**: Filter by job type (INTERNSHIP, PART_TIME, FULL_TIME, FREELANCE)
    - **experience_level**: Filter by experience level (STUDENT, ENTRY, JUNIOR)
    - **skills**: Comma-separated list of skills (e.g., "Python,JavaScript")
    """
    # Parse skills if provided
    skills_list = None
    if skills:
        skills_list = [s.strip() for s in skills.split(",") if s.strip()]
    
    jobs = get_jobs(
        db=db,
        skip=skip,
        limit=limit,
        job_type=job_type,
        experience_level=experience_level,
        skills=skills_list,
    )
    return jobs


@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: str, db: Session = Depends(get_db)):
    """
    Get a specific job by ID.
    
    - **job_id**: The unique identifier of the job
    """
    job = get_job_by_id(db, job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )
    return job

@router.put("/{job_id}", response_model=JobResponse)
async def update_job(job_id: str, job: JobUpdate, db: Session = Depends(get_db)):
    """
    Update an existing job listing.
    
    - **job_id**: The unique identifier of the job to update
    - All fields are optional - only provided fields will be updated
    """
    update_data = job.model_dump(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update",
        )
    
    updated_job = crud_update_job(db, job_id, update_data)
    
    if not updated_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )
    
    return updated_job

@router.delete("/{job_id}", status_code=status.HTTP_200_OK)
async def delete_job(job_id: str, db: Session = Depends(get_db)):
    """
    Delete a job listing.
    
    - **job_id**: The unique identifier of the job to delete
    """
    success = crud_delete_job(db, job_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )
    
    return {"message": "Job deleted successfully"}