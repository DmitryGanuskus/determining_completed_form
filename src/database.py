from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings

client = AsyncIOMotorClient(settings.db.mongo_url)

db = client[settings.db.MONGO_DB_NAME]

forms_collection = db[settings.db.MONGO_DB_COLLECTION_NAME]
