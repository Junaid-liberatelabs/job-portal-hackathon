from datetime import timedelta
from typing import Annotated

from app.db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.schemas.job import (JobCreate, JobInDB, JobResponse, JobUpdate)
router = APIRouter()


@router.post("/", response_model=JobResponse)
async def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = JobInDB(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: str, db: Session = Depends(get_db)):
    job = db.query(JobInDB).filter(JobInDB.id == job_id).first()
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not found"
        )
    return job

@router.put("/{job_id}", response_model=JobResponse)
async def update_job(job_id: str, job: JobUpdate, db: Session = Depends(get_db)):
    db_job = db.query(JobInDB).filter(JobInDB.id == job_id).first()
    if not db_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not found"
        )
    for key, value in job.dict().items():
        setattr(db_job, key, value)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.delete("/{job_id}")
async def delete_job(job_id: str, db: Session = Depends(get_db)):
    db_job = db.query(JobInDB).filter(JobInDB.id == job_id).first()
    if not db_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not found"
        )
    db.delete(db_job)
    db.commit()
    return {"message": "Job deleted successfully"}