from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings

client = AsyncIOMotorClient(settings.db.mongo_url)

db = client.forms_db

forms_collection = db.forms_collection
