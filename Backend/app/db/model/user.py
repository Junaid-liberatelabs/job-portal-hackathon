from sqlalchemy import Column, String, Boolean, ARRAY
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    education_level = Column(String, nullable=False)
    preferred_career_track = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    # skills = Column(ARRAY(String), nullable=False)