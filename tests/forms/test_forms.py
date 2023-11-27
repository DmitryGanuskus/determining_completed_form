"""Forms Router Tests."""
import pytest
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection


@pytest.mark.asyncio
async def test_mongodb_connection(db: AsyncIOMotorDatabase):
    """Test to check the connection to the database.

    Args:
    ----
        db (AsyncIOMotorDatabase): The test database connection.
    """
    # Send a ping command to the database and get the result
    result = await db.command('ping')

    assert result['ok'] == 1


@pytest.mark.asyncio
async def test_db_insertion(collection: AsyncIOMotorCollection):
    """Test to check the insertion of data into the database collection.

    Args:
    ----
        collection (AsyncIOMotorCollection): The test collection in the
            database.
    """
    # Define the data to be inserted
    data = [{'name': 'name', 'fields': [{'value': 'value'}]}]
    # Insert the data into the collection
    await collection.insert_one(*data)
    # Retrieve the data from the collection
    result = await collection.find({}).to_list(length=1)
    # Check if the retrieved data is equal to the inserted data
    assert result == data


@pytest.mark.asyncio
async def test_get_form_without_data_in_db(client: AsyncClient):
    """Test to check the response of getting a form when there is no data in
    the database.

    Args:
    ----
        client (AsyncClient): The test HTTP client.
    """
    # Send a POST request to the '/get_form' endpoint with some data
    response = await client.post(
        url='/get_form', data={
            'text': 'value', 'date1': '1999-03-07', 'date2': '07.03.1999',
            'phone': '+7 999 999 99 99', 'email': 'art.333@mail.ru'
        }
    )
    # Check if the response status code is 200
    assert response.status_code == 200
    # Check if the response JSON is equal to the expected JSON
    assert response.json() == {
        'text': 'text', 'date1': 'date', 'date2': 'date',
        'phone': 'phone', 'email': 'email'
    }


@pytest.mark.asyncio
async def test_get_form_with_data_in_db(collection: AsyncIOMotorCollection,
                                        client: AsyncClient):
    """Test to check the response of getting a form when there is data in the
        database.

    Args:
    ----
        collection (AsyncIOMotorCollection): The test collection in the
            database.
        client (AsyncClient): The test HTTP client.
    """
    # Define the data to be inserted into the collection
    data = [
        {'name': '1 template',
         'fields': {'user_name': 'text', 'user_email': 'email'}},
        {'name': '2 template',
         'fields': {'user_name': 'text', 'phone': 'phone'}},
        {'name': '3 template',
         'fields': {'user_name': 'text', 'phone': 'phone',
                    'user_email': 'email'}},

    ]
    # Insert the data into the collection
    await collection.insert_many(data)
    # Send a POST request to the '/get_form' endpoint with some data
    response = await client.post(url='/get_form', data={
        'user_name': 'ПуЛи_От_БаБуЛи', 'phone': '+7 999 999 99 99'})

    # Check if the response status code is 200
    assert response.status_code == 200
    # Check if the response JSON is equal to the expected JSON
    assert response.json() == {'template_name': '2 template'}
