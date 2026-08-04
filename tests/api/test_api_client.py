from framework.clients.api_client import ApiClient


def test_create_client():
    client = ApiClient()

    assert client.base_url == "http://localhost:8080"
