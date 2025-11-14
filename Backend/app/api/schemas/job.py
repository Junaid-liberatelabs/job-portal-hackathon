from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from app.db.model.job import ExperienceLevel, JobLocation, JobType
from pydantic import BaseModel, Field, field_validator


# Base schema with common fields
class JobBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    company: str = Field(..., min_length=1, max_length=255)
    job_type: JobType
    job_location: Optional[JobLocation] = None
    required_skills: List[str] = Field(..., min_items=1)
    url: Optional[str] = Field(None, min_length=1, max_length=255)
    recommended_experience_level: ExperienceLevel
    salary_range_min: Optional[float] = Field(None, ge=0)
    salary_range_max: Optional[float] = Field(None, ge=0)

    @field_validator("required_skills")
    @classmethod
    def validate_skills(cls, v):
        """Ensure all skills are non-empty strings"""
        if not v:
            raise ValueError("At least one skill is required")
        for skill in v:
            if not skill or not skill.strip():
                raise ValueError("Skills cannot be empty strings")
        return [skill.strip() for skill in v]

    @field_validator("salary_range_max")
    @classmethod
    def validate_salary_range(cls, v, info):
        """Ensure salary_range_max >= salary_range_min if both are provided"""
        if v is not None and info.data.get("salary_range_min") is not None:
            if v < info.data["salary_range_min"]:
                raise ValueError(
                    "salary_range_max must be greater than or equal to salary_range_min"
                )
        return v


# Schema for creating a job
class JobCreate(JobBase):
    pass


# Schema for updating a job
class JobUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1)
    company: Optional[str] = Field(None, min_length=1, max_length=255)
    job_type: Optional[JobType] = None
    job_location: Optional[JobLocation] = None
    url: Optional[str] = Field(None, min_length=1, max_length=255)
    required_skills: Optional[List[str]] = Field(None, min_items=1)
    recommended_experience_level: Optional[ExperienceLevel] = None
    salary_range_min: Optional[float] = Field(None, ge=0)
    salary_range_max: Optional[float] = Field(None, ge=0)

    @field_validator("required_skills")
    @classmethod
    def validate_skills(cls, v):
        """Ensure all skills are non-empty strings"""
        if v is not None:
            if not v:
                raise ValueError("At least one skill is required")
            for skill in v:
                if not skill or not skill.strip():
                    raise ValueError("Skills cannot be empty strings")
            return [skill.strip() for skill in v]
        return v

    @field_validator("salary_range_max")
    @classmethod
    def validate_salary_range(cls, v, info):
        """Ensure salary_range_max >= salary_range_min if both are provided"""
        if v is not None and info.data.get("salary_range_min") is not None:
            if v < info.data["salary_range_min"]:
                raise ValueError(
                    "salary_range_max must be greater than or equal to salary_range_min"
                )
        return v


# Schema for job response (includes all fields from database)
class JobResponse(BaseModel):
    id: str
    title: str
    description: str
    company: str
    job_type: JobType
    url: str
    job_location: Optional[JobLocation]
    required_skills: List[str]
    recommended_experience_level: ExperienceLevel
    salary_range_min: Optional[float]
    salary_range_max: Optional[float]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # For SQLAlchemy ORM compatibility


# Schema for job in database (internal use, same as response for now)
class JobInDB(JobResponse):
    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
