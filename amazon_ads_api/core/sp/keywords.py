"""
Sponsored Products - Keywords API (异步版本)
SP关键词管理（正向关键词 + 否定关键词）
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

# API v3 Content-Types
CONTENT_TYPE_KEYWORD = "application/vnd.spKeyword.v3+json"
CONTENT_TYPE_NEGATIVE_KEYWORD = "application/vnd.spNegativeKeyword.v3+json"
CONTENT_TYPE_CAMPAIGN_NEGATIVE_KEYWORD = "application/vnd.spCampaignNegativeKeyword.v3+json"


class SPKeywordsAPI(BaseAdsClient):
    """SP Keywords API (全异步)"""

    # ============ 正向关键词 ============

    async def list_keywords(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        keyword_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
        include_extended_data: bool = False,
    ) -> JSONData:
        """
        获取Keyword列表
        
        Args:
            ad_group_id: Ad Group ID过滤
            campaign_id: Campaign ID过滤
            keyword_ids: Keyword ID过滤
            state_filter: 状态过滤 ["ENABLED", "PAUSED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
            include_extended_data: 是否包含扩展字段
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if ad_group_id:
            params["adGroupIdFilter"] = {"include": [ad_group_id]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if keyword_ids:
            params["keywordIdFilter"] = {"include": keyword_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        if next_token:
            params["nextToken"] = next_token
        
        if include_extended_data:
            params["includeExtendedDataFields"] = True

        result = await self.post("/sp/keywords/list", json_data=params, content_type=CONTENT_TYPE_KEYWORD)
        return result if isinstance(result, dict) else {"keywords": []}

    async def get_keyword(self, keyword_id: str) -> JSONData:
        """获取单个Keyword详情"""
        result = await self.get(f"/sp/keywords/{keyword_id}", content_type=CONTENT_TYPE_KEYWORD)
        return result if isinstance(result, dict) else {}

    async def create_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量创建Keyword
        
        Args:
            keywords: Keyword列表
            [
                {
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "keywordText": "running shoes",
                    "matchType": "BROAD",  # BROAD | PHRASE | EXACT
                    "bid": 1.0
                }
            ]
        """
        result = await self.post("/sp/keywords", json_data={"keywords": keywords}, content_type=CONTENT_TYPE_KEYWORD)
        return result if isinstance(result, dict) else {"keywords": {"success": [], "error": []}}

    async def update_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量更新Keyword
        
        Args:
            keywords: [{"keywordId": "xxx", "state": "paused", "bid": 1.5}]
        """
        result = await self.put("/sp/keywords", json_data={"keywords": keywords}, content_type=CONTENT_TYPE_KEYWORD)
        return result if isinstance(result, dict) else {"keywords": {"success": [], "error": []}}

    async def delete_keywords(self, keyword_ids: list[str]) -> JSONData:
        """
        批量归档Keyword（官方 v3 /delete 端点）
        
        注意：Amazon Ads 不支持真正删除广告实体，此操作将 Keyword 状态设置为 "archived"。
        
        Args:
            keyword_ids: Keyword ID列表
            
        Returns:
            {"keywords": {"success": [...], "error": [...]}}
        """
        # 官方请求格式: {"keywordIdFilter": {"include": [...]}}
        body = {"keywordIdFilter": {"include": keyword_ids}}
        result = await self.post("/sp/keywords/delete", json_data=body, content_type=CONTENT_TYPE_KEYWORD)
        return result if isinstance(result, dict) else {"keywords": {"success": [], "error": []}}

    async def delete_keyword(self, keyword_id: str) -> JSONData:
        """归档单个Keyword（状态变为 archived）"""
        return await self.delete_keywords([keyword_id])
    
    # archive_keyword 是 delete_keyword 的别名
    async def archive_keyword(self, keyword_id: str) -> JSONData:
        """归档Keyword（等同于 delete_keyword）"""
        return await self.delete_keyword(keyword_id)

    # ============ 便捷方法 ============

    async def pause_keyword(self, keyword_id: str) -> JSONData:
        """暂停Keyword"""
        return await self.update_keywords([{"keywordId": keyword_id, "state": "paused"}])

    async def enable_keyword(self, keyword_id: str) -> JSONData:
        """启用Keyword"""
        return await self.update_keywords([{"keywordId": keyword_id, "state": "enabled"}])

    async def update_bid(self, keyword_id: str, bid: float) -> JSONData:
        """更新Keyword竞价"""
        return await self.update_keywords([{"keywordId": keyword_id, "bid": bid}])

    async def batch_update_bids(self, bid_updates: list[dict]) -> JSONData:
        """
        批量更新竞价
        
        Args:
            bid_updates: [{"keywordId": "xxx", "bid": 1.5}, ...]
        """
        return await self.update_keywords(bid_updates)

    # ============ Ad Group级别否定关键词 ============

    async def list_negative_keywords(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        keyword_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Ad Group级别Negative Keyword列表
        
        Args:
            ad_group_id: Ad Group ID过滤
            campaign_id: Campaign ID过滤
            keyword_ids: Keyword ID过滤
            state_filter: 状态过滤 ["ENABLED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if ad_group_id:
            params["adGroupIdFilter"] = {"include": [ad_group_id]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if keyword_ids:
            params["keywordIdFilter"] = {"include": keyword_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sp/negativeKeywords/list", json_data=params, content_type=CONTENT_TYPE_NEGATIVE_KEYWORD)
        return result if isinstance(result, dict) else {"negativeKeywords": []}

    async def create_negative_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量创建Negative Keyword
        
        官方端点: POST /sp/negativeKeywords
        
        Args:
            keywords: [
                {
                    "campaignId": "xxx",
                    "adGroupId": "xxx",
                    "state": "enabled",
                    "keywordText": "free",
                    "matchType": "NEGATIVE_EXACT"  # NEGATIVE_EXACT | NEGATIVE_PHRASE
                }
            ]
        """
        result = await self.post("/sp/negativeKeywords", json_data={"negativeKeywords": keywords}, content_type=CONTENT_TYPE_NEGATIVE_KEYWORD)
        return result if isinstance(result, dict) else {"negativeKeywords": {"success": [], "error": []}}

    async def update_negative_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量更新Negative Keyword
        
        官方端点: PUT /sp/negativeKeywords
        
        Args:
            keywords: [{"keywordId": "xxx", "state": "paused"}]
        """
        result = await self.put("/sp/negativeKeywords", json_data={"negativeKeywords": keywords}, content_type=CONTENT_TYPE_NEGATIVE_KEYWORD)
        return result if isinstance(result, dict) else {"negativeKeywords": {"success": [], "error": []}}

    async def delete_negative_keywords(self, keyword_ids: list[str]) -> JSONData:
        """
        批量归档Ad Group级别Negative Keyword（官方 v3 /delete 端点）
        
        注意：此操作将 Negative Keyword 状态设置为 "archived"。
        
        Args:
            keyword_ids: Keyword ID列表
        """
        # 官方请求格式: {"keywordIdFilter": {"include": [...]}}
        body = {"keywordIdFilter": {"include": keyword_ids}}
        result = await self.post("/sp/negativeKeywords/delete", json_data=body, content_type=CONTENT_TYPE_NEGATIVE_KEYWORD)
        return result if isinstance(result, dict) else {"negativeKeywords": {"success": [], "error": []}}

    async def delete_negative_keyword(self, keyword_id: str) -> JSONData:
        """归档单个Negative Keyword（状态变为 archived）"""
        return await self.delete_negative_keywords([keyword_id])

    # ============ Campaign级别否定关键词 ============

    async def list_campaign_negative_keywords(
        self,
        campaign_id: str | None = None,
        keyword_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Campaign级别Negative Keyword列表
        
        Args:
            campaign_id: Campaign ID过滤
            keyword_ids: Keyword ID过滤
            state_filter: 状态过滤 ["ENABLED", "ARCHIVED"]
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if keyword_ids:
            params["keywordIdFilter"] = {"include": keyword_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        if next_token:
            params["nextToken"] = next_token

        result = await self.post("/sp/campaignNegativeKeywords/list", json_data=params, content_type=CONTENT_TYPE_CAMPAIGN_NEGATIVE_KEYWORD)
        return result if isinstance(result, dict) else {"campaignNegativeKeywords": []}

    async def create_campaign_negative_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量创建Campaign Negative Keyword
        
        官方端点: POST /sp/campaignNegativeKeywords
        
        Args:
            keywords: [
                {
                    "campaignId": "xxx",
                    "state": "enabled",
                    "keywordText": "cheap",
                    "matchType": "NEGATIVE_EXACT"
                }
            ]
        """
        result = await self.post("/sp/campaignNegativeKeywords", json_data={"campaignNegativeKeywords": keywords}, content_type=CONTENT_TYPE_CAMPAIGN_NEGATIVE_KEYWORD)
        return result if isinstance(result, dict) else {"campaignNegativeKeywords": {"success": [], "error": []}}

    async def update_campaign_negative_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量更新Campaign Negative Keyword
        
        官方端点: PUT /sp/campaignNegativeKeywords
        
        Args:
            keywords: [{"keywordId": "xxx", "state": "paused"}]
        """
        result = await self.put("/sp/campaignNegativeKeywords", json_data={"campaignNegativeKeywords": keywords}, content_type=CONTENT_TYPE_CAMPAIGN_NEGATIVE_KEYWORD)
        return result if isinstance(result, dict) else {"campaignNegativeKeywords": {"success": [], "error": []}}

    async def delete_campaign_negative_keywords(self, keyword_ids: list[str]) -> JSONData:
        """
        批量归档Campaign级别Negative Keyword（官方 v3 /delete 端点）
        
        注意：此操作将 Campaign Negative Keyword 状态设置为 "archived"。
        
        Args:
            keyword_ids: Keyword ID列表
        """
        # 官方请求格式: {"keywordIdFilter": {"include": [...]}}
        body = {"keywordIdFilter": {"include": keyword_ids}}
        result = await self.post("/sp/campaignNegativeKeywords/delete", json_data=body, content_type=CONTENT_TYPE_CAMPAIGN_NEGATIVE_KEYWORD)
        return result if isinstance(result, dict) else {"campaignNegativeKeywords": {"success": [], "error": []}}

    async def delete_campaign_negative_keyword(self, keyword_id: str) -> JSONData:
        """归档单个Campaign Negative Keyword（状态变为 archived）"""
        return await self.delete_campaign_negative_keywords([keyword_id])

    # ============ 批量获取 ============

    async def list_all_keywords(
        self,
        campaign_id: str | None = None,
        ad_group_id: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有Keyword（自动分页）"""
        all_keywords = []
        next_token = None

        while True:
            result = await self.list_keywords(
                campaign_id=campaign_id,
                ad_group_id=ad_group_id,
                state_filter=state_filter,
                max_results=100,
                next_token=next_token,
            )
            keywords = result.get("keywords", [])
            all_keywords.extend(keywords)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_keywords
