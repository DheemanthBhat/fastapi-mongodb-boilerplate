"""
Module containing all reusable logics as utility functions.
"""

from src.constants import str_constants as sc


def is_empty(element) -> bool:
    """
    Function to check if input `element` is empty.

    Other than some special exclusions and inclusions,
    this function returns boolean result of Falsy check.
    """
    if (isinstance(element, int) or isinstance(element, float)) and element == 0:
        # Exclude 0 and 0.0 from the Falsy set.
        return False
    elif isinstance(element, str) and len(element.strip()) == 0:
        # Include string with one or more empty space(s) into Falsy set.
        return True
    elif isinstance(element, bool):
        # Exclude False from the Falsy set.
        return False
    elif (isinstance(element, list) or isinstance(element, dict) or isinstance(element, set)) and len(element) == 0:
        return True
    else:
        # Falsy check.
        return False if element else True


def is_not_empty(element) -> bool:
    """
    Function to check if input `element` is not empty.
    """
    return not is_empty(element)


def success_response(message: str = sc.SUCCESS_MESSAGE, data: dict = None):
    """
    Function to build and return success response.
    """
    res = {
        "status": True,
        "message": message,
    }

    if is_not_empty(data):
        res["data"] = data

    return res


def failure_response(message: str = sc.INTERNAL_SERVER_ERROR, errors: list = None):
    """
    Function to build and return failure response.
    """
    res = {
        "status": False,
        "message": message,
    }

    if is_empty(errors):
        return res

    """
    Check if 'errors' is a list of dictionary containing validation
    details for each field (in Pydantic model) validated by FastAPI.
    """
    err_list = []
    for error in errors:
        if "type" in error and "loc" in error and "msg" in error:
            err_list.append(
                {
                    "type": error["type"],
                    "field": "NA" if is_empty(error["loc"]) else " -> ".join([str(fn) for fn in error["loc"]]),
                    "message": error["msg"],
                }
            )

    res["errors"] = err_list if len(err_list) > 0 else errors

    return res
