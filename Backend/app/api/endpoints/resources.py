from datetime import timedelta
from typing import Annotated

from app.db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.schemas.resources import (ResourceCreate, ResourceInDB,
                                               ResourceResponse,
                                               ResourceUpdate)

router = APIRouter()


@router.post("/", response_model=ResourceResponse)
async def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    new_resource = ResourceInDB(**resource.dict())
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource


@router.get("/{resource_id}", response_model=ResourceResponse)
async def get_resource(resource_id: str, db: Session = Depends(get_db)):
    resource = db.query(ResourceInDB).filter(ResourceInDB.id == resource_id).first()
    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found"
        )
    return resource


@router.put("/{resource_id}", response_model=ResourceResponse)
async def update_resource(
    resource_id: str, resource: ResourceUpdate, db: Session = Depends(get_db)
):
    db_resource = db.query(ResourceInDB).filter(ResourceInDB.id == resource_id).first()
    if not db_resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found"
        )
    for key, value in resource.dict().items():
        setattr(db_resource, key, value)
    db.commit()
    db.refresh(db_resource)
    return db_resource


@router.delete("/{resource_id}")
async def delete_resource(resource_id: str, db: Session = Depends(get_db)):
    db_resource = db.query(ResourceInDB).filter(ResourceInDB.id == resource_id).first()
    if not db_resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found"
        )
    db.delete(db_resource)
    db.commit()
    return {"message": "Resource deleted successfully"}
