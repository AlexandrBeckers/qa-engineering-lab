import pytest

from framework.clients.api_client import ApiClient


def test_get_post_by_id(api_client: ApiClient) -> None:
    response = api_client.get("/posts/1")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")
    assert response.json() == {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": (
            "quia et suscipit\n"
            "suscipit recusandae consequuntur expedita et cum\n"
            "reprehenderit molestiae ut ut quas totam\n"
            "nostrum rerum est autem sunt rem eveniet architecto"
        ),
    }


def test_filter_posts_by_user(api_client: ApiClient) -> None:
    response = api_client.get("/posts", params={"userId": 1})

    assert response.status_code == 200
    posts = response.json()
    assert posts
    assert all(post["userId"] == 1 for post in posts)


def test_create_post(api_client: ApiClient) -> None:
    payload = {"title": "qa", "body": "api test", "userId": 7}

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201
    assert response.json() == {**payload, "id": 101}


def test_unknown_post_returns_not_found(api_client: ApiClient) -> None:
    response = api_client.get("/posts/0")

    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.parametrize("resource", ["posts", "comments", "users"])
def test_collection_smoke(api_client: ApiClient, resource: str) -> None:
    response = api_client.get(f"/{resource}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()
