from framework.config.settings import (
    BASE_URL,
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER,
    REQUEST_TIMEOUT,
)


def test_settings():
    assert BASE_URL.startswith(("http://", "https://"))
    assert isinstance(REQUEST_TIMEOUT, float)
    assert REQUEST_TIMEOUT > 0

    assert DB_HOST
    assert isinstance(DB_PORT, int)
    assert DB_PORT > 0
    assert DB_NAME
    assert DB_USER
    assert DB_PASSWORD
