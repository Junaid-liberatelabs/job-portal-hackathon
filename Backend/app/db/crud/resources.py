import logging
import uuid
from typing import Optional

from app.core.exceptions import EmbeddingGenerationError
from app.db.model.resources import Resource
from app.services.embedding_service import embedding_service
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


def create_resource(db: Session, resource_data: dict):
    """Create a new learning resource"""
    db_resource = Resource(id=str(uuid.uuid4()), **resource_data)

    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)

    # Generate and store embedding
    try:
        embedding = embedding_service.generate_resource_embedding(db_resource)
        db_resource.embedding = embedding
        db.commit()
        db.refresh(db_resource)
        logger.info(f"Successfully generated embedding for resource {db_resource.id}")
    except EmbeddingGenerationError as e:
        logger.error(f"Failed to generate embedding for resource {db_resource.id}: {e}")
        # Continue without embedding - resource creation should not fail

    return db_resource


def get_resource_by_id(db: Session, resource_id: str):
    """Get resource by ID"""
    return db.query(Resource).filter(Resource.id == resource_id).first()


def get_resources(
    db: Session, skip: int = 0, limit: int = 100, tags: Optional[list[str]] = None
):
    """Get resources with optional filtering by tags"""
    query = db.query(Resource)

    if tags:
        query = query.filter(Resource.tags.overlap(tags))

    return query.offset(skip).limit(limit).all()


def update_resource(db: Session, resource_id: str, update_data: dict):
    """Update a learning resource"""
    resource = get_resource_by_id(db, resource_id)
    if not resource:
        return None

    # Check if embedding-relevant fields are being updated
    embedding_fields = {"name", "description", "tags"}
    should_regenerate_embedding = any(
        field in update_data for field in embedding_fields
    )

    for key, value in update_data.items():
        if hasattr(resource, key) and key not in ["id", "created_at"]:
            setattr(resource, key, value)

    db.commit()
    db.refresh(resource)

    # Regenerate embedding if relevant fields changed
    if should_regenerate_embedding:
        try:
            embedding = embedding_service.generate_resource_embedding(resource)
            resource.embedding = embedding
            db.commit()
            db.refresh(resource)
            logger.info(
                f"Successfully regenerated embedding for resource {resource.id}"
            )
        except EmbeddingGenerationError as e:
            logger.error(
                f"Failed to regenerate embedding for resource {resource.id}: {e}"
            )
            # Continue without embedding update

    return resource


def delete_resource(db: Session, resource_id: str):
    """Delete a learning resource"""
    resource = get_resource_by_id(db, resource_id)
    if not resource:
        return False

    db.delete(resource)
    db.commit()
    return True
