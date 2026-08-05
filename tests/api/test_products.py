from framework.endpoints.products import ProductEndpoints


def test_get_products(api_client):

    response = api_client.get(
        ProductEndpoints.LIST
    )

    assert response.status_code == 200

    data = response.json()

    assert "count" in data
    assert "results" in data
    assert isinstance(data["count"], int)
    assert isinstance(data["results"], list)
