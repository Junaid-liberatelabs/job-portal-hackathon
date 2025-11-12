"""Database initialization module."""
from app.db.session import engine
from app.db.base import Base

from app.core.logging_config import get_logger

logger = get_logger(__name__)


async def init_db():
    """
    Initialize the database by creating all tables.
    
    This function creates all database tables defined in the models.
    Make sure to import all models before calling this function.
    """
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise


# def create_tables():
#     """
#     Synchronous version of table creation.
    
#     Use this function when you need to create tables synchronously.
#     """
#     try:
#         Base.metadata.create_all(bind=engine)
#         logger.info("Database tables created successfully (sync)")
#     except Exception as e:
#         logger.error(f"Error creating database tables (sync): {e}")
#         raise


# if __name__ == "__main__":
#     # Create tables when running this script directly
#     create_tables()