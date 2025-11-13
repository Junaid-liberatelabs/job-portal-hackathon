import logging
import os
import urllib.parse
from functools import lru_cache
from typing import Any, List, Optional

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, PostgresDsn, RedisDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "CareerIN"
    DEBUG: bool = True
    PROJECT_NAME: str = "CareerIN"
    VERSION: str = "0.1.0"
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Security
    SECRET_KEY: str = "kljlkjal;jkdfokpokl;huj"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    ENVIRONMENT: str = "development"

    # POSTGRES_SERVER:str
    # POSTGRES_USER:str
    # POSTGRES_PASSWORD:str
    # POSTGRES_PORT:str
    # POSTGRES_DB:str
    DATABASE_URL: str = "postgresql://postgres:postgres@database:5432/postgres"

    class Config:
        env_file = ".env"
        env_ignore_empty = False
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    env_name = os.environ.get("ENVIRONMENT", "development")
    logging.info(f"Loading settings for environment: {env_name}")
    load_dotenv(override=True)
    return Settings()


settings = get_settings()
