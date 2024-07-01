"""
Module to define dummy API response.
"""

from pydantic import BaseModel
from src.models.response_models.api_response_model import APISuccessResponse
from src.constants import str_constants as sc


class DummyResponse1(APISuccessResponse):
    """
    Definition for dummy API response.
    """

    message: str = sc.OPERATION_SUCCESS


class DummyObject(BaseModel):
    """
    Definition for dummy object.
    """

    str_field: str
    int_field: int
    float_field: float
    bool_field: bool
    list_field: list
    optional_field: str | None = None


class DummyData2(DummyObject):
    """
    Definition for dummy response data (example 2).
    Also contains example for model inheritance.
    """

    complex_field: list[DummyObject] | None = None


class DummyResponse2(APISuccessResponse):
    """
    Definition for dummy API response.
    """

    message: str = sc.OPERATION_SUCCESS
    data: DummyData2


class DummyData3(BaseModel):
    """
    Definition for dummy response data (example 3).
    """

    item_id: str


class DummyResponse3(APISuccessResponse):
    """
    Definition for dummy API response.
    """

    message: str = sc.OPERATION_SUCCESS
    data: DummyData3
