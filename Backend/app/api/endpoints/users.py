from typing import Annotated

from app.auth.dependencies import get_current_user
from app.api.schemas.user import UserResponse, UserUpdate
from app.db.crud.user import (
    add_user_skill,
    remove_user_skill,
    update_user,
)
from app.db.model.user import User
from app.db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/me", response_model=UserResponse)
def get_current_user_profile(
    current_user: Annotated[User, Depends(get_current_user)]
):
    """
    Get the current authenticated user's profile.
    Returns all user information including skills, education, and career preferences.
    """
    return current_user


@router.put("/me", response_model=UserResponse)
def update_user_profile(
    user_update: UserUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    """
    Update the current user's profile.
    Can update:
    - **full_name**: User's full name
    - **education_level**: User's education level
    - **preferred_career_track**: User's preferred career path
    - **skills**: Complete list of skills (replaces existing)
    """
    # Convert Pydantic model to dict, excluding unset fields
    update_data = user_update.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update",
        )

    updated_user = update_user(db, current_user.id, update_data)

    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return updated_user


@router.post("/me/skills", response_model=UserResponse)
def add_skill_to_profile(
    skill: str,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    """
    Add a single skill to the current user's profile.
    The skill will only be added if it doesn't already exist.
    
    - **skill**: The skill name to add (non-empty string, max 100 characters)
    """
    # Validate skill
    if not skill or len(skill.strip()) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Skill cannot be empty",
        )

    if len(skill) > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Skill name cannot exceed 100 characters",
        )

    skill = skill.strip()

    updated_user = add_user_skill(db, current_user.id, skill)

    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return updated_user


@router.delete("/me/skills/{skill}", response_model=UserResponse)
def remove_skill_from_profile(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    skill: str = Path(..., description="The skill to remove from the user's profile"),
):
    """
    Remove a skill from the current user's profile.
    
    - **skill**: The skill name to remove
    """
    updated_user = remove_user_skill(db, current_user.id, skill)

    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return updated_user
