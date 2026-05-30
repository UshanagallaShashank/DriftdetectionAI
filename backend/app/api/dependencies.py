from app.core.config import Settings, settings

# Returns the current application settings as a FastAPI dependency
def get_settings() -> Settings:
    return settings
