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
    TIMEZONE: str = ac.TIMEZONE

    # Application logging level.
    LOG_LEVEL: str = ac.DEFAULT_LOG_LEVEL

    # CORS parameters.
    ALLOW_ORIGIN: list = ["*"]

    # MongoDB connection string.
    MONGO_CONNECTION_STRING: str

    # Load environment variables from `.env` file.
    model_config = SettingsConfigDict(env_file="../../.env", env_file_encoding="utf-8")


app_config = AppConfig()
