def test_public_products_show_available_and_hide_draft(
    products_api,
    public_products_test_data,
):
    response = products_api.get_products()

    assert response.status_code == 200

    data = response.json()
    products_by_slug = {
        product["slug"]: product
        for product in data["results"]
    }

    available_slug = public_products_test_data["available_slug"]
    draft_slug = public_products_test_data["draft_slug"]

    assert available_slug in products_by_slug
    assert products_by_slug[available_slug]["status"] == "available"
    assert draft_slug not in products_by_slug

def test_public_product_detail_returns_available_product(
    products_api,
    public_products_test_data,
):
    available_slug = public_products_test_data["available_slug"]

    response = products_api.get_product(available_slug)

    assert response.status_code == 200

    data = response.json()

    assert data["slug"] == available_slug
    assert data["status"] == "available"
    assert data["final_price"] == "99.99"

def test_public_product_detail_hides_draft_product(
    products_api,
    public_products_test_data,
):
    draft_slug = public_products_test_data["draft_slug"]

    response = products_api.get_product(draft_slug)

    assert response.status_code == 404
