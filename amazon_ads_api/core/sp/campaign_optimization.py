"""
Sponsored Products - Campaign Optimization Rules API (异步版本)
SP广告优化规则管理

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/Campaign-Optimization-Rules
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

# API Content-Types
OPTIMIZATION_RULES_V1_CONTENT_TYPE = "application/vnd.spoptimizationrules.v1+json"
OPTIMIZATION_RULES_V2_CONTENT_TYPE = "application/vnd.spoptimizationrules.v2+json"
CAMPAIGN_OPTIMIZATION_CONTENT_TYPE = "application/vnd.optimizationrules.v1+json"


class SPCampaignOptimizationAPI(BaseAdsClient):
    """
    SP Campaign Optimization Rules API (全异步)
    
    允许创建基于时间或效果的竞价/预算自动优化规则。
    支持两种规则类型：
    - Schedule Rules: 基于时间调度的规则
    - Performance Rules: 基于效果指标的规则
    """

    # ============ Optimization Rules CRUD ============

    async def create_optimization_rules(self, optimization_rules: JSONList) -> JSONData:
        """
        创建优化规则
        
        官方端点: POST /sp/rules/optimization
        
        Args:
            optimization_rules: 规则列表
            [
                {
                    "ruleName": "Increase bids on weekends",
                    "ruleCategory": "BID",
                    "ruleSubCategory": "SCHEDULE",
                    "status": "ENABLED",
                    "recurrence": {
                        "type": "WEEKLY",
                        "daysOfWeek": ["SATURDAY", "SUNDAY"],
                        "timesOfDay": [{"startTime": "08:00", "endTime": "22:00"}],
                        "duration": {
                            "startTime": "2024-01-01T00:00:00Z"
                        }
                    },
                    "action": {
                        "actionType": "ADOPT",
                        "actionDetails": {
                            "actionOperator": "INCREMENT",
                            "actionUnit": "PERCENT",
                            "value": "20"
                        }
                    }
                }
            ]
        """
        result = await self.post(
            "/sp/rules/optimization",
            json_data={"optimizationRules": optimization_rules},
            content_type=OPTIMIZATION_RULES_V2_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"optimizationRules": {"success": [], "error": []}}

    async def update_optimization_rules(self, optimization_rules: JSONList) -> JSONData:
        """
        更新优化规则
        
        官方端点: PUT /sp/rules/optimization
        """
        result = await self.put(
            "/sp/rules/optimization",
            json_data={"optimizationRules": optimization_rules},
            content_type=OPTIMIZATION_RULES_V2_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"optimizationRules": {"success": [], "error": []}}

    async def search_optimization_rules(
        self,
        campaign_ids: list[str] | None = None,
        rule_ids: list[str] | None = None,
        rule_states: list[str] | None = None,
        page_size: int = 30,
        next_token: str | None = None,
    ) -> JSONData:
        """
        搜索优化规则
        
        官方端点: POST /sp/rules/optimization/search
        
        Args:
            campaign_ids: 按Campaign过滤
            rule_ids: 按规则ID过滤
            rule_states: 按状态过滤 ["ENABLED", "PAUSED", "DELETED"]
            page_size: 每页大小
            next_token: 分页token
        """
        body: JSONData = {"pageSize": page_size}
        
        filters = []
        if campaign_ids:
            filters.append({"field": "campaignId", "values": campaign_ids})
        if rule_ids:
            filters.append({"field": "ruleId", "values": rule_ids})
        if rule_states:
            filters.append({"field": "status", "values": rule_states})
        
        if filters:
            body["filters"] = filters
        if next_token:
            body["nextToken"] = next_token

        result = await self.post(
            "/sp/rules/optimization/search",
            json_data=body,
            content_type=OPTIMIZATION_RULES_V2_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"optimizationRules": []}

    # ============ Campaign Optimization Rules ============

    async def create_campaign_optimization_rules(
        self,
        rules: JSONList,
    ) -> JSONData:
        """
        创建Campaign优化规则
        
        官方端点: POST /sp/rules/campaignOptimization
        """
        result = await self.post(
            "/sp/rules/campaignOptimization",
            json_data={"campaignOptimizationRules": rules},
            content_type=CAMPAIGN_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"campaignOptimizationRules": {"success": [], "error": []}}

    async def update_campaign_optimization_rules(self, rules: JSONList) -> JSONData:
        """
        更新Campaign优化规则
        
        官方端点: PUT /sp/rules/campaignOptimization
        """
        result = await self.put(
            "/sp/rules/campaignOptimization",
            json_data={"campaignOptimizationRules": rules},
            content_type=CAMPAIGN_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"campaignOptimizationRules": {"success": [], "error": []}}

    async def get_campaign_optimization_rule(self, campaign_optimization_id: str) -> JSONData:
        """
        获取单个Campaign优化规则
        
        官方端点: GET /sp/rules/campaignOptimization/{campaignOptimizationId}
        """
        result = await self.get(
            f"/sp/rules/campaignOptimization/{campaign_optimization_id}",
            content_type=CAMPAIGN_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    async def delete_campaign_optimization_rule(self, campaign_optimization_id: str) -> JSONData:
        """
        删除Campaign优化规则
        
        官方端点: DELETE /sp/rules/campaignOptimization/{campaignOptimizationId}
        """
        result = await self.delete(
            f"/sp/rules/campaignOptimization/{campaign_optimization_id}",
            content_type=CAMPAIGN_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    async def check_campaign_optimization_eligibility(
        self,
        campaign_ids: list[str],
    ) -> JSONData:
        """
        检查Campaigns是否有资格使用优化规则
        
        官方端点: POST /sp/rules/campaignOptimization/eligibility
        """
        result = await self.post(
            "/sp/rules/campaignOptimization/eligibility",
            json_data={"campaignIds": campaign_ids},
            content_type=CAMPAIGN_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"eligibilityResults": []}

    async def update_campaign_optimization_state(
        self,
        updates: JSONList,
    ) -> JSONData:
        """
        批量更新Campaign优化规则状态
        
        官方端点: POST /sp/rules/campaignOptimization/state
        
        Args:
            updates: [
                {
                    "campaignOptimizationId": "xxx",
                    "state": "ENABLED"  # ENABLED | PAUSED
                }
            ]
        """
        result = await self.post(
            "/sp/rules/campaignOptimization/state",
            json_data={"stateUpdates": updates},
            content_type=CAMPAIGN_OPTIMIZATION_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"stateUpdates": {"success": [], "error": []}}

    async def associate_optimization_rules_to_campaign(
        self,
        campaign_id: str,
        rule_ids: list[str],
    ) -> JSONData:
        """
        将优化规则关联到Campaign
        
        官方端点: POST /sp/campaigns/{campaignId}/optimizationRules
        """
        result = await self.post(
            f"/sp/campaigns/{campaign_id}/optimizationRules",
            json_data={"ruleIds": rule_ids},
            content_type=OPTIMIZATION_RULES_V1_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"associations": {"success": [], "error": []}}

    # ============ 便捷方法 ============

    async def create_bid_schedule_rule(
        self,
        name: str,
        increase_percent: float,
        days_of_week: list[str],
        start_time: str = "00:00",
        end_time: str = "23:59",
        start_date: str | None = None,
    ) -> JSONData:
        """
        创建竞价调度规则
        
        Args:
            name: 规则名称
            increase_percent: 竞价增加百分比
            days_of_week: ["MONDAY", "TUESDAY", ...]
            start_time: 每天开始时间 HH:mm
            end_time: 每天结束时间 HH:mm
            start_date: 规则开始日期 (ISO 8601)
        """
        rule = {
            "ruleName": name,
            "ruleCategory": "BID",
            "ruleSubCategory": "SCHEDULE",
            "status": "ENABLED",
            "recurrence": {
                "type": "WEEKLY",
                "daysOfWeek": days_of_week,
                "timesOfDay": [{"startTime": start_time, "endTime": end_time}],
                "duration": {
                    "startTime": start_date or "2024-01-01T00:00:00Z"
                }
            },
            "action": {
                "actionType": "ADOPT",
                "actionDetails": {
                    "actionOperator": "INCREMENT",
                    "actionUnit": "PERCENT",
                    "value": str(increase_percent)
                }
            }
        }
        result = await self.create_optimization_rules([rule])
        success = result.get("optimizationRules", {}).get("success", [])
        return success[0] if success else {}

    async def create_bid_performance_rule(
        self,
        name: str,
        increase_percent: float,
        metric: str,
        comparison_operator: str,
        threshold: float,
        lookback_days: int = 14,
    ) -> JSONData:
        """
        创建基于效果的竞价规则
        
        Args:
            name: 规则名称
            increase_percent: 竞价调整百分比
            metric: CLICKS | CONVERSIONS | ROAS | ACOS
            comparison_operator: GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL_TO | LESS_THAN_OR_EQUAL_TO
            threshold: 阈值
            lookback_days: 回溯天数
        """
        rule = {
            "ruleName": name,
            "ruleCategory": "TARGETING",
            "ruleSubCategory": "PERFORMANCE",
            "status": "ENABLED",
            "targeting": [{
                "targetingType": "KEYWORD",
                "expressionTypes": ["BROAD", "PHRASE", "EXACT"],
                "lookbackDays": str(lookback_days)
            }],
            "conditions": [{
                "attributeName": metric,
                "criteria": {
                    "comparisonOperator": comparison_operator,
                    "value": str(threshold)
                }
            }],
            "action": {
                "actionType": "ADOPT",
                "actionDetails": {
                    "actionOperator": "INCREMENT",
                    "actionUnit": "PERCENT",
                    "value": str(increase_percent)
                }
            }
        }
        result = await self.create_optimization_rules([rule])
        success = result.get("optimizationRules", {}).get("success", [])
        return success[0] if success else {}

    async def pause_optimization_rule(self, rule_id: str) -> JSONData:
        """暂停优化规则"""
        return await self.update_optimization_rules([{
            "ruleId": rule_id,
            "status": "PAUSED"
        }])

    async def enable_optimization_rule(self, rule_id: str) -> JSONData:
        """启用优化规则"""
        return await self.update_optimization_rules([{
            "ruleId": rule_id,
            "status": "ENABLED"
        }])

    async def delete_optimization_rule(self, rule_id: str) -> JSONData:
        """删除优化规则"""
        return await self.update_optimization_rules([{
            "ruleId": rule_id,
            "status": "DELETED"
        }])

    async def list_all_optimization_rules(
        self,
        campaign_ids: list[str] | None = None,
    ) -> JSONList:
        """获取所有优化规则（自动分页）"""
        all_rules = []
        next_token = None

        while True:
            result = await self.search_optimization_rules(
                campaign_ids=campaign_ids,
                page_size=100,
                next_token=next_token
            )
            rules = result.get("optimizationRules", [])
            all_rules.extend(rules)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_rules

