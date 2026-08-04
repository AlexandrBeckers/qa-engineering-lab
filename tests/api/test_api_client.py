from framework.clients.api_client import ApiClient


def test_create_client():

    client = ApiClient()

    assert client.base_url == "http://localhost:8080"

    assert client.session is not None

    assert (
        client.session.headers["Content-Type"]
        == "application/json"
    )
