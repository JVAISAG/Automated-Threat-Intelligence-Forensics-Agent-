from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "ATIF Agent"
    API_V1_STR: str = "/api/v1"
    
    # AI Config
    GOOGLE_API_KEY: str
    GEMINI_MODEL: str = "gemini-1.5-pro"
    
    # Database Config
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "atif_forensics"
    
    # Storage
    UPLOAD_DIR: str = "uploads"
    YARA_RULES_PATH: str = "rules/malware.yar"

    class Config:
        env_file = ".env"

settings = Settings()
