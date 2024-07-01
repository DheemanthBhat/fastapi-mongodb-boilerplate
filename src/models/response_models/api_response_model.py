"""
Module containing definition of custom API response model.
"""

from pydantic import BaseModel
from src.constants import str_constants as sc


class APIResponse(BaseModel):
    """
    Definition for custom API response.
    """

    status: bool = True
    message: str


class APISuccessResponse(BaseModel):
    """
    Definition for custom API response.
    """

    status: bool = True
    message: str = sc.SUCCESS_MESSAGE
    data: dict | None = None


class APIFailureResponse(BaseModel):
    """
    Definition for custom API failure response.
    """

    status: bool = False
    message: str = sc.INTERNAL_SERVER_ERROR


class FiledError(BaseModel):
    """
    Definition for Field level errors.
    """

    type: str
    field: str
    message: str


class ValidationErrorResponse(APIFailureResponse):
    """
    Definition for custom API Validation response.
    """

    message: str = sc.INVALID_REQUEST
    errors: list[FiledError] | None = None
