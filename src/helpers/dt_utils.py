"""
Module containing all datetime utility functions.
"""

import time
from datetime import datetime, timedelta
from pytz import timezone, utc
from src.helpers import utils
from src.configs.app_config import app_config as ag
from src.constants import str_constants as sc, app_constants as ac


def get_datetime() -> datetime:
    """
    Function to return current datetime or input datetime in IST time zone.
    """
    # Set timezone based on config.
    ist_tz = timezone(ag.TIMEZONE)

    # Get UTC current datetime.
    utc_dt = datetime.now(utc)

    # Convert to specified time zone.
    ist_dt = utc_dt.astimezone(ist_tz)

    return ist_dt


def is_valid_timestamp(ts: int) -> bool:
    """
    Function to check if input `ts` is a valid timestamp.

    A valid timestamp must be of integer datatype and
    number of digits in timestamp must be either 10 or 13.
    """
    return isinstance(ts, int) and len(str(ts)) in [ac.TIMESTAMP_LEN_SEC, ac.TIMESTAMP_LEN_MSEC]


def get_timestamp(in_seconds: bool = False) -> int:
    """
    Function to return current timestamp in milliseconds by default.
    """
    ts_sec = time.time()  # Current timestamp in seconds.
    ts_msec = ts_sec * 1000  # Current timestamp in milliseconds.

    return round(ts_sec if in_seconds else ts_msec)


def get_timestamp_in_sec(timestamp: int = time.time()) -> int:
    """
    Function to convert input `timestamp` to seconds if it is in milliseconds.
    """
    if len(str(timestamp)) == ac.TIMESTAMP_LEN_SEC:
        return timestamp
    elif len(str(timestamp)) == ac.TIMESTAMP_LEN_MSEC:
        return timestamp // 1000
    else:
        raise ValueError(sc.INVALID_TIMESTAMP)


def timestamp_to_datetime(timestamp) -> datetime:
    """
    Function to convert timestamp to Python datetime object.
    """
    # Get timestamp in seconds.
    ts_in_sec = get_timestamp_in_sec(timestamp)

    # Convert timestamp to Python datetime object.
    return datetime.fromtimestamp(ts_in_sec, tz=timezone(ag.TIMEZONE))


def adjust_days(dt=None, days=0):
    """
    Function to adjust days by adding or subtracting days from input `date_time`.
    """
    if utils.is_empty(dt):
        dt = get_datetime()

    return dt.date() + timedelta(days=days)


def get_formatted_datetime(dt=None, dt_fmt="%Y-%m-%dT%H:%M:%S.%f", rm_ms=False):
    """
    Function to return formatted datetime without microsecond.
    """
    if utils.is_empty(dt):
        dt = get_datetime()

    # Remove microsecond if `rm_ms` is set to True.
    dt = dt.replace(microsecond=0) if rm_ms else dt
    return dt.strftime(dt_fmt)


def set_time(dt=None, h=0, m=0, s=0, ms=0):
    """
    Function set time in Datetime object.
    """
    if utils.is_empty(dt):
        dt = get_datetime()

    return dt.replace(hour=h, minute=m, second=s, microsecond=ms)
