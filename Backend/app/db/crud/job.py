import uuid
from typing import Optional

from app.db.model.job import ExperienceLevel, Job, JobType
from sqlalchemy.orm import Session


def create_job(db: Session, job_data: dict):
    """Create a new job listing"""
    db_job = Job(id=str(uuid.uuid4()), **job_data)

    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_job_by_id(db: Session, job_id: str):
    """Get job by ID"""
    return db.query(Job).filter(Job.id == job_id).first()


def get_jobs(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    job_type: Optional[JobType] = None,
    experience_level: Optional[ExperienceLevel] = None,
    skills: Optional[list[str]] = None,
):
    """Get jobs with optional filtering"""
    query = db.query(Job)

    if job_type:
        query = query.filter(Job.job_type == job_type)

    if experience_level:
        query = query.filter(Job.recommended_experience_level == experience_level)

    if skills:
        query = query.filter(Job.required_skills.overlap(skills))

    return query.offset(skip).limit(limit).all()


def update_job(db: Session, job_id: str, update_data: dict):
    """Update a job listing"""
    job = get_job_by_id(db, job_id)
    if not job:
        return None

    for key, value in update_data.items():
        if hasattr(job, key) and key not in ["id", "created_at"]:
            setattr(job, key, value)

    db.commit()
    db.refresh(job)
    return job


def delete_job(db: Session, job_id: str):
    """Delete a job listing"""
    job = get_job_by_id(db, job_id)
    if not job:
        return False

    db.delete(job)
    db.commit()
    return True
