"""
Database seeding module.
Provides functions to populate the database with initial data.
"""

import logging
from app.db.session import SessionLocal
from app.db.seeded_data.jobs_seed import seed_jobs
from app.db.seeded_data.resources_seed import seed_resources

logger = logging.getLogger(__name__)


def seed_all():
    """
    Seeds the database with all initial data.
    
    This function:
    - Creates a database session
    - Seeds jobs
    - Seeds resources
    - Logs the seeding progress
    - Handles errors gracefully
    
    Returns:
        dict: Summary of seeding results with counts
    """
    db = SessionLocal()
    results = {
        "jobs_created": 0,
        "resources_created": 0,
        "success": False,
        "error": None
    }
    
    try:
        logger.info("Starting database seeding...")
        
        # Seed jobs
        logger.info("Seeding jobs...")
        jobs_created = seed_jobs(db)
        results["jobs_created"] = jobs_created
        logger.info(f"Created {jobs_created} new job listings")
        
        # Seed resources
        logger.info("Seeding resources...")
        resources_created = seed_resources(db)
        results["resources_created"] = resources_created
        logger.info(f"Created {resources_created} new learning resources")
        
        results["success"] = True
        logger.info(
            f"Database seeding completed successfully. "
            f"Jobs: {jobs_created}, Resources: {resources_created}"
        )
        
    except Exception as e:
        logger.error(f"Error during database seeding: {e}", exc_info=True)
        results["error"] = str(e)
        db.rollback()
        raise
        
    finally:
        db.close()
    
    return results


def check_seed_status():
    """
    Checks if the database has already been seeded.
    
    Returns:
        dict: Status information about existing data
    """
    from app.db.model.job import Job
    from app.db.model.resources import Resource
    
    db = SessionLocal()
    status = {
        "jobs_count": 0,
        "resources_count": 0,
        "is_seeded": False
    }
    
    try:
        status["jobs_count"] = db.query(Job).count()
        status["resources_count"] = db.query(Resource).count()
        status["is_seeded"] = status["jobs_count"] > 0 or status["resources_count"] > 0
        
    except Exception as e:
        logger.error(f"Error checking seed status: {e}", exc_info=True)
        
    finally:
        db.close()
    
    return status


if __name__ == "__main__":
    """
    Run seeding when this module is executed directly.
    Usage: python -m app.db.seeds
    """
    import sys
    
    # Check current status
    status = check_seed_status()
    logger.info(f"Current database status: {status}")
    
    if status["is_seeded"]:
        response = input(
            f"Database already contains {status['jobs_count']} jobs and "
            f"{status['resources_count']} resources. "
            "Do you want to add more? (y/n): "
        )
        if response.lower() != 'y':
            logger.info("Seeding cancelled by user")
            sys.exit(0)
    
    # Run seeding
    results = seed_all()
    
    if results["success"]:
        logger.info("✓ Seeding completed successfully!")
        logger.info(f"  - Jobs created: {results['jobs_created']}")
        logger.info(f"  - Resources created: {results['resources_created']}")
    else:
        logger.error(f"✗ Seeding failed: {results['error']}")
        sys.exit(1)
