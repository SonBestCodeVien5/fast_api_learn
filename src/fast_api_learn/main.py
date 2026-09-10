from fastapi import FastAPI

from fast_api_learn.api.routes.users import router as users_router


app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello FastAPI"
    }


app.include_router(
    users_router,
    prefix="/users",
)