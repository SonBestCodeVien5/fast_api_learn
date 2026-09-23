from fastapi import Request
from fastapi.responses import JSONResponse

from fast_api_learn.exceptions.user import (
    UserEmailAlreadyExistsError,
    UserNotFoundError,
)


async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundError,
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": "User not found",
        },
    )


async def user_email_already_exists_handler(
    request: Request,
    exc: UserEmailAlreadyExistsError,
):
    return JSONResponse(
        status_code=409,
        content={
            "detail": "Email already exists",
        },
    )