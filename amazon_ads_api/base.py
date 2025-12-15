"""
Amazon Ads API 基础客户端（全异步版本）

使用 httpx 实现高性能异步 HTTP 客户端

特性：
- 全异步设计，支持高并发
- HTTP/2 支持，连接复用
- 自动重试和 Rate Limit 处理
- 共享 Token 管理器
- 连接池优化

SOLID原则：
- S: 只负责HTTP通信和认证
- O: 通过继承扩展功能
- L: 子类可替换
- I: 最小接口
- D: 依赖抽象
"""

import asyncio
import gzip
import json
from abc import ABC
from datetime import datetime, timedelta
from enum import StrEnum
from typing import Any, Self, Callable, Coroutine
from dataclasses import dataclass, field

import httpx
from loguru import logger

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
        if self.details:
            return f"[{self.status_code}] {self.message} - Details: {self.details}"
        return f"[{self.status_code}] {self.message}"


class AsyncTokenManager:
    """
    异步 Token 管理器（线程安全单例）
    
    所有 API 模块共享同一个 token，避免重复刷新
    使用 asyncio.Lock 保证并发安全
    """
    
    TOKEN_URL = "https://api.amazon.com/auth/o2/token"
    
    _instances: dict[str, "AsyncTokenManager"] = {}
    _lock = asyncio.Lock()
    
    def __new__(cls, client_id: str, client_secret: str, refresh_token: str, timeout: int = 30):
        """根据 refresh_token 创建或获取单例"""
        key = f"{client_id}:{refresh_token[:20]}"
        if key not in cls._instances:
            instance = super().__new__(cls)
            instance._initialized = False
            cls._instances[key] = instance
        return cls._instances[key]
    
    def __init__(self, client_id: str, client_secret: str, refresh_token: str, timeout: int = 30):
        if getattr(self, "_initialized", False):
            return
        
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.timeout = timeout
        self._access_token: AccessToken | None = None
        self._token_expires_at: datetime | None = None
        self._token_lock = asyncio.Lock()
        self._initialized = True
    
    async def get_access_token(self) -> AccessToken:
        """获取有效的 Access Token（异步，自动刷新）"""
        # 快速路径：token 有效时直接返回
        if (
            self._access_token is not None
            and self._token_expires_at is not None
            and datetime.now() < self._token_expires_at
        ):
            return self._access_token
        
        # 慢路径：需要刷新 token（加锁）
        async with self._token_lock:
            # 双重检查
            if (
                self._access_token is not None
                and self._token_expires_at is not None
                and datetime.now() < self._token_expires_at
            ):
                return self._access_token
            return await self._refresh_access_token()
    
    async def _refresh_access_token(self) -> AccessToken:
        """刷新 Access Token（调用前需持有锁）"""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                self.TOKEN_URL,
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": self.refresh_token,
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                },
            )

            if not response.is_success:
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


