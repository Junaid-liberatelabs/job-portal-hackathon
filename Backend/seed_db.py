#!/usr/bin/env python3
"""
Database seeding CLI script.

Usage:
    python seed_db.py              # Seed the database
    python seed_db.py --check      # Check seed status without seeding
    python seed_db.py --force      # Force seed without confirmation
"""

import argparse
import sys
import logging

# Simple logging setup for CLI
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

from app.db.seeded_data import seed_all, check_seed_status


def main():
    parser = argparse.ArgumentParser(description="Seed the database with initial data")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check seed status without seeding"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force seed without confirmation"
    )
    
    args = parser.parse_args()
    
    # Check status
    status = check_seed_status()
    logger.info(f"Current database status:")
    logger.info(f"  - Jobs: {status['jobs_count']}")
    logger.info(f"  - Resources: {status['resources_count']}")
    
    if args.check:
        return
    
    # Confirm if database already has data
    if status["is_seeded"] and not args.force:
        print(
            f"\nDatabase already contains {status['jobs_count']} jobs and "
            f"{status['resources_count']} resources."
        )
        response = input("Do you want to add more seed data? (y/n): ")
        if response.lower() != 'y':
            logger.info("Seeding cancelled by user")
            return
    
    # Run seeding
    logger.info("\nStarting database seeding...")
    results = seed_all()
    
    if results["success"]:
        print("\n✓ Seeding completed successfully!")
        print(f"  - Jobs created: {results['jobs_created']}")
        print(f"  - Resources created: {results['resources_created']}")
    else:
        print(f"\n✗ Seeding failed: {results['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
