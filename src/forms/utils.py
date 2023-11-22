import re
from datetime import datetime

from validate_email import validate_email


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
        if datetime.strptime(field_value, '%d-%m-%Y') or datetime.strptime(
                field_value, '%Y-%m-%d'):
            return 'date'

    except ValueError:
        pass

    if re.match(pattern=r'^\+7 \d{3} \d{3} \d{2} \d{2}$',
                string=field_value):
        return 'phone'

    elif validate_email(field_value):
        return 'email'

    return 'text'