class BaseAdsClient(ABC):
    """
    Amazon Ads API 异步基础客户端
    
    特性：
    - 全异步设计（async/await）
    - HTTP/2 支持（连接复用，更低延迟）
    - 自动重试（指数退避）
    - Rate Limit 处理（自动等待）
    - 共享连接池
    
    使用方法：
        client = MyAPIClient(...)
        result = await client.get("/endpoint")
    """

    __slots__ = (
        "client_id", "client_secret", "refresh_token",
        "base_url", "profile_id", "max_retries", "timeout",
        "_token_manager", "_client", "_client_lock"
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

        # 使用共享的异步 TokenManager
        self._token_manager = AsyncTokenManager(client_id, client_secret, refresh_token, timeout)
        
        # 延迟初始化的 httpx 客户端
        self._client: httpx.AsyncClient | None = None
        self._client_lock = asyncio.Lock()

    async def _get_client(self) -> httpx.AsyncClient:
        """获取或创建 httpx 异步客户端（懒加载，带连接池）"""
        if self._client is None or self._client.is_closed:
            async with self._client_lock:
                if self._client is None or self._client.is_closed:
                    self._client = httpx.AsyncClient(
                        http2=True,  # 启用 HTTP/2
                        timeout=httpx.Timeout(self.timeout, connect=10.0),
                        limits=httpx.Limits(
                            max_connections=100,
                            max_keepalive_connections=20,
                            keepalive_expiry=30.0,
                        ),
                    )
        return self._client

    async def close(self) -> None:
        """关闭客户端连接"""
        if self._client and not self._client.is_closed:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> Self:
        """支持 async with 语法"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """退出时关闭连接"""
        await self.close()

    def with_profile(self, profile_id: ProfileID) -> Self:
        """设置 Profile ID，支持链式调用"""
        self.profile_id = profile_id
        return self

    # ============ OAuth2 认证 ============

    async def _get_access_token(self) -> AccessToken:
        """获取有效的 Access Token"""
        return await self._token_manager.get_access_token()

    async def _get_headers(self, content_type: str | None = None) -> dict[str, str]:
        """构建请求头
        
        Args:
            content_type: 自定义 Content-Type（用于 API v3）
        """
        token = await self._get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Amazon-Advertising-API-ClientId": self.client_id,
            "Content-Type": content_type or "application/json",
        }
        if content_type:
            headers["Accept"] = content_type
        if self.profile_id:
            headers["Amazon-Advertising-API-Scope"] = self.profile_id
        return headers

    # ============ HTTP 方法（全异步） ============

    async def _request(
        self,
        method: str,
        endpoint: str,
        params: JSONData | None = None,
        json_data: JSONData | JSONList | None = None,
        content_type: str | None = None,
        accept: str | None = None,
    ) -> JSONData | JSONList:
        """执行异步 HTTP 请求（带自动重试）
        
        Args:
            method: HTTP方法
            endpoint: API端点
            params: 查询参数
            json_data: JSON请求体
            content_type: 自定义 Content-Type
            accept: 自定义 Accept 头
        """
        url = f"{self.base_url}{endpoint}"
        headers = await self._get_headers(content_type)
        if accept:
            headers["Accept"] = accept
        client = await self._get_client()
        
        last_error: Exception | None = None
        
        for attempt in range(self.max_retries + 1):
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    json=json_data,
                )
                
                # Rate Limit 处理
                if response.status_code == 429:
                    retry_after = int(response.headers.get("Retry-After", 5))
                    logger.warning(f"Rate limited, waiting {retry_after}s (attempt {attempt + 1})")
                    await asyncio.sleep(retry_after)
                    continue
                
                # 服务器错误，重试
                if response.status_code >= 500:
                    wait_time = min(2 ** attempt, 30)  # 指数退避，最大30秒
                    logger.warning(f"Server error {response.status_code}, retrying in {wait_time}s")
                    await asyncio.sleep(wait_time)
                    continue
                
                # 客户端错误，不重试
                if not response.is_success:
                    error_detail = response.json() if response.text else {}
                    raise AmazonAdsError(
                        status_code=response.status_code,
                        message=f"API request failed: {endpoint}",
                        details=error_detail,
                    )
                
                # 成功
                if response.status_code == 204:
                    return {}
                
                return response.json()
                
            except httpx.TimeoutException as e:
                last_error = e
                wait_time = min(2 ** attempt, 30)
                logger.warning(f"Request timeout, retrying in {wait_time}s (attempt {attempt + 1})")
                await asyncio.sleep(wait_time)
                
            except httpx.RequestError as e:
                last_error = e
                wait_time = min(2 ** attempt, 30)
                logger.warning(f"Request error: {e}, retrying in {wait_time}s")
                await asyncio.sleep(wait_time)
        
        # 所有重试都失败
        raise AmazonAdsError(
            status_code=0,
            message=f"Request failed after {self.max_retries + 1} attempts",
            details={"last_error": str(last_error)},
        )

    async def get(
        self,
        endpoint: str,
        params: JSONData | None = None,
        content_type: str | None = None,
    ) -> JSONData | JSONList:
        """异步 GET 请求"""
        return await self._request("GET", endpoint, params=params, content_type=content_type)

    async def post(
        self,
        endpoint: str,
        json_data: JSONData | JSONList | None = None,
        params: JSONData | None = None,
        content_type: str | None = None,
        accept: str | None = None,
    ) -> JSONData | JSONList:
        """异步 POST 请求"""
        return await self._request("POST", endpoint, params=params, json_data=json_data, content_type=content_type, accept=accept)

    async def put(
        self,
        endpoint: str,
        json_data: JSONData | JSONList | None = None,
        content_type: str | None = None,
    ) -> JSONData | JSONList:
        """异步 PUT 请求"""
        return await self._request("PUT", endpoint, json_data=json_data, content_type=content_type)

    async def delete(self, endpoint: str) -> JSONData:
        """异步 DELETE 请求"""
        result = await self._request("DELETE", endpoint)
        return result if isinstance(result, dict) else {}

    # ============ 报告下载 ============

    async def download_report(self, url: str) -> JSONList:
        """异步下载并解压报告"""
        client = await self._get_client()
        
        try:
            response = await client.get(url, timeout=60.0)
            if not response.is_success:
                return []
            
            # 解压 gzip 数据
            decompressed = gzip.decompress(response.content)
            return json.loads(decompressed)
            
        except Exception as e:
            logger.error(f"Failed to download/decompress report: {e}")
            return []

    # ============ 并行执行 ============

    @staticmethod
    async def parallel_execute(
        tasks: list[Coroutine[Any, Any, Any]],
        max_concurrent: int = 10,
    ) -> list[Any]:
        """
        并行执行多个异步任务（带并发限制）
        
        Args:
            tasks: 协程列表
            max_concurrent: 最大并发数
            
        Returns:
            结果列表（按任务顺序）
        
        Example:
            tasks = [client.get(f"/campaigns/{id}") for id in campaign_ids]
            results = await client.parallel_execute(tasks, max_concurrent=5)
        """
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def limited_task(coro: Coroutine) -> Any:
            async with semaphore:
                return await coro
        
        return await asyncio.gather(
            *[limited_task(task) for task in tasks],
            return_exceptions=True,
        )

    async def parallel_paginate(
        self,
        fetch_page: Callable[[str | None], Coroutine[Any, Any, tuple[list, str | None]]],
        max_workers: int = 5,
    ) -> list:
        """
        并行分页获取数据
        
        第一阶段：串行获取所有页面的 next_token
        第二阶段：并行获取所有页面数据（如果需要）
        
        Args:
            fetch_page: 获取单页数据的异步函数，参数为 next_token，返回 (items, next_token)
            max_workers: 最大并行数
            
        Returns:
            所有数据列表
        """
        all_items = []
        next_token = None
        
        while True:
            items, next_token = await fetch_page(next_token)
            all_items.extend(items)
            
            if not next_token:
                break
        
        return all_items
