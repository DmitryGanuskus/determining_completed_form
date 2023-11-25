import re
from datetime import datetime

from validate_email import validate_email
from motor.motor_asyncio import AsyncIOMotorCollection


async def get_query(form: dict, collection: AsyncIOMotorCollection) -> dict:
    # Условия для проверки существования полей из шаблона
    field_conditions = [
        {f"fields.{field}": {'$exists': True}} for field in form.keys()
    ]

    # Получаем список всех ключей в коллекции
    all_keys = await collection.find_one(projection={'fields': True})
    if all_keys:
        all_keys = all_keys['fields'].keys()

        # Условие для проверки отсутствия полей не из шаблона
        extra_field_conditions = [
            {f"fields.{key}": {'$exists': True}} for key in all_keys if
            key not in form.keys()
        ]

        # Формируем запрос с использованием $and и $nor
        query = {
            '$and': field_conditions,
            '$nor': extra_field_conditions
        }


    else:
        # Формируем запрос с использованием $and
        query = {'$and': field_conditions}

    return query


def check_fields_match(form_fields: dict, template_fields: dict) -> bool:
    return all(
        [item in template_fields.items() for item in form_fields.items()]
    )


def converting_fields_in_form_to_type(form_dict: dict) -> dict:
    result = {}
    for key, value in form_dict.items():
        result[key] = get_field_type(value)
    return result


def get_field_type(field_value: str) -> str:
    try:
        if datetime.strptime(field_value, '%d.%m.%Y'):
            return 'date'
    except ValueError:
        pass

    try:
        if datetime.strptime(field_value, '%Y-%m-%d'):
            return 'date'
    except ValueError:
        pass

    if re.match(pattern=r'^\+7 \d{3} \d{3} \d{2} \d{2}$',
                string=field_value):
        return 'phone'

    elif validate_email(field_value):
        return 'email'

    return 'text'
