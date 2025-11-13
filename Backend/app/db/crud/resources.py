import uuid
from typing import Optional

from app.db.model.resources import Resource
from sqlalchemy.orm import Session


def create_resource(db: Session, resource_data: dict):
    """Create a new learning resource"""
    db_resource = Resource(id=str(uuid.uuid4()), **resource_data)

    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
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

    for key, value in update_data.items():
        if hasattr(resource, key) and key not in ["id", "created_at"]:
            setattr(resource, key, value)

    db.commit()
    db.refresh(resource)
    return resource


def delete_resource(db: Session, resource_id: str):
    """Delete a learning resource"""
    resource = get_resource_by_id(db, resource_id)
    if not resource:
        return False

    db.delete(resource)
    db.commit()
    return True
