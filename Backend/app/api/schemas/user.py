from typing import List, Optional

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


# Base schema with common fields
class UserBase(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    education_level: str = Field(..., min_length=1, max_length=255)
    preferred_career_track: str = Field(..., min_length=1, max_length=255)


# Schema for user registration
class UserRegister(UserBase):
    password: str = Field(..., min_length=8)
    skills: List[str] = Field(default_factory=list)


# Schema for user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema for updating user profile
class UserUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=1, max_length=255)
    education_level: Optional[str] = Field(None, min_length=1, max_length=255)
    preferred_career_track: Optional[str] = Field(None, min_length=1, max_length=255)
    skills: Optional[List[str]] = None
    #new information fields
    field_of_study: Optional[str] = Field(None, min_length=1, max_length=255)
    cgpa: Optional[float] = Field(None, ge=0.0, le=4.0)
    location: Optional[str] = Field(None, min_length=1, max_length=255)
    linkedin_url: Optional[str] = Field(None, min_length=1, max_length=255)
    github_url: Optional[str] = Field(None, min_length=1, max_length=255)
    phone_number: Optional[str] = Field(None, min_length=1, max_length=255)
    graduation_year: Optional[int] = Field(None, ge=1900, le=2025)
    profile_picture: Optional[str] = Field(None, min_length=1, max_length=255)
    bio: Optional[str] = Field(None, min_length=1, max_length=255)


# Schema for managing user skills
class UserSkillsUpdate(BaseModel):
    skills: List[str] = Field(..., min_items=1)


# Schema for user response (includes all fields from database)
class UserResponse(BaseModel):
    id: str
    full_name: str
    email: str
    education_level: str
    preferred_career_track: str
    skills: List[str]
    is_active: bool
    #new information fields
    field_of_study: Optional[str] = Field(None, min_length=1, max_length=255)
    cgpa: Optional[float] = Field(None, ge=0.0, le=4.0)
    location: Optional[str] = Field(None, min_length=1, max_length=255)
    linkedin_url: Optional[str] = Field(None, min_length=1, max_length=255)
    github_url: Optional[str] = Field(None, min_length=1, max_length=255)
    phone_number: Optional[str] = Field(None, min_length=1, max_length=255)
    graduation_year: Optional[int] = Field(None, ge=1900, le=2025)
    profile_picture: Optional[str] = Field(None, min_length=1, max_length=255)
    bio: Optional[str] = Field(None, min_length=1, max_length=255)
    
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # For SQLAlchemy ORM compatibility


# Schema for user in database (internal use)
class UserInDB(UserResponse):
    hashed_password: str


# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    user_id: str | None = None
