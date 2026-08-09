from urllib.parse import urljoin

import requests


class ApiClient:
    """Small HTTP client shared by API tests."""

    def __init__(self, base_url: str, timeout_seconds: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/") + "/"
        self.timeout_seconds = timeout_seconds
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def get(self, path: str, **kwargs: object) -> requests.Response:
        return self.session.get(
            self._url(path),
            timeout=self.timeout_seconds,
            **kwargs,
        )

    def post(self, path: str, **kwargs: object) -> requests.Response:
        return self.session.post(
            self._url(path),
            timeout=self.timeout_seconds,
            **kwargs,
        )

    def close(self) -> None:
        self.session.close()

    def _url(self, path: str) -> str:
        return urljoin(self.base_url, path.lstrip("/"))
