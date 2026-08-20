from os import getenv
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def get_required_env(name: str) -> str:
    value = getenv(name)

    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}"
        )

    return value


BASE_URL = get_required_env("BASE_URL").rstrip("/")
REQUEST_TIMEOUT = float(get_required_env("REQUEST_TIMEOUT"))

DB_HOST = get_required_env("DB_HOST")
DB_PORT = int(get_required_env("DB_PORT"))
DB_NAME = get_required_env("DB_NAME")
DB_USER = get_required_env("DB_USER")
DB_PASSWORD = get_required_env("DB_PASSWORD")
