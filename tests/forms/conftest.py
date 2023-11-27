"""forms_test fixtures."""
import asyncio

import httpx
import pytest
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.config import settings
from src.main import app


@pytest.fixture(autouse=True)
async def switch_test_mode():
    """Fixture that switches on the test mode globally."""
    settings.TESTING = True
    yield
    settings.TESTING = False


@pytest.fixture
async def client():
    """Fixture that provides an HTTP client for testing the application."""
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """Fixture that sets up the event loop for the test session."""
    # Create a new event loop for the session
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    # Close the event loop at the end of the session
    loop.close()


@pytest.fixture(scope="session")
async def db():
    """Fixture that provides a test database connection."""
    # Create a new connection to the test database
    client_test = AsyncIOMotorClient(settings.test_db.mongo_test_url)
    db = client_test[settings.test_db.MONGO_TEST_DB_NAME]
    yield db
    # Close the test database connection at the end of the session
    client_test.close()


@pytest.fixture(autouse=True, scope="function")
async def collection(switch_test_mode, db: AsyncIOMotorDatabase):
    """Fixture that provides a test collection within the test database."""
    # Get the test collection from the test database
    collection = db[settings.test_db.MONGO_TEST_DB_COLLECTION_NAME]
    yield collection
    # Drop the test collection at the end of each test function
    await collection.drop()
