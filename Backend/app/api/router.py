"""
API router for v1 endpoints.
"""

from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.jobs import router as jobs_router
from app.api.endpoints.recommendations import router as recommendations_router
from app.api.endpoints.resources import router as resources_router
from app.api.endpoints.users import router as users_router
from app.api.endpoints.applications import router as applications_router
from app.api.endpoints.skill_analysis import router as skill_analysis_router
from app.api.endpoints.skill_gap_analysis import router as skill_gap_analysis_router
from app.api.endpoints.career_roadmap import router as career_roadmap_router
from app.api.endpoints.cv_export import router as cv_export_router

from fastapi import APIRouter

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(jobs_router, prefix="/jobs", tags=["jobs"])
router.include_router(resources_router, prefix="/resources", tags=["resources"])
router.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])
router.include_router(applications_router, prefix="/applications", tags=["applications"])
router.include_router(skill_analysis_router, prefix="/skill-analysis", tags=["skill-analysis"])
router.include_router(skill_gap_analysis_router, prefix="/skill-gap-analysis", tags=["skill-gap-analysis"])
router.include_router(career_roadmap_router, prefix="/career-roadmap", tags=["career-roadmap"])
router.include_router(cv_export_router, prefix="/cv", tags=["cv-export"])