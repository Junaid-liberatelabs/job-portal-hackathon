"""
API router for v1 endpoints.
"""
from fastapi import APIRouter
from app.api.endpoints.auth import router as auth_router
router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["auth"])