from datetime import datetime
from pydantic import BaseModel
from app.api.schemas.user import UserResponse
from app.api.schemas.job import JobResponse


class ApplicationBase(BaseModel):
    job_id: str
    user_id: str


class ApplicationCreate(BaseModel):
    job_id: str


class ApplicationResponse(BaseModel):
    id: str
    user_id: str
    job_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ApplicantInfo(BaseModel):
    """Information about a user who applied for a job"""
    application_id: str
    user_id: str
    applied_at: datetime
    user: UserResponse

    class Config:
        from_attributes = True


class JobWithApplicantsCount(BaseModel):
    """Job with count of applicants - for admin dashboard"""
    job: JobResponse
    applicants_count: int

    class Config:
        from_attributes = True

