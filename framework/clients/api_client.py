import requests

from framework.config.settings import BASE_URL


class ApiClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"

        response = self.session.request(
            method=method,
            url=url,
            timeout=10,
            **kwargs,
        )

        return response

    def get(self, endpoint: str, **kwargs):
        return self._request(
            "GET",
            endpoint,
            **kwargs,
        )

    def post(self, endpoint: str, **kwargs):
        return self._request(
            "POST",
            endpoint,
            **kwargs,
        )
