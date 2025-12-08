"""
Posts API - 帖子管理 (异步版本)

端点前缀: /bp/v2/
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient, JSONData


class PostsAPI(BaseAdsClient):
    """Posts管理 - 管理Posts内容 (全异步)"""
    
    # ==================== Posts ====================
    
    async def create_post(
        self,
        post_data: Dict[str, Any],
    ) -> JSONData:
        """创建帖子"""
        result = await self.post("/bp/v2/posts", json_data=post_data)
        return result if isinstance(result, dict) else {}
    
    async def get_post(
        self,
        post_id: str,
    ) -> JSONData:
        """获取帖子详情"""
        result = await self.get(f"/bp/v2/posts/{post_id}")
        return result if isinstance(result, dict) else {}
    
    async def update_post(
        self,
        post_id: str,
        post_data: Dict[str, Any],
    ) -> JSONData:
        """更新帖子"""
        result = await self.put(f"/bp/v2/posts/{post_id}", json_data=post_data)
        return result if isinstance(result, dict) else {}
    
    async def list_posts(
        self,
        *,
        profile_id: Optional[str] = None,
        filters: Optional[List[Dict[str, Any]]] = None,
        sort: Optional[Dict[str, Any]] = None,
        max_results: int = 100,
        next_token: Optional[str] = None,
    ) -> JSONData:
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
            
        result = await self.post("/bp/v2/posts/list", json_data=request_body)
        return result if isinstance(result, dict) else {"posts": []}
    
    async def submit_for_review(
        self,
        post_id: str,
        *,
        schedule_time: Optional[str] = None,
    ) -> JSONData:
        """提交帖子审核"""
        request_body: Dict[str, Any] = {}
        if schedule_time:
            request_body["scheduleTime"] = schedule_time
            
        result = await self.put(
            f"/bp/v2/posts/{post_id}/submitForReview",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {}
    
    async def withdraw_post(
        self,
        post_id: str,
    ) -> JSONData:
        """撤回/取消发布帖子"""
        result = await self.put(f"/bp/v2/posts/{post_id}/unpublish", json_data={})
        return result if isinstance(result, dict) else {}
    
    # ==================== Profiles ====================
    
    async def list_profiles(self) -> JSONData:
        """获取Post Profiles列表"""
        result = await self.get("/bp/v2/profiles")
        return result if isinstance(result, dict) else {"profiles": []}
    
    async def get_profile(
        self,
        profile_id: str,
    ) -> JSONData:
        """获取Post Profile详情"""
        result = await self.get(f"/bp/v2/profiles/{profile_id}")
        return result if isinstance(result, dict) else {}
    
    async def get_profile_metrics(
        self,
        profile_id: str,
        *,
        start_date: str,
        end_date: str,
        metrics: Optional[List[str]] = None,
        aggregate_type: str = "SUMMARY",
    ) -> JSONData:
        """获取品牌级别Posts性能指标"""
        request_body: Dict[str, Any] = {
            "startDate": start_date,
            "endDate": end_date,
            "aggregateType": aggregate_type,
        }
        if metrics:
            request_body["metrics"] = metrics
            
        result = await self.post(
            f"/bp/v2/profiles/{profile_id}/metrics",
            json_data=request_body
        )
        return result if isinstance(result, dict) else {}
    
    async def get_metrics_download_link(
        self,
        profile_id: str,
    ) -> JSONData:
        """获取指标报告下载链接"""
        result = await self.get(f"/bp/v2/profiles/{profile_id}/metrics/download")
        return result if isinstance(result, dict) else {}
    
    # ==================== Products ====================
    
    async def get_post_products(
        self,
        *,
        product_ids: Optional[List[str]] = None,
    ) -> JSONData:
        """获取产品列表信息"""
        params = {}
        if product_ids:
            params["productIds"] = ",".join(product_ids)
        result = await self.get("/bp/v2/products/list", params=params or None)
        return result if isinstance(result, dict) else {"products": []}
