import pytest

from framework.api.products_api import ProductsApi
from framework.clients.api_client import ApiClient


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def products_api(api_client):
    return ProductsApi(api_client)
