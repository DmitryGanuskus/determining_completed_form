import asyncio

import pytest
from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings


@pytest.fixture(autouse=True, scope="session")
async def db():
    client_test = AsyncIOMotorClient(settings.db.mongo_url_test)
    db_test = client_test.forms_db_test

    yield db_test

    await client_test.drop_database(db_test)
    client_test.close()


@pytest.fixture(scope="session")
def loop():
    return asyncio.get_event_loop()
