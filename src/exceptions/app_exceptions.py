"""
Module containing definitions of custom exceptions.
"""


class ValidationError(Exception):
    """
    Definition for custom validation error.
    """

    def __init__(self, message):
        self.message = message
