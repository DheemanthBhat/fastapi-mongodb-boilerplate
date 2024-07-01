"""
Module to configure logging.
"""

from logging.config import dictConfig


def setup_loggers(log_level):
    """
    Function to setup loggers using custom logging configuration.
    """
    # Default format.
    dft_fmt = "%(levelprefix)s %(message)s"
    # Uvicorn access format.
    acc_fmt = '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
    # Detail format.
    dtl_fmt = '%(levelprefix)s %(name)s.%(funcName)s() L:%(lineno)d - "%(message)s"'

    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "format": dft_fmt,
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "use_colors": True,
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "format": acc_fmt,
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "use_colors": True,
            },
            "detailed": {
                "()": "uvicorn.logging.DefaultFormatter",
                "format": dtl_fmt,
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "use_colors": True,
            },
        },
        "handlers": {
            "default": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "default",
            },
            "access": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "access",
            },
            "detailed": {
                "class": "logging.StreamHandler",
                "level": "ERROR",
                "formatter": "detailed",
            },
        },
        "root": {
            "level": log_level,
            "handlers": ["default", "detailed"],
        },
        "loggers": {
            "uvicorn": {
                "level": log_level,
                "handlers": ["default"],
                "propagate": False,
            },
            "uvicorn.access": {
                "level": log_level,
                "handlers": ["access"],
                "propagate": False,
            },
            "uvicorn.error": {
                "level": log_level,
                "handlers": ["default"],
                "propagate": False,
            },
        },
    }

    dictConfig(log_config)
