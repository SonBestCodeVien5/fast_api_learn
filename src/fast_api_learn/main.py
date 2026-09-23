from fastapi import FastAPI

from fast_api_learn.api.routes.users import router as users_router
from fast_api_learn.exceptions.handlers import (
    user_email_already_exists_handler,
    user_not_found_handler,
)
from fast_api_learn.exceptions.user import (
    UserEmailAlreadyExistsError,
    UserNotFoundError,
)


app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello FastAPI"
    }


app.add_exception_handler(
    UserNotFoundError,
    user_not_found_handler,
)

app.add_exception_handler(
    UserEmailAlreadyExistsError,
    user_email_already_exists_handler,
)


app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"],
)