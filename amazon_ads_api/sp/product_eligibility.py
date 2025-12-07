"""
Sponsored Products - Product Eligibility API
SP产品资格和推广资格
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SPProductEligibilityAPI(BaseAdsClient):
    """SP Product Eligibility API"""

    # ============ Product Eligibility ============

    def check_product_eligibility(
        self,
        asins: list[str],
    ) -> JSONData:
        """
        检查产品SP广告资格
        
        Args:
            asins: ASIN列表（最多1000个）
            
        Returns:
            {
                "productEligibility": [
                    {
                        "asin": "B00XXX",
                        "eligible": true,
                        "eligibilityStatus": "ELIGIBLE"
                    },
                    {
                        "asin": "B00YYY",
                        "eligible": false,
                        "eligibilityStatus": "NOT_ELIGIBLE",
                        "ineligibilityReasons": ["NO_INVENTORY", "NOT_BUYABLE"]
                    }
                ]
            }
        """
        result = self.post("/sp/eligibility/products", json_data={
            "asins": asins
        })
        return result if isinstance(result, dict) else {"productEligibility": []}

    def get_product_details(
        self,
        asins: list[str],
    ) -> JSONData:
        """获取产品详情（用于广告）"""
        result = self.post("/sp/products", json_data={
            "asins": asins
        })
        return result if isinstance(result, dict) else {"products": []}

    # ============ SKU Eligibility ============

    def check_sku_eligibility(
        self,
        skus: list[str],
    ) -> JSONData:
        """
        检查SKU SP广告资格（卖家用）
        
        Args:
            skus: SKU列表
        """
        result = self.post("/sp/eligibility/skus", json_data={
            "skus": skus
        })
        return result if isinstance(result, dict) else {"skuEligibility": []}

    def list_eligible_skus(
        self,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取所有有资格的SKU列表"""
        params: JSONData = {"maxResults": max_results}
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/sp/eligibility/skus", params=params)
        return result if isinstance(result, dict) else {"skus": []}

    # ============ Campaign Eligibility ============

    def check_campaign_targeting_eligibility(
        self,
        targeting_type: str,
        asins: list[str],
    ) -> JSONData:
        """
        检查Campaign定向资格
        
        Args:
            targeting_type: MANUAL | AUTO
        """
        result = self.post("/sp/eligibility/campaigns", json_data={
            "targetingType": targeting_type,
            "asins": asins,
        })
        return result if isinstance(result, dict) else {}

    # ============ Targeting Eligibility ============

    def check_keyword_targeting_eligibility(
        self,
        keywords: list[dict],
    ) -> JSONData:
        """
        检查关键词定向资格
        
        Args:
            keywords: [
                {"keywordText": "running shoes", "matchType": "EXACT"},
                ...
            ]
        """
        result = self.post("/sp/eligibility/keywords", json_data={
            "keywords": keywords
        })
        return result if isinstance(result, dict) else {}

    def check_product_targeting_eligibility(
        self,
        targets: list[dict],
    ) -> JSONData:
        """
        检查产品定向资格
        
        Args:
            targets: [
                {"type": "asinSameAs", "value": "B00XXX"},
                {"type": "asinCategorySameAs", "value": "category_id"}
            ]
        """
        result = self.post("/sp/eligibility/targets", json_data={
            "targets": targets
        })
        return result if isinstance(result, dict) else {}

    # ============ Auto Targeting Eligibility ============

    def get_auto_targeting_preview(
        self,
        asins: list[str],
    ) -> JSONData:
        """
        预览自动定向
        
        查看自动定向会匹配哪些关键词和产品
        """
        result = self.post("/sp/eligibility/autoTargeting/preview", json_data={
            "asins": asins
        })
        return result if isinstance(result, dict) else {}

    # ============ Restrictions ============

    def get_product_restrictions(
        self,
        asin: str,
    ) -> JSONData:
        """
        获取产品广告限制
        
        返回该产品的广告投放限制
        """
        result = self.get(f"/sp/products/{asin}/restrictions")
        return result if isinstance(result, dict) else {}

    def get_category_restrictions(
        self,
        category_id: str,
    ) -> JSONData:
        """获取品类广告限制"""
        result = self.get(f"/sp/categories/{category_id}/restrictions")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def list_all_eligible_skus(self) -> JSONList:
        """获取所有有资格的SKU（自动分页）"""
        all_skus = []
        next_token = None

        while True:
            result = self.list_eligible_skus(
                max_results=100,
                next_token=next_token,
            )
            skus = result.get("skus", [])
            all_skus.extend(skus)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_skus

    def filter_eligible_asins(self, asins: list[str]) -> list[str]:
        """过滤有资格的ASIN"""
        result = self.check_product_eligibility(asins)
        eligible = []
        for item in result.get("productEligibility", []):
            if item.get("eligible"):
                eligible.append(item.get("asin"))
        return eligible

    def get_ineligible_reasons(self, asins: list[str]) -> dict[str, list[str]]:
        """获取不合格ASIN的原因"""
        result = self.check_product_eligibility(asins)
        reasons = {}
        for item in result.get("productEligibility", []):
            if not item.get("eligible"):
                asin = item.get("asin")
                reasons[asin] = item.get("ineligibilityReasons", ["UNKNOWN"])
        return reasons

    def batch_check_eligibility(
        self,
        asins: list[str],
        batch_size: int = 100,
    ) -> JSONData:
        """批量检查产品资格"""
        all_results = []

        for i in range(0, len(asins), batch_size):
            batch = asins[i:i + batch_size]
            result = self.check_product_eligibility(batch)
            all_results.extend(result.get("productEligibility", []))

        return {"productEligibility": all_results}

