from sqlalchemy.orm import Session
from app.db.model.application import ApplicationList


def create_application(db: Session, user_id: str, job_id: str):
    """Create a new job application"""
    application = ApplicationList(user_id=user_id, job_id=job_id)
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


def get_application(db: Session, application_id: str):
    """Get a specific application by ID"""
    return db.query(ApplicationList).filter(ApplicationList.id == application_id).first()


def get_user_application_for_job(db: Session, user_id: str, job_id: str):
    """Check if user has already applied for a specific job"""
    return db.query(ApplicationList).filter(
        ApplicationList.user_id == user_id,
        ApplicationList.job_id == job_id
    ).first()


def get_applications_by_job(db: Session, job_id: str):
    """Get all applications for a specific job"""
    return db.query(ApplicationList).filter(ApplicationList.job_id == job_id).all()


def get_applications_by_user(db: Session, user_id: str):
    """Get all applications made by a specific user"""
    return db.query(ApplicationList).filter(ApplicationList.user_id == user_id).all()


def delete_application(db: Session, application_id: str):
    """Delete an application by ID"""
    application = get_application(db, application_id)
    if application:
        db.delete(application)
        db.commit()
        return True
    return False


def cancel_user_application(db: Session, user_id: str, job_id: str):
    """Cancel a user's application for a specific job"""
    application = get_user_application_for_job(db, user_id, job_id)
    if application:
        db.delete(application)
        db.commit()
        return True
    return False

