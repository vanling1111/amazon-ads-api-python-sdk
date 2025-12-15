"""
Sponsored Display - Optimization Rules API (异步版本)
SD优化规则管理

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SDOptimizationAPI(BaseAdsClient):
    """SD Optimization Rules API (全异步)"""

    # ============ Optimization Rules CRUD ============

    async def list_optimization_rules(
        self,
        rule_ids: list[str] | None = None,
        states: list[str] | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """
        获取优化规则列表
        
        Args:
            rule_ids: 过滤的Rule ID列表
            states: 状态过滤 (ENABLED, PAUSED)
            max_results: 最大结果数
        """
        params: JSONData = {}
        if rule_ids:
            params["ruleIdFilter"] = ",".join(rule_ids)
        if states:
            params["stateFilter"] = ",".join(states)
        if max_results:
            params["count"] = max_results

        result = await self.get("/sd/optimizationRules", params=params or None)
        return result if isinstance(result, dict) else {"optimizationRules": []}

    async def get_optimization_rule(self, rule_id: str) -> JSONData:
        """获取单个优化规则详情"""
        result = await self.get(f"/sd/optimizationRules/{rule_id}")
        return result if isinstance(result, dict) else {}

    async def create_optimization_rules(self, rules: JSONList) -> JSONData:
        """
        批量创建优化规则
        
        Args:
            rules: [
                {
                    "name": "My Optimization Rule",
                    "ruleType": "BID_OPTIMIZATION",
                    "state": "ENABLED",
                    "conditions": {...},
                    "actions": {...}
                }
            ]
        """
        result = await self.post("/sd/optimizationRules", json_data={"optimizationRules": rules})
        return result if isinstance(result, dict) else {"optimizationRules": {"success": [], "error": []}}

    async def update_optimization_rules(self, rules: JSONList) -> JSONData:
        """批量更新优化规则"""
        result = await self.put("/sd/optimizationRules", json_data={"optimizationRules": rules})
        return result if isinstance(result, dict) else {"optimizationRules": {"success": [], "error": []}}

    # ============ Ad Group Optimization Rules ============

    async def list_ad_group_optimization_rules(self, ad_group_id: str) -> JSONData:
        """获取Ad Group关联的优化规则"""
        result = await self.get(f"/sd/adGroups/{ad_group_id}/optimizationRules")
        return result if isinstance(result, dict) else {"optimizationRules": []}

    async def associate_ad_group_optimization_rules(
        self, 
        ad_group_id: str, 
        rule_ids: list[str]
    ) -> JSONData:
        """将优化规则关联到Ad Group"""
        result = await self.post(
            f"/sd/adGroups/{ad_group_id}/optimizationRules",
            json_data={"optimizationRuleIds": rule_ids}
        )
        return result if isinstance(result, dict) else {"success": [], "error": []}

    async def disassociate_ad_group_optimization_rules(
        self, 
        ad_group_id: str, 
        rule_ids: list[str]
    ) -> JSONData:
        """从Ad Group移除优化规则关联"""
        result = await self.post(
            f"/sd/adGroups/{ad_group_id}/optimizationRules/disassociate",
            json_data={"optimizationRuleIds": rule_ids}
        )
        return result if isinstance(result, dict) else {"success": [], "error": []}

    # ============ 便捷方法 ============

    async def pause_rule(self, rule_id: str) -> JSONData:
        """暂停优化规则"""
        return await self.update_optimization_rules([{
            "optimizationRuleId": rule_id,
            "state": "PAUSED"
        }])

    async def enable_rule(self, rule_id: str) -> JSONData:
        """启用优化规则"""
        return await self.update_optimization_rules([{
            "optimizationRuleId": rule_id,
            "state": "ENABLED"
        }])

