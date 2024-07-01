"""
Entry point for application server.
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError, ResponseValidationError, HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.helpers import utils, log_config
from src.constants import api_docs as ad, app_constants as ac, str_constants as sc
from src.configs.app_config import app_config as ag
from src.exceptions.app_exceptions import ValidationError
from src.db import MongoDBManager
from src.routes import app_router


# Setup application logging at required log level.
log_config.setup_loggers(log_level=ag.LOG_LEVEL)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    Function to perform tasks that are executed
    only once in the lifespan of the application.
    """
    manager = MongoDBManager()
    yield
    manager.close_connection()


# Initialize FastAPi application.
app = FastAPI(
    title=ac.APPLICATION_NAME,
    summary=ad.APP_SUMMARY,
    description=ad.APP_DESC,
    lifespan=lifespan,
    swagger_ui_parameters={
        # In Swagger docs, collapse the `Schemas` section by default.
        "defaultModelsExpandDepth": 0,
    },
)

# Enable CORS.
app.add_middleware(
    CORSMiddleware,
    allow_origins=ag.ALLOW_ORIGIN,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def fnf_exception_handler(req: Request, exc: HTTPException):
    """
    Exception handler:
    Custom exception handler for '404 Not Found'.
    """
    logger.error("Status:%s - %s - %s", exc.status_code, req.url.path, exc.detail)
    res = utils.failure_response(message=sc.RESOURCE_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=res)


@app.exception_handler(HTTPException)
async def http_exception_handler(_: Request, exc: HTTPException):
    """
    HTTPException handler:
    Receives all the errors captured while processing a HTTP request.
    """
    if exc and exc.status_code == status.HTTP_401_UNAUTHORIZED:
        message = sc.UNAUTHORIZED_REQUEST
        status_code = exc.status_code
    elif exc and exc.status_code == status.HTTP_403_FORBIDDEN:
        message = sc.FORBIDDEN_REQUEST
        status_code = exc.status_code
    elif exc and exc.status_code == status.HTTP_503_SERVICE_UNAVAILABLE:
        message = sc.SERVICE_UNAVAILABLE
        status_code = exc.status_code
    else:
        message = sc.INTERNAL_SERVER_ERROR
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    logger.error("Status:%s - %s", exc.status_code, exc.detail)
    res = utils.failure_response(message)
    return JSONResponse(status_code=status_code, content=res)


@app.exception_handler(RequestValidationError)
async def req_error_handler(_: Request, exc: RequestValidationError):
    """
    Exception handler:
    Receives all the errors captured while validating the request body.
    Request body validation is done in their respective pydantic models.
    """
    logger.error("Type:%s - %s", exc.__class__.__name__, exc.errors())
    res = utils.failure_response(message=sc.INVALID_REQUEST, errors=exc.errors())
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=res)


@app.exception_handler(ResponseValidationError)
async def response_error_handler(_: Request, exc: ResponseValidationError):
    """
    Exception handler:
    Receives all the errors captured while validating the response body.
    Response body validation is done in their respective pydantic models.
    """
    logger.error("Type:%s - %s", exc.__class__.__name__, exc.errors())
    res = utils.failure_response(message=sc.INTERNAL_SERVER_ERROR)
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=res)


@app.exception_handler(ValidationError)
async def validation_error_handler(_: Request, err: ValidationError):
    """
    Exception handler:
    Receives all the exceptions raised while validating the value in a variable.
    """
    logger.error("Type:%s - %s", err.__class__.__name__, err.message)
    res = utils.failure_response(message=err.message)
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=res)


@app.exception_handler(Exception)
async def general_exception_handler(_: Request, exc: Exception):
    """
    Exception handler:
    Receives all the exceptions that escaped above exception handlers.
    """
    logger.error("Type:%s - %s", exc.__class__.__name__, exc)
    res = utils.failure_response(message=sc.INTERNAL_SERVER_ERROR)
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=res)


@app.get("/", response_class=PlainTextResponse, tags=["Default"])
async def server_health():
    """
    Function to check server health by responding with "Success" message.
    """
    return sc.SUCCESS_MESSAGE


# Import App router.
app.include_router(app_router.router)
