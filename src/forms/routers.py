from typing import List

from fastapi import APIRouter, Request

from src.database import forms_collection
from src.forms.models import FormTemplate
from src.forms.utils import validate_form

router = APIRouter(
    prefix='/get_form',
    tags=['Forms'],
)


@router.post("")
async def get_form(request: Request):
    form_data = await request.form()
    form = validate_form(dict(form_data))
    templates = forms_collection.find({})
    async for template in templates:
        if form in template:
            return {'template_name': template.name}
    return form


@router.post("/form_template/")
async def create_form_template(form_template: FormTemplate) -> dict:
    form_template.fields = validate_form(form_template.fields)
    result = await forms_collection.insert_one(dict(form_template))
    return {"_id": str(result.inserted_id)}
