from fastapi import APIRouter, HTTPException, status

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
    for user in users:
        if user["id"] == user_id:
            return user
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
    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists",
            )

    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
    }

    users.append(new_user)

    return new_user

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
    )