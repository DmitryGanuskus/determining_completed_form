from typing import List

from pydantic import BaseModel


class FormField(BaseModel):
    name: str
    value: str


class FormTemplate(BaseModel):
    name: str
    fields: List[FormField]
