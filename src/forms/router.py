from fastapi import APIRouter, Request

from src.database import forms_collection
from src.forms.models import FormTemplate
from src.forms.utils import (
    converting_fields_in_form_to_type, check_fields_match
)

router = APIRouter(
    prefix='/get_form',
    tags=['Forms'],
)


@router.post("")
async def get_form(request: Request):
    form_data = await request.form()
    form = converting_fields_in_form_to_type(dict(form_data))

    query = {"$expr": {
        "$gte": [{"$size": {"$objectToArray": "$fields"}}, len(form)]
    }}

    async for template in forms_collection.find(query):
        if check_fields_match(form, template["fields"]):
            return template["name"]

    return form


@router.post("/form_template/")
async def create_form_template(form_template: FormTemplate) -> dict:
    form_template.fields = converting_fields_in_form_to_type(
        {field.name: field.value for field in form_template.fields}
    )

    result = await forms_collection.insert_one(dict(form_template))
    return {"_id": str(result.inserted_id)}
