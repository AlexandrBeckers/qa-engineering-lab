import requests

from framework.config.settings import BASE_URL


class ApiClient:

    def __init__(self):
        self.base_url = BASE_URL

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"

        return requests.request(
            method=method,
            url=url,
            timeout=10,
            **kwargs
        )

    def get(self, endpoint: str, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request("POST", endpoint, **kwargs)
