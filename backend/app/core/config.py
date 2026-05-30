from pydantic_settings import BaseSettings


# Loads application configuration from environment variables and .env file
class Settings(BaseSettings):
    app_name: str = "DriftdetectionAI"
    debug: bool = False
    log_level: str = "INFO"
    gemini_api_key: str = ""
    langsmith_api_key: str = ""
    langchain_tracing_v2: str = "false"
    langchain_project: str = "driftdetection-ai"
    database_url: str = ""

    model_config = {"env_file": ".env"}

settings = Settings()
