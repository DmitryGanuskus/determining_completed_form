from fastapi import APIRouter

from src.database import forms_collection
from src.forms.models import FormTemplate, FormData
from src.forms.utils import validate_field

router = APIRouter(
    prefix='/get_form',
    tags=['Формы'],
)


@router.post("")
async def get_form(form_data: FormData) -> dict:
    form_data = dict(form_data.data)
    templates = forms_collection.find({})

    async for template in templates:
        for field_name, field_value in template['fields'].items():
            form_data_value = form_data[field_name]

            if field_name in form_data and field_value == form_data_value:
                return {"template_name": template['name']}

    return {field: validate_field(value) for field, value in form_data.items()}


@router.post("/form_template/")
async def create_form_template(form_template: FormTemplate) -> dict:
    form = dict(form_template)
    result = await forms_collection.insert_one(form)

    return {"_id": str(result.inserted_id)}
