"""
Amazon Ads Eligibility API (异步版本)
广告资格检查
"""

from ..base import BaseAdsClient, JSONData, JSONList


class EligibilityAPI(BaseAdsClient):
    """Eligibility API (全异步)"""

    # ============ Product Eligibility ============

    async def check_product_eligibility(
        self,
        asins: list[str],
        ad_type: str = "SP",
    ) -> JSONData:
        """检查产品广告资格"""
        result = await self.post(f"/{ad_type.lower()}/eligibility/products", json_data={
            "asins": asins,
        })
        return result if isinstance(result, dict) else {"eligible": [], "ineligible": []}

    async def check_sp_product_eligibility(self, asins: list[str]) -> JSONData:
        """检查SP产品资格"""
        return await self.check_product_eligibility(asins, "SP")

    async def check_sb_product_eligibility(self, asins: list[str]) -> JSONData:
        """检查SB产品资格"""
        return await self.check_product_eligibility(asins, "SB")

    async def check_sd_product_eligibility(self, asins: list[str]) -> JSONData:
        """检查SD产品资格"""
        return await self.check_product_eligibility(asins, "SD")

    # ============ Brand Eligibility ============

    async def check_brand_eligibility(self) -> JSONData:
        """检查品牌广告资格"""
        result = await self.get("/sb/eligibility/brands")
        return result if isinstance(result, dict) else {}

    async def get_brand_registry_status(self) -> JSONData:
        """获取品牌备案状态"""
        result = await self.get("/sb/brands/registry")
        return result if isinstance(result, dict) else {}

    async def list_eligible_brands(self) -> JSONList:
        """获取有资格投放广告的品牌列表"""
        result = await self.get("/sb/brands")
        return result if isinstance(result, list) else []

    # ============ Feature Eligibility ============

    async def check_feature_eligibility(self, features: list[str]) -> JSONData:
        """检查功能资格"""
        result = await self.post("/eligibility/features", json_data={
            "features": features,
        })
        return result if isinstance(result, dict) else {}

    async def check_video_ads_eligibility(self) -> JSONData:
        """检查视频广告资格"""
        return await self.check_feature_eligibility(["VIDEO_ADS"])

    async def check_attribution_eligibility(self) -> JSONData:
        """检查归因功能资格"""
        return await self.check_feature_eligibility(["AMAZON_ATTRIBUTION"])

    # ============ Category Eligibility ============

    async def check_category_eligibility(
        self,
        category_ids: list[str],
        ad_type: str = "SP",
    ) -> JSONData:
        """检查品类广告资格"""
        result = await self.post(f"/{ad_type.lower()}/eligibility/categories", json_data={
            "categoryIds": category_ids,
        })
        return result if isinstance(result, dict) else {}

    async def get_restricted_categories(self, ad_type: str = "SP") -> JSONList:
        """获取受限品类列表"""
        result = await self.get(f"/{ad_type.lower()}/eligibility/restrictedCategories")
        return result if isinstance(result, list) else []

    # ============ Targeting Eligibility ============

    async def check_targeting_eligibility(
        self,
        targeting_type: str,
        targets: list[dict],
    ) -> JSONData:
        """检查定向资格"""
        result = await self.post("/eligibility/targeting", json_data={
            "targetingType": targeting_type,
            "targets": targets,
        })
        return result if isinstance(result, dict) else {}

    async def check_keyword_eligibility(self, keywords: list[str]) -> JSONData:
        """检查关键词资格"""
        targets = [{"keywordText": kw} for kw in keywords]
        return await self.check_targeting_eligibility("KEYWORD", targets)

    # ============ Account Eligibility ============

    async def check_account_eligibility(self) -> JSONData:
        """检查账户广告资格"""
        result = await self.get("/eligibility/account")
        return result if isinstance(result, dict) else {}

    async def get_account_requirements(self) -> JSONData:
        """获取账户开通广告的要求"""
        result = await self.get("/eligibility/account/requirements")
        return result if isinstance(result, dict) else {}

    async def get_account_restrictions(self) -> JSONList:
        """获取账户当前的限制"""
        result = await self.get("/eligibility/account/restrictions")
        return result if isinstance(result, list) else []

    # ============ Store Eligibility ============

    async def check_store_eligibility(self, store_id: str | None = None) -> JSONData:
        """检查品牌旗舰店资格"""
        params = {}
        if store_id:
            params["storeId"] = store_id

        result = await self.get("/sb/eligibility/stores", params=params or None)
        return result if isinstance(result, dict) else {}

    # ============ DSP Eligibility ============

    async def check_dsp_eligibility(self) -> JSONData:
        """检查DSP资格"""
        result = await self.get("/dsp/eligibility")
        return result if isinstance(result, dict) else {}

    async def check_dsp_audience_eligibility(
        self,
        audience_types: list[str],
    ) -> JSONData:
        """检查DSP受众资格"""
        result = await self.post("/dsp/eligibility/audiences", json_data={
            "audienceTypes": audience_types,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_full_eligibility_status(self) -> JSONData:
        """获取完整资格状态"""
        account = await self.check_account_eligibility()
        brand = await self.check_brand_eligibility()
        features = await self.check_feature_eligibility([
            "VIDEO_ADS",
            "STORE_SPOTLIGHT",
            "CUSTOM_IMAGES",
            "AMAZON_ATTRIBUTION",
            "BRAND_METRICS"
        ])

        return {
            "account": account,
            "brand": brand,
            "features": features,
        }

    async def is_eligible_for_sp(self) -> bool:
        """检查是否有SP资格"""
        account = await self.check_account_eligibility()
        return account.get("sp", {}).get("eligible", False)

    async def is_eligible_for_sb(self) -> bool:
        """检查是否有SB资格"""
        account = await self.check_account_eligibility()
        brand = await self.check_brand_eligibility()
        return (
            account.get("sb", {}).get("eligible", False) and
            brand.get("eligible", False)
        )

    async def is_eligible_for_sd(self) -> bool:
        """检查是否有SD资格"""
        account = await self.check_account_eligibility()
        return account.get("sd", {}).get("eligible", False)

    async def filter_eligible_asins(
        self,
        asins: list[str],
        ad_type: str = "SP",
    ) -> list[str]:
        """过滤有资格的ASIN"""
        result = await self.check_product_eligibility(asins, ad_type)
        return result.get("eligible", [])
