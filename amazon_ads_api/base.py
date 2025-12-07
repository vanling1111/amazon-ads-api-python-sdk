"""
Amazon Ads API 基础客户端
职责：认证、HTTP请求、错误处理

SOLID原则：
- S: 只负责HTTP通信和认证
- O: 通过继承扩展功能
- L: 子类可替换
- I: 最小接口
- D: 依赖抽象
"""

import gzip
import json
import time
from abc import ABC
from datetime import datetime, timedelta
from enum import StrEnum
from typing import Any, Self
from dataclasses import dataclass, field

import requests
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

# Type Aliases
type AccessToken = str
type ProfileID = str
type JSONData = dict[str, Any]
type JSONList = list[JSONData]


class AdsRegion(StrEnum):
    """Amazon Ads API 区域"""
    NA = "https://advertising-api.amazon.com"
    EU = "https://advertising-api-eu.amazon.com"
    FE = "https://advertising-api-fe.amazon.com"


@dataclass
class AmazonAdsError(Exception):
    """Amazon Ads API 错误"""
    status_code: int
    message: str
    details: JSONData = field(default_factory=dict)

    def __str__(self) -> str:
        return f"[{self.status_code}] {self.message}"


class BaseAdsClient(ABC):
    """
    Amazon Ads API 基础客户端
    
    职责：
    - OAuth2认证（自动刷新Token）
    - HTTP请求封装（GET/POST/PUT/DELETE）
    - 错误处理和重试
    - Rate Limit处理
    """

    TOKEN_URL = "https://api.amazon.com/auth/o2/token"

    __slots__ = (
        "client_id", "client_secret", "refresh_token",
        "base_url", "profile_id", "max_retries", "timeout",
        "_access_token", "_token_expires_at", "session"
    )

    def __init__(
        self,
        client_id: str = "",
        client_secret: str = "",
        refresh_token: str = "",
        region: AdsRegion = AdsRegion.NA,
        profile_id: ProfileID | None = None,
        max_retries: int = 3,
        timeout: int = 30,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.base_url = region.value
        self.profile_id = profile_id
        self.max_retries = max_retries
        self.timeout = timeout

        self._access_token: AccessToken | None = None
        self._token_expires_at: datetime | None = None

        self.session = requests.Session()

    def with_profile(self, profile_id: ProfileID) -> Self:
        """设置Profile ID，支持链式调用"""
        self.profile_id = profile_id
        return self

    # ============ OAuth2 认证 ============

    def _refresh_access_token(self) -> AccessToken:
        """刷新Access Token"""
        response = requests.post(
            self.TOKEN_URL,
            data={
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
            timeout=self.timeout,
        )

        if not response.ok:
            raise AmazonAdsError(
                status_code=response.status_code,
                message="Failed to refresh token",
                details=response.json() if response.text else {},
            )

        data = response.json()
        self._access_token = data["access_token"]
        expires_in = data.get("expires_in", 3600)
        self._token_expires_at = datetime.now() + timedelta(seconds=expires_in - 60)

        logger.debug(f"Token refreshed, expires at {self._token_expires_at}")
        return self._access_token

    def _get_access_token(self) -> AccessToken:
        """获取有效的Access Token"""
        if (
            self._access_token is None
            or self._token_expires_at is None
            or datetime.now() >= self._token_expires_at
        ):
            return self._refresh_access_token()
        return self._access_token

    def _get_headers(self) -> dict[str, str]:
        """构建请求头"""
        headers = {
            "Authorization": f"Bearer {self._get_access_token()}",
            "Amazon-Advertising-API-ClientId": self.client_id,
            "Content-Type": "application/json",
        }
        if self.profile_id:
            headers["Amazon-Advertising-API-Scope"] = self.profile_id
        return headers

    # ============ HTTP 方法 ============

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        reraise=True,
    )
    def _request(
        self,
        method: str,
        endpoint: str,
        params: JSONData | None = None,
        json_data: JSONData | JSONList | None = None,
    ) -> JSONData | JSONList:
        """执行HTTP请求"""
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers()

        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_data,
            timeout=self.timeout,
        )

        # Rate Limit处理
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            logger.warning(f"Rate limited, sleeping {retry_after}s")
            time.sleep(retry_after)
            raise AmazonAdsError(429, "Rate limited", {"retry_after": retry_after})

        if not response.ok:
            error_detail = response.json() if response.text else {}
            raise AmazonAdsError(
                status_code=response.status_code,
                message=f"API request failed: {endpoint}",
                details=error_detail,
            )

        if response.status_code == 204:
            return {}

        return response.json()

    def get(self, endpoint: str, params: JSONData | None = None) -> JSONData | JSONList:
        """GET请求"""
        return self._request("GET", endpoint, params=params)

    def post(
        self,
        endpoint: str,
        json_data: JSONData | JSONList | None = None,
        params: JSONData | None = None,
    ) -> JSONData | JSONList:
        """POST请求"""
        return self._request("POST", endpoint, params=params, json_data=json_data)

    def put(
        self,
        endpoint: str,
        json_data: JSONData | JSONList | None = None,
    ) -> JSONData | JSONList:
        """PUT请求"""
        return self._request("PUT", endpoint, json_data=json_data)

    def delete(self, endpoint: str) -> JSONData:
        """DELETE请求"""
        result = self._request("DELETE", endpoint)
        return result if isinstance(result, dict) else {}

    # ============ 报告下载 ============

    def download_report(self, url: str) -> JSONList:
        """下载并解压报告"""
        response = self.session.get(url, timeout=60)
        if not response.ok:
            return []

        try:
            decompressed = gzip.decompress(response.content)
            return json.loads(decompressed)
        except Exception as e:
            logger.error(f"Failed to decompress report: {e}")
            return []

