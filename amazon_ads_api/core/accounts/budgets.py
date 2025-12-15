"""
Amazon Ads Account Budget Feature Flags API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/account-management/average-daily-budget
OpenAPI Spec: Advertisers_prod_3p.json

账户预算功能标志管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData


# Content-Type 常量
FEATURE_FLAGS_CONTENT_TYPE = "application/vnd.accountBudgetFeatureFlags.v1+json"


class AccountBudgetsAPI(BaseAdsClient):
    """
    Account Budget Feature Flags API (全异步)
    
    官方端点 (共2个):
    - GET /accountBudgets/featureFlags - 获取功能标志
    - POST /accountBudgets/featureFlags - 更新功能标志
    
    注意：此 API 用于管理账户预算功能标志，而非直接管理预算金额。
    账户预算金额通过 Profiles API 的 dailyBudget 字段管理。
    """

    async def get_feature_flags(self) -> JSONData:
        """
        获取账户预算功能标志
        
        GET /accountBudgets/featureFlags
        
        Returns:
            {
                "featureFlags": {
                    "isOptedOutForAverageDailyBudgetIncrease": bool
                }
            }
            
        功能说明:
            isOptedOutForAverageDailyBudgetIncrease:
            - true: 选择退出，每日预算最多增加 25%
            - false: 选择加入，每日预算最多增加 100%
            
            如果实体支出少于每日预算，未使用的金额可用于
            在当月其他日子增加每日预算。
        """
        result = await self.get(
            "/accountBudgets/featureFlags",
            accept=FEATURE_FLAGS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    async def update_feature_flags(
        self,
        is_opted_out_for_average_daily_budget_increase: bool,
    ) -> JSONData:
        """
        更新账户预算功能标志
        
        POST /accountBudgets/featureFlags
        
        Args:
            is_opted_out_for_average_daily_budget_increase:
                - True: 选择退出，限制每日预算增加为最多 25%
                - False: 选择加入，允许每日预算增加为最多 100%
        
        Returns:
            {
                "code": "OK",
                "details": "Successfully updated account budget feature flags"
            }
        """
        body = {
            "featureFlags": {
                "isOptedOutForAverageDailyBudgetIncrease": is_opted_out_for_average_daily_budget_increase
            }
        }
        result = await self.post(
            "/accountBudgets/featureFlags",
            json_data=body,
            content_type=FEATURE_FLAGS_CONTENT_TYPE,
            accept=FEATURE_FLAGS_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def opt_in_budget_increase(self) -> JSONData:
        """
        选择加入每日预算增加功能
        
        允许每日预算最多增加 100%（使用未花费的预算）
        """
        return await self.update_feature_flags(
            is_opted_out_for_average_daily_budget_increase=False
        )

    async def opt_out_budget_increase(self) -> JSONData:
        """
        选择退出每日预算增加功能
        
        限制每日预算最多增加 25%
        """
        return await self.update_feature_flags(
            is_opted_out_for_average_daily_budget_increase=True
        )

    async def is_opted_out(self) -> bool:
        """检查是否已选择退出预算增加功能"""
        result = await self.get_feature_flags()
        flags = result.get("featureFlags", {})
        return flags.get("isOptedOutForAverageDailyBudgetIncrease", False)
