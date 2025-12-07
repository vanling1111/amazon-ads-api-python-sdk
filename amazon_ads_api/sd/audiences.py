"""
Sponsored Display - Audiences API
SD受众定向管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SDAudiencesAPI(BaseAdsClient):
    """SD Audiences API"""

    # ============ Amazon Audiences ============

    def list_amazon_audiences(
        self,
        audience_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取亚马逊预定义受众列表
        
        Args:
            audience_type: IN_MARKET | LIFESTYLE | INTEREST | LIFE_EVENT
        """
        params: JSONData = {"maxResults": max_results}
        if audience_type:
            params["audienceType"] = audience_type
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/sd/audiences/amazon", params=params)
        return result if isinstance(result, dict) else {"audiences": []}

    def get_amazon_audience(self, audience_id: str) -> JSONData:
        """获取亚马逊受众详情"""
        result = self.get(f"/sd/audiences/amazon/{audience_id}")
        return result if isinstance(result, dict) else {}

    def search_amazon_audiences(
        self,
        query: str,
        max_results: int = 100,
    ) -> JSONData:
        """搜索亚马逊受众"""
        result = self.post("/sd/audiences/amazon/search", json_data={
            "query": query,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"audiences": []}

    # ============ Custom Audiences (Remarketing) ============

    def list_custom_audiences(
        self,
        audience_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取自定义受众列表
        
        Args:
            audience_type: VIEWS | PURCHASES | ADVERTISER_GENERATED
        """
        params: JSONData = {"maxResults": max_results}
        if audience_type:
            params["audienceType"] = audience_type
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/sd/audiences/custom", params=params)
        return result if isinstance(result, dict) else {"audiences": []}

    def get_custom_audience(self, audience_id: str) -> JSONData:
        """获取自定义受众详情"""
        result = self.get(f"/sd/audiences/custom/{audience_id}")
        return result if isinstance(result, dict) else {}

    def create_custom_audience(
        self,
        name: str,
        audience_type: str,
        definition: JSONData,
        description: str | None = None,
    ) -> JSONData:
        """
        创建自定义受众
        
        Args:
            audience_type: VIEWS_REMARKETING | PURCHASES_REMARKETING | ASIN_SEED
            definition: {
                "lookbackDays": 30,  # for remarketing
                "asins": ["B00XXX"],  # for ASIN_SEED
                "categories": ["category_id"]  # optional
            }
        """
        body: JSONData = {
            "name": name,
            "audienceType": audience_type,
            "definition": definition,
        }
        if description:
            body["description"] = description

        result = self.post("/sd/audiences/custom", json_data=body)
        return result if isinstance(result, dict) else {}

    def update_custom_audience(
        self,
        audience_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新自定义受众"""
        result = self.put(f"/sd/audiences/custom/{audience_id}", json_data=updates)
        return result if isinstance(result, dict) else {}

    def delete_custom_audience(self, audience_id: str) -> JSONData:
        """删除自定义受众"""
        return self.delete(f"/sd/audiences/custom/{audience_id}")

    # ============ Views Remarketing ============

    def create_views_remarketing_audience(
        self,
        name: str,
        asins: list[str],
        lookback_days: int = 30,
    ) -> JSONData:
        """
        创建浏览再营销受众
        
        定向浏览过指定产品但未购买的用户
        """
        return self.create_custom_audience(
            name=name,
            audience_type="VIEWS_REMARKETING",
            definition={
                "asins": asins,
                "lookbackDays": lookback_days,
            }
        )

    def create_purchases_remarketing_audience(
        self,
        name: str,
        asins: list[str],
        lookback_days: int = 365,
    ) -> JSONData:
        """
        创建购买再营销受众
        
        定向购买过指定产品的用户（用于交叉销售）
        """
        return self.create_custom_audience(
            name=name,
            audience_type="PURCHASES_REMARKETING",
            definition={
                "asins": asins,
                "lookbackDays": lookback_days,
            }
        )

    # ============ Lookalike Audiences ============

    def create_lookalike_audience(
        self,
        name: str,
        seed_audience_id: str,
        expansion_level: int = 5,
    ) -> JSONData:
        """
        创建相似受众
        
        Args:
            seed_audience_id: 种子受众ID
            expansion_level: 扩展级别1-10（越高越广泛但相似度越低）
        """
        result = self.post("/sd/audiences/lookalike", json_data={
            "name": name,
            "seedAudienceId": seed_audience_id,
            "expansionLevel": expansion_level,
        })
        return result if isinstance(result, dict) else {}

    def get_lookalike_audience_preview(
        self,
        seed_audience_id: str,
        expansion_level: int = 5,
    ) -> JSONData:
        """预览相似受众（估算规模等）"""
        result = self.post("/sd/audiences/lookalike/preview", json_data={
            "seedAudienceId": seed_audience_id,
            "expansionLevel": expansion_level,
        })
        return result if isinstance(result, dict) else {}

    # ============ Audience Size ============

    def get_audience_size(self, audience_id: str) -> JSONData:
        """获取受众规模"""
        result = self.get(f"/sd/audiences/{audience_id}/size")
        return result if isinstance(result, dict) else {}

    def estimate_combined_audience_size(
        self,
        audience_ids: list[str],
        combination_type: str = "UNION",
    ) -> JSONData:
        """
        估算组合受众规模
        
        Args:
            combination_type: UNION | INTERSECTION | EXCLUSION
        """
        result = self.post("/sd/audiences/estimateSize", json_data={
            "audienceIds": audience_ids,
            "combinationType": combination_type,
        })
        return result if isinstance(result, dict) else {}

    # ============ Audience Recommendations ============

    def get_audience_recommendations(
        self,
        asins: list[str],
        max_results: int = 20,
    ) -> JSONData:
        """
        基于ASIN获取受众推荐
        
        推荐最适合这些产品的受众
        """
        result = self.post("/sd/audiences/recommendations", json_data={
            "asins": asins,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"audiences": []}

    def get_high_performing_audiences(
        self,
        metric: str = "ROAS",
        limit: int = 20,
    ) -> JSONList:
        """
        获取高效果受众
        
        Args:
            metric: ROAS | CVR | CTR
        """
        result = self.get("/sd/audiences/highPerforming", params={
            "metric": metric,
            "limit": limit,
        })
        return result if isinstance(result, list) else []

    # ============ Audience Targeting in Campaigns ============

    def add_audience_to_ad_group(
        self,
        ad_group_id: str,
        audience_id: str,
        bid: float,
    ) -> JSONData:
        """将受众添加到Ad Group"""
        result = self.post("/sd/targets", json_data={
            "adGroupId": ad_group_id,
            "targetingClause": {
                "type": "audience",
                "audienceId": audience_id,
            },
            "bid": bid,
        })
        return result if isinstance(result, dict) else {}

    def remove_audience_from_ad_group(
        self,
        ad_group_id: str,
        target_id: str,
    ) -> JSONData:
        """从Ad Group移除受众"""
        return self.delete(f"/sd/targets/{target_id}")

    def update_audience_bid(
        self,
        target_id: str,
        bid: float,
    ) -> JSONData:
        """更新受众竞价"""
        result = self.put(f"/sd/targets/{target_id}", json_data={"bid": bid})
        return result if isinstance(result, dict) else {}

    # ============ Negative Audiences ============

    def add_negative_audience(
        self,
        ad_group_id: str,
        audience_id: str,
    ) -> JSONData:
        """添加否定受众"""
        result = self.post("/sd/negativeTargets", json_data={
            "adGroupId": ad_group_id,
            "targetingClause": {
                "type": "audience",
                "audienceId": audience_id,
            },
        })
        return result if isinstance(result, dict) else {}

    def remove_negative_audience(self, target_id: str) -> JSONData:
        """移除否定受众"""
        return self.delete(f"/sd/negativeTargets/{target_id}")

    # ============ 便捷方法 ============

    def list_all_amazon_audiences(self) -> JSONList:
        """获取所有亚马逊受众（自动分页）"""
        all_audiences = []
        next_token = None

        while True:
            result = self.list_amazon_audiences(
                max_results=100,
                next_token=next_token,
            )
            audiences = result.get("audiences", [])
            all_audiences.extend(audiences)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_audiences

    def list_all_custom_audiences(self) -> JSONList:
        """获取所有自定义受众（自动分页）"""
        all_audiences = []
        next_token = None

        while True:
            result = self.list_custom_audiences(
                max_results=100,
                next_token=next_token,
            )
            audiences = result.get("audiences", [])
            all_audiences.extend(audiences)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_audiences

    def get_in_market_audiences(self) -> JSONList:
        """获取In-Market受众"""
        result = self.list_amazon_audiences(audience_type="IN_MARKET", max_results=100)
        return result.get("audiences", [])

    def get_lifestyle_audiences(self) -> JSONList:
        """获取Lifestyle受众"""
        result = self.list_amazon_audiences(audience_type="LIFESTYLE", max_results=100)
        return result.get("audiences", [])

    def setup_full_funnel_audiences(
        self,
        ad_group_id: str,
        asins: list[str],
        base_bid: float,
    ) -> JSONData:
        """
        设置全漏斗受众定向
        
        包括浏览者、购买者和相似受众
        """
        results = {}

        # 1. 浏览再营销（高意向）
        views_audience = self.create_views_remarketing_audience(
            name=f"Views_{'_'.join(asins[:3])}",
            asins=asins,
            lookback_days=30,
        )
        if views_audience.get("audienceId"):
            results["viewsAudience"] = self.add_audience_to_ad_group(
                ad_group_id=ad_group_id,
                audience_id=views_audience["audienceId"],
                bid=base_bid * 1.5,  # 高竞价
            )

        # 2. 购买再营销（交叉销售）
        purchases_audience = self.create_purchases_remarketing_audience(
            name=f"Purchases_{'_'.join(asins[:3])}",
            asins=asins,
            lookback_days=180,
        )
        if purchases_audience.get("audienceId"):
            results["purchasesAudience"] = self.add_audience_to_ad_group(
                ad_group_id=ad_group_id,
                audience_id=purchases_audience["audienceId"],
                bid=base_bid * 1.2,
            )

        # 3. 受众推荐
        recommendations = self.get_audience_recommendations(asins, max_results=5)
        for rec in recommendations.get("audiences", []):
            audience_id = rec.get("audienceId")
            if audience_id:
                results[f"recommended_{audience_id}"] = self.add_audience_to_ad_group(
                    ad_group_id=ad_group_id,
                    audience_id=audience_id,
                    bid=base_bid,
                )

        return results

