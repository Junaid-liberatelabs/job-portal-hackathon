from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


# Base schema with common fields
class ResourceBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    url: HttpUrl  # Pydantic's HttpUrl type validates URL format
    tags: Optional[List[str]] = Field(default_factory=list)
    pricing: Optional[str] = Field(None, min_length=1, max_length=255)
    platform: Optional[str] = Field(None, min_length=1, max_length=255)
    duration: Optional[str] = Field(None, min_length=1, max_length=255)


# Schema for creating a resource
class ResourceCreate(ResourceBase):
    pass


# Schema for updating a resource
class ResourceUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1)
    url: Optional[HttpUrl] = None
    tags: Optional[List[str]] = None


# Schema for resource response (includes all fields from database)
class ResourceResponse(BaseModel):
    id: str
    name: str
    description: str
    url: str  # HttpUrl is converted to string in response
    tags: List[str]
    pricing: Optional[str] = Field(None, min_length=1, max_length=255)
    platform: Optional[str] = Field(None, min_length=1, max_length=255)
    duration: Optional[str] = Field(None, min_length=1, max_length=255)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # For SQLAlchemy ORM compatibility


# Schema for resource in database (internal use, same as response for now)
class ResourceInDB(ResourceResponse):
    pass
