"""
Module containing configuration parameters
initialized using the environment variables.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from src.constants import app_constants as ac


class AppConfig(BaseSettings):
    """
    Define and initialize multiple config parameters
    whose values are taken from environment variables.
    """

    # Set application timezone.
    TIMEZONE: str = ac.DEFAULT_TIMEZONE

    # Application logging level.
    LOG_LEVEL: str = ac.DEFAULT_LOG_LEVEL

    # CORS: Whitelist origins.
    ALLOW_ORIGIN: list = ["*"]

    # MongoDB connection string.
    MONGO_CONNECTION_STRING: str

    # Load required environment variables from the full list in `.env` file and ignore others.
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


app_config = AppConfig()
