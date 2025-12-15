"""
Sponsored Products - Recommendations API (异步版本)
SP智能建议（竞价建议、关键词建议、产品建议等）
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SPRecommendationsAPI(BaseAdsClient):
    """SP Recommendations API (全异步)"""

    # ============ Bid Recommendations ============

    async def get_bid_recommendations(
        self,
        ad_group_id: str,
        keywords: list[dict] | None = None,
        targets: list[dict] | None = None,
    ) -> JSONData:
        """
        获取竞价建议
        
        Args:
            ad_group_id: 广告组ID
            keywords: [{"keyword": "running shoes", "matchType": "BROAD"}]
            targets: [{"type": "asinSameAs", "value": "B00XXXX"}]
        """
        body: JSONData = {"adGroupId": ad_group_id}
        if keywords:
            body["keywords"] = keywords
        if targets:
            body["targets"] = targets

        result = await self.post("/sp/targets/bid/recommendations", json_data=body)
        return result if isinstance(result, dict) else {}

    async def get_keyword_bid_recommendations(self, keyword_ids: list[str]) -> JSONList:
        """
        获取已有关键词竞价建议
        
        Args:
            keyword_ids: 关键词ID列表
        """
        result = await self.post("/sp/keywords/bidRecommendations", json_data={"keywordIds": keyword_ids})
        return result if isinstance(result, list) else []

    async def get_target_bid_recommendations(self, target_ids: list[str]) -> JSONList:
        """
        获取已有Target竞价建议
        
        Args:
            target_ids: Target ID列表
        """
        result = await self.post("/sp/targets/bidRecommendations", json_data={"targetIds": target_ids})
        return result if isinstance(result, list) else []

    # ============ Keyword Recommendations ============

    async def get_keyword_recommendations(
        self,
        ad_group_id: str | None = None,
        asins: list[str] | None = None,
        max_recommendations: int = 100,
        bid_type: str = "suggested",
    ) -> JSONData:
        """
        获取关键词建议
        
        Args:
            ad_group_id: 广告组ID（二选一）
            asins: ASIN列表（二选一）
            max_recommendations: 最大建议数
            bid_type: suggested | range
        """
        body: JSONData = {
            "maxRecommendations": max_recommendations,
            "bidsConfiguration": {"bidType": bid_type}
        }
        if ad_group_id:
            body["adGroupId"] = ad_group_id
        if asins:
            body["asins"] = asins

        result = await self.post("/sp/targets/keywords/recommendations", json_data=body)
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_ranked_keyword_recommendations(
        self,
        asins: list[str],
        max_recommendations: int = 100,
    ) -> JSONData:
        """
        获取按相关性排序的关键词建议
        
        Args:
            asins: ASIN列表
            max_recommendations: 最大建议数
        """
        result = await self.post("/sp/keywords/recommendations", json_data={
            "asins": asins,
            "maxRecommendations": max_recommendations,
        })
        return result if isinstance(result, dict) else {"recommendations": []}

    # ============ Product Recommendations ============

    async def get_product_recommendations(
        self,
        ad_group_id: str | None = None,
        asins: list[str] | None = None,
        max_recommendations: int = 100,
    ) -> JSONData:
        """
        获取产品定向建议
        
        Args:
            ad_group_id: 广告组ID
            asins: 基于这些ASIN推荐相关产品
            max_recommendations: 最大建议数
        """
        body: JSONData = {"maxRecommendations": max_recommendations}
        if ad_group_id:
            body["adGroupId"] = ad_group_id
        if asins:
            body["asins"] = asins

        result = await self.post("/sp/targets/products/recommendations", json_data=body)
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_category_recommendations(
        self,
        asins: list[str],
        max_recommendations: int = 50,
    ) -> JSONData:
        """
        获取品类定向建议
        
        Args:
            asins: ASIN列表
            max_recommendations: 最大建议数
        """
        result = await self.post("/sp/targets/categories/recommendations", json_data={
            "asins": asins,
            "maxRecommendations": max_recommendations,
        })
        return result if isinstance(result, dict) else {"recommendations": []}

    # ============ Consolidated Recommendations ============

    async def get_consolidated_recommendations(
        self,
        campaign_id: str,
        recommendation_types: list[str] | None = None,
    ) -> JSONData:
        """
        获取综合建议（一站式获取所有建议）
        
        Args:
            campaign_id: Campaign ID
            recommendation_types: [
                "KEYWORD", "TARGETING", "BID", "BUDGET", 
                "NEGATIVE_KEYWORD", "NEGATIVE_TARGETING"
            ]
        """
        body: JSONData = {"campaignId": campaign_id}
        if recommendation_types:
            body["recommendationTypes"] = recommendation_types

        result = await self.post("/sp/campaigns/recommendations", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Negative Keyword/Target Recommendations ============

    async def get_negative_keyword_recommendations(
        self,
        ad_group_id: str,
        max_recommendations: int = 100,
    ) -> JSONData:
        """
        获取否定关键词建议
        
        基于Search Term Report分析，推荐应该否定的关键词
        """
        result = await self.post("/sp/negativeKeywords/recommendations", json_data={
            "adGroupId": ad_group_id,
            "maxRecommendations": max_recommendations,
        })
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_negative_target_recommendations(
        self,
        ad_group_id: str,
        max_recommendations: int = 100,
    ) -> JSONData:
        """
        获取否定定向建议
        
        推荐应该排除的ASIN/品类
        """
        result = await self.post("/sp/negativeTargets/recommendations", json_data={
            "adGroupId": ad_group_id,
            "maxRecommendations": max_recommendations,
        })
        return result if isinstance(result, dict) else {"recommendations": []}

    # ============ ASIN Recommendations ============

    async def get_asin_recommendations(
        self,
        campaign_id: str | None = None,
        ad_group_id: str | None = None,
    ) -> JSONData:
        """
        获取ASIN（产品）推荐
        
        推荐应该添加到广告组的产品
        """
        body: JSONData = {}
        if campaign_id:
            body["campaignId"] = campaign_id
        if ad_group_id:
            body["adGroupId"] = ad_group_id

        result = await self.post("/sp/productAds/recommendations", json_data=body)
        return result if isinstance(result, dict) else {"recommendations": []}

    # ============ Theme-based Bid Suggestions ============

    async def get_theme_based_bid_suggestions(
        self,
        ad_group_id: str,
        keywords: list[dict],
    ) -> JSONData:
        """
        获取基于主题的竞价建议（新版）
        
        Args:
            ad_group_id: 广告组ID
            keywords: [
                {
                    "keyword": "running shoes",
                    "matchType": "BROAD"
                }
            ]
        """
        result = await self.post("/sp/adGroups/bidRecommendations", json_data={
            "adGroupId": ad_group_id,
            "keywords": keywords,
        })
        return result if isinstance(result, dict) else {}

    # ============ 批量应用建议 ============

    async def apply_keyword_recommendations(
        self,
        ad_group_id: str,
        recommendations: list[dict],
    ) -> JSONData:
        """
        应用关键词建议
        
        Args:
            ad_group_id: 广告组ID
            recommendations: 从get_keyword_recommendations获取的建议
        """
        keywords = []
        for rec in recommendations:
            keywords.append({
                "adGroupId": ad_group_id,
                "keywordText": rec.get("keyword") or rec.get("keywordText"),
                "matchType": rec.get("matchType", "BROAD"),
                "bid": rec.get("suggestedBid") or rec.get("bid", 1.0),
                "state": "enabled",
            })

        result = await self.post("/sp/keywords", json_data={"keywords": keywords})
        return result if isinstance(result, dict) else {}

    async def apply_bid_recommendations(
        self,
        recommendations: list[dict],
    ) -> JSONData:
        """
        应用竞价建议
        
        Args:
            recommendations: [{"keywordId": "xxx", "suggestedBid": 1.5}]
        """
        updates = []
        for rec in recommendations:
            if "keywordId" in rec:
                updates.append({
                    "keywordId": rec["keywordId"],
                    "bid": rec.get("suggestedBid") or rec.get("bid"),
                })
            elif "targetId" in rec:
                updates.append({
                    "targetId": rec["targetId"],
                    "bid": rec.get("suggestedBid") or rec.get("bid"),
                })

        if not updates:
            return {}

        # 分开处理关键词和Target
        keyword_updates = [u for u in updates if "keywordId" in u]
        target_updates = [u for u in updates if "targetId" in u]

        results = {}
        if keyword_updates:
            result = await self.put("/sp/keywords", json_data={"keywords": keyword_updates})
            results["keywords"] = result
        if target_updates:
            result = await self.put("/sp/targets", json_data={"targetingClauses": target_updates})
            results["targets"] = result

        return results
