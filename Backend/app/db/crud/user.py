import logging
import uuid

from app.api.schemas.user import UserRegister
from app.auth.security import get_password_hash
from app.core.exceptions import EmbeddingGenerationError
from app.db.model.user import User
from app.services.embedding_service import embedding_service
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


def get_user_by_email(db: Session, email: str):
    """Get user by email"""
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserRegister):
    """Create a new user with optional skills"""
    hashed_password = get_password_hash(user.password)

    db_user = User(
        id=str(uuid.uuid4()),
        full_name=user.full_name,
        email=user.email,
        education_level=user.education_level,
        preferred_career_track=user.preferred_career_track,
        hashed_password=hashed_password,
        skills=user.skills,  # Skills from UserRegister schema (defaults to empty list)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Generate and store embedding
    try:
        embedding = embedding_service.generate_user_embedding(db_user)
        db_user.embedding = embedding
        db.commit()
        db.refresh(db_user)
        logger.info(f"Successfully generated embedding for user {db_user.id}")
    except EmbeddingGenerationError as e:
        logger.error(f"Failed to generate embedding for user {db_user.id}: {e}")
        # Continue without embedding - user creation should not fail

    return db_user


def authenticate_user(db: Session, email: str, password: str):
    """Authenticate user with email and password"""
    from app.auth.security import verify_password

    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def get_user_by_id(db: Session, user_id: str):
    """Get user by ID"""
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: str, update_data: dict):
    """Update user profile"""
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    # Check if embedding-relevant fields are being updated
    embedding_fields = {
        "skills",
        "education_level",
        "preferred_career_track",
        "field_of_study",
        "cgpa",
        "location",
        "preferred_job_location",
        "preferred_job_type",
        "bio",
    }
    should_regenerate_embedding = any(
        field in update_data for field in embedding_fields
    )

    for key, value in update_data.items():
        if hasattr(user, key) and key not in ["id", "hashed_password", "created_at"]:
            setattr(user, key, value)

    db.commit()
    db.refresh(user)

    # Regenerate embedding if relevant fields changed
    if should_regenerate_embedding:
        try:
            embedding = embedding_service.generate_user_embedding(user)
            user.embedding = embedding
            db.commit()
            db.refresh(user)
            logger.info(f"Successfully regenerated embedding for user {user.id}")
        except EmbeddingGenerationError as e:
            logger.error(f"Failed to regenerate embedding for user {user.id}: {e}")
            # Continue without embedding update

    return user


def add_user_skill(db: Session, user_id: str, skill: str):
    """Add a skill to user's skills array"""
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    if skill and skill not in user.skills:
        user.skills = user.skills + [skill]
        db.commit()
        db.refresh(user)

        # Regenerate embedding since skills changed
        try:
            embedding = embedding_service.generate_user_embedding(user)
            user.embedding = embedding
            db.commit()
            db.refresh(user)
            logger.info(
                f"Successfully regenerated embedding for user {user.id} after adding skill"
            )
        except EmbeddingGenerationError as e:
            logger.error(f"Failed to regenerate embedding for user {user.id}: {e}")

    return user


def remove_user_skill(db: Session, user_id: str, skill: str):
    """Remove a skill from user's skills array"""
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    if skill in user.skills:
        user.skills = [s for s in user.skills if s != skill]
        db.commit()
        db.refresh(user)

        # Regenerate embedding since skills changed
        try:
            embedding = embedding_service.generate_user_embedding(user)
            user.embedding = embedding
            db.commit()
            db.refresh(user)
            logger.info(
                f"Successfully regenerated embedding for user {user.id} after removing skill"
            )
        except EmbeddingGenerationError as e:
            logger.error(f"Failed to regenerate embedding for user {user.id}: {e}")

    return user


def get_users_by_skills(
    db: Session, skills: list[str], skip: int = 0, limit: int = 100
):
    """Get users that have any of the specified skills"""
    return (
        db.query(User)
        .filter(User.skills.overlap(skills))
        .offset(skip)
        .limit(limit)
        .all()
    )
