"""
Amazon Ads Account Budgets API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/account-management/average-daily-budget
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Advertisers_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class AccountBudgetsAPI(BaseAdsClient):
    """Account Budgets API - 账户预算管理
    
    管理广告账户的平均每日预算设置。
    """
    
    # ==================== 账户预算 ====================
    
    async def get_advertiser_budget(
        self,
        advertiser_id: str,
    ) -> Dict[str, Any]:
        """获取广告商账户预算设置
        
        Args:
            advertiser_id: 广告商ID
            
        Returns:
            账户预算信息
        """
        return await self._make_request(
            "GET",
            f"/advertisers/{advertiser_id}/budget",
        )
    
    async def update_advertiser_budget(
        self,
        advertiser_id: str,
        average_daily_budget: float,
        currency_code: str = "USD",
    ) -> Dict[str, Any]:
        """更新广告商账户预算
        
        Args:
            advertiser_id: 广告商ID
            average_daily_budget: 平均每日预算金额
            currency_code: 货币代码
            
        Returns:
            更新后的预算信息
        """
        data = {
            "averageDailyBudget": {
                "amount": average_daily_budget,
                "currencyCode": currency_code,
            }
        }
        return await self._make_request(
            "PUT",
            f"/advertisers/{advertiser_id}/budget",
            json=data,
        )
    
    async def get_budget_usage(
        self,
        advertiser_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取账户预算使用情况
        
        Args:
            advertiser_id: 广告商ID
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            
        Returns:
            预算使用详情
        """
        params = {}
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
            
        return await self._make_request(
            "GET",
            f"/advertisers/{advertiser_id}/budget/usage",
            params=params if params else None,
        )
    
    async def get_budget_recommendations(
        self,
        advertiser_id: str,
    ) -> Dict[str, Any]:
        """获取账户预算建议
        
        Args:
            advertiser_id: 广告商ID
            
        Returns:
            预算建议
        """
        return await self._make_request(
            "GET",
            f"/advertisers/{advertiser_id}/budget/recommendations",
        )
    
    # ==================== 预算规则 ====================
    
    async def list_budget_rules(
        self,
        advertiser_id: str,
    ) -> List[Dict[str, Any]]:
        """获取账户预算规则列表
        
        Args:
            advertiser_id: 广告商ID
            
        Returns:
            预算规则列表
        """
        response = await self._make_request(
            "GET",
            f"/advertisers/{advertiser_id}/budget/rules",
        )
        return response.get("rules", [])
    
    async def create_budget_rule(
        self,
        advertiser_id: str,
        rule_name: str,
        rule_type: str,
        budget_increase_percentage: float,
        conditions: Dict[str, Any],
    ) -> Dict[str, Any]:
        """创建账户预算规则
        
        Args:
            advertiser_id: 广告商ID
            rule_name: 规则名称
            rule_type: 规则类型 (performance_based, schedule_based)
            budget_increase_percentage: 预算增加百分比
            conditions: 触发条件
            
        Returns:
            创建的规则
        """
        data = {
            "name": rule_name,
            "ruleType": rule_type,
            "budgetIncreasePercentage": budget_increase_percentage,
            "conditions": conditions,
        }
        return await self._make_request(
            "POST",
            f"/advertisers/{advertiser_id}/budget/rules",
            json=data,
        )
    
    async def delete_budget_rule(
        self,
        advertiser_id: str,
        rule_id: str,
    ) -> None:
        """删除账户预算规则
        
        Args:
            advertiser_id: 广告商ID
            rule_id: 规则ID
        """
        await self._make_request(
            "DELETE",
            f"/advertisers/{advertiser_id}/budget/rules/{rule_id}",
        )

