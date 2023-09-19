"""HomeLINK Auth."""
import logging
from abc import ABC, abstractmethod
from typing import Any, Mapping, Optional

from aiohttp import ClientError, ClientResponse, ClientSession

from .const import BASE_URL

AUTHURL = "https://auth.live.homelync.io/oauth2"

AUTHORIZATION_HEADER = "Authorization"


_LOGGER = logging.getLogger(__name__)


class AbstractAuth(ABC):
    """Abstract class to make authenticated requests."""

    def __init__(
        self,
        websession: ClientSession,
    ):
        """Initialize the auth."""
        self._websession = websession
        # self._url = AUTHURL

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def request(
        self, method: str, url_suffix: str, **kwargs: Optional[Mapping[str, Any]]
    ) -> ClientResponse:
        """Make a request."""
        try:
            access_token = await self.async_get_access_token()
        except ClientError as err:
            raise RuntimeError(f"Access token failure: {err}") from err
        headers = {
            AUTHORIZATION_HEADER: f"Bearer {access_token}",
            "accept": "application/json",
        }
        url = f"{BASE_URL}{url_suffix}"
        _LOGGER.debug("request[%s]=%s %s", method, url, kwargs.get("params"))
        if method == "post" and "json" in kwargs:
            _LOGGER.debug("request[post json]=%s", kwargs["json"])
        return await self._websession.request(method, url, **kwargs, headers=headers)

    async def async_get_token(
        self, url: str, **kwargs: Optional[Mapping[str, Any]]
    ) -> ClientResponse:
        """Make a request."""
        url = f"{AUTHURL}{url}"
        _LOGGER.debug("request[%s]=%s %s", "get", url, kwargs.get("params"))
        return await self._websession.request("get", url, **kwargs)
