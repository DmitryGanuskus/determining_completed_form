"""Forms models."""
from typing import List

from pydantic import BaseModel


class FormField(BaseModel):
    """Model for the form field.

    Attributes
    ----------
    - name (str): Name of the form field.
    - value (str): The value of the form field.
    """

    name: str
    value: str


class FormTemplate(BaseModel):
    """Model for the form template.

    Attributes
    ----------
    - name (str): Name of the form template.
    - fields (List[FormField]): A list of form fields specified via the
    FormField model
    """

    name: str
    fields: List[FormField]
