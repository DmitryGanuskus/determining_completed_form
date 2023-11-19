from os import getenv

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient


load_dotenv()

MONGODB_URL = getenv('DB_URL', default='mongodb://localhost:27017')

client = AsyncIOMotorClient(MONGODB_URL)

database = client['forms_db']

forms_collection = database['forms_collection']
