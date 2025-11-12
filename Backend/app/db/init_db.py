"""Database initialization module."""

from app.core.logging_config import get_logger
from app.db.base import Base  # This import ensures all models are registered
from app.db.session import engine

logger = get_logger(__name__)


async def init_db():
    """
    Initialize the database by creating all tables.

    This function creates all database tables defined in the models.
    All models are automatically imported via app.db.base.
    """
    try:
        logger.info("Starting database initialization...")

        # Create all tables
        Base.metadata.create_all(bind=engine)

        # Log the tables that were created
        table_names = [table.name for table in Base.metadata.sorted_tables]
        logger.info(f"Database tables created successfully: {', '.join(table_names)}")

    except Exception as e:
        logger.error(f"Error creating database tables: {e}", exc_info=True)
        raise RuntimeError(f"Failed to initialize database: {str(e)}") from e


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
