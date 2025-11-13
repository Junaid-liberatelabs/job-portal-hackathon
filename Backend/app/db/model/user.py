import uuid

from app.db.base import Base
from sqlalchemy import ARRAY, Boolean, Column, DateTime, String, func, Integer, Float
from pgvector.sqlalchemy import Vector


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    education_level = Column(String, nullable=False)
    preferred_career_track = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    skills = Column(ARRAY(String), nullable=False, default=list, server_default="{}")
    is_active = Column(Boolean, nullable=False, default=True, server_default="true")
    created_at = Column(
        DateTime, nullable=False, default=func.now(), server_default=func.now()
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        server_default=func.now(),
    )
    embedding = Column(Vector(384), nullable=True)

    #optional fields
    profile_picture = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    location = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    github_url = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    field_of_study = Column(String, nullable=True)
    graduation_year = Column(Integer, nullable=True)
    cgpa = Column(Float, nullable=True)


    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, full_name={self.full_name}, skills={self.skills}, is_active={self.is_active})>"
