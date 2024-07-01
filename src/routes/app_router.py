"""
Module to handle routes for entire application.
This module contains sub routes to various features.
"""

from fastapi import APIRouter, status
from src.models.response_models.api_response_model import ValidationErrorResponse, APIFailureResponse
from src.routes import dummy_router
from src.constants import str_constants as sc


router = APIRouter(
    prefix="/api",
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "model": ValidationErrorResponse,
            "description": sc.INVALID_REQUEST,
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": APIFailureResponse,
            "description": sc.INTERNAL_SERVER_ERROR,
        },
    },
)

# Router for Dummy APIs.
router.include_router(router=dummy_router.router)
