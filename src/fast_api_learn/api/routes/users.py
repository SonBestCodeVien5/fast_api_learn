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
    try:
        return user_service.get_user_by_id(user_id)
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user: UserCreate):
    try:
        return user_service.create_user(user)
    except UserEmailAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(user_id: int):
    try:
        user_service.delete_user(user_id)
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )