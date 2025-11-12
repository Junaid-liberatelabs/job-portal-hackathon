"""
Logging configuration for the app.
"""

import logging
import sys
from pathlib import Path
from typing import Any, Dict, Optional

from app.core.config import settings


def setup_logging(log_file: Optional[Path] = None) -> None:
    """
    Configure logging for the application.

    Args:
        log_file: Optional path to a log file. If not provided, logs will only go to stdout.
    """
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

    # Configure basic logging
    logging_config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": settings.LOG_FORMAT,
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "level": log_level,
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": sys.stdout,
            },
        },
        "loggers": {
            "app": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            "uvicorn": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            "celery": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            "sqlalchemy": {
                "handlers": ["console"],
                "level": logging.WARNING,  # Set SQL logging to WARNING by default
                "propagate": False,
            },
        },
        "root": {
            "handlers": ["console"],
            "level": log_level,
        },
    }

    # Add file handler if log_file is provided
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        logging_config["handlers"]["file"] = {
            "level": log_level,
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": str(log_file),
            "encoding": "utf-8",
        }
        # Add file handler to all loggers
        for logger in logging_config["loggers"].values():
            logger["handlers"].append("file")
        logging_config["root"]["handlers"].append("file")

    # Apply configuration
    logging.config.dictConfig(logging_config)

    # Configure SQL echo if debug is enabled
    if settings.DEBUG:
        logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

    # Log startup message
    logger = logging.getLogger("app")
    logger.info(
        f"Logging configured with level {settings.LOG_LEVEL} in {settings.ENVIRONMENT} mode"
    )


def get_logger(name: str):
    """
    Get a named logger.

    Args:
        name: The name of the logger

    Returns:
        A logger instance
    """
    return logging.getLogger(name)
