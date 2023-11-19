from pydantic import BaseModel


class FormTemplate(BaseModel):
    name: str
    fields: dict


class FormData(BaseModel):
    data: dict
