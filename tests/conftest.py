import pytest

from framework.clients.api_client import ApiClient


@pytest.fixture
def api_client():
    return ApiClient()
