"""
Amazon DSP - Advertisers API (异步版本)

官方端点 (2个):
- GET /dsp/advertisers/{advertiserId} - 获取单个广告主
- GET /dsp/advertisers - 获取广告主列表

官方规范: https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/dsp/3-0/advertiser.yaml
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class DSPAdvertisersAPI(BaseAdsClient):
    """
    DSP Advertisers API (全异步)
    
    官方只支持读取操作，不支持创建/更新/删除广告主。
    """

    async def get_advertiser(self, advertiser_id: str) -> JSONData:
        """
        获取单个广告主详情
        
        官方端点: GET /dsp/advertisers/{advertiserId}
        
        Args:
            advertiser_id: 广告主 ID
            
        Returns:
            广告主详情
        """
        result = await self.get(f"/dsp/advertisers/{advertiser_id}")
        return result if isinstance(result, dict) else {}

    async def list_advertisers(self) -> JSONList:
        """
        获取广告主列表
        
        官方端点: GET /dsp/advertisers
        
        Returns:
            广告主列表
        """
        result = await self.get("/dsp/advertisers")
        return result if isinstance(result, list) else []

    # ============ 便捷方法 ============

    async def get_advertiser_by_name(self, name: str) -> JSONData | None:
        """
        根据名称获取广告主
        
        Args:
            name: 广告主名称
            
        Returns:
            匹配的广告主，未找到返回 None
        """
        advertisers = await self.list_advertisers()
        for adv in advertisers:
            if adv.get("name") == name:
                return adv
        return None
