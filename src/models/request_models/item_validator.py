"""
Module containing models.
"""

from pydantic import BaseModel


class Item(BaseModel):
    """
    Definition for Item.
    """

    name: str
