"""Lighting Gale api module interface

CONSTANTS:
    FMT_LG: LG datetime format
"""
from abc import ABC, abstractmethod
import urllib3
from datetime import datetime
import json
import logging
from pathlib import Path
from typing import Union, Optional
from zoneinfo import ZoneInfo

from pydantic import BaseModel, Field, ConfigDict
import requests

logger = logging.getLogger(__name__)

# Datetime format for LG
FMT_LG = "%a, %d %b %Y %H:%M:%S GMT"


class Token(BaseModel):
    access_token: str
    token_type: str  # bearer
    expires_in: int  # 43199
    issued: str = Field(..., alias=".issued")  # Tue, 25 Oct 2022 21:11:55 GMT
    expires: str = Field(..., alias=".expires")  # Wed, 26 Oct 2022 09:11:55 GMT
    client_name: str = Field(..., alias="clientName")
    expiration_date: str = Field(..., alias="expirationDate")  # 2020-03-31


class TokenResponse(BaseModel):
    status: int
    token: Optional[Token] = None
    message: Optional[str] = None

    model_config = ConfigDict(extra="allow")


class TokenCache(ABC):
    """Interface for token cache."""

    @abstractmethod
    def save(self, token_data: dict) -> None:
        """Save token in persisten storage."""

    @abstractmethod
    def retrieve(self) -> dict:
        """Load token from persisten storage."""


class TokenFileStorage(TokenCache):
    """_summary_

    Args:
        filename: _A path that reference a file.
    """

    def __init__(self, filename: Path) -> None:
        filename.parent.mkdir(exist_ok=True, parents=True)
        self.filename = filename

    def save(self, token_data: dict) -> None:
        """Save token in persisten storage as json."""
        logger.debug(f"Saving token to {self.filename}")
        with open(self.filename, "w") as j:
            json.dump(token_data, j)

    def retrieve(self) -> dict:
        """Load token from persisten storage as json."""
        try:
            with open(self.filename, "r") as j:
                return json.load(j)
        except FileNotFoundError:
            return {}


class LGAuth:
    """LG Authentication related process.

    Attributes:
        auth_file: A path that reference a cache auth response.

    Args:
        username: LG username account
        password: LG password account
        base_url: API base URL
        ssl_verify: False for disable SSL warnings. LG use HTTP, less secure.
        disable_request_warning: disable logger urllib3 InsecureRequestWarning.
    """

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        ssl_verify: bool,
        disable_request_warning: bool = False,
        token_cache: TokenCache = None,
        # token: Token = None,
    ) -> None:
        self.username = username
        self.__password = password
        self.base_url = base_url
        self.ssl_verify = ssl_verify
        self.token_cache = token_cache
        if disable_request_warning:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def get_access_token(self) -> str:
        """Start process for getting token.

        1. Verify if token in cache.
        2. Verify if token is expired.
        3. Renew token if expired or not in cache.

        Returns:
            A valid access token.
        """
        token = self.get_token_from_cache()
        if token and self.token_expiration_is_valid(token.expires):
            return token.access_token

        logger.debug("Requesting new token to server")
        token = self.request_token()
        if self.token_cache:
            logger.debug("Saving token to cache")
            self.token_cache.save(token_data=token.model_dump(by_alias=True))
        else:
            logger.debug("Token is not cached")
        return token.access_token

    def get_token_from_cache(self) -> Union[Token, None]:
        """Load token from cache.

        Returns:
            TokenResponse: data from file if cached or None
        """
        if not self.token_cache:
            return
        token_data = self.token_cache.retrieve()
        if not token_data:
            return
        token = Token(**token_data)
        return token

    def request_token(self) -> Token:
        """Make a request to server to obtain a token.

        Returns:
            Authentication response with access_token and expiration.

        Raises:
            ValueError: If username or password is invalid.
            HTTPError: If error response.
        """
        url = self.base_url + "/GetToken"
        auth_headers = {"username": self.username, "password": self.__password}
        response = requests.post(url, headers=auth_headers, verify=self.ssl_verify)

        try:
            data_response = response.json()
        except requests.exceptions.JSONDecodeError:
            logger.exception("Error in JSON response from server")
            raise

        token_response = TokenResponse(**data_response)

        if token_response.status == -1:
            # {"message": "User Name or Password is Invalid", "status": "-1"}
            raise ValueError(
                f"Code:{response.status_code}. Response message: {token_response.message}"
            )

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            logger.exception("Error in response from server")
            raise
        return token_response.token

    @staticmethod
    def token_expiration_is_valid(expires: str) -> bool:
        """Check if token is expired or not based on datetime.

        Args:
            expires: value retrived from server and found in `Token.expires`

        Returns:
            True for valid token, false otherwise (token is expired).
        """
        # GIVE extra seconds before expiration occurs

        THRESHOLD = 60
        expires_dt = datetime.strptime(expires, FMT_LG).replace(
            tzinfo=ZoneInfo("UTC")
        )
        now = datetime.now().astimezone()
        elapsed = expires_dt - now

        if elapsed.total_seconds() > THRESHOLD:
            valid = True
        else:
            valid = False
        return valid
