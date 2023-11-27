from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings


def get_db() -> dict:
    if settings.TESTING:
        client = AsyncIOMotorClient(settings.test_db.mongo_test_url)
        db = client[settings.test_db.MONGO_TEST_DB_NAME]
        collection = db[settings.test_db.MONGO_TEST_DB_COLLECTION_NAME]

    else:
        client = AsyncIOMotorClient(settings.db.mongo_url)
        db = client[settings.db.MONGO_DB_NAME]
        collection = db[settings.db.MONGO_DB_COLLECTION_NAME]

    return {'client': client, 'db': db, 'collection': collection}
