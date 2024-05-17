import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from asyncio import Queue
from typing import List, Dict

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Niyo Group Backend Assessment"
    DEBUG: bool = True
    API_VERSION: str = '/api/v1'
    LOG_LEVEL: str = "INFO"
    ACCESS_TOKEN_EXPIRE: int = 7200
    OAUTH_URL: str ="/o2auth/login"
    DB_CONNECTION_STR: str = os.getenv("MG_CONN_STR")
    JWT_SECRET: str = os.environ.get("JWT_SECRET")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM")
    subscribers: List[Dict[str,Queue]] = []

settings = Settings()