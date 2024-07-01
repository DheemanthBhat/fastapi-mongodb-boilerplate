"""
Module containing string constants used in the application.
"""

# General messages.
SUCCESS_MESSAGE = "Success!"  # used in health check.
INTERNAL_SERVER_ERROR = "Internal server error."
VALID_REQUEST = "Valid request."
INVALID_REQUEST = "Invalid request."
INVALID_TIMESTAMP = "Invalid timestamp. Number of digits in timestamp must be either 10 or 13."

# HTTP error response messages.
UNAUTHORIZED_REQUEST = "Unauthorized request."  # HTTP status 401.
FORBIDDEN_REQUEST = "Forbidden request."  # HTTP status 403.
RESOURCE_NOT_FOUND = "Resource not found."  # HTTP status 404.
SERVICE_UNAVAILABLE = "Service is unavailable."  # HTTP status 503.

# Dummy payload field descriptions
STR_FIELD_DESC = "String datatype field."
INT_FIELD_DESC = "Integer datatype field."
FLOAT_FIELD_DESC = "Float datatype field."
BOOL_FIELD_DESC = "Boolean datatype field."
LIST_FIELD_DESC = "List datatype field."
OPTIONAL_FIELD_DESC = "Option field of String datatype."
COMPLEX_FIELD_DESC = "List of complex object."

# Dummy API response.
OPERATION_SUCCESS = "Operation performed successfully."
