import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Literal

from httpx import URL, codes

from wrapzor.core.credentials import Credentials
from wrapzor.errors import Message, ArgsError
from wrapzor.logs import logs
from wrapzor.utils import clean_domain, top_level_domain, now_str
from wrapzor.env import (
    TOKENS_DIR,
)


ZOHO_API = None


@dataclass
class ZohoApi:
    client_id: str | None
    client_secret: str | None
    account_domain: str | URL
    version: Literal["v5"] = "v5"
    credentials: Credentials = field(init=False)

    code: str | None = None
    _refresh_token: str | None = None
    _access_token: str | None = None

    country_code: Literal["eu", "in", "cn", "jp", "com.au", "com"] = "eu"
    domain: str | URL = URL(f"https://zohoapis.{country_code.lower()}")
    auth_type: Literal["Zoho-oauthtoken"] = "Zoho-oauthtoken"
    auth_header: dict | None = None

    max_retries: int = 5
    expected_status_code: int | list[int] | list[codes] = field(
        default_factory=lambda: [codes.OK, codes.CREATED, codes.NO_CONTENT]
    )
    http_invalid_token_status: int = codes.UNAUTHORIZED

    created_at: datetime = field(init=False, default_factory=datetime.utcnow)
    last_access_token_update: datetime | None = None
    last_token_injection: datetime | None = None

    tokens_path: Path = TOKENS_DIR
    tokens_filename: str = "tokens"

    @property
    def access_token(self):
        return self._access_token

    @property
    def refresh_token(self):
        return self._refresh_token

    def generate_auth_header(self):
        if self._access_token is None:
            self.auth_header = None
        else:
            self.auth_header = {
                "Authorization": f"{self.auth_type} {self._access_token}",
                "Content-Type": "application/json",
            }

    @access_token.setter
    def access_token(self, access_token: str):
        self._access_token = access_token
        self.last_access_token_update = datetime.utcnow()
        self.generate_auth_header()
        self.save_tokens()

    @refresh_token.setter
    def refresh_token(self, refresh_token: str | None):
        self._refresh_token = refresh_token
        self.save_tokens()

    def save_tokens(self):
        filename = (
            now_str()
            if self.tokens_filename is None
            else f"{self.tokens_filename}_{now_str()}"
            if self.tokens_filename != "test"
            else "test"
        )
        filename += ".json"

        if self.refresh_token is None:
            return

        with open(self.tokens_path / filename, "w") as file:
            json.dump(
                {
                    "datetime": datetime.utcnow(),
                    "ZOHO_CODE": self.code,
                    "ZOHO_CLIENT_ID": self.client_id,
                    "ZOHO_CLIENT_PASSWORD": self.client_secret,
                    "ZOHO_REFRESH_TOKEN": self.refresh_token,
                    "ZOHO_ACCESS_TOKEN": self.access_token,
                },
                file,
                default=self.serialize_token,
            )

    def __post_init__(self):
        self.credentials = Credentials(
            code=self.code, client_id=self.client_id, client_secret=self.client_secret
        )
        self.domain = clean_domain(self.domain)
        self.account_domain = clean_domain(self.account_domain)

        self.generate_auth_header()
        self.save_tokens()

        if self.code is not None and self.refresh_token is not None:
            logs.warning(Message.env_mismatch.value)

        if str(self.domain)[:4] != "http" or str(self.account_domain)[:4] != "http":
            raise ValueError(Message.missing_domain)

        if not isinstance(self.domain, URL):
            self.domain = URL(self.domain)

        if not isinstance(self.account_domain, URL):
            self.account_domain = URL(self.account_domain)

        if top_level_domain(self.domain) != top_level_domain(self.account_domain):
            raise ValueError(Message.suffix_mismatch.value)

    @staticmethod
    def serialize_token(cls):
        if isinstance(cls, datetime):
            return cls.isoformat()
        raise TypeError(f"Type {type(cls)!r} not serializable")

    @staticmethod
    def valid_credentials(
        client_id: str | None,
        client_secret: str | None,
        code: str | None = None,
        refresh_token: str | None = None,
    ):
        return (
            client_id is not None
            and client_secret is not None
            and (code is not None or refresh_token is not None)
        )

    @classmethod
    def init(
        cls,
        client_id: str | None,
        client_secret: str | None,
        code: str | None = None,
        refresh_token: str | None = None,
        account_domain: str | URL = "https://accounts.zoho.eu",
    ):
        global ZOHO_API

        if not cls.valid_credentials(client_id, client_secret, code, refresh_token):
            raise ArgsError(
                "You need to initialize wrapzor with at least valid client_id, "
                "client_secret and a zoho code or a refresh_token"
            )

        ZOHO_API = cls(
            code=code,
            client_id=client_id,
            client_secret=client_secret,
            account_domain=account_domain,
            _refresh_token=refresh_token,
        )
        return ZOHO_API


"""
VALID_CREDENTIALS = ZohoApi.valid_credentials(
    client_id=ZOHO_CLIENT_ID, client_secret=ZOHO_CLIENT_PASSWORD, code=ZOHO_CODE, refresh_token=ZOHO_REFRESH_TOKEN
)

if VALID_CREDENTIALS:
    ZohoApi.init(
        code=ZOHO_CODE,
        client_id=ZOHO_CLIENT_ID,
        client_secret=ZOHO_CLIENT_PASSWORD,
        account_domain=ZOHO_ACCOUNT_DOMAIN,
        refresh_token=ZOHO_REFRESH_TOKEN,
    )
"""
