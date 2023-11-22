import json
from random import randint, choice

import requests
from tqdm import trange


async def generate_random_fields():
    rand_dict = {
        field: value for field, value in
        [await get_random_json_items('fields.json')] for _ in trange(
            randint(1, 10), desc='Выбор элемента'
        )
    }
    return rand_dict


async def get_random_json_items(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        parsed_file = json.load(file)
        items = choice(list(parsed_file.items()))
        return items


async def get_random_json_value(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        parsed_file = json.load(file)
        value = choice(list(parsed_file.values()))
        return value


async def request_post(url: str, headers: dict, data: dict):
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    print(response.json())
