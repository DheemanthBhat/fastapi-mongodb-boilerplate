"""
Module to manage database connections, sessions and transactions.
"""

import logging
from motor.motor_asyncio import AsyncIOMotorClient
from src.configs.app_config import app_config as ag
from src.constants import app_constants as ac
from src.helpers import dt_utils


logger = logging.getLogger(__name__)


class MongoDBManager:
    """
    Definition for Mongo Client.
    """

    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            logger.info("Creating instance of `MongoDBManager` class...")
            cls._instance = super(MongoDBManager, cls).__new__(cls)

            logger.info("Initializing client with access to MongoDB database...")
            start = dt_utils.get_timestamp()
            cls._instance._client = AsyncIOMotorClient(ag.MONGO_CONNECTION_STRING)
            end = dt_utils.get_timestamp()
            time_diff = str(end - start)
            logger.info("Connected to MongoDB database in: %s milliseconds.", time_diff)

        return cls._instance

    def get_client(self):
        """
        Function to return Async Motor client.
        """
        logger.info("Reusing `AsyncIOMotorClient` client.")
        return self._client

    def close_connection(self):
        """
        Function to close database connection.
        """
        logger.info("Closing database connection.")
        self._client.close()


async def get_db_session():
    """
    Function to start transaction in a session and
    return database connection and active session.
    """
    client = MongoDBManager().get_client()

    # Start MongoDB session.
    async with await client.start_session() as ssn:
        # Get session id for current active session.
        ssn_id = ssn.session_id.get("id", None).hex()
        logger.info("Session %s: Started.", ssn_id)

        # Start MongoDB transaction.
        async with ssn.start_transaction():
            try:
                # Get database from client.
                logger.info("Session %s: Starting new transaction.", ssn_id)
                db = client.get_database(ac.DATABASE_NAME)
                yield db, ssn

                # Commit transaction if all okay.
                await ssn.commit_transaction()
                logger.info("Session %s: Commit transaction.", ssn_id)

            except Exception as exc:
                # Rollback transaction on exception.
                await ssn.abort_transaction()
                logger.info("Session %s: Rollback transaction.", ssn_id)
                raise exc

            finally:
                # Close active session.
                ssn.end_session()
                logger.info("Session %s: Closed gracefully.", ssn_id)
