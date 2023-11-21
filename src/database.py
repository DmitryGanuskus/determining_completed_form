from os import getenv

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

from src.config import DB_URL

load_dotenv()

client = AsyncIOMotorClient(DB_URL)

db = client[getenv('DB_NAME')]

forms_collection = db[getenv('DB_COLLECTION')]
