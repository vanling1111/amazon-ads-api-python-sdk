"""
Sponsored Products - Budget Rules API (异步版本)
SP预算规则管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SPBudgetRulesAPI(BaseAdsClient):
    """SP Budget Rules API (全异步)"""

    # ============ Budget Rules ============

    async def list_budget_rules(
        self,
        campaign_id: str | None = None,
        rule_state: str | None = None,
    ) -> JSONList:
        """
        获取Budget Rule列表
        
        Args:
            campaign_id: 过滤特定Campaign
            rule_state: ACTIVE, PAUSED
        """
        params: JSONData = {}
        if campaign_id:
            params["campaignIdFilter"] = campaign_id
        if rule_state:
            params["ruleState"] = rule_state

        result = await self.get("/sp/campaigns/budgetRules", params=params or None)
        return result if isinstance(result, list) else []

    async def get_budget_rule(self, rule_id: str) -> JSONData:
        """获取单个Budget Rule详情"""
        result = await self.get(f"/sp/campaigns/budgetRules/{rule_id}")
        return result if isinstance(result, dict) else {}

    async def create_budget_rules(self, rules: JSONList) -> JSONList:
        """
        批量创建Budget Rule
        
        Args:
            rules: [
                {
                    "campaignId": "xxx",
                    "name": "Weekend Budget Boost",
                    "ruleType": "schedule",  # schedule | performance
                    "budget": {
                        "budgetIncreaseBy": {"type": "percent", "value": 20}
                    },
                    "scheduleCondition": {
                        "schedule": [
                            {"dayOfWeek": "SATURDAY"},
                            {"dayOfWeek": "SUNDAY"}
                        ]
                    }
                }
            ]
        """
        result = await self.post("/sp/campaigns/budgetRules", json_data=rules)
        return result if isinstance(result, list) else []

    async def update_budget_rules(self, rules: JSONList) -> JSONList:
        """
        批量更新Budget Rule
        
        Args:
            rules: [{"ruleId": "xxx", "ruleState": "PAUSED"}]
        """
        result = await self.put("/sp/campaigns/budgetRules", json_data=rules)
        return result if isinstance(result, list) else []

    async def delete_budget_rule(self, rule_id: str) -> JSONData:
        """删除Budget Rule"""
        return await self.delete(f"/sp/campaigns/budgetRules/{rule_id}")

    # ============ Budget Rule Recommendations ============

    async def get_budget_rule_recommendations(self, campaign_id: str) -> JSONList:
        """
        获取Budget Rule建议
        
        根据Campaign历史表现推荐预算规则
        """
        result = await self.get(f"/sp/campaigns/{campaign_id}/budgetRules/recommendations")
        return result if isinstance(result, list) else []

    # ============ Budget Usage ============

    async def get_budget_usage(self, campaign_ids: list[str]) -> JSONList:
        """
        获取预算使用情况
        
        Args:
            campaign_ids: Campaign ID列表
            
        Returns:
            预算使用详情列表
        """
        result = await self.post("/sp/campaigns/budget/usage", json_data={"campaignIds": campaign_ids})
        return result if isinstance(result, list) else []

    # ============ Budget Recommendations ============

    async def get_budget_recommendations_for_new_campaign(
        self,
        daily_budget: float,
        targeting_type: str,
        asins: list[str],
    ) -> JSONData:
        """
        获取新Campaign预算建议
        
        Args:
            daily_budget: 计划的日预算
            targeting_type: MANUAL | AUTO
            asins: 要推广的ASIN列表
        """
        result = await self.post("/sp/campaigns/initialBudgetRecommendation", json_data={
            "dailyBudget": daily_budget,
            "targetingType": targeting_type,
            "asins": asins,
        })
        return result if isinstance(result, dict) else {}

    async def get_budget_recommendations(self, campaign_id: str) -> JSONData:
        """
        获取现有Campaign预算建议
        
        基于Campaign表现给出预算优化建议
        """
        result = await self.get(f"/sp/campaigns/{campaign_id}/budgetRecommendations")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def create_schedule_rule(
        self,
        campaign_id: str,
        name: str,
        increase_percent: float,
        days_of_week: list[str],
    ) -> JSONData:
        """
        创建时间调度规则
        
        Args:
            campaign_id: Campaign ID
            name: 规则名称
            increase_percent: 预算增加百分比
            days_of_week: ["MONDAY", "TUESDAY", ...]
        """
        rules = [{
            "campaignId": campaign_id,
            "name": name,
            "ruleType": "schedule",
            "budget": {
                "budgetIncreaseBy": {"type": "percent", "value": increase_percent}
            },
            "scheduleCondition": {
                "schedule": [{"dayOfWeek": day} for day in days_of_week]
            }
        }]
        result = await self.create_budget_rules(rules)
        return result[0] if result else {}

    async def create_performance_rule(
        self,
        campaign_id: str,
        name: str,
        increase_percent: float,
        acos_threshold: float,
    ) -> JSONData:
        """
        创建效果触发规则
        
        Args:
            campaign_id: Campaign ID
            name: 规则名称
            increase_percent: 预算增加百分比
            acos_threshold: ACoS阈值（低于此值触发）
        """
        rules = [{
            "campaignId": campaign_id,
            "name": name,
            "ruleType": "performance",
            "budget": {
                "budgetIncreaseBy": {"type": "percent", "value": increase_percent}
            },
            "performanceCondition": {
                "metricConditions": [{
                    "metric": "ACOS",
                    "comparisonOperator": "LESS_THAN",
                    "threshold": acos_threshold
                }]
            }
        }]
        result = await self.create_budget_rules(rules)
        return result[0] if result else {}

    async def pause_rule(self, rule_id: str) -> JSONList:
        """暂停Budget Rule"""
        return await self.update_budget_rules([{"ruleId": rule_id, "ruleState": "PAUSED"}])

    async def activate_rule(self, rule_id: str) -> JSONList:
        """激活Budget Rule"""
        return await self.update_budget_rules([{"ruleId": rule_id, "ruleState": "ACTIVE"}])
