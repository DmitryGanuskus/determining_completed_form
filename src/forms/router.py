from pprint import pprint

from fastapi import APIRouter, Request

from src.config import settings
from src.database import forms_collection
from src.forms.models import FormTemplate
from src.forms.utils import (
    converting_fields_in_form_to_type, check_fields_match, get_query
)

router = APIRouter(
    prefix='/get_form',
    tags=['Forms'],
)


@router.post("")
async def get_form(request: Request) -> dict:
    form_data = await request.form()
    form = converting_fields_in_form_to_type(dict(form_data))

    # Собираем запрос
    query = await get_query(form=form, collection=forms_collection)
    # Выводим результаты
    async for result in forms_collection.find(query):
        if check_fields_match(
                form_fields=form, template_fields=result['fields']
        ):
            return {'template_name': result['name']}

    return form


@router.post("/form_template/")
async def create_form_template(form_template: FormTemplate) -> dict:
    form_template.fields = converting_fields_in_form_to_type(
        {field.name: field.value for field in form_template.fields}
    )

    result = await forms_collection.insert_one(dict(form_template))
    return {"_id": str(result.inserted_id)}
