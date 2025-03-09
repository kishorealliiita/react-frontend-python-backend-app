from typing import Dict, Any
from pydantic import BaseModel
import os

class VersionInfo(BaseModel):
    version: str
    build_number: str
    git_commit: str
    build_date: str
    environment: str

def get_version_info() -> VersionInfo:
    """Get version information from environment variables."""
    return VersionInfo(
        version=os.getenv("APP_VERSION", "1.0.0"),
        build_number=os.getenv("BUILD_NUMBER", "dev"),
        git_commit=os.getenv("GIT_COMMIT", "unknown"),
        build_date=os.getenv("BUILD_DATE", "unknown"),
        environment=os.getenv("ENVIRONMENT", "development")
    )

def get_api_version() -> str:
    """Get the current API version."""
    return os.getenv("API_VERSION", "v1")

def get_version_header() -> Dict[str, str]:
    """Get version information as HTTP headers."""
    version_info = get_version_info()
    return {
        "X-API-Version": get_api_version(),
        "X-App-Version": version_info.version,
        "X-Build-Number": version_info.build_number,
        "X-Git-Commit": version_info.git_commit
    } 