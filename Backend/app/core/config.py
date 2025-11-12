import logging
import os
import urllib.parse
from functools import lru_cache
from typing import Any, List, Optional

from pydantic import AnyHttpUrl, PostgresDsn, RedisDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


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
    # CORS settings
    # Security settings
    # SECRET_KEY: str
    # ALGORITHM: str = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes
    # REFRESH_TOKEN_EXPIRE_DAYS: int = 7  # 7 days

    # # LLM Settings
    # OPENAI_API_KEY: Optional[str] = None
    # ANTHROPIC_API_KEY: Optional[str] = None
    # GOOGLE_API_KEY: Optional[str] = None
    # PPLX_API_KEY: Optional[str] = None
    # SERPER_DEV_API_KEY: Optional[str] = None

    # LANGCHAIN_TRACING_V2: str = "true"
    # LANGCHAIN_ENDPOINT: str = "https://api.smith.langchain.com"
    # LANGCHAIN_API_KEY: Optional[str] = None
    # LANGCHAIN_PROJECT: Optional[str] = None



    ENVIRONMENT: str = "development"


    # POSTGRES_SERVER:str
    # POSTGRES_USER:str
    # POSTGRES_PASSWORD:str
    # POSTGRES_PORT:str
    # POSTGRES_DB:str
    DATABASE_URL: str
    


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