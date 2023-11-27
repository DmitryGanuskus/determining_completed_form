"""File for database initialization."""
from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings


def get_db() -> dict:
    """Return the database object, the MongoDB client, and the collection,
    depending on the application settings.
    """
    if settings.TESTING:
        # If the application is in testing mode, create a MongoDB client and
        # connect to the test database and collection
        client = AsyncIOMotorClient(settings.test_db.mongo_test_url)
        db = client[settings.test_db.MONGO_TEST_DB_NAME]
        collection = db[settings.test_db.MONGO_TEST_DB_COLLECTION_NAME]

    else:
        # If the application is not in testing mode, create a MongoDB client
        # and connect to the main database
        client = AsyncIOMotorClient(settings.db.mongo_url)
        db = client[settings.db.MONGO_DB_NAME]
        collection = db[settings.db.MONGO_DB_COLLECTION_NAME]

    # Returning the dictionary with the client, database and collection
    return {'client': client, 'db': db, 'collection': collection}
