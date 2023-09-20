import os
from urllib.parse import urljoin

import httpx


class Coinfeeds:
    def __init__(
        self,
        api_key: str | None = None,
        api_url: str = "https://api.coinfeeds.io/",
    ) -> None:
        api_key = api_key or os.getenv("COINFEEDS_API_KEY")
        if not api_key:
            msg = "`COINFEEDS_API_KEY` is not provided"
            raise RuntimeError(msg)
        self.api_key = api_key
        self.api_url = api_url

    def headers(self) -> dict:
        return {
            "x-api-key": self.api_key,
        }

    def coins(self, **kwargs) -> list[dict]:
        url = urljoin(self.api_url, "/coins/list")

        return httpx.get(url, headers=self.headers(), **kwargs)

    def news(self, coin_name: str, *, symbol: bool = False, **kwargs) -> dict:
        url = urljoin(
            self.api_url,
            f"/coins/{coin_name}/news?symbol={str(symbol).lower()}",
        )

        return httpx.get(url, headers=self.headers(), **kwargs).json()

    def tweets(self, coin_name: str, *, symbol: bool = False, **kwargs) -> dict:
        url = urljoin(
            self.api_url,
            f"/coins/{coin_name}/tweets?symbol={str(symbol).lower()}",
        )

        return httpx.get(url, headers=self.headers(), **kwargs).json()

    def podcasts(self, coin_name: str, *, symbol: bool = False, **kwargs) -> dict:
        url = urljoin(
            self.api_url,
            f"/coins/{coin_name}/podcasts?symbol={str(symbol).lower()}",
        )

        return httpx.get(url, headers=self.headers(), **kwargs).json()

    def videos(self, coin_name: str, *, symbol: bool = False, **kwargs) -> dict:
        url = urljoin(
            self.api_url,
            f"/coins/{coin_name}/videos?symbol={str(symbol).lower()}",
        )

        return httpx.get(url, headers=self.headers(), **kwargs).json()
