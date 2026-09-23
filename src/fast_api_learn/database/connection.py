import psycopg


DATABASE_URL = (
    "postgresql://fastapi:fastapi"
    "@localhost:5432/fastapi_learn"
)


def test_connection():
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

    return result