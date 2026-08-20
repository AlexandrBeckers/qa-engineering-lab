from typing import Any

import psycopg

from framework.config.settings import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER,
)


class DatabaseClient:
    def __init__(self):
        self.connection = psycopg.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            autocommit=True,
        )

    def fetchone(
        self,
        query: str,
        params: tuple[Any, ...] = (),
    ) -> tuple[Any, ...] | None:
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()

    def execute(
        self,
        query: str,
        params: tuple[Any, ...] = (),
    ) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)

    def close(self) -> None:
        self.connection.close()
