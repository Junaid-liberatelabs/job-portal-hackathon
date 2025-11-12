"""
API router for v1 endpoints.
"""

from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.jobs import router as jobs_router
from app.api.endpoints.resources import router as resources_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(jobs_router, prefix="/jobs", tags=["jobs"])
router.include_router(resources_router, prefix="/resources", tags=["resources"])
