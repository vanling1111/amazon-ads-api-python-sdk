"""
Sponsored Brands - Optimization Rules API (异步版本)
SB优化规则管理

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SBOptimizationAPI(BaseAdsClient):
    """SB Optimization Rules API (全异步)"""

    SB_OPTIMIZATION_CONTENT_TYPE = "application/vnd.sboptimizationrules.v1+json"

    # ============ Optimization Rules CRUD ============

    async def list_optimization_rules(
        self,
        campaign_ids: list[str] | None = None,
        rule_ids: list[str] | None = None,
        states: list[str] | str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取优化规则列表
        
        Args:
            campaign_ids: 过滤的Campaign ID列表
            rule_ids: 过滤的Rule ID列表
            states: 状态过滤 ["ENABLED", "PAUSED"]
            max_results: 最大结果数
            next_token: 分页token
        """
        body: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if campaign_ids:
            body["campaignIdFilter"] = {"include": campaign_ids}
        if rule_ids:
            body["ruleIdFilter"] = {"include": rule_ids}
        
        # 状态过滤
        if states:
            state_list = [states] if isinstance(states, str) else states
            body["stateFilter"] = {"include": [s.upper() for s in state_list]}
        
        if next_token:
            body["nextToken"] = next_token

        result = await self.post(
            "/sb/rules/optimization/list",
            json_data=body,
            content_type=self.SB_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"rules": []}

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
        result = await self.post(
            "/sb/rules/optimization",
            json_data={"rules": rules},
            content_type=self.SB_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"rules": {"success": [], "error": []}}

    async def update_optimization_rules(self, rules: JSONList) -> JSONData:
        """
        批量更新优化规则
        
        Args:
            rules: [{"ruleId": "xxx", "state": "PAUSED", ...}]
        """
        result = await self.put(
            "/sb/rules/optimization",
            json_data={"rules": rules},
            content_type=self.SB_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"rules": {"success": [], "error": []}}

    # ============ Rule-Campaign Association ============

    async def associate_rules_to_campaigns(
        self, 
        associations: list[dict[str, str]]
    ) -> JSONData:
        """
        将优化规则关联到Campaign
        
        Args:
            associations: [{"ruleId": "xxx", "campaignId": "yyy"}, ...]
        """
        result = await self.post(
            "/sb/rules/optimization/associate",
            json_data={"associations": associations},
            content_type=self.SB_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"success": [], "error": []}

    async def disassociate_rules_from_campaigns(
        self, 
        associations: list[dict[str, str]]
    ) -> JSONData:
        """
        从Campaign移除优化规则关联
        
        Args:
            associations: [{"ruleId": "xxx", "campaignId": "yyy"}, ...]
        """
        result = await self.post(
            "/sb/rules/optimization/disassociate",
            json_data={"associations": associations},
            content_type=self.SB_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"success": [], "error": []}

    # ============ Recommendations ============

    async def get_optimization_recommendations(
        self,
        campaign_ids: list[str],
        recommendation_types: list[str] | None = None,
    ) -> JSONData:
        """
        获取优化建议
        
        Args:
            campaign_ids: Campaign ID列表
            recommendation_types: 建议类型过滤
        """
        body: JSONData = {"campaignIds": campaign_ids}
        if recommendation_types:
            body["recommendationTypes"] = recommendation_types

        result = await self.post(
            "/sb/recommendations/optimization",
            json_data=body
        )
        return result if isinstance(result, dict) else {"recommendations": []}

    # ============ 便捷方法 ============

    async def pause_rule(self, rule_id: str) -> JSONData:
        """暂停优化规则"""
        return await self.update_optimization_rules([{
            "ruleId": rule_id,
            "state": "PAUSED"
        }])

    async def enable_rule(self, rule_id: str) -> JSONData:
        """启用优化规则"""
        return await self.update_optimization_rules([{
            "ruleId": rule_id,
            "state": "ENABLED"
        }])

    async def list_all_optimization_rules(
        self, 
        campaign_ids: list[str] | None = None
    ) -> JSONList:
        """获取所有优化规则（自动分页）"""
        all_rules = []
        next_token = None

        while True:
            result = await self.list_optimization_rules(
                campaign_ids=campaign_ids,
                max_results=100,
                next_token=next_token
            )
            rules = result.get("rules", [])
            all_rules.extend(rules)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_rules

