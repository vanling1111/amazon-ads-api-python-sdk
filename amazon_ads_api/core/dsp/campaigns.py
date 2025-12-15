"""
Amazon DSP - Ad Group and Campaign API (异步版本)

官方端点 (6个):
- PATCH /dsp/v1/adGroups - 批量更新广告组
- POST /dsp/v1/adGroups - 批量创建广告组
- POST /dsp/v1/adGroups/list - 列出广告组
- PATCH /dsp/v1/campaigns - 批量更新广告活动
- POST /dsp/v1/campaigns - 批量创建广告活动
- POST /dsp/v1/campaigns/list - 列出广告活动

官方规范: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdGroupandCampaign-V1_prod_3p.json
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class DSPCampaignsAPI(BaseAdsClient):
    """
    DSP Campaign and Ad Group API (全异步)
    
    用于管理 DSP 广告活动和广告组。
    """

    # ============ Campaigns ============

    async def list_campaigns(
        self,
        advertiser_id: str | None = None,
        campaign_ids: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
        **kwargs,
    ) -> JSONData:
        """
        列出广告活动
        
        官方端点: POST /dsp/v1/campaigns/list
        
        Args:
            advertiser_id: 广告主 ID
            campaign_ids: 广告活动 ID 列表（过滤）
            max_results: 最大返回数量
            next_token: 分页令牌
            **kwargs: 其他过滤条件
            
        Returns:
            广告活动列表
        """
        body: JSONData = {"maxResults": max_results}
        
        if advertiser_id:
            body["advertiserId"] = advertiser_id
        if campaign_ids:
            body["campaignIds"] = campaign_ids
        if next_token:
            body["nextToken"] = next_token
            
        body.update(kwargs)
        
        result = await self.post("/dsp/v1/campaigns/list", json_data=body)
        return result if isinstance(result, dict) else {"campaigns": []}

    async def create_campaigns(
        self,
        campaigns: JSONList,
    ) -> JSONData:
        """
        批量创建广告活动
        
        官方端点: POST /dsp/v1/campaigns
        
        Args:
            campaigns: 广告活动列表
            
        Returns:
            创建结果（207 Multi-Status）
        """
        body: JSONData = {"campaigns": campaigns}
        
        result = await self.post("/dsp/v1/campaigns", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_campaigns(
        self,
        campaigns: JSONList,
    ) -> JSONData:
        """
        批量更新广告活动
        
        官方端点: PATCH /dsp/v1/campaigns
        
        Args:
            campaigns: 要更新的广告活动列表（必须包含 campaignId）
            
        Returns:
            更新结果（207 Multi-Status）
        """
        body: JSONData = {"campaigns": campaigns}
        
        result = await self.patch("/dsp/v1/campaigns", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Ad Groups ============

    async def list_ad_groups(
        self,
        advertiser_id: str | None = None,
        campaign_id: str | None = None,
        ad_group_ids: list[str] | None = None,
        max_results: int = 100,
        next_token: str | None = None,
        **kwargs,
    ) -> JSONData:
        """
        列出广告组
        
        官方端点: POST /dsp/v1/adGroups/list
        
        Args:
            advertiser_id: 广告主 ID
            campaign_id: 广告活动 ID（过滤）
            ad_group_ids: 广告组 ID 列表（过滤）
            max_results: 最大返回数量
            next_token: 分页令牌
            **kwargs: 其他过滤条件
            
        Returns:
            广告组列表
        """
        body: JSONData = {"maxResults": max_results}
        
        if advertiser_id:
            body["advertiserId"] = advertiser_id
        if campaign_id:
            body["campaignId"] = campaign_id
        if ad_group_ids:
            body["adGroupIds"] = ad_group_ids
        if next_token:
            body["nextToken"] = next_token
            
        body.update(kwargs)
        
        result = await self.post("/dsp/v1/adGroups/list", json_data=body)
        return result if isinstance(result, dict) else {"adGroups": []}

    async def create_ad_groups(
        self,
        ad_groups: JSONList,
    ) -> JSONData:
        """
        批量创建广告组
        
        官方端点: POST /dsp/v1/adGroups
        
        Args:
            ad_groups: 广告组列表
            
        Returns:
            创建结果（207 Multi-Status）
        """
        body: JSONData = {"adGroups": ad_groups}
        
        result = await self.post("/dsp/v1/adGroups", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_ad_groups(
        self,
        ad_groups: JSONList,
    ) -> JSONData:
        """
        批量更新广告组
        
        官方端点: PATCH /dsp/v1/adGroups
        
        Args:
            ad_groups: 要更新的广告组列表（必须包含 adGroupId）
            
        Returns:
            更新结果（207 Multi-Status）
        """
        body: JSONData = {"adGroups": ad_groups}
        
        result = await self.patch("/dsp/v1/adGroups", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_campaign(self, campaign_id: str) -> JSONData | None:
        """
        获取单个广告活动
        
        Args:
            campaign_id: 广告活动 ID
            
        Returns:
            广告活动详情，未找到返回 None
        """
        result = await self.list_campaigns(campaign_ids=[campaign_id])
        campaigns = result.get("campaigns", [])
        return campaigns[0] if campaigns else None

    async def get_ad_group(self, ad_group_id: str) -> JSONData | None:
        """
        获取单个广告组
        
        Args:
            ad_group_id: 广告组 ID
            
        Returns:
            广告组详情，未找到返回 None
        """
        result = await self.list_ad_groups(ad_group_ids=[ad_group_id])
        ad_groups = result.get("adGroups", [])
        return ad_groups[0] if ad_groups else None

