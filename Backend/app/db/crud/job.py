import logging
import uuid
from typing import Optional

from app.core.exceptions import EmbeddingGenerationError
from app.db.model.job import ExperienceLevel, Job, JobType
from app.services.embedding_service import embedding_service
from sqlalchemy.orm import Session
from sqlalchemy import func, cast
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.types import String

logger = logging.getLogger(__name__)


def create_job(db: Session, job_data: dict):
    """Create a new job listing"""
    db_job = Job(id=str(uuid.uuid4()), **job_data)

    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    
    # Generate and store embedding
    try:
        embedding = embedding_service.generate_job_embedding(db_job)
        db_job.embedding = embedding
        db.commit()
        db.refresh(db_job)
        logger.info(f"Successfully generated embedding for job {db_job.id}")
    except EmbeddingGenerationError as e:
        logger.error(f"Failed to generate embedding for job {db_job.id}: {e}")
        # Continue without embedding - job creation should not fail
    
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
        # Use PostgreSQL && (overlap) operator for array matching
        # This checks if any of the user's skills match any of the job's required skills
        query = query.filter(Job.required_skills.op('&&')(cast(skills, ARRAY(String))))

    return query.offset(skip).limit(limit).all()


def update_job(db: Session, job_id: str, update_data: dict):
    """Update a job listing"""
    job = get_job_by_id(db, job_id)
    if not job:
        return None

    # Check if embedding-relevant fields are being updated
    embedding_fields = {"title", "description", "required_skills", "recommended_experience_level"}
    should_regenerate_embedding = any(field in update_data for field in embedding_fields)

    for key, value in update_data.items():
        if hasattr(job, key) and key not in ["id", "created_at"]:
            setattr(job, key, value)

    db.commit()
    db.refresh(job)
    
    # Regenerate embedding if relevant fields changed
    if should_regenerate_embedding:
        try:
            embedding = embedding_service.generate_job_embedding(job)
            job.embedding = embedding
            db.commit()
            db.refresh(job)
            logger.info(f"Successfully regenerated embedding for job {job.id}")
        except EmbeddingGenerationError as e:
            logger.error(f"Failed to regenerate embedding for job {job.id}: {e}")
            # Continue without embedding update
    
    return job


def delete_job(db: Session, job_id: str):
    """Delete a job listing"""
    job = get_job_by_id(db, job_id)
    if not job:
        return False

    db.delete(job)
    db.commit()
    return True
