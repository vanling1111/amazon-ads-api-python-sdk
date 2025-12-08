"""
Sponsored Display - Audiences API (异步版本)
SD受众定向管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SDAudiencesAPI(BaseAdsClient):
    """SD Audiences API (全异步)"""

    # ============ Amazon Audiences ============

    async def list_amazon_audiences(
        self,
        audience_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取亚马逊预定义受众列表"""
        params: JSONData = {"maxResults": max_results}
        if audience_type:
            params["audienceType"] = audience_type
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/sd/audiences/amazon", params=params)
        return result if isinstance(result, dict) else {"audiences": []}

    async def get_amazon_audience(self, audience_id: str) -> JSONData:
        """获取亚马逊受众详情"""
        result = await self.get(f"/sd/audiences/amazon/{audience_id}")
        return result if isinstance(result, dict) else {}

    async def search_amazon_audiences(
        self,
        query: str,
        max_results: int = 100,
    ) -> JSONData:
        """搜索亚马逊受众"""
        result = await self.post("/sd/audiences/amazon/search", json_data={
            "query": query,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"audiences": []}

    # ============ Custom Audiences (Remarketing) ============

    async def list_custom_audiences(
        self,
        audience_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取自定义受众列表"""
        params: JSONData = {"maxResults": max_results}
        if audience_type:
            params["audienceType"] = audience_type
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/sd/audiences/custom", params=params)
        return result if isinstance(result, dict) else {"audiences": []}

    async def get_custom_audience(self, audience_id: str) -> JSONData:
        """获取自定义受众详情"""
        result = await self.get(f"/sd/audiences/custom/{audience_id}")
        return result if isinstance(result, dict) else {}

    async def create_custom_audience(
        self,
        name: str,
        audience_type: str,
        definition: JSONData,
        description: str | None = None,
    ) -> JSONData:
        """创建自定义受众"""
        body: JSONData = {
            "name": name,
            "audienceType": audience_type,
            "definition": definition,
        }
        if description:
            body["description"] = description

        result = await self.post("/sd/audiences/custom", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_custom_audience(
        self,
        audience_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新自定义受众"""
        result = await self.put(f"/sd/audiences/custom/{audience_id}", json_data=updates)
        return result if isinstance(result, dict) else {}

    async def delete_custom_audience(self, audience_id: str) -> JSONData:
        """删除自定义受众"""
        return await self.delete(f"/sd/audiences/custom/{audience_id}")

    # ============ Views Remarketing ============

    async def create_views_remarketing_audience(
        self,
        name: str,
        asins: list[str],
        lookback_days: int = 30,
    ) -> JSONData:
        """创建浏览再营销受众"""
        return await self.create_custom_audience(
            name=name,
            audience_type="VIEWS_REMARKETING",
            definition={
                "asins": asins,
                "lookbackDays": lookback_days,
            }
        )

    async def create_purchases_remarketing_audience(
        self,
        name: str,
        asins: list[str],
        lookback_days: int = 365,
    ) -> JSONData:
        """创建购买再营销受众"""
        return await self.create_custom_audience(
            name=name,
            audience_type="PURCHASES_REMARKETING",
            definition={
                "asins": asins,
                "lookbackDays": lookback_days,
            }
        )

    # ============ Lookalike Audiences ============

    async def create_lookalike_audience(
        self,
        name: str,
        seed_audience_id: str,
        expansion_level: int = 5,
    ) -> JSONData:
        """创建相似受众"""
        result = await self.post("/sd/audiences/lookalike", json_data={
            "name": name,
            "seedAudienceId": seed_audience_id,
            "expansionLevel": expansion_level,
        })
        return result if isinstance(result, dict) else {}

    async def get_lookalike_audience_preview(
        self,
        seed_audience_id: str,
        expansion_level: int = 5,
    ) -> JSONData:
        """预览相似受众"""
        result = await self.post("/sd/audiences/lookalike/preview", json_data={
            "seedAudienceId": seed_audience_id,
            "expansionLevel": expansion_level,
        })
        return result if isinstance(result, dict) else {}

    # ============ Audience Size ============

    async def get_audience_size(self, audience_id: str) -> JSONData:
        """获取受众规模"""
        result = await self.get(f"/sd/audiences/{audience_id}/size")
        return result if isinstance(result, dict) else {}

    async def estimate_combined_audience_size(
        self,
        audience_ids: list[str],
        combination_type: str = "UNION",
    ) -> JSONData:
        """估算组合受众规模"""
        result = await self.post("/sd/audiences/estimateSize", json_data={
            "audienceIds": audience_ids,
            "combinationType": combination_type,
        })
        return result if isinstance(result, dict) else {}

    # ============ Audience Recommendations ============

    async def get_audience_recommendations(
        self,
        asins: list[str],
        max_results: int = 20,
    ) -> JSONData:
        """基于ASIN获取受众推荐"""
        result = await self.post("/sd/audiences/recommendations", json_data={
            "asins": asins,
            "maxResults": max_results,
        })
        return result if isinstance(result, dict) else {"audiences": []}

    async def get_high_performing_audiences(
        self,
        metric: str = "ROAS",
        limit: int = 20,
    ) -> JSONList:
        """获取高效果受众"""
        result = await self.get("/sd/audiences/highPerforming", params={
            "metric": metric,
            "limit": limit,
        })
        return result if isinstance(result, list) else []

    # ============ Audience Targeting in Campaigns ============

    async def add_audience_to_ad_group(
        self,
        ad_group_id: str,
        audience_id: str,
        bid: float,
    ) -> JSONData:
        """将受众添加到Ad Group"""
        result = await self.post("/sd/targets", json_data={
            "adGroupId": ad_group_id,
            "targetingClause": {
                "type": "audience",
                "audienceId": audience_id,
            },
            "bid": bid,
        })
        return result if isinstance(result, dict) else {}

    async def remove_audience_from_ad_group(
        self,
        ad_group_id: str,
        target_id: str,
    ) -> JSONData:
        """从Ad Group移除受众"""
        return await self.delete(f"/sd/targets/{target_id}")

    async def update_audience_bid(
        self,
        target_id: str,
        bid: float,
    ) -> JSONData:
        """更新受众竞价"""
        result = await self.put(f"/sd/targets/{target_id}", json_data={"bid": bid})
        return result if isinstance(result, dict) else {}

    # ============ Negative Audiences ============

    async def add_negative_audience(
        self,
        ad_group_id: str,
        audience_id: str,
    ) -> JSONData:
        """添加否定受众"""
        result = await self.post("/sd/negativeTargets", json_data={
            "adGroupId": ad_group_id,
            "targetingClause": {
                "type": "audience",
                "audienceId": audience_id,
            },
        })
        return result if isinstance(result, dict) else {}

    async def remove_negative_audience(self, target_id: str) -> JSONData:
        """移除否定受众"""
        return await self.delete(f"/sd/negativeTargets/{target_id}")

    # ============ 便捷方法 ============

    async def list_all_amazon_audiences(self) -> JSONList:
        """获取所有亚马逊受众（自动分页）"""
        all_audiences = []
        next_token = None

        while True:
            result = await self.list_amazon_audiences(
                max_results=100,
                next_token=next_token,
            )
            audiences = result.get("audiences", [])
            all_audiences.extend(audiences)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_audiences

    async def list_all_custom_audiences(self) -> JSONList:
        """获取所有自定义受众（自动分页）"""
        all_audiences = []
        next_token = None

        while True:
            result = await self.list_custom_audiences(
                max_results=100,
                next_token=next_token,
            )
            audiences = result.get("audiences", [])
            all_audiences.extend(audiences)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_audiences

    async def get_in_market_audiences(self) -> JSONList:
        """获取In-Market受众"""
        result = await self.list_amazon_audiences(audience_type="IN_MARKET", max_results=100)
        return result.get("audiences", [])

    async def get_lifestyle_audiences(self) -> JSONList:
        """获取Lifestyle受众"""
        result = await self.list_amazon_audiences(audience_type="LIFESTYLE", max_results=100)
        return result.get("audiences", [])

    async def setup_full_funnel_audiences(
        self,
        ad_group_id: str,
        asins: list[str],
        base_bid: float,
    ) -> JSONData:
        """设置全漏斗受众定向"""
        results = {}

        # 1. 浏览再营销（高意向）
        views_audience = await self.create_views_remarketing_audience(
            name=f"Views_{'_'.join(asins[:3])}",
            asins=asins,
            lookback_days=30,
        )
        if views_audience.get("audienceId"):
            results["viewsAudience"] = await self.add_audience_to_ad_group(
                ad_group_id=ad_group_id,
                audience_id=views_audience["audienceId"],
                bid=base_bid * 1.5,
            )

        # 2. 购买再营销（交叉销售）
        purchases_audience = await self.create_purchases_remarketing_audience(
            name=f"Purchases_{'_'.join(asins[:3])}",
            asins=asins,
            lookback_days=180,
        )
        if purchases_audience.get("audienceId"):
            results["purchasesAudience"] = await self.add_audience_to_ad_group(
                ad_group_id=ad_group_id,
                audience_id=purchases_audience["audienceId"],
                bid=base_bid * 1.2,
            )

        # 3. 受众推荐
        recommendations = await self.get_audience_recommendations(asins, max_results=5)
        for rec in recommendations.get("audiences", []):
            audience_id = rec.get("audienceId")
            if audience_id:
                results[f"recommended_{audience_id}"] = await self.add_audience_to_ad_group(
                    ad_group_id=ad_group_id,
                    audience_id=audience_id,
                    bid=base_bid,
                )

        return results
