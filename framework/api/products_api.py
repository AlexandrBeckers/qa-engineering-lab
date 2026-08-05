from framework.clients.api_client import ApiClient
from framework.endpoints.products import ProductEndpoints


class ProductsApi:

    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def get_products(self):
        return self.api_client.get(
            ProductEndpoints.LIST
        )
