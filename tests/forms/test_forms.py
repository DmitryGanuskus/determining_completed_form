from tqdm import trange

from motor.motor_asyncio import AsyncIOMotorDatabase

from tests.forms.utils import (
    get_random_json_value, generate_random_fields, request_post
)


async def test_mongodb_connection(db: AsyncIOMotorDatabase):
    # Проверка подключения к базе данных
    result = await db.command('ping')
    assert result['ok'] == 1


async def test_form_template():
    url = "http://127.0.0.1:8000/get_form/form_template/"
    headers = {"Content-Type": "application/json"}

    for _ in trange(100, desc='Создание записей в бд'):
        form_template = {
            "name": await get_random_json_value('form_names.json'),
            "fields": await generate_random_fields()
        }

        await request_post(url, headers, form_template)


async def test_get_form():
    url = "http://127.0.0.1:8000/get_form"
    headers = {"Content-Type": "application/json"}

    form_data = {
        "data": await generate_random_fields()
    }

    await request_post(url, headers, form_data)
