import uuid
from enum import Enum as PyEnum
from pgvector.sqlalchemy import Vector

from app.db.base import Base
from sqlalchemy import (ARRAY, Column, DateTime, Enum, Float, Index, String,
                        func)


class JobType(PyEnum):
    # Internship / Part-time / Full-time / Freelance
    INTERNSHIP = "internship"
    PART_TIME = "part_time"
    FULL_TIME = "full_time"
    FREELANCE = "freelance"


class JobLocation(PyEnum):
    REMOTE = "remote"
    HYBRID = "hybrid"
    ON_SITE = "on_site"


class ExperienceLevel(PyEnum):
    STUDENT = "student"
    ENTRY = "entry"
    JUNIOR = "junior"  # included for a touch of flexibility


class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    company = Column(String, nullable=False)
    job_type = Column(Enum(JobType), nullable=False, index=True)  # mandatory
    job_location = Column(Enum(JobLocation), nullable=True)  # optional

    required_skills = Column(ARRAY(String), nullable=False, default=list)

    recommended_experience_level = Column(
        Enum(ExperienceLevel), nullable=False, index=True
    )

    salary_range_min = Column(Float, nullable=True)  # optional
    salary_range_max = Column(Float, nullable=True)  # optional

    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    embedding = Column(Vector(384), nullable=True)

    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title}, company={self.company}, job_type={self.job_type}, job_location={self.job_location}, required_skills={self.required_skills}, recommended_experience_level={self.recommended_experience_level}, salary_range_min={self.salary_range_min}, salary_range_max={self.salary_range_max})>"
