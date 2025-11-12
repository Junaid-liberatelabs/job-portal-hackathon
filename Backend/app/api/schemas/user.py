from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    education_level: str
    preferred_career_track: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    education_level: str
    preferred_career_track: str
    is_active: bool

    class Config:
        from_attributes = True  # For SQLAlchemy ORM compatibility

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None