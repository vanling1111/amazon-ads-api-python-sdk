"""
Amazon Ads Ad Library API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/ad-library
官方规范: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdLibraryAPI_prod_3p.json

官方端点 (共2个):
- POST /adRepository/ads/list - 列出广告
- GET /adRepository/ads/{id} - 获取单个广告
"""

from typing import Literal
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# Content-Type
AD_REPOSITORY_CONTENT_TYPE = "application/vnd.adsrepository.v1.1+json"

# 名称匹配类型
NameMatchType = Literal["CONTAINS", "EXACT_MATCH"]


class AdLibraryAPI(BaseAdsClient):
    """
    Ad Library API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI Spec: AdLibraryAPI_prod_3p.json
    Stability: 高
    
    官方端点 (共2个):
    - POST /adRepository/ads/list - 列出广告
    - GET /adRepository/ads/{id} - 获取单个广告
    """

    async def list_ads(
        self,
        *,
        advertiser_name: str | None = None,
        advertisement_purpose: str | None = None,
        name_match_type: NameMatchType | None = None,
        delivery_after_date_utc: str | None = None,
        delivery_before_date_utc: str | None = None,
        is_restricted: bool | None = None,
        site_name: str | None = None,
        max_results: int = 10,
        next_token: str | None = None,
    ) -> JSONData:
        """
        列出广告
        
        官方端点: POST /adRepository/ads/list
        官方规范: AdLibraryAPI_prod_3p.json
        
        Args:
            advertiser_name: 广告主名称过滤
            advertisement_purpose: 广告目的过滤
            name_match_type: 名称匹配类型 (CONTAINS, EXACT_MATCH)
            delivery_after_date_utc: 投放开始日期过滤 (ISO 格式 YYYY-MM-DD)
            delivery_before_date_utc: 投放结束日期过滤 (ISO 格式 YYYY-MM-DD)
            is_restricted: 是否被限制
            site_name: 站点名称 (如 amazon.de, amazon.fr)
            max_results: 最大结果数 (1-1000, 默认10)
            next_token: 分页令牌
            
        Returns:
            {
                "ads": [...],
                "totalResults": 100,
                "nextToken": "..."
            }
        """
        request_body: JSONData = {}
        
        if advertiser_name:
            request_body["advertiserName"] = advertiser_name
        if advertisement_purpose:
            request_body["advertisementPurpose"] = advertisement_purpose
        if name_match_type:
            request_body["nameMatchType"] = name_match_type
        if delivery_after_date_utc:
            request_body["deliveryAfterDateUtc"] = delivery_after_date_utc
        if delivery_before_date_utc:
            request_body["deliveryBeforeDateUtc"] = delivery_before_date_utc
        if is_restricted is not None:
            request_body["isRestricted"] = is_restricted
        if site_name:
            request_body["siteName"] = site_name
        if max_results != 10:
            request_body["maxResults"] = max_results
        if next_token:
            request_body["nextToken"] = next_token

        result = await self.post(
            "/adRepository/ads/list",
            json_data=request_body if request_body else None,
            content_type=AD_REPOSITORY_CONTENT_TYPE,
            accept=AD_REPOSITORY_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {"ads": [], "totalResults": 0}

    async def get_ad_by_id(self, ad_id: str) -> JSONData:
        """
        获取单个广告详情
        
        官方端点: GET /adRepository/ads/{id}
        官方规范: AdLibraryAPI_prod_3p.json
        
        Args:
            ad_id: 广告ID (全局唯一标识符)
            
        Returns:
            {
                "ad": {
                    "id": "...",
                    "advertiserName": "...",
                    "advertisementPurpose": "...",
                    "contentUrls": [...],
                    "deliveryAfterDateUtc": "...",
                    "deliveryBeforeDateUtc": "...",
                    "isRestricted": false,
                    "subjectMatterUrl": "...",
                    "targetingMethods": [...],
                    "totalRecipientsRange": {...},
                    "totalRecipientsRangeBySite": {...},
                    "type": "AD" | "AFFILIATE_MARKETING_CONTENT"
                }
            }
        """
        result = await self.get(
            f"/adRepository/ads/{ad_id}",
            accept=AD_REPOSITORY_CONTENT_TYPE,
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def list_all_ads(
        self,
        advertiser_name: str | None = None,
        **kwargs,
    ) -> JSONList:
        """
        获取所有广告 (自动分页)
        
        Args:
            advertiser_name: 广告主名称过滤
            **kwargs: 其他 list_ads 参数
            
        Returns:
            所有广告列表
        """
        all_ads: JSONList = []
        next_token = None
        
        while True:
            result = await self.list_ads(
                advertiser_name=advertiser_name,
                max_results=1000,
                next_token=next_token,
                **kwargs,
            )
            ads = result.get("ads", [])
            all_ads.extend(ads)
            
            next_token = result.get("nextToken")
            if not next_token or not ads:
                break
        
        return all_ads

    async def search_by_advertiser(
        self,
        advertiser_name: str,
        exact_match: bool = False,
    ) -> JSONList:
        """
        按广告主名称搜索广告
        
        Args:
            advertiser_name: 广告主名称
            exact_match: 是否精确匹配 (默认模糊匹配)
            
        Returns:
            匹配的广告列表
        """
        return await self.list_all_ads(
            advertiser_name=advertiser_name,
            name_match_type="EXACT_MATCH" if exact_match else "CONTAINS",
        )

    async def get_restricted_ads(self) -> JSONList:
        """获取所有被限制的广告"""
        return await self.list_all_ads(is_restricted=True)
