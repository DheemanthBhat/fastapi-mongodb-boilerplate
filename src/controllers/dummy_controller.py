"""
Module containing business login related to User management.
"""

import random
import logging
from fastapi import status, HTTPException
from src.helpers import utils, dt_utils
from src.constants import str_constants as sc


logger = logging.getLogger(__name__)


def do_operation_1():
    """
    Function to perform dummy operation-1 and return output as API response.
    """
    try:
        logger.info("Performing operation: 1 / 0")
        _ = 1 / 0

    except ZeroDivisionError as err:
        logger.error("Failed to perform operation: 1 / 0")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=err) from err

    return utils.success_response(message=sc.OPERATION_SUCCESS)


def get_dummy_obj():
    """
    Function to generate random object.
    """
    return {
        "str_field": "Hello World!",
        "int_field": random.randint(0, 99),
        "float_field": random.uniform(0, 99),
        "bool_field": True if random.getrandbits(1) else False,
        "list_field": random.sample(range(0, 99), 5),
        "optional_field": f"Current timestamp: {dt_utils.get_timestamp()}",
    }


def do_operation_2(_):
    """
    Function to perform dummy operation-2 and return output as API response.
    """
    logger.info("Generating random dummy data for response.")

    upper_limit = random.randint(2, 5)
    logger.info("Generating %s dummy objects for `complex_field`.", upper_limit)

    dummy_obj = get_dummy_obj()

    data = {
        **dummy_obj,  # Spread above `dummy_obj` here.
        "complex_field": [get_dummy_obj() for _ in range(0, upper_limit)],
    }

    return utils.success_response(message=sc.OPERATION_SUCCESS, data=data)
