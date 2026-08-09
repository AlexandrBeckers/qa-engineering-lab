import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    api_base_url: str
    api_timeout_seconds: float

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            api_base_url=os.getenv(
                "API_BASE_URL",
                "https://jsonplaceholder.typicode.com",
            ),
            api_timeout_seconds=float(os.getenv("API_TIMEOUT_SECONDS", "10")),
        )
