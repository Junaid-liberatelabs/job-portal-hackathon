"""
FastAPI dependencies for authentication and authorization.
"""

import jwt
from app.auth.security import oauth2_scheme
from app.core.config import settings
from app.db.crud.user import get_user_by_email
from app.db.session import get_db
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    """
    Dependency to get the current authenticated user from JWT token.

    Args:
        token: JWT token from Authorization header
        db: Database session

    Returns:
        User object if authentication is successful

    Raises:
        HTTPException: If token is invalid or user not found
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        user_id: str = payload.get("user_id")
        if email is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception

    # Fetch user from database to get fresh data including skills
    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception

    # Verify user_id matches if present in token
    if user_id and user.id != user_id:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user"
        )

    return user
