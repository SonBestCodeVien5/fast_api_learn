from fastapi import APIRouter, HTTPException, status
from fast_api_learn.exceptions.user import (
    UserEmailAlreadyExistsError,
    UserNotFoundError,
)
from fast_api_learn.schemas.user import UserCreate, UserResponse
from fast_api_learn.services import user_service


router = APIRouter()


@router.get(
    "/",
    response_model=list[UserResponse],
)
async def get_users(skip: int = 0, limit: int = 10):
    return user_service.get_users(skip, limit)


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
async def get_user(user_id: int):
   return user_service.get_user_by_id(user_id)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user: UserCreate):
    return user_service.create_user(user)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(user_id: int):
    return user_service.delete_user(user_id)