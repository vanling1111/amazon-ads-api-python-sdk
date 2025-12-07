"""
Amazon DSP - Advertisers API
DSP广告主管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class DSPAdvertisersAPI(BaseAdsClient):
    """DSP Advertisers API"""

    # ============ Advertisers ============

    def list_advertisers(
        self,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取广告主列表
        
        Returns:
            广告主列表，包含advertiser_id、name、status等
        """
        params: JSONData = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/dsp/advertisers", params=params)
        return result if isinstance(result, dict) else {"advertisers": []}

    def get_advertiser(self, advertiser_id: str) -> JSONData:
        """获取单个广告主详情"""
        result = self.get(f"/dsp/advertisers/{advertiser_id}")
        return result if isinstance(result, dict) else {}

    def create_advertiser(
        self,
        name: str,
        advertiser_type: str = "BRAND",
        billing_address: JSONData | None = None,
    ) -> JSONData:
        """
        创建广告主
        
        Args:
            name: 广告主名称
            advertiser_type: BRAND | AGENCY
            billing_address: 账单地址
        """
        body: JSONData = {
            "name": name,
            "advertiserType": advertiser_type,
        }
        if billing_address:
            body["billingAddress"] = billing_address

        result = self.post("/dsp/advertisers", json_data=body)
        return result if isinstance(result, dict) else {}

    def update_advertiser(
        self,
        advertiser_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新广告主"""
        result = self.put(f"/dsp/advertisers/{advertiser_id}", json_data=updates)
        return result if isinstance(result, dict) else {}

    # ============ Advertiser Settings ============

    def get_advertiser_settings(self, advertiser_id: str) -> JSONData:
        """获取广告主设置"""
        result = self.get(f"/dsp/advertisers/{advertiser_id}/settings")
        return result if isinstance(result, dict) else {}

    def update_advertiser_settings(
        self,
        advertiser_id: str,
        settings: JSONData,
    ) -> JSONData:
        """更新广告主设置"""
        result = self.put(
            f"/dsp/advertisers/{advertiser_id}/settings",
            json_data=settings
        )
        return result if isinstance(result, dict) else {}

    # ============ Brand Safety ============

    def get_brand_safety_settings(self, advertiser_id: str) -> JSONData:
        """获取品牌安全设置"""
        result = self.get(f"/dsp/advertisers/{advertiser_id}/brandSafety")
        return result if isinstance(result, dict) else {}

    def update_brand_safety_settings(
        self,
        advertiser_id: str,
        settings: JSONData,
    ) -> JSONData:
        """
        更新品牌安全设置
        
        Args:
            settings: {
                "blockList": ["domain1.com"],
                "categories": ["ADULT_CONTENT"],
                "level": "STANDARD"  # STANDARD | STRICT | CUSTOM
            }
        """
        result = self.put(
            f"/dsp/advertisers/{advertiser_id}/brandSafety",
            json_data=settings
        )
        return result if isinstance(result, dict) else {}

    # ============ Conversion Tracking ============

    def get_conversion_settings(self, advertiser_id: str) -> JSONData:
        """获取转化追踪设置"""
        result = self.get(f"/dsp/advertisers/{advertiser_id}/conversions")
        return result if isinstance(result, dict) else {}

    def create_conversion_definition(
        self,
        advertiser_id: str,
        name: str,
        conversion_type: str,
        attribution_window_days: int = 14,
    ) -> JSONData:
        """
        创建转化定义
        
        Args:
            conversion_type: PURCHASE | ADD_TO_CART | PAGE_VIEW | SIGN_UP | CUSTOM
            attribution_window_days: 归因窗口（1-30天）
        """
        result = self.post(
            f"/dsp/advertisers/{advertiser_id}/conversions",
            json_data={
                "name": name,
                "conversionType": conversion_type,
                "attributionWindowDays": attribution_window_days,
            }
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def list_all_advertisers(self) -> JSONList:
        """获取所有广告主（自动分页）"""
        all_advertisers = []
        next_token = None

        while True:
            result = self.list_advertisers(
                max_results=100,
                next_token=next_token,
            )
            advertisers = result.get("advertisers", [])
            all_advertisers.extend(advertisers)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_advertisers

    def get_advertiser_by_name(self, name: str) -> JSONData | None:
        """根据名称获取广告主"""
        advertisers = self.list_all_advertisers()
        for adv in advertisers:
            if adv.get("name") == name:
                return adv
        return None

