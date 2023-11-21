import asyncio
from os import getenv

import pytest
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

from src.config import DB_URL_TEST, DB_NAME_TEST

load_dotenv()


@pytest.fixture(autouse=True, scope="session")
async def db():
    client_test = AsyncIOMotorClient(DB_URL_TEST)
    db_test = client_test[DB_NAME_TEST]

    yield db_test

    await client_test.drop_database(db_test)
    client_test.close()


@pytest.fixture(scope="session")
def loop():
    return asyncio.get_event_loop()
