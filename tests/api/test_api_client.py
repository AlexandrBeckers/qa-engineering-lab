def test_create_client(api_client):

    assert api_client.base_url == "http://localhost:8001"

    assert api_client.session is not None

    assert (
        api_client.session.headers["Content-Type"]
        == "application/json"
    )
