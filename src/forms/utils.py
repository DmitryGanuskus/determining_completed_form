import re
from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorCollection
from validate_email import validate_email


async def get_query(form: dict, collection: AsyncIOMotorCollection) -> dict:
    # Conditions to check for the existence of fields from the template
    field_conditions = [
        {f"fields.{field}": {'$exists': True}} for field in form.keys()
    ]

    # Get a list of all keys in the collection
    all_keys = await collection.find_one({}, projection={'fields': True})
    if all_keys:
        all_keys = all_keys['fields'].keys()

        # Condition to check for the absence of fields not from the template
        extra_field_conditions = [
            {f"fields.{key}": {'$exists': True}} for key in all_keys if
            key not in form.keys()
        ]

        # Form query using $and and $nor
        query = {
            '$and': field_conditions,
            '$nor': extra_field_conditions
        }
        return query

    # Return query with $and
    return {'$and': field_conditions}


def check_fields_match(form_fields: dict, template_fields: dict) -> bool:
    # Check if the form fields match the template fields
    return all(
        [item in template_fields.items() for item in form_fields.items()]
    )


def converting_fields_in_form_to_type(form_dict: dict) -> dict:
    # Convert fields in the form dictionary to their respective types
    return {key: get_field_type(value) for key, value in form_dict.items()}


def get_field_type(field_value: str) -> str:
    # Determine the type of field value
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
