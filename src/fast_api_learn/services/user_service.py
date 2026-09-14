from fast_api_learn.exceptions.user import (
    UserEmailAlreadyExistsError,
    UserNotFoundError,
)
from fast_api_learn.schemas.user import UserCreate


users = [
    {"id": 1, "name": "Son", "email": "son@example.com", "age": 21},
    {"id": 2, "name": "Alice", "email": "alice@example.com", "age": 25},
]


def get_users(skip: int = 0, limit: int = 10):
    return users[skip : skip + limit]


def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise UserNotFoundError()


def create_user(user: UserCreate):
    for existing_user in users:
        if existing_user["email"] == user.email:
            raise UserEmailAlreadyExistsError()

    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
    }

    users.append(new_user)

    return new_user


def delete_user(user_id: int):
    user = get_user_by_id(user_id)
    users.remove(user)