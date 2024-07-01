"""
Module to define dummy payload validator.
"""

from pydantic import BaseModel, Field
from src.constants import str_constants as sc


class DummyObject(BaseModel):
    """
    Definition for dummy object.
    """

    str_field: str = Field(description=sc.STR_FIELD_DESC)
    int_field: int = Field(description=sc.INT_FIELD_DESC)
    float_field: float = Field(description=sc.FLOAT_FIELD_DESC)
    bool_field: bool = Field(description=sc.BOOL_FIELD_DESC)
    list_field: list = Field(description=sc.LIST_FIELD_DESC)
    optional_field: str | None = Field(default=None, description=sc.OPTIONAL_FIELD_DESC)


class DummyPayload(DummyObject):
    """
    Definition for dummy request body payload.
    Also contains example for model inheritance.
    """

    complex_field: list[DummyObject] = Field(description=sc.COMPLEX_FIELD_DESC)
