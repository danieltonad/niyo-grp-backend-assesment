import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    application: str
    debug: bool = True
    port: str = 9080
    api_version: str = '/api/v1'
    log_level: str = "INFO"
    db_connection_str: str = os.environ.get("MG_CONN_STR")


settings = Settings()