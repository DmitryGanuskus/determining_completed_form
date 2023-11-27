"""Forms router."""
from fastapi import APIRouter, Request

from src.database import get_db
from src.forms.models import FormTemplate
from src.forms.utils import (
    converting_fields_in_form_to_type, check_fields_match, get_query
)

# Create an APIRouter instance with a prefix and tag
router = APIRouter(
    prefix='/get_form',
    tags=['Forms'],
)


@router.post("")
async def get_form(request: Request) -> dict:
    """Convert the request to the format f_name1=value1&f_name2=value2 to the
    dictionary and, based on the data received, return the template name from
    the database. Or convert the resulting form in the format
    {f_name 1: FIELD_TYPE, f_name 2: FIELD_TYPE}.
    """
    # Get the collection from the database
    collection = get_db()['collection']

    # Get the form data from the request
    form_data = await request.form()

    # Convert the form data to a typed dictionary
    form = converting_fields_in_form_to_type(dict(form_data))

    # Build the query
    query = await get_query(form=form, collection=collection)

    # Output the results
    async for result in collection.find(query):
        if check_fields_match(
                form_fields=form, template_fields=result['fields']
        ):
            return {'template_name': result['name']}

    return form


@router.post("/form_template/")
async def create_form_template(form_template: FormTemplate) -> dict:
    """Create an entry in the database."""
    # Get the collection from the database
    collection = get_db()['collection']

    # Convert the form field values to a typed dictionary
    form_template.fields = converting_fields_in_form_to_type(
        {field.name: field.value for field in form_template.fields}
    )

    # Insert the form template into the collection
    result = await collection.insert_one(dict(form_template))

    # Return the ID of the inserted document
    return {"_id": str(result.inserted_id)}
