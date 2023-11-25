from time import sleep

import pytest
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection

from tests.forms.utils import data


@pytest.mark.asyncio
async def test_mongodb_connection(db: AsyncIOMotorDatabase):
    # Проверка подключения к базе данных
    result = await db.command('ping')

    assert result['ok'] == 1


@pytest.mark.asyncio
async def test_db_insertion(collection: AsyncIOMotorCollection):
    data_dict = [{'name': 'name', 'fields': [{'value': 'value'}]}]
    await collection.insert_one(*data_dict)
    result = await collection.find({}).to_list(length=1)

    assert result == data_dict


@pytest.mark.asyncio
async def test_get_form_without_data_in_db(client: AsyncClient):
    response = await client.post(
        url='/get_form', data={
            'text': 'value', 'date1': '1999-03-07', 'date2': '07.03.1999',
            'phone': '+7 999 999 99 99', 'email': 'art.333@mail.ru'
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        'text': 'text', 'date1': 'date', 'date2': 'date',
        'phone': 'phone', 'email': 'email'
    }


@pytest.mark.asyncio
async def test_get_form_with_data_in_db(collection: AsyncIOMotorCollection,
                                        client: AsyncClient):
    data_dict = [
        {'name': '1 template',
         'fields': {'user_name': 'text', 'user_email': 'email'}},
        {'name': '2 template',
         'fields': {'user_name': 'text', 'phone': 'phone'}},
        {'name': '3 template',
         'fields': {'user_name': 'text', 'phone': 'phone',
                    'user_email': 'email'}},

    ]

    await collection.insert_many(data_dict)
    response = await client.post(url=f'/get_form', data={
        'user_name': 'ПуЛи_От_БаБуЛи', 'phone': '+7 999 999 99 99'})

    assert response.status_code == 200
    assert response.json() == {'template_name': '2 template'}
