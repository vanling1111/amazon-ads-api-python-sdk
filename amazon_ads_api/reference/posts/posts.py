"""
Posts API - 帖子管理 (异步版本)

API Tier: L2 (API Reference Only)
Source: https://advertising.amazon.com/API/docs/en-us/posts
端点前缀: /bp/v2/
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData

# Posts API 自定义 Content-Type
BP_POST_CONTENT_TYPE = "application/vnd.bpPost.v2+json"
BP_PROFILE_CONTENT_TYPE = "application/vnd.bpProfile.v2+json"
BP_PRODUCT_CONTENT_TYPE = "application/vnd.bpProduct.v2+json"


class PostsAPI(BaseAdsClient):
    """Posts管理 - 管理Posts内容 (全异步)
    
    API Tier: L2 (API Reference Only)
    官方文档: https://advertising.amazon.com/API/docs/en-us/posts
    """
    
    # ==================== Posts ====================
    
    async def create_post(
        self,
        post_data: dict[str, Any],
    ) -> dict[str, Any]:
        """创建帖子 - POST /bp/v2/posts"""
        result = await self.post(
            "/bp/v2/posts", 
            json_data=post_data,
            content_type=BP_POST_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
    
    async def get_post(
        self,
        post_id: str,
    ) -> dict[str, Any]:
        """获取帖子详情 - GET /bp/v2/posts/{postId}"""
        result = await self.get(
            f"/bp/v2/posts/{post_id}",
            content_type=BP_POST_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
    
    async def update_post(
        self,
        post_id: str,
        post_data: dict[str, Any],
    ) -> dict[str, Any]:
        """更新帖子 - PUT /bp/v2/posts/{postId}"""
        result = await self.put(
            f"/bp/v2/posts/{post_id}", 
            json_data=post_data,
            content_type=BP_POST_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
    
    async def list_posts(
        self,
        profile_id: str,
        *,
        filters: list[dict[str, Any]] | None = None,
        sort_criterion: dict[str, Any] | None = None,
        selected_metrics: list[str] | None = None,
        metric_start_date: str | None = None,
        metric_end_date: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> dict[str, Any]:
        """获取帖子列表 - POST /bp/v2/posts/list
        
        Args:
            profile_id: 帖子档案ID (必需)
            filters: 过滤条件列表
            sort_criterion: 排序条件 {"sortField": str, "sortOrder": "ASC"|"DESC"}
            selected_metrics: 要返回的指标列表
            metric_start_date: 指标开始日期
            metric_end_date: 指标结束日期
            max_results: 返回结果数量 (50-500)
            next_token: 分页令牌
        """
        request_body: dict[str, Any] = {
            "profileId": profile_id,
            "maxResults": max_results,
        }
        
        if filters:
            request_body["filters"] = filters
        if sort_criterion:
            request_body["sortCriterion"] = sort_criterion
        if selected_metrics:
            request_body["selectedMetrics"] = selected_metrics
        if metric_start_date:
            request_body["metricStartDate"] = metric_start_date
        if metric_end_date:
            request_body["metricEndDate"] = metric_end_date
        if next_token:
            request_body["nextToken"] = next_token
            
        result = await self.post(
            "/bp/v2/posts/list", 
            json_data=request_body,
            content_type=BP_POST_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"posts": []}
    
    async def submit_for_review(
        self,
        post_id: str,
        version: int,
    ) -> dict[str, Any]:
        """提交帖子审核 - PUT /bp/v2/posts/{postId}/submitForReview
        
        Args:
            post_id: 帖子ID
            version: 帖子版本号（必需）- 确保写入一致性，只能更新最新版本
        """
        request_body: dict[str, Any] = {"version": version}
            
        result = await self.put(
            f"/bp/v2/posts/{post_id}/submitForReview",
            json_data=request_body,
            content_type=BP_POST_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
    
    async def withdraw_post(
        self,
        post_id: str,
        version: int,
    ) -> dict[str, Any]:
        """撤回/取消发布帖子 - PUT /bp/v2/posts/{postId}/unpublish
        
        Args:
            post_id: 帖子ID
            version: 帖子版本号（必需）- 确保写入一致性，只能更新最新版本
        """
        request_body: dict[str, Any] = {"version": version}
        result = await self.put(
            f"/bp/v2/posts/{post_id}/unpublish", 
            json_data=request_body,
            content_type=BP_POST_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
    
    # ==================== Profiles ====================
    
    async def list_profiles(self) -> dict[str, Any]:
        """获取Post Profiles列表 - GET /bp/v2/profiles"""
        result = await self.get(
            "/bp/v2/profiles",
            content_type=BP_PROFILE_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"profiles": []}
    
    async def get_profile(
        self,
        profile_id: str,
    ) -> dict[str, Any]:
        """获取Post Profile详情 - GET /bp/v2/profiles/{profileId}"""
        result = await self.get(
            f"/bp/v2/profiles/{profile_id}",
            content_type=BP_PROFILE_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
    
    async def get_profile_metrics(
        self,
        profile_id: str,
        *,
        metric_start_date: str | None = None,
        metric_end_date: str | None = None,
        aggregate_type: str | None = None,
    ) -> dict[str, Any]:
        """获取品牌级别Posts性能指标 - POST /bp/v2/profiles/{profileId}/metrics
        
        Args:
            profile_id: 帖子档案ID
            metric_start_date: 指标开始日期 (ISO8601格式，如 2020-08-16)
            metric_end_date: 指标结束日期 (ISO8601格式)
            aggregate_type: 聚合类型 ("DAY" 或 "WEEK")，默认返回最近30天数据
        
        Note:
            - 开始和结束日期之间最大365天
            - 如果不提供日期，返回最近30天数据
        """
        request_body: dict[str, Any] = {}
        
        if metric_start_date:
            request_body["metricStartDate"] = metric_start_date
        if metric_end_date:
            request_body["metricEndDate"] = metric_end_date
        if aggregate_type:
            request_body["aggregateType"] = aggregate_type
            
        result = await self.post(
            f"/bp/v2/profiles/{profile_id}/metrics",
            json_data=request_body,
            content_type=BP_PROFILE_CONTENT_TYPE,  # 使用正确的 Content-Type
        )
        return result if isinstance(result, dict) else {}
    
    async def get_metrics_download_link(
        self,
        profile_id: str,
        *,
        metric_start_date: str | None = None,
        metric_end_date: str | None = None,
    ) -> dict[str, Any]:
        """获取指标报告下载链接 - GET /bp/v2/profiles/{profileId}/metrics/download
        
        Args:
            profile_id: 帖子档案ID
            metric_start_date: 指标开始日期
            metric_end_date: 指标结束日期
        """
        params = {}
        if metric_start_date:
            params["metricStartDate"] = metric_start_date
        if metric_end_date:
            params["metricEndDate"] = metric_end_date
            
        result = await self.get(
            f"/bp/v2/profiles/{profile_id}/metrics/download",
            params=params or None,
            content_type=BP_PROFILE_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}
    
    # ==================== Products ====================
    
    async def get_post_products(
        self,
        *,
        asins: list[str] | None = None,
    ) -> dict[str, Any]:
        """获取产品列表信息 - GET /bp/v2/products/list
        
        Args:
            asins: 产品ASIN列表 (1-5个)
        """
        params = {}
        if asins:
            params["asins"] = asins  # 官方参数名是 asins
        result = await self.get(
            "/bp/v2/products/list", 
            params=params or None,
            content_type=BP_PRODUCT_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"eligibleProducts": [], "ineligibleProducts": []}
