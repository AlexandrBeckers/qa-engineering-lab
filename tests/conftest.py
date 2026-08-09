from collections.abc import Iterator

import pytest

from framework.clients.api_client import ApiClient
from framework.config.settings import Settings


@pytest.fixture
def api_client() -> Iterator[ApiClient]:
    settings = Settings.from_env()
    client = ApiClient(
        base_url=settings.api_base_url,
        timeout_seconds=settings.api_timeout_seconds,
    )
    yield client
    client.close()
