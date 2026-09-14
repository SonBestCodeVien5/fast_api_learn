from fastapi import APIRouter, status

from fast_api_learn.schemas.user import UserCreate, UserResponse


router = APIRouter()

users = [
    {
        "id": 1,
        "name": "Son",
        "email": "son@example.com",
        "age": 21,
    },
    {
        "id": 2,
        "name": "Alice",
        "email": "alice@example.com",
        "age": 25,
    },
]


@router.get(
    "/",
    response_model=list[UserResponse],
    )
async def get_users(
    skip: int = 0,
    limit: int = 10,
): 
    return users[skip : skip + limit]



@router.get(
    "/{user_id}",
    response_model=UserResponse,
    )
async def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "User example",
        "email": "Email example",
        "age": 20,
    }


@router.post(
        "/",
        response_model=UserResponse,
        status_code=status.HTTP_201_CREATED,
    )
async def create_user(user: UserCreate):
    return {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
    }
