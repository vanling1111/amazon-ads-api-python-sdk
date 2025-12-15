"""
Sponsored Products - Budget Rules API (异步版本)
SP预算规则管理

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/BudgetRules
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

# API Content-Types
BUDGET_RULES_V1_CONTENT_TYPE = "application/vnd.spbudgetrules.v1+json"


class SPBudgetRulesAPI(BaseAdsClient):
    """
    SP Budget Rules API (全异步)
    
    Budget Rules 允许你设置基于时间或效果的预算自动调整规则。
    """

    # ============ Budget Rules CRUD ============

    async def list_budget_rules(
        self,
        page_size: int = 30,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取所有Budget Rule列表
        
        官方端点: GET /sp/budgetRules
        
        Args:
            page_size: 每页结果数 (默认30，最大100)
            next_token: 分页token
        """
        params: JSONData = {"pageSize": page_size}
        if next_token:
            params["nextToken"] = next_token

        result = await self.get(
            "/sp/budgetRules", 
            params=params,
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"budgetRules": []}

    async def get_budget_rule(self, budget_rule_id: str) -> JSONData:
        """
        获取单个Budget Rule详情
        
        官方端点: GET /sp/budgetRules/{budgetRuleId}
        """
        result = await self.get(
            f"/sp/budgetRules/{budget_rule_id}",
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    async def create_budget_rules(self, budget_rules: JSONList) -> JSONData:
        """
        批量创建Budget Rule
        
        官方端点: POST /sp/budgetRules
        
        Args:
            budget_rules: Budget Rule 列表
            [
                {
                    "name": "Weekend Budget Boost",
                    "budgetRuleType": "schedule",  # schedule | performance
                    "ruleDetails": {
                        "budgetIncreaseBy": {
                            "type": "PERCENT",
                            "value": 20.0
                        },
                        "duration": {
                            "dateRangeTypeDuration": {
                                "startDate": "2024-01-01",
                                "endDate": "2024-12-31"
                            }
                        },
                        "recurrence": {
                            "daysOfWeek": ["SATURDAY", "SUNDAY"],
                            "type": "WEEKLY"
                        }
                    }
                }
            ]
        """
        result = await self.post(
            "/sp/budgetRules", 
            json_data={"budgetRules": budget_rules},
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"budgetRules": {"success": [], "error": []}}

    async def update_budget_rules(self, budget_rules: JSONList) -> JSONData:
        """
        批量更新Budget Rule
        
        官方端点: PUT /sp/budgetRules
        
        Args:
            budget_rules: 包含 budgetRuleId 的更新列表
            [
                {
                    "budgetRuleId": "xxx",
                    "name": "New Name",
                    "ruleState": "ACTIVE"  # ACTIVE | PAUSED
                }
            ]
        """
        result = await self.put(
            "/sp/budgetRules", 
            json_data={"budgetRules": budget_rules},
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"budgetRules": {"success": [], "error": []}}

    async def get_budget_rule_campaigns(self, budget_rule_id: str) -> JSONData:
        """
        获取Budget Rule关联的所有Campaigns
        
        官方端点: GET /sp/budgetRules/{budgetRuleId}/campaigns
        """
        result = await self.get(
            f"/sp/budgetRules/{budget_rule_id}/campaigns",
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"campaigns": []}

    # ============ Budget Rules Association ============

    async def associate_budget_rules(self, associations: JSONList) -> JSONData:
        """
        将Budget Rules关联到Campaigns
        
        官方端点: POST /sp/budgetRulesAssociation
        
        Args:
            associations: 关联列表
            [
                {
                    "budgetRuleId": "rule-123",
                    "campaignId": "campaign-456"
                }
            ]
        """
        result = await self.post(
            "/sp/budgetRulesAssociation", 
            json_data={"associations": associations},
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"associations": {"success": [], "error": []}}

    async def disassociate_budget_rules(self, associations: JSONList) -> JSONData:
        """
        删除Budget Rules与Campaigns的关联
        
        官方端点: POST /sp/budgetRulesAssociation/delete
        
        Args:
            associations: 要删除的关联列表
            [
                {
                    "budgetRuleId": "rule-123",
                    "campaignId": "campaign-456"
                }
            ]
        """
        result = await self.post(
            "/sp/budgetRulesAssociation/delete", 
            json_data={"associations": associations},
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"associations": {"success": [], "error": []}}

    # ============ Campaign Budget Rules ============

    async def get_campaign_budget_rules(
        self, 
        campaign_id: str,
        page_size: int = 30,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Campaign关联的所有Budget Rules
        
        官方端点: GET /sp/campaigns/{campaignId}/budgetRules
        """
        params: JSONData = {"pageSize": page_size}
        if next_token:
            params["nextToken"] = next_token

        result = await self.get(
            f"/sp/campaigns/{campaign_id}/budgetRules", 
            params=params,
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"budgetRules": []}

    async def associate_campaign_budget_rules(
        self, 
        campaign_id: str, 
        budget_rule_ids: list[str]
    ) -> JSONData:
        """
        将Budget Rules关联到特定Campaign
        
        官方端点: POST /sp/campaigns/{campaignId}/budgetRules
        """
        result = await self.post(
            f"/sp/campaigns/{campaign_id}/budgetRules", 
            json_data={"budgetRuleIds": budget_rule_ids},
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"budgetRules": {"success": [], "error": []}}

    async def delete_campaign_budget_rule(
        self, 
        campaign_id: str, 
        budget_rule_id: str
    ) -> JSONData:
        """
        从Campaign删除特定Budget Rule关联
        
        官方端点: DELETE /sp/campaigns/{campaignId}/budgetRules/{budgetRuleId}
        """
        result = await self.delete(
            f"/sp/campaigns/{campaign_id}/budgetRules/{budget_rule_id}",
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    # ============ Budget Usage & Recommendations ============

    async def get_budget_usage(self, campaign_ids: list[str]) -> JSONData:
        """
        获取Campaigns预算使用情况
        
        官方端点: POST /sp/campaigns/budget/usage
        
        Args:
            campaign_ids: Campaign ID列表
        """
        result = await self.post(
            "/sp/campaigns/budget/usage", 
            json_data={"campaignIds": campaign_ids}
        )
        return result if isinstance(result, dict) else {"budgetUsageList": []}

    async def get_budget_recommendations(self, campaign_ids: list[str]) -> JSONData:
        """
        获取Campaigns预算建议（批量）
        
        官方端点: POST /sp/campaigns/budgetRecommendations
        """
        result = await self.post(
            "/sp/campaigns/budgetRecommendations", 
            json_data={"campaignIds": campaign_ids}
        )
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_budget_rules_recommendations(
        self,
        campaign_ids: list[str] | None = None,
        page_size: int = 30,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Budget Rules建议
        
        官方端点: POST /sp/campaigns/budgetRules/recommendations
        
        根据Campaign历史表现推荐预算规则
        """
        body: JSONData = {"pageSize": page_size}
        if campaign_ids:
            body["campaignIds"] = campaign_ids
        if next_token:
            body["nextToken"] = next_token

        result = await self.post(
            "/sp/campaigns/budgetRules/recommendations", 
            json_data=body
        )
        return result if isinstance(result, dict) else {"recommendations": []}

    async def get_initial_budget_recommendation(
        self,
        daily_budget: float,
        targeting_type: str,
        asins: list[str] | None = None,
        keywords: list[str] | None = None,
    ) -> JSONData:
        """
        获取新Campaign预算建议
        
        官方端点: POST /sp/campaigns/initialBudgetRecommendation
        
        Args:
            daily_budget: 计划的日预算
            targeting_type: MANUAL | AUTO
            asins: 要推广的ASIN列表
            keywords: 关键词列表（手动定向时）
        """
        body: JSONData = {
            "dailyBudget": daily_budget,
            "targetingType": targeting_type,
        }
        if asins:
            body["asins"] = asins
        if keywords:
            body["keywords"] = keywords

        result = await self.post(
            "/sp/campaigns/initialBudgetRecommendation", 
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def create_schedule_rule(
        self,
        name: str,
        increase_percent: float,
        days_of_week: list[str],
        start_date: str,
        end_date: str | None = None,
    ) -> JSONData:
        """
        创建时间调度规则
        
        Args:
            name: 规则名称
            increase_percent: 预算增加百分比 (0-900)
            days_of_week: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
            start_date: 开始日期 YYYY-MM-DD
            end_date: 结束日期 YYYY-MM-DD (可选)
        """
        duration: JSONData = {"dateRangeTypeDuration": {"startDate": start_date}}
        if end_date:
            duration["dateRangeTypeDuration"]["endDate"] = end_date

        rules = [{
            "name": name,
            "budgetRuleType": "schedule",
            "ruleDetails": {
                "budgetIncreaseBy": {
                    "type": "PERCENT",
                    "value": increase_percent
                },
                "duration": duration,
                "recurrence": {
                    "daysOfWeek": days_of_week,
                    "type": "WEEKLY"
                }
            }
        }]
        result = await self.create_budget_rules(rules)
        success = result.get("budgetRules", {}).get("success", [])
        return success[0] if success else {}

    async def create_performance_rule(
        self,
        name: str,
        increase_percent: float,
        acos_threshold: float,
        start_date: str,
        end_date: str | None = None,
    ) -> JSONData:
        """
        创建效果触发规则
        
        Args:
            name: 规则名称
            increase_percent: 预算增加百分比
            acos_threshold: ACoS阈值（低于此值触发）
            start_date: 开始日期 YYYY-MM-DD
            end_date: 结束日期 YYYY-MM-DD (可选)
        """
        duration: JSONData = {"dateRangeTypeDuration": {"startDate": start_date}}
        if end_date:
            duration["dateRangeTypeDuration"]["endDate"] = end_date

        rules = [{
            "name": name,
            "budgetRuleType": "performance",
            "ruleDetails": {
                "budgetIncreaseBy": {
                    "type": "PERCENT",
                    "value": increase_percent
                },
                "duration": duration,
                "performanceCondition": {
                    "metricConditions": [{
                        "metric": "ACOS",
                        "comparisonOperator": "LESS_THAN",
                        "threshold": acos_threshold
                    }]
                }
            }
        }]
        result = await self.create_budget_rules(rules)
        success = result.get("budgetRules", {}).get("success", [])
        return success[0] if success else {}

    async def pause_rule(self, budget_rule_id: str) -> JSONData:
        """暂停Budget Rule"""
        return await self.update_budget_rules([{
            "budgetRuleId": budget_rule_id, 
            "ruleState": "PAUSED"
        }])

    async def activate_rule(self, budget_rule_id: str) -> JSONData:
        """激活Budget Rule"""
        return await self.update_budget_rules([{
            "budgetRuleId": budget_rule_id, 
            "ruleState": "ACTIVE"
        }])

    async def list_all_budget_rules(self) -> JSONList:
        """获取所有Budget Rules（自动分页）"""
        all_rules = []
        next_token = None

        while True:
            result = await self.list_budget_rules(page_size=100, next_token=next_token)
            rules = result.get("budgetRules", [])
            all_rules.extend(rules)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_rules

    # ============ Special Events ============

    async def get_rule_events(self, marketplace_id: str | None = None) -> JSONData:
        """
        获取所有特殊事件和日期范围建议
        
        官方端点: POST /sp/v1/events
        
        返回所有个别和分组的特殊事件（如黑五、Prime Day），
        以及在广告主市场中建议的日期范围。
        
        用于创建 EVENT_BASED 预算规则时选择事件。
        
        Args:
            marketplace_id: 市场ID（可选）
        """
        body: JSONData = {}
        if marketplace_id:
            body["marketplaceId"] = marketplace_id

        result = await self.post(
            "/sp/v1/events",
            json_data=body,
            content_type=BUDGET_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"events": []}
