"""
Change History API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/reference/change-history
官方端点: POST /history (唯一端点)
"""

from typing import Literal
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# 支持的实体类型
EntityType = Literal[
    "CAMPAIGN",
    "AD_GROUP", 
    "AD",
    "KEYWORD",
    "TARGET",
    "NEGATIVE_KEYWORD",
    "NEGATIVE_TARGET",
    "PRODUCT_AD",
    "CAMPAIGN_NEGATIVE_KEYWORD",
]

# 支持的广告产品
AdProduct = Literal[
    "SPONSORED_PRODUCTS",
    "SPONSORED_BRANDS",
    "SPONSORED_DISPLAY",
]


class HistoryAPI(BaseAdsClient):
    """
    Change History API (全异步)
    
    官方只有 1 个端点: POST /history
    用于查询广告实体的变更历史记录
    """

    async def get_history(
        self,
        *,
        from_date: str,
        to_date: str,
        event_types: list[str] | None = None,
        parent_entity_ids: list[str] | None = None,
        entity_ids: list[str] | None = None,
        parent_entity_type_filters: list[EntityType] | None = None,
        entity_type_filters: list[EntityType] | None = None,
        ad_product_filters: list[AdProduct] | None = None,
        sort_order: Literal["ASC", "DESC"] = "DESC",
        count: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取变更历史记录
        
        官方端点: POST /history
        
        Args:
            from_date: 开始日期 (YYYY-MM-DD, 最多90天前)
            to_date: 结束日期 (YYYY-MM-DD)
            event_types: 事件类型列表 [
                "BUDGET", "BID", "STATUS", "TARGETING_EXPRESSION",
                "MATCH_TYPE", "CREATION", "DELETION", "OTHER"
            ]
            parent_entity_ids: 父实体ID列表 (如 campaign_id)
            entity_ids: 实体ID列表
            parent_entity_type_filters: 父实体类型过滤
            entity_type_filters: 实体类型过滤
            ad_product_filters: 广告产品过滤
            sort_order: 排序顺序 ASC/DESC
            count: 返回数量 (最大100)
            next_token: 分页令牌
            
        Returns:
            {
                "events": [...],
                "totalResults": 100,
                "nextToken": "..."
            }
            
        Example:
            # 获取最近7天所有 SP Campaign 的预算变更
            history = await client.common.history.get_history(
                from_date="2024-12-07",
                to_date="2024-12-14",
                event_types=["BUDGET"],
                parent_entity_type_filters=["CAMPAIGN"],
                ad_product_filters=["SPONSORED_PRODUCTS"],
            )
        """
        body: JSONData = {
            "fromDate": from_date,
            "toDate": to_date,
            "sortOrder": sort_order,
            "count": count,
        }
        
        if event_types:
            body["eventTypes"] = event_types
        if parent_entity_ids:
            body["parentEntityIds"] = parent_entity_ids
        if entity_ids:
            body["entityIds"] = entity_ids
        if parent_entity_type_filters:
            body["parentEntityTypeFilters"] = parent_entity_type_filters
        if entity_type_filters:
            body["entityTypeFilters"] = entity_type_filters
        if ad_product_filters:
            body["adProductFilters"] = ad_product_filters
        if next_token:
            body["nextToken"] = next_token

        result = await self.post("/history", json_data=body)
        return result if isinstance(result, dict) else {"events": [], "totalResults": 0}

    # ============ 便捷方法 ============

    async def list_all_history(
        self,
        from_date: str,
        to_date: str,
        **kwargs,
    ) -> JSONList:
        """
        获取所有变更历史（自动分页）
        
        Args:
            from_date: 开始日期
            to_date: 结束日期
            **kwargs: 其他 get_history 参数
            
        Returns:
            所有事件列表
        """
        all_events: JSONList = []
        next_token = None

        while True:
            result = await self.get_history(
                from_date=from_date,
                to_date=to_date,
                next_token=next_token,
                **kwargs,
            )
            events = result.get("events", [])
            all_events.extend(events)

            next_token = result.get("nextToken")
            if not next_token or not events:
                break

        return all_events

    async def get_recent_changes(
        self,
        days: int = 7,
        **kwargs,
    ) -> JSONList:
        """
        获取最近N天的变更
        
        Args:
            days: 天数 (最大90天)
            **kwargs: 其他 get_history 参数
        """
        from datetime import datetime, timedelta

        to_date = datetime.now().strftime("%Y-%m-%d")
        from_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        return await self.list_all_history(from_date, to_date, **kwargs)
