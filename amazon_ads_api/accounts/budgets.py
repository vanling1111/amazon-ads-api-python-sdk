"""
Amazon Ads Account Budgets API (异步版本)
账户预算管理
"""

from typing import Any
from ..base import BaseAdsClient, JSONData, JSONList


class AccountBudgetsAPI(BaseAdsClient):
    """Account Budgets API - 账户预算管理 (全异步)"""

    # ==================== 账户预算 ====================

    async def get_advertiser_budget(self, advertiser_id: str) -> JSONData:
        """获取广告商账户预算设置"""
        result = await self.get(f"/advertisers/{advertiser_id}/budget")
        return result if isinstance(result, dict) else {}

    async def update_advertiser_budget(
        self,
        advertiser_id: str,
        average_daily_budget: float,
        currency_code: str = "USD",
    ) -> JSONData:
        """更新广告商账户预算"""
        data = {
            "averageDailyBudget": {
                "amount": average_daily_budget,
                "currencyCode": currency_code,
            }
        }
        result = await self.put(f"/advertisers/{advertiser_id}/budget", json_data=data)
        return result if isinstance(result, dict) else {}

    async def get_budget_usage(
        self,
        advertiser_id: str,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> JSONData:
        """获取账户预算使用情况"""
        params: dict[str, Any] = {}
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        result = await self.get(
            f"/advertisers/{advertiser_id}/budget/usage",
            params=params if params else None,
        )
        return result if isinstance(result, dict) else {}

    async def get_budget_recommendations(self, advertiser_id: str) -> JSONData:
        """获取账户预算建议"""
        result = await self.get(f"/advertisers/{advertiser_id}/budget/recommendations")
        return result if isinstance(result, dict) else {}

    # ==================== 预算规则 ====================

    async def list_budget_rules(self, advertiser_id: str) -> JSONList:
        """获取账户预算规则列表"""
        response = await self.get(f"/advertisers/{advertiser_id}/budget/rules")
        if isinstance(response, dict):
            return response.get("rules", [])
        return []

    async def create_budget_rule(
        self,
        advertiser_id: str,
        rule_name: str,
        rule_type: str,
        budget_increase_percentage: float,
        conditions: dict[str, Any],
    ) -> JSONData:
        """创建账户预算规则"""
        data = {
            "name": rule_name,
            "ruleType": rule_type,
            "budgetIncreasePercentage": budget_increase_percentage,
            "conditions": conditions,
        }
        result = await self.post(
            f"/advertisers/{advertiser_id}/budget/rules", json_data=data
        )
        return result if isinstance(result, dict) else {}

    async def delete_budget_rule(
        self,
        advertiser_id: str,
        rule_id: str,
    ) -> JSONData:
        """删除账户预算规则"""
        result = await self.delete(
            f"/advertisers/{advertiser_id}/budget/rules/{rule_id}"
        )
        return result if isinstance(result, dict) else {}
