"""
Audience Insights API
受众洞察分析
"""

from ..base import BaseAdsClient, JSONData, JSONList


class AudienceInsightsAPI(BaseAdsClient):
    """Audience Insights API"""

    # ============ Audience Discovery ============

    def list_available_audiences(
        self,
        audience_type: str | None = None,
        marketplace: str = "US",
    ) -> JSONList:
        """
        获取可用受众列表
        
        Args:
            audience_type: IN_MARKET | LIFESTYLE | LIFE_EVENT | INTEREST
        """
        params: JSONData = {"marketplace": marketplace}
        if audience_type:
            params["audienceType"] = audience_type

        result = self.get("/insights/audiences", params=params)
        return result if isinstance(result, list) else []

    def get_audience(self, audience_id: str) -> JSONData:
        """获取受众详情"""
        result = self.get(f"/insights/audiences/{audience_id}")
        return result if isinstance(result, dict) else {}

    def search_audiences(
        self,
        query: str,
        marketplace: str = "US",
        max_results: int = 100,
    ) -> JSONList:
        """搜索受众"""
        result = self.post("/insights/audiences/search", json_data={
            "query": query,
            "marketplace": marketplace,
            "maxResults": max_results,
        })
        return result if isinstance(result, list) else []

    def get_audience_taxonomy(self, marketplace: str = "US") -> JSONData:
        """获取受众分类树"""
        result = self.get("/insights/audiences/taxonomy", params={
            "marketplace": marketplace
        })
        return result if isinstance(result, dict) else {}

    # ============ Audience Metrics ============

    def get_audience_size(
        self,
        audience_id: str,
        marketplace: str = "US",
    ) -> JSONData:
        """获取受众规模"""
        result = self.get(f"/insights/audiences/{audience_id}/size", params={
            "marketplace": marketplace
        })
        return result if isinstance(result, dict) else {}

    def estimate_combined_audience_size(
        self,
        audience_ids: list[str],
        combination_type: str = "UNION",
        marketplace: str = "US",
    ) -> JSONData:
        """
        估算组合受众规模
        
        Args:
            combination_type: UNION | INTERSECTION
        """
        result = self.post("/insights/audiences/estimateSize", json_data={
            "audienceIds": audience_ids,
            "combinationType": combination_type,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    def get_audience_demographics(
        self,
        audience_id: str,
        marketplace: str = "US",
    ) -> JSONData:
        """
        获取受众人口统计
        
        返回年龄、性别、收入等分布
        """
        result = self.get(f"/insights/audiences/{audience_id}/demographics", params={
            "marketplace": marketplace
        })
        return result if isinstance(result, dict) else {}

    def get_audience_behavior(
        self,
        audience_id: str,
        marketplace: str = "US",
    ) -> JSONData:
        """
        获取受众行为特征
        
        返回购买行为、浏览行为等
        """
        result = self.get(f"/insights/audiences/{audience_id}/behavior", params={
            "marketplace": marketplace
        })
        return result if isinstance(result, dict) else {}

    # ============ Audience Overlap ============

    def get_audience_overlap(
        self,
        audience_id_1: str,
        audience_id_2: str,
        marketplace: str = "US",
    ) -> JSONData:
        """获取两个受众的重叠度"""
        result = self.post("/insights/audiences/overlap", json_data={
            "audienceId1": audience_id_1,
            "audienceId2": audience_id_2,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    def get_audience_affinity(
        self,
        audience_id: str,
        marketplace: str = "US",
        limit: int = 20,
    ) -> JSONList:
        """
        获取受众亲和度
        
        返回与该受众高度相关的其他受众
        """
        result = self.get(f"/insights/audiences/{audience_id}/affinity", params={
            "marketplace": marketplace,
            "limit": limit,
        })
        return result if isinstance(result, list) else []

    # ============ Product-Audience Match ============

    def get_audience_recommendations_for_asin(
        self,
        asin: str,
        marketplace: str = "US",
        max_results: int = 20,
    ) -> JSONList:
        """基于ASIN获取受众推荐"""
        result = self.post("/insights/audiences/recommendationsForAsin", json_data={
            "asin": asin,
            "marketplace": marketplace,
            "maxResults": max_results,
        })
        return result if isinstance(result, list) else []

    def get_audience_recommendations_for_category(
        self,
        category_id: str,
        marketplace: str = "US",
        max_results: int = 20,
    ) -> JSONList:
        """基于品类获取受众推荐"""
        result = self.post("/insights/audiences/recommendationsForCategory", json_data={
            "categoryId": category_id,
            "marketplace": marketplace,
            "maxResults": max_results,
        })
        return result if isinstance(result, list) else []

    # ============ Audience Performance ============

    def get_audience_performance_benchmark(
        self,
        audience_id: str,
        ad_type: str = "SD",
        marketplace: str = "US",
    ) -> JSONData:
        """
        获取受众效果基准
        
        返回该受众的平均CTR、CVR、CPA等
        """
        result = self.get(f"/insights/audiences/{audience_id}/benchmark", params={
            "adType": ad_type,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    def get_top_performing_audiences(
        self,
        ad_type: str = "SD",
        marketplace: str = "US",
        metric: str = "CVR",
        limit: int = 20,
    ) -> JSONList:
        """
        获取效果最好的受众
        
        Args:
            metric: CTR | CVR | ROAS | CPA
        """
        result = self.get("/insights/audiences/topPerforming", params={
            "adType": ad_type,
            "marketplace": marketplace,
            "metric": metric,
            "limit": limit,
        })
        return result if isinstance(result, list) else []

    # ============ Custom Audience Analysis ============

    def analyze_custom_audience(
        self,
        definition: JSONData,
        marketplace: str = "US",
    ) -> JSONData:
        """
        分析自定义受众
        
        在创建前分析受众特征和规模
        """
        result = self.post("/insights/audiences/analyzeCustom", json_data={
            "definition": definition,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    def get_lookalike_audience_preview(
        self,
        seed_audience_id: str,
        expansion_level: int = 5,
        marketplace: str = "US",
    ) -> JSONData:
        """
        预览相似受众
        
        Args:
            expansion_level: 1-10, 数字越大受众越广但相似度越低
        """
        result = self.post("/insights/audiences/lookalikePreview", json_data={
            "seedAudienceId": seed_audience_id,
            "expansionLevel": expansion_level,
            "marketplace": marketplace,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    def get_audience_full_profile(
        self,
        audience_id: str,
        marketplace: str = "US",
    ) -> JSONData:
        """获取受众完整画像"""
        audience = self.get_audience(audience_id)
        size = self.get_audience_size(audience_id, marketplace)
        demographics = self.get_audience_demographics(audience_id, marketplace)
        behavior = self.get_audience_behavior(audience_id, marketplace)
        affinity = self.get_audience_affinity(audience_id, marketplace)

        return {
            "audience": audience,
            "size": size,
            "demographics": demographics,
            "behavior": behavior,
            "relatedAudiences": affinity,
        }

    def find_best_audiences_for_product(
        self,
        asin: str,
        marketplace: str = "US",
        limit: int = 10,
    ) -> JSONList:
        """为产品找到最佳受众"""
        recommendations = self.get_audience_recommendations_for_asin(asin, marketplace, limit * 2)
        
        # 获取每个受众的benchmark
        results = []
        for rec in recommendations[:limit]:
            audience_id = rec.get("audienceId")
            if not audience_id:
                continue

            benchmark = self.get_audience_performance_benchmark(audience_id, "SD", marketplace)
            results.append({
                **rec,
                "benchmark": benchmark,
            })

        return sorted(results, key=lambda x: x.get("benchmark", {}).get("cvr", 0), reverse=True)

    def get_in_market_audiences(self, marketplace: str = "US") -> JSONList:
        """获取所有In-Market受众"""
        return self.list_available_audiences("IN_MARKET", marketplace)

    def get_lifestyle_audiences(self, marketplace: str = "US") -> JSONList:
        """获取所有Lifestyle受众"""
        return self.list_available_audiences("LIFESTYLE", marketplace)

    def get_life_event_audiences(self, marketplace: str = "US") -> JSONList:
        """获取所有Life Event受众"""
        return self.list_available_audiences("LIFE_EVENT", marketplace)

