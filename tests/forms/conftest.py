import asyncio

import httpx
import pytest
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.config import settings
from src.main import app


@pytest.fixture(scope='session', autouse=True)
def set_testing_flag():
    # Установка TESTING в значение True перед началом тестов
    settings.TESTING = True
    yield
    # Изменение TESTING на значение False после окончания тестов
    settings.TESTING = False


@pytest.fixture
async def client():
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def db():
    client_test = AsyncIOMotorClient(settings.db.mongo_test_url)

    db = client_test[settings.db.MONGO_TEST_DB_NAME]
    yield db

    client_test.close()


@pytest.fixture(autouse=True, scope="function")
async def collection(db: AsyncIOMotorDatabase):
    collection = db[settings.db.MONGO_TEST_DB_COLLECTION_NAME]
    yield collection
    collection.drop()
