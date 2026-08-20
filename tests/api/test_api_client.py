from framework.config.settings import BASE_URL


def test_create_client(api_client):
    assert api_client.base_url == BASE_URL
    assert api_client.session is not None
    assert (
        api_client.session.headers["Content-Type"]
        == "application/json"
    )
