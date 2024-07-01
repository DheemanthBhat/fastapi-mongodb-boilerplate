"""
Module containing db queries.
"""

from src.helpers import dt_utils


async def create_item_in_db(db_ssn, new_item: dict):
    """
    Function containing query to add item to `items` collection.
    """
    db, ssn = db_ssn

    new_item["created_at"] = dt_utils.get_datetime()
    result = await db.items.insert_one(new_item, session=ssn)

    return str(result.inserted_id)
