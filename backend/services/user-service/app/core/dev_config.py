from typing import Dict, Any
from pydantic import BaseSettings
import os

class DevConfig(BaseSettings):
    # Development environment settings
    DEBUG: bool = True
    RELOAD: bool = True
    WORKERS: int = 1
    
    # Development tools
    ENABLE_SWAGGER: bool = True
    ENABLE_RELOADER: bool = True
    ENABLE_DEBUG_TOOLBAR: bool = True
    
    # Development database
    DEV_DATABASE_URL: str = "sqlite:///./dev.db"
    
    # Development logging
    LOG_LEVEL: str = "DEBUG"
    LOG_FORMAT: str = "json"
    
    # Development security
    DEV_SECRET_KEY: str = "dev_secret_key"
    DEV_ALGORITHM: str = "HS256"
    DEV_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Development CORS
    DEV_CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:5173"]
    
    # Development rate limiting
    DEV_RATE_LIMIT: int = 1000
    DEV_RATE_LIMIT_PERIOD: int = 60
    
    class Config:
        env_prefix = "DEV_"
        case_sensitive = True

# Global development config instance
dev_config = DevConfig()

def get_dev_settings() -> Dict[str, Any]:
    """Get all development settings as a dictionary."""
    return dev_config.dict()

def update_dev_settings(updates: Dict[str, Any]) -> None:
    """Update development settings with new values."""
    for key, value in updates.items():
        if hasattr(dev_config, key):
            setattr(dev_config, key, value)

def is_development() -> bool:
    """Check if the application is running in development mode."""
    return os.getenv("ENVIRONMENT", "development").lower() == "development"

def get_development_urls() -> Dict[str, str]:
    """Get development URLs for various services."""
    return {
        "api": "http://localhost:8000",
        "frontend": "http://localhost:5173",
        "swagger": "http://localhost:8000/docs",
        "redoc": "http://localhost:8000/redoc",
    } 