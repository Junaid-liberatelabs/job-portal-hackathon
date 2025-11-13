from typing import List, Optional

from app.api.schemas.recommendation import ResourceRecommendation
from app.api.schemas.resources import (
    ResourceCreate,
    ResourceResponse,
    ResourceUpdate,
)
from app.db.crud.resources import (
    create_resource as crud_create_resource,
    delete_resource as crud_delete_resource,
    get_resource_by_id,
    get_resources,
    update_resource as crud_update_resource,
)
from app.db.session import get_db
from app.services.recommendation_service import recommendation_service
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ResourceResponse, status_code=status.HTTP_201_CREATED)
async def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    """
    Create a new learning resource.
    
    - **name**: Resource name (required)
    - **description**: Resource description (required)
    - **url**: Resource URL (required, must be valid URL)
    - **tags**: List of tags for categorization (optional)
    """
    try:
        # Use mode='json' to convert HttpUrl to string
        resource_data = resource.model_dump(mode='json')
        new_resource = crud_create_resource(db, resource_data)
        return new_resource
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create resource: {str(e)}",
        )


@router.get("/", response_model=List[ResourceResponse])
async def list_resources(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    tags: Optional[str] = Query(None, description="Comma-separated list of tags to filter by"),
    db: Session = Depends(get_db),
):
    """
    Get a list of learning resources with optional filtering.
    
    - **skip**: Number of records to skip (for pagination)
    - **limit**: Maximum number of records to return (default: 100, max: 1000)
    - **tags**: Comma-separated list of tags (e.g., "Python,Web Development")
    """
    # Parse tags if provided
    tags_list = None
    if tags:
        tags_list = [t.strip() for t in tags.split(",") if t.strip()]
    
    resources = get_resources(
        db=db,
        skip=skip,
        limit=limit,
        tags=tags_list,
    )
    return resources


@router.get("/{resource_id}", response_model=ResourceResponse)
async def get_resource(resource_id: str, db: Session = Depends(get_db)):
    """
    Get a specific learning resource by ID.
    
    - **resource_id**: The unique identifier of the resource
    """
    resource = get_resource_by_id(db, resource_id)
    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )
    return resource


@router.put("/{resource_id}", response_model=ResourceResponse)
async def update_resource(
    resource_id: str, resource: ResourceUpdate, db: Session = Depends(get_db)
):
    """
    Update an existing learning resource.
    
    - **resource_id**: The unique identifier of the resource to update
    - All fields are optional - only provided fields will be updated
    """
    # Use mode='json' to convert HttpUrl to string
    update_data = resource.model_dump(exclude_unset=True, mode='json')
    
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update",
        )
    
    updated_resource = crud_update_resource(db, resource_id, update_data)
    
    if not updated_resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )
    
    return updated_resource


@router.delete("/{resource_id}", status_code=status.HTTP_200_OK)
async def delete_resource(resource_id: str, db: Session = Depends(get_db)):
    """
    Delete a learning resource.
    
    - **resource_id**: The unique identifier of the resource to delete
    """
    success = crud_delete_resource(db, resource_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )
    
    return {"message": "Resource deleted successfully"}


@router.get("/{resource_id}/similar", response_model=List[ResourceRecommendation])
async def get_similar_resources(
    resource_id: str,
    limit: int = Query(5, ge=1, le=20, description="Maximum number of similar resources to return"),
    db: Session = Depends(get_db),
):
    """
    Get learning resources similar to the specified resource based on vector similarity.
    
    Returns resources ranked by similarity to the specified resource's content (name, description, tags).
    Each result includes the resource details and a similarity score (0-1).
    
    - **resource_id**: The unique identifier of the resource to find similar resources for
    - **limit**: Maximum number of similar resources (default: 5, max: 20)
    """
    # Get the specified resource
    resource = get_resource_by_id(db, resource_id)
    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )
    
    # Check if resource has an embedding
    if resource.embedding is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Resource embedding not available",
        )
    
    # Get similar resources using cosine similarity
    results = recommendation_service.get_similar_resources(
        db=db,
        resource_embedding=resource.embedding,
        exclude_resource_id=resource_id,
        limit=limit
    )
    
    # Format response with similarity scores
    recommendations = [
        ResourceRecommendation(resource=similar_resource, similarity_score=score)
        for similar_resource, score in results
    ]
    
    return recommendations
