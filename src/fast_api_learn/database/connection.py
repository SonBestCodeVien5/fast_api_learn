import psycopg
from fast_api_learn.core.config import settings


def test_connection():
    with psycopg.connect(settings.database_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

    return result