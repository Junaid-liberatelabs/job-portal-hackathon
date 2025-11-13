"""
Pydantic schemas for recommendation responses with similarity scores.
"""
from pydantic import BaseModel, Field

from app.api.schemas.job import JobResponse
from app.api.schemas.resources import ResourceResponse


class JobRecommendation(BaseModel):
    """Job with similarity score"""
    job: JobResponse
    similarity_score: float = Field(..., ge=0, le=1, description="Cosine similarity score between 0 and 1")
    
    class Config:
        from_attributes = True


class ResourceRecommendation(BaseModel):
    """Resource with similarity score"""
    resource: ResourceResponse
    similarity_score: float = Field(..., ge=0, le=1, description="Cosine similarity score between 0 and 1")
    
    class Config:
        from_attributes = True
