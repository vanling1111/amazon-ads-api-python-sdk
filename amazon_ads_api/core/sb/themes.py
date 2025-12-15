"""
Sponsored Brands - Themes API (异步版本)
SB主题定向管理

官方文档: SponsoredBrands_v3.yaml
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SBThemesAPI(BaseAdsClient):
    """
    SB Themes API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: SponsoredBrands_v3.yaml
    Stability: 高
    """

    async def create_themes(self, themes: JSONList) -> JSONData:
        """
        创建主题定向
        
        官方端点: POST /sb/themes
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            themes: 主题定向列表
        """
        result = await self.post("/sb/themes", json_data=themes)
        return result if isinstance(result, dict) else {"themes": {"success": [], "error": []}}

    async def update_themes(self, themes: JSONList) -> JSONData:
        """
        更新主题定向
        
        官方端点: PUT /sb/themes
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            themes: 主题定向列表
        """
        result = await self.put("/sb/themes", json_data=themes)
        return result if isinstance(result, dict) else {"themes": {"success": [], "error": []}}

    async def list_themes(
        self,
        campaign_id_filter: list[str] | None = None,
        ad_group_id_filter: list[str] | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取主题定向列表
        
        官方端点: POST /sb/themes/list
        官方文档: SponsoredBrands_v3.yaml
        
        Args:
            campaign_id_filter: Campaign ID 过滤
            ad_group_id_filter: Ad Group ID 过滤
            state_filter: 状态过滤
            max_results: 最大结果数
            next_token: 分页令牌
        """
        body: JSONData = {"maxResults": max_results}
        if campaign_id_filter:
            body["campaignIdFilter"] = campaign_id_filter
        if ad_group_id_filter:
            body["adGroupIdFilter"] = ad_group_id_filter
        if state_filter:
            body["stateFilter"] = state_filter
        if next_token:
            body["nextToken"] = next_token

        result = await self.post("/sb/themes/list", json_data=body)
        return result if isinstance(result, dict) else {"themes": []}

