"""
Amazon DSP - Advertisers API (异步版本)
DSP广告主管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class DSPAdvertisersAPI(BaseAdsClient):
    """DSP Advertisers API (全异步)"""

    # ============ Advertisers ============

    async def list_advertisers(
        self,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取广告主列表"""
        params: JSONData = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/dsp/advertisers", params=params)
        return result if isinstance(result, dict) else {"advertisers": []}

    async def get_advertiser(self, advertiser_id: str) -> JSONData:
        """获取单个广告主详情"""
        result = await self.get(f"/dsp/advertisers/{advertiser_id}")
        return result if isinstance(result, dict) else {}

    async def create_advertiser(
        self,
        name: str,
        advertiser_type: str = "BRAND",
        billing_address: JSONData | None = None,
    ) -> JSONData:
        """创建广告主"""
        body: JSONData = {
            "name": name,
            "advertiserType": advertiser_type,
        }
        if billing_address:
            body["billingAddress"] = billing_address

        result = await self.post("/dsp/advertisers", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_advertiser(
        self,
        advertiser_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新广告主"""
        result = await self.put(f"/dsp/advertisers/{advertiser_id}", json_data=updates)
        return result if isinstance(result, dict) else {}

    # ============ Advertiser Settings ============

    async def get_advertiser_settings(self, advertiser_id: str) -> JSONData:
        """获取广告主设置"""
        result = await self.get(f"/dsp/advertisers/{advertiser_id}/settings")
        return result if isinstance(result, dict) else {}

    async def update_advertiser_settings(
        self,
        advertiser_id: str,
        settings: JSONData,
    ) -> JSONData:
        """更新广告主设置"""
        result = await self.put(
            f"/dsp/advertisers/{advertiser_id}/settings",
            json_data=settings
        )
        return result if isinstance(result, dict) else {}

    # ============ Brand Safety ============

    async def get_brand_safety_settings(self, advertiser_id: str) -> JSONData:
        """获取品牌安全设置"""
        result = await self.get(f"/dsp/advertisers/{advertiser_id}/brandSafety")
        return result if isinstance(result, dict) else {}

    async def update_brand_safety_settings(
        self,
        advertiser_id: str,
        settings: JSONData,
    ) -> JSONData:
        """更新品牌安全设置"""
        result = await self.put(
            f"/dsp/advertisers/{advertiser_id}/brandSafety",
            json_data=settings
        )
        return result if isinstance(result, dict) else {}

    # ============ Conversion Tracking ============

    async def get_conversion_settings(self, advertiser_id: str) -> JSONData:
        """获取转化追踪设置"""
        result = await self.get(f"/dsp/advertisers/{advertiser_id}/conversions")
        return result if isinstance(result, dict) else {}

    async def create_conversion_definition(
        self,
        advertiser_id: str,
        name: str,
        conversion_type: str,
        attribution_window_days: int = 14,
    ) -> JSONData:
        """创建转化定义"""
        result = await self.post(
            f"/dsp/advertisers/{advertiser_id}/conversions",
            json_data={
                "name": name,
                "conversionType": conversion_type,
                "attributionWindowDays": attribution_window_days,
            }
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def list_all_advertisers(self) -> JSONList:
        """获取所有广告主（自动分页）"""
        all_advertisers = []
        next_token = None

        while True:
            result = await self.list_advertisers(
                max_results=100,
                next_token=next_token,
            )
            advertisers = result.get("advertisers", [])
            all_advertisers.extend(advertisers)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_advertisers

    async def get_advertiser_by_name(self, name: str) -> JSONData | None:
        """根据名称获取广告主"""
        advertisers = await self.list_all_advertisers()
        for adv in advertisers:
            if adv.get("name") == name:
                return adv
        return None
