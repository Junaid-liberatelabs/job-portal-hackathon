from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all models here to ensure they're registered with SQLAlchemy
# This is required for Base.metadata.create_all() to work properly
# from app.db.model.user import User  # noqa: F401
from app.db.model.job import (ExperienceLevel, Job, JobLocation,  # noqa: F401
                              JobType)
from app.db.model.resources import Resource  # noqa: F401
