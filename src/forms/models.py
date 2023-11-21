from typing import List, Dict, Any

from pydantic import BaseModel


# class FormField(BaseModel):
#     name: str
#     value: str


class FormTemplate(BaseModel):
    name: str
    fields: Dict[str, Any]
