"""
Posts API - 帖子管理

端点前缀: /bp/v2/
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class PostsAPI(BaseAdsClient):
    """Posts管理 - 管理Posts内容"""
    
    # ==================== Posts ====================
    
    async def create_post(
        self,
        post_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """创建帖子"""
        return await self._request(
            "POST",
            "/bp/v2/posts",
            json=post_data
        )
    
    async def get_post(
        self,
        post_id: str,
    ) -> Dict[str, Any]:
        """获取帖子详情"""
        return await self._request("GET", f"/bp/v2/posts/{post_id}")
    
    async def update_post(
        self,
        post_id: str,
        post_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """更新帖子"""
        return await self._request(
            "PUT",
            f"/bp/v2/posts/{post_id}",
            json=post_data
        )
    
    async def list_posts(
        self,
        *,
        profile_id: Optional[str] = None,
        filters: Optional[List[Dict[str, Any]]] = None,
        sort: Optional[Dict[str, Any]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取帖子列表"""
        request_body: Dict[str, Any] = {"maxResults": max_results}
        
        if profile_id:
            request_body["profileId"] = profile_id
        if filters:
            request_body["filters"] = filters
        if sort:
            request_body["sort"] = sort
        if next_token:
            request_body["nextToken"] = next_token
            
        return await self._request("POST", "/bp/v2/posts/list", json=request_body)
    
    async def submit_for_review(
        self,
        post_id: str,
        *,
        schedule_time: Optional[str] = None,
    ) -> Dict[str, Any]:
        """提交帖子审核"""
        request_body: Dict[str, Any] = {}
        if schedule_time:
            request_body["scheduleTime"] = schedule_time
            
        return await self._request(
            "PUT",
            f"/bp/v2/posts/{post_id}/submitForReview",
            json=request_body
        )
    
    async def withdraw_post(
        self,
        post_id: str,
    ) -> Dict[str, Any]:
        """撤回/取消发布帖子"""
        return await self._request(
            "PUT",
            f"/bp/v2/posts/{post_id}/unpublish",
            json={}
        )
    
    # ==================== Profiles ====================
    
    async def list_profiles(self) -> Dict[str, Any]:
        """获取Post Profiles列表"""
        return await self._request("GET", "/bp/v2/profiles")
    
    async def get_profile(
        self,
        profile_id: str,
    ) -> Dict[str, Any]:
        """获取Post Profile详情"""
        return await self._request("GET", f"/bp/v2/profiles/{profile_id}")
    
    async def get_profile_metrics(
        self,
        profile_id: str,
        *,
        start_date: str,
        end_date: str,
        metrics: Optional[List[str]] = None,
        aggregate_type: str = "SUMMARY",
    ) -> Dict[str, Any]:
        """获取品牌级别Posts性能指标"""
        request_body: Dict[str, Any] = {
            "startDate": start_date,
            "endDate": end_date,
            "aggregateType": aggregate_type,
        }
        if metrics:
            request_body["metrics"] = metrics
            
        return await self._request(
            "POST",
            f"/bp/v2/profiles/{profile_id}/metrics",
            json=request_body
        )
    
    async def get_metrics_download_link(
        self,
        profile_id: str,
    ) -> Dict[str, Any]:
        """获取指标报告下载链接"""
        return await self._request(
            "GET",
            f"/bp/v2/profiles/{profile_id}/metrics/download"
        )
    
    # ==================== Products ====================
    
    async def get_post_products(
        self,
        *,
        product_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """获取产品列表信息"""
        params = {}
        if product_ids:
            params["productIds"] = ",".join(product_ids)
        return await self._request("GET", "/bp/v2/products/list", params=params)

