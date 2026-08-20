from uuid import uuid4

import pytest

from framework.api.products_api import ProductsApi
from framework.clients.api_client import ApiClient
from framework.clients.db_client import DatabaseClient


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def products_api(api_client):
    return ProductsApi(api_client)


@pytest.fixture
def db_client():
    client = DatabaseClient()

    yield client

    client.close()

@pytest.fixture
def public_products_test_data(db_client):
    suffix = uuid4().hex[:12]

    category_slug = f"qa-auto-category-{suffix}"
    available_slug = f"qa-auto-available-{suffix}"
    draft_slug = f"qa-auto-draft-{suffix}"

    category = db_client.fetchone(
        """
        INSERT INTO category_category (
            name,
            slug,
            created_at,
            updated_at
        )
        VALUES (%s, %s, NOW(), NOW())
        RETURNING id
        """,
        (
            f"QA Auto Category {suffix}",
            category_slug,
        ),
    )
    category_id = category[0]

    try:
        db_client.execute(
            """
            INSERT INTO product_product (
                name,
                slug,
                description,
                price,
                discount_price,
                status,
                created_at,
                updated_at,
                category_id,
                creator_id
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, NOW(), NOW(), %s, %s
            )
            """,
            (
                f"QA Auto Available {suffix}",
                available_slug,
                "Temporary available product for API testing.",
                "99.99",
                None,
                "available",
                category_id,
                None,
            ),
        )

        db_client.execute(
            """
            INSERT INTO product_product (
                name,
                slug,
                description,
                price,
                discount_price,
                status,
                created_at,
                updated_at,
                category_id,
                creator_id
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, NOW(), NOW(), %s, %s
            )
            """,
            (
                f"QA Auto Draft {suffix}",
                draft_slug,
                "Temporary draft product for API testing.",
                "49.99",
                None,
                "draft",
                category_id,
                None,
            ),
        )

        yield {
            "available_slug": available_slug,
            "draft_slug": draft_slug,
        }

    finally:
        db_client.execute(
            "DELETE FROM product_product WHERE slug = %s",
            (available_slug,),
        )
        db_client.execute(
            "DELETE FROM product_product WHERE slug = %s",
            (draft_slug,),
        )
        db_client.execute(
            "DELETE FROM category_category WHERE id = %s",
            (category_id,),
        )
