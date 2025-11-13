from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.schemas.application import ApplicationCreate, ApplicationResponse, ApplicantInfo, JobWithApplicantsCount
from app.api.schemas.user import UserResponse
from app.auth.dependencies import get_current_user
from app.db.crud.application import (
    cancel_user_application,
    create_application,
    get_applications_by_job,
    get_applications_by_user,
    get_user_application_for_job,
)
from app.db.crud.job import get_job_by_id, get_jobs
from app.db.crud.user import get_user_by_id
from app.db.model.user import User
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
async def apply_for_job(
    application: ApplicationCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    """
    Apply for a job. Users can apply for jobs they're interested in.
    
    - **job_id**: The ID of the job to apply for
    """
    job = get_job_by_id(db, application.job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )
    
    existing_application = get_user_application_for_job(db, current_user.id, application.job_id)
    if existing_application:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already applied for this job",
        )
    
    new_application = create_application(db, current_user.id, application.job_id)
    return new_application


@router.get("/my-applications", response_model=List[ApplicationResponse])
async def get_my_applications(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    """
    Get all applications made by the current user.
    """
    applications = get_applications_by_user(db, current_user.id)
    return applications


@router.delete("/cancel/{job_id}", status_code=status.HTTP_200_OK)
async def cancel_application(
    job_id: str,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    """
    Cancel your application for a specific job.
    Users can only cancel their own applications.
    
    - **job_id**: The ID of the job to cancel application for
    """
    # Check if application exists
    application = get_user_application_for_job(db, current_user.id, job_id)
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found. You have not applied for this job.",
        )
    
    # Cancel the application
    success = cancel_user_application(db, current_user.id, job_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to cancel application",
        )
    
    return {
        "message": "Application cancelled successfully",
        "job_id": job_id
    }



@router.get("/job/{job_id}/check", response_model=dict)
async def check_application_status(
    job_id: str,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    """
    Check if the current user has applied for a specific job.
    
    - **job_id**: The ID of the job
    
    Returns whether the user has applied and the application details if exists.
    """
    application = get_user_application_for_job(db, current_user.id, job_id)
    
    return {
        "has_applied": application is not None,
        "application": ApplicationResponse.model_validate(application) if application else None,
    }


@router.get("/dashboard", response_model=List[JobWithApplicantsCount])
async def get_jobs_with_applicants_dashboard(
    db: Session = Depends(get_db),
):
    """
    Admin dashboard: Get all jobs with applicant counts.
    Returns a list of all jobs with the number of applicants for each.
    
    This endpoint is for admins to see an overview of all jobs and how many people applied.
    """
    jobs = get_jobs(db, skip=0, limit=1000)
    
    jobs_with_counts = []
    for job in jobs:
        applications = get_applications_by_job(db, job.id)
        applicant_count = len(applications)
        
        jobs_with_counts.append(
            JobWithApplicantsCount(
                job=job,
                applicants_count=applicant_count
            )
        )
    
    return jobs_with_counts


@router.get("/job/{job_id}/applicants", response_model=List[ApplicantInfo])
async def get_job_applicants(
    job_id: str,
    db: Session = Depends(get_db),
):
    """
    Get all users who applied for a specific job.
    This endpoint is for admins to see the list of applicants.
    
    - **job_id**: The ID of the job
    
    Returns a list of applicants with their user information.
    """
    job = get_job_by_id(db, job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )
    
    applications = get_applications_by_job(db, job_id)
    
    applicants = []
    for application in applications:
        user = get_user_by_id(db, application.user_id)
        if user:
            applicants.append(
                ApplicantInfo(
                    application_id=application.id,
                    user_id=application.user_id,
                    applied_at=application.created_at,
                    user=UserResponse.model_validate(user),
                )
            )
    
    return applicants