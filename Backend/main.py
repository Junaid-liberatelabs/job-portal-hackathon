"""
Main application entry point for the saaslab AI system.
"""

import logging
import os
from contextlib import asynccontextmanager

# from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app.api.router import router as api_router
from app.core.config import settings
# from app.core.exceptions import register_exception_handlers
from app.core.logging_config import get_logger, setup_logging
from app.db.init_db import init_db
# from langgraph.checkpoint.memory import MemorySaver
# from saaslab.db.base import Base
# from saaslab.db.session import sync_engine


# Load environment variables before importing settings
# load_dotenv()

import asyncio
import sys
#check if the os is windows with sys


logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI lifespan context manager for startup and shutdown events.

    Args:
        app: FastAPI application
    """
    # Startup: Set up logging and create database tables if they don't exist
    setup_logging()
    # app.state.checkpointer = MemorySaver()
    logger.info("Starting up application...")
    # Example: Initialize database connections, load models, etc.
    await init_db()
    
    

    if settings.ENVIRONMENT in ["development", "staging", "production"]:
        logger.info("Creating database tables")
        # Base.metadata.create_all(bind=sync_engine)

    yield

    # Shutdown: Clean up resources
    logger.info("Shutting down application...")
    # Example: Close database connections
    # await close_db()

def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        Configured FastAPI application
    """
    if sys.platform.startswith('win'):
        logger.info("Setting Windows selector event loop policy")
        from asyncio import WindowsSelectorEventLoopPolicy
        asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    # Create FastAPI app
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Multi-Agent AI System for Culture, Brand, and CX Report Generation",
        version=settings.VERSION,
        # openapi_url=f"{settings.API_V1_STR}/openapi.json",
        # docs_url=f"{settings.API_V1_STR}/docs",
        # redoc_url=f"{settings.API_V1_STR}/redoc",
        lifespan=lifespan,
        debug=settings.DEBUG,
    )

    # Set up CORS middleware
    # if settings.BACKEND_CORS_ORIGINS:
    #     app.add_middleware(
    #         CORSMiddleware,
    #         allow_origins=settings.BACKEND_CORS_ORIGINS,
    #         allow_credentials=True,
    #         allow_methods=["*"],
    #         allow_headers=["*"],
    #     )

    # Add security middleware
    # app.add_middleware(GZipMiddleware, minimum_size=1000)

    # Add trusted host middleware if not in development
    # if settings.ENVIRONMENT != "development":
    #     app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)

    # Register exception handlers
    # register_exception_handlers(app)

    # Include API routers
    app.include_router(api_router)

    # Health check endpoint
    @app.get("/health")
    async def health_check():
        """Health check endpoint."""
        return {"status": "ok", "version": settings.VERSION}

    # Root endpoint (optional)
    @app.get("/", tags=["root"])
    async def read_root():
        return {"message": "SaasLab AI is Running"}

    return app


# Create the FastAPI application
app = create_application()


if __name__ == "__main__":
    """Run the application using Uvicorn when script is executed directly."""
    import uvicorn

    # Get port from environment or use default
    port = int(os.environ.get("PORT", 8000))

    # Run the application
    print(settings.DEBUG)
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info",
    )
