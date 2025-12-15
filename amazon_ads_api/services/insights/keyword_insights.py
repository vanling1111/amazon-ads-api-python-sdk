"""
Keyword Insights API (异步版本)

基于 Amazon Ads API 官方 Keyword Recommendations 端点：
- SP: POST /sp/targets/keywords/recommendations
- SP: POST /sp/global/targets/keywords/recommendations/list  
- SB: POST /sb/recommendations/keyword
- SP: POST /sp/targets/categories/recommendations

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class KeywordInsightsAPI(BaseAdsClient):
    """
    Keyword Insights API (全异步)
    
    基于官方 SP/SB Keyword Recommendations API
    """

    # ============ SP Keyword Recommendations (官方 API) ============

    async def get_sp_keyword_recommendations(
        self,
        asins: list[str],
        max_recommendations: int = 100,
        sort_dimension: str = "CLICKS",
        locale: str | None = None,
    ) -> JSONData:
        """
        获取 SP 关键词推荐 (官方 API v5)
        
        POST /sp/targets/keywords/recommendations
        
        Args:
            asins: 产品ASIN列表
            max_recommendations: 最大推荐数量 (最大 200)
            sort_dimension: 排序维度 CLICKS | CONVERSIONS | DEFAULT
            locale: 语言 (如 "en-US")
        
        Returns:
            {
                "keywordTargetList": [
                    {
                        "keyword": "iphone 11",
                        "bidInfo": [
                            {
                                "matchType": "BROAD",
                                "theme": "CONVERSION_OPPORTUNITIES",
                                "bid": 63,
                                "suggestedBid": {...}
                            }
                        ],
                        "recId": "..."
                    }
                ]
            }
        """
        body: JSONData = {
            "recommendationType": "KEYWORDS_FOR_ASINS",
            "asins": asins,
            "maxRecommendations": min(max_recommendations, 200),
            "sortDimension": sort_dimension,
        }
        if locale:
            body["locale"] = locale
        
        result = await self.post(
            "/sp/targets/keywords/recommendations",
            json_data=body,
            content_type="application/vnd.spkeywordsrecommendation.v5+json",
            accept="application/vnd.spkeywordsrecommendation.v5+json"
        )
        return result if isinstance(result, dict) else {"keywordTargetList": []}

    async def get_sp_keyword_recommendations_for_adgroup(
        self,
        campaign_id: str,
        ad_group_id: str,
        max_recommendations: int = 200,
        sort_dimension: str = "CLICKS",
        locale: str | None = None,
    ) -> JSONData:
        """
        获取广告组的 SP 关键词推荐
        
        POST /sp/targets/keywords/recommendations
        
        Args:
            campaign_id: Campaign ID
            ad_group_id: Ad Group ID
            max_recommendations: 最大推荐数
            sort_dimension: 排序维度 DEFAULT | CLICKS | CONVERSIONS
            locale: 语言 (如 "en-US")
        """
        body: JSONData = {
            "recommendationType": "KEYWORDS_FOR_ADGROUP",
            "campaignId": campaign_id,
            "adGroupId": ad_group_id,
            "maxRecommendations": min(max_recommendations, 200),
            "sortDimension": sort_dimension,
        }
        if locale:
            body["locale"] = locale
        
        result = await self.post(
            "/sp/targets/keywords/recommendations",
            json_data=body,
            content_type="application/vnd.spkeywordsrecommendation.v5+json",
            accept="application/vnd.spkeywordsrecommendation.v5+json"
        )
        return result if isinstance(result, dict) else {"keywordTargetList": []}

    async def get_sp_global_keyword_recommendations(
        self,
        product_details_list: list[dict],
        ad_group_id: str | None = None,
        max_recommendations: int = 200,
        sort_dimension: str = "DEFAULT",
    ) -> JSONData:
        """
        获取 SP 全球关键词推荐 (跨市场)
        
        POST /sp/global/targets/keywords/recommendations/list
        
        Args:
            product_details_list: [
                {"asin": "B001", "catalogSourceCountryCode": "US"},
                {"asin": "B002", "catalogSourceCountryCode": "DE"}
            ]
            ad_group_id: Ad Group ID
            max_recommendations: 最大推荐数
            sort_dimension: 排序维度
        """
        body: JSONData = {
            "productDetailsList": product_details_list,
            "maxRecommendations": max_recommendations,
            "sortDimension": sort_dimension,
        }
        if ad_group_id:
            body["adGroupId"] = ad_group_id
        
        result = await self.post(
            "/sp/global/targets/keywords/recommendations/list",
            json_data=body,
            content_type="application/vnd.spkeywordsrecommendation.v5+json"
        )
        return result if isinstance(result, dict) else {}

    # ============ SB Keyword Recommendations (官方 API) ============

    async def get_sb_keyword_recommendations(
        self,
        asins: list[str] | None = None,
        url: str | None = None,
        max_recommendations: int = 100,
    ) -> JSONData:
        """
        获取 SB 关键词推荐 (官方 API)
        
        POST /sb/recommendations/keyword
        
        Args:
            asins: ASIN列表 (与 url 二选一)
            url: Landing page URL (与 asins 二选一)
            max_recommendations: 最大推荐数
        """
        body: JSONData = {
            "maxNumSuggestions": max_recommendations,
        }
        if asins:
            body["asins"] = asins
        elif url:
            body["url"] = url
        else:
            raise ValueError("必须提供 asins 或 url 之一")
        
        result = await self.post(
            "/sb/recommendations/keyword",
            json_data=body,
        )
        return result if isinstance(result, dict) else {"recommendations": []}

    # ============ SP Category Recommendations (官方 API) ============

    async def get_sp_category_recommendations(
        self,
        asins: list[str],
        max_recommendations: int = 100,
    ) -> JSONData:
        """
        获取 SP 类目推荐
        
        POST /sp/targets/categories/recommendations
        
        Args:
            asins: ASIN列表
            max_recommendations: 最大推荐数
        """
        body: JSONData = {
            "asins": asins,
            "maxRecommendations": max_recommendations,
        }
        
        result = await self.post(
            "/sp/targets/categories/recommendations",
            json_data=body,
        )
        return result if isinstance(result, dict) else {"recommendedCategories": []}

    # ============ SP Bid Recommendations (官方 API) ============

    async def get_sp_keyword_bid_recommendations(
        self,
        ad_group_id: str,
        keywords: list[dict],
    ) -> JSONData:
        """
        获取 SP 关键词竞价建议
        
        POST /sp/keywords/bids/recommendations
        
        Args:
            ad_group_id: Ad Group ID
            keywords: [
                {"keyword": "running shoes", "matchType": "EXACT"},
                {"keyword": "men shoes", "matchType": "BROAD"}
            ]
        """
        body: JSONData = {
            "adGroupId": ad_group_id,
            "keywords": keywords,
        }
        
        result = await self.post(
            "/sp/keywords/bids/recommendations",
            json_data=body,
            content_type="application/vnd.spkeywordbidrecommendation.v3+json"
        )
        return result if isinstance(result, dict) else {"bidRecommendations": []}

    # ============ 便捷方法 ============

    async def get_keyword_recommendations_for_products(
        self,
        asins: list[str],
        max_recommendations: int = 100,
    ) -> JSONList:
        """
        获取产品的关键词推荐 (便捷方法)
        
        综合使用 SP Keyword Recommendations API
        
        Args:
            asins: ASIN列表
            max_recommendations: 最大推荐数
        
        Returns:
            推荐关键词列表
        """
        result = await self.get_sp_keyword_recommendations(
            asins=asins,
            max_recommendations=max_recommendations,
        )
        return result.get("keywordTargetList", [])

    async def get_all_recommendations_for_asin(
        self,
        asin: str,
    ) -> JSONData:
        """
        获取单个ASIN的所有推荐
        
        包括关键词推荐和类目推荐
        """
        keywords = await self.get_sp_keyword_recommendations(
            asins=[asin],
            max_recommendations=100,
        )
        
        categories = await self.get_sp_category_recommendations(
            asins=[asin],
            max_recommendations=50,
        )
        
        return {
            "asin": asin,
            "keywordRecommendations": keywords.get("keywordTargetList", []),
            "categoryRecommendations": categories.get("recommendedCategories", []),
        }

    async def batch_get_keyword_recommendations(
        self,
        asins: list[str],
        batch_size: int = 50,
    ) -> JSONList:
        """
        批量获取关键词推荐
        
        分批处理大量ASIN
        """
        all_keywords = []
        
        for i in range(0, len(asins), batch_size):
            batch = asins[i:i + batch_size]
            result = await self.get_sp_keyword_recommendations(
                asins=batch,
                max_recommendations=200,
            )
            all_keywords.extend(result.get("keywordTargetList", []))
        
        return all_keywords


# 别名（向后兼容）
KeywordRecommendationsAPI = KeywordInsightsAPI
