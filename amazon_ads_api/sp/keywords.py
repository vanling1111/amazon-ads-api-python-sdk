"""
Sponsored Products - Keywords API
SP关键词管理（正向关键词 + 否定关键词）
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SPKeywordsAPI(BaseAdsClient):
    """SP Keywords API"""

    # ============ 正向关键词 ============

    def list_keywords(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Keyword列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = self.post("/sp/keywords/list", json_data=params)
        return result if isinstance(result, dict) else {"keywords": []}

    def get_keyword(self, keyword_id: str) -> JSONData:
        """获取单个Keyword详情"""
        result = self.get(f"/sp/keywords/{keyword_id}")
        return result if isinstance(result, dict) else {}

    def create_keywords(self, keywords: JSONList) -> JSONData:
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
        result = self.post("/sp/keywords", json_data={"keywords": keywords})
        return result if isinstance(result, dict) else {"keywords": {"success": [], "error": []}}

    def update_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量更新Keyword
        
        Args:
            keywords: [{"keywordId": "xxx", "state": "paused", "bid": 1.5}]
        """
        result = self.put("/sp/keywords", json_data={"keywords": keywords})
        return result if isinstance(result, dict) else {"keywords": {"success": [], "error": []}}

    def delete_keyword(self, keyword_id: str) -> JSONData:
        """归档Keyword"""
        return self.delete(f"/sp/keywords/{keyword_id}")

    # ============ 便捷方法 ============

    def pause_keyword(self, keyword_id: str) -> JSONData:
        """暂停Keyword"""
        return self.update_keywords([{"keywordId": keyword_id, "state": "paused"}])

    def enable_keyword(self, keyword_id: str) -> JSONData:
        """启用Keyword"""
        return self.update_keywords([{"keywordId": keyword_id, "state": "enabled"}])

    def update_bid(self, keyword_id: str, bid: float) -> JSONData:
        """更新Keyword竞价"""
        return self.update_keywords([{"keywordId": keyword_id, "bid": bid}])

    def batch_update_bids(self, bid_updates: list[dict]) -> JSONData:
        """
        批量更新竞价
        
        Args:
            bid_updates: [{"keywordId": "xxx", "bid": 1.5}, ...]
        """
        return self.update_keywords(bid_updates)

    # ============ Ad Group级别否定关键词 ============

    def list_negative_keywords(
        self,
        ad_group_id: str | None = None,
        campaign_id: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Ad Group级别Negative Keyword列表"""
        params: JSONData = {"maxResults": max_results}
        if ad_group_id:
            params["adGroupIdFilter"] = [ad_group_id]
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if next_token:
            params["nextToken"] = next_token

        result = self.post("/sp/negativeKeywords/list", json_data=params)
        return result if isinstance(result, dict) else {"negativeKeywords": []}

    def create_negative_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量创建Negative Keyword
        
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
        result = self.post("/sp/negativeKeywords", json_data={"negativeKeywords": keywords})
        return result if isinstance(result, dict) else {"negativeKeywords": {"success": [], "error": []}}

    def delete_negative_keyword(self, keyword_id: str) -> JSONData:
        """删除Negative Keyword"""
        return self.delete(f"/sp/negativeKeywords/{keyword_id}")

    # ============ Campaign级别否定关键词 ============

    def list_campaign_negative_keywords(
        self,
        campaign_id: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Campaign级别Negative Keyword列表"""
        params: JSONData = {"maxResults": max_results}
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if next_token:
            params["nextToken"] = next_token

        result = self.post("/sp/campaignNegativeKeywords/list", json_data=params)
        return result if isinstance(result, dict) else {"campaignNegativeKeywords": []}

    def create_campaign_negative_keywords(self, keywords: JSONList) -> JSONData:
        """
        批量创建Campaign Negative Keyword
        
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
        result = self.post("/sp/campaignNegativeKeywords", json_data={"campaignNegativeKeywords": keywords})
        return result if isinstance(result, dict) else {"campaignNegativeKeywords": {"success": [], "error": []}}

    def delete_campaign_negative_keyword(self, keyword_id: str) -> JSONData:
        """删除Campaign Negative Keyword"""
        return self.delete(f"/sp/campaignNegativeKeywords/{keyword_id}")

    # ============ 批量获取 ============

    def list_all_keywords(
        self,
        campaign_id: str | None = None,
        ad_group_id: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有Keyword（自动分页）"""
        all_keywords = []
        next_token = None

        while True:
            result = self.list_keywords(
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

