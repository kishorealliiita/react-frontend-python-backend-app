from typing import Dict, Any
from pydantic import BaseSettings

class FeatureFlags(BaseSettings):
    # Feature flags for gradual rollouts
    ENABLE_NEW_AUTH: bool = False
    ENABLE_RATE_LIMITING: bool = True
    ENABLE_CACHE: bool = False
    ENABLE_ANALYTICS: bool = True
    
    # A/B testing flags
    ENABLE_AB_TESTING: bool = False
    AB_TEST_VARIANT: str = "control"
    
    # Maintenance flags
    MAINTENANCE_MODE: bool = False
    READ_ONLY_MODE: bool = False
    
    class Config:
        env_prefix = "FEATURE_"
        case_sensitive = True

# Global feature flags instance
feature_flags = FeatureFlags()

def is_feature_enabled(feature_name: str) -> bool:
    """Check if a feature is enabled."""
    return getattr(feature_flags, f"ENABLE_{feature_name.upper()}", False)

def get_feature_value(feature_name: str, default: Any = None) -> Any:
    """Get the value of a feature flag."""
    return getattr(feature_flags, feature_name.upper(), default)

def update_feature_flags(updates: Dict[str, Any]) -> None:
    """Update feature flags with new values."""
    for key, value in updates.items():
        if hasattr(feature_flags, key):
            setattr(feature_flags, key, value) 