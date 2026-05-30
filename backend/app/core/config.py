from pydantic_settings import BaseSettings

# Loads application configuration from environment variables and .env file
class Settings(BaseSettings):
    app_name: str = "DriftdetectionAI"
    debug: bool = False
    log_level: str = "INFO"
    anthropic_api_key: str = ""
    database_url: str = "sqlite:///./drift.db"

    model_config = {"env_file": ".env"}

settings = Settings()
