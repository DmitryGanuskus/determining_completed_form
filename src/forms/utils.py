import re
from datetime import datetime

from validate_email import validate_email


def validate_form(form_dict: dict) -> dict:
    result = {}
    for key, value in form_dict.items():
        result[key] = validate_field(value)
    return result


def validate_field(field_value: str) -> str:
    try:
        if datetime.strptime(field_value, '%d-%m-%Y') or datetime.strptime(
                field_value, '%Y-%m-%d'):
            return 'date'

    except ValueError:
        pass

    if re.match(pattern=r'^\+7 \d{3} \d{3} \d{2} \d{2}$',
                string=field_value):
        return 'phone'

    # elif re.match(pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    #               string=field_value):
    elif validate_email(field_value):
        return 'email'

    return 'text'
