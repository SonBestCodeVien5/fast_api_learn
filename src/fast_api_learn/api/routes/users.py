from fastapi import APIRouter

from fast_api_learn.schemas.user import UserCreate


router = APIRouter()


@router.get("/")
async def get_users(
    skip: int = 0,
    limit: int = 10,
):
    return {
        "skip": skip,
        "limit": limit,
    }


@router.get("/{user_id}")
async def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "User example",
    }


@router.post("/")
async def create_user(user: UserCreate):
    return {
        "message": "User created",
        "user": user,
    }