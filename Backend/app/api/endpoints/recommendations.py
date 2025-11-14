"""
API endpoints for personalized recommendations based on vector similarity.
"""

from typing import Annotated, List

from app.api.schemas.recommendation import JobRecommendation, ResourceRecommendation
from app.auth.dependencies import get_current_user
from app.core.exceptions import EmbeddingNotAvailableError
from app.db.model.user import User
from app.db.session import get_db
from app.services.recommendation_service import recommendation_service
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/jobs", response_model=List[JobRecommendation])
async def get_job_recommendations(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    limit: int = Query(
        10, ge=1, le=50, description="Maximum number of recommendations to return"
    ),
):
    """
    Get personalized job recommendations for the authenticated user.

    Uses a hybrid approach combining:
    - **TF-IDF** (40%): Keyword-based similarity for exact skill/term matching
    - **Vector Embeddings** (60%): Semantic similarity for contextual understanding

    Returns jobs ranked by combined similarity score to the user's profile (skills, education, career track).
    Each result includes the job details and a similarity score (0-1).

    - **limit**: Maximum number of recommendations (default: 10, max: 50)

    Requires authentication.
    """
    # Check if user has an embedding
    if current_user.embedding is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User profile embedding not available. Please update your profile.",
        )

    # Get recommended jobs using hybrid TF-IDF + vector similarity
    results = recommendation_service.get_recommended_jobs(
        db=db,
        user_embedding=current_user.embedding,
        user=current_user,  # Pass user for TF-IDF calculation
        limit=limit,
    )

    # Format response with similarity scores
    recommendations = [
        JobRecommendation(job=job, similarity_score=score) for job, score in results
    ]

    return recommendations


@router.get("/resources", response_model=List[ResourceRecommendation])
async def get_resource_recommendations(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    limit: int = Query(
        10, ge=1, le=50, description="Maximum number of recommendations to return"
    ),
):
    """
    Get personalized learning resource recommendations for the authenticated user.

    Uses a hybrid approach combining:
    - **TF-IDF** (40%): Keyword-based similarity for exact skill/term matching
    - **Vector Embeddings** (60%): Semantic similarity for contextual understanding

    Returns resources ranked by combined similarity score to the user's profile (skills, education, career track).
    Each result includes the resource details and a similarity score (0-1).

    - **limit**: Maximum number of recommendations (default: 10, max: 50)

    Requires authentication.
    """
    # Check if user has an embedding
    if current_user.embedding is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User profile embedding not available. Please update your profile.",
        )

    # Get recommended resources using hybrid TF-IDF + vector similarity
    results = recommendation_service.get_recommended_resources(
        db=db,
        user_embedding=current_user.embedding,
        user=current_user,  # Pass user for TF-IDF calculation
        limit=limit,
    )

    # Format response with similarity scores
    recommendations = [
        ResourceRecommendation(resource=resource, similarity_score=score)
        for resource, score in results
    ]

    return recommendations
