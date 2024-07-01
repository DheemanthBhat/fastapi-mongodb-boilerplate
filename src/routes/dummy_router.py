"""
Module containing all the APIs related to User.
"""

from fastapi import APIRouter
from src.models.request_models.dummy_validator import DummyPayload
from src.models.response_models.dummy_response_model import DummyResponse1, DummyResponse2
from src.controllers import dummy_controller
from src.constants import api_docs as ad


router = APIRouter(prefix="/dummy", tags=["Dummy"])


@router.get("/operation-1", response_model=DummyResponse1, description=ad.API_DUMMY_1)
async def perform_operation_1():
    """
    API to perform dummy operation-1 to test application logging.
    """
    return dummy_controller.do_operation_1()


@router.post("/operation-2", response_model=DummyResponse2, description=ad.API_DUMMY_2)
async def perform_operation_2(dummy_payload: DummyPayload):
    """
    API to perform dummy operation-2 to test payload validation.
    """
    return dummy_controller.do_operation_2(dummy_payload)
