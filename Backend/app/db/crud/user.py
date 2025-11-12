from sqlalchemy.orm import Session
from app.db.model.user import User
from app.api.schemas.user import UserRegister
from app.auth.security import get_password_hash
import uuid
def get_user_by_email(db: Session, email: str):
    """Get user by email"""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserRegister):
    """Create a new user"""
    hashed_password = get_password_hash(user.password)
    
    db_user = User(
        id=uuid.uuid4(),
        full_name=user.full_name,
        email=user.email,
        education_level=user.education_level,
        preferred_career_track=user.preferred_career_track,
        hashed_password=hashed_password,
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
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
