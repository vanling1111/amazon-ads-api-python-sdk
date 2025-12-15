"""
Portfolios API v3 (异步版本)
广告组合管理（Campaign分组）

重要更新：
- 使用 v3 API 端点
- List 操作改为 POST /portfolios/list
- Content-Type: application/vnd.spPortfolio.v3+json
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


# v3 API Content-Type
PORTFOLIO_CONTENT_TYPE = "application/vnd.spPortfolio.v3+json"
BUDGET_USAGE_CONTENT_TYPE = "application/vnd.portfoliobudgetusage.v1+json"


class PortfoliosAPI(BaseAdsClient):
    """Portfolios API v3 (全异步)"""

    # ============ Portfolios v3 ============

    async def list_portfolios(
        self,
        name_filter: str | None = None,
        portfolio_ids: list[str] | None = None,
        state_filter: str | None = None,
        include_extended: bool = False,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Portfolio列表 (v3 API)
        
        使用 POST /portfolios/list 端点
        
        Args:
            name_filter: 按名称过滤（支持模糊匹配）
            portfolio_ids: 按 ID 列表过滤
            state_filter: 按状态过滤 (enabled, paused, archived)
            include_extended: 是否包含扩展字段
            next_token: 分页 token
        
        Returns:
            {
                "portfolios": [...],
                "nextToken": "..."
            }
        """
        body: JSONData = {}
        
        if include_extended:
            body["includeExtendedDataFields"] = True
        
        if name_filter:
            body["nameFilter"] = {"queryTermMatchType": "BROAD_MATCH", "include": [name_filter]}
        
        if portfolio_ids:
            body["portfolioIdFilter"] = {"include": portfolio_ids}
        
        if state_filter:
            body["stateFilter"] = {"include": [state_filter.upper()]}
        
        if next_token:
            body["nextToken"] = next_token
        
        result = await self.post(
            "/portfolios/list",
            json_data=body,
            content_type=PORTFOLIO_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {"portfolios": []}

    async def list_all_portfolios(
        self,
        name_filter: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """
        获取所有Portfolio（自动处理分页）
        """
        all_portfolios: JSONList = []
        next_token = None
        
        while True:
            result = await self.list_portfolios(
                name_filter=name_filter,
                state_filter=state_filter,
                next_token=next_token,
            )
            portfolios = result.get("portfolios", [])
            all_portfolios.extend(portfolios)
            
            next_token = result.get("nextToken")
            if not next_token:
                break
        
        return all_portfolios

    async def get_portfolio(self, portfolio_id: str) -> JSONData:
        """
        获取单个Portfolio详情
        
        通过 list 接口过滤单个 ID
        """
        result = await self.list_portfolios(portfolio_ids=[portfolio_id])
        portfolios = result.get("portfolios", [])
        return portfolios[0] if portfolios else {}

    async def create_portfolios(self, portfolios: JSONList) -> JSONData:
        """
        批量创建Portfolio (v3 API)
        
        Args:
            portfolios: [
                {
                    "name": "Brand A Campaigns",
                    "budget": {
                        "amount": 1000.0,
                        "policy": "DATE_RANGE",  # DATE_RANGE | MONTHLY_RECURRING
                        "startDate": "2024-01-01",
                        "endDate": "2024-12-31"
                    },
                    "state": "ENABLED"
                }
            ]
        
        Returns:
            {
                "portfolios": {
                    "success": [...],
                    "error": [...]
                }
            }
        """
        result = await self.post(
            "/portfolios",
            json_data={"portfolios": portfolios},
            content_type=PORTFOLIO_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    async def update_portfolios(self, portfolios: JSONList) -> JSONData:
        """
        批量更新Portfolio (v3 API)
        
        Args:
            portfolios: [
                {
                    "portfolioId": "xxx",
                    "name": "New Name",
                    "state": "PAUSED"
                }
            ]
        """
        result = await self.put(
            "/portfolios",
            json_data={"portfolios": portfolios},
            content_type=PORTFOLIO_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    # ============ Budget Usage v3 ============

    async def get_budget_usage(self, portfolio_ids: list[str]) -> JSONData:
        """
        获取Portfolio预算使用情况
        
        Args:
            portfolio_ids: Portfolio ID 列表（最多100个）
        
        Returns:
            {
                "success": [...],
                "error": [...]
            }
        """
        result = await self.post(
            "/portfolios/budget/usage",
            json_data={"portfolioIds": portfolio_ids},
            content_type=BUDGET_USAGE_CONTENT_TYPE
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def set_portfolio_budget(
        self,
        portfolio_id: str,
        amount: float,
        policy: str = "DATE_RANGE",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> JSONData:
        """
        设置Portfolio预算
        
        Args:
            amount: 预算金额
            policy: DATE_RANGE | MONTHLY_RECURRING
            start_date: YYYY-MM-DD（DATE_RANGE必填）
            end_date: YYYY-MM-DD（DATE_RANGE必填）
        """
        budget: JSONData = {
            "amount": amount,
            "policy": policy,
        }
        if policy == "DATE_RANGE":
            budget["startDate"] = start_date
            budget["endDate"] = end_date

        return await self.update_portfolios([{
            "portfolioId": portfolio_id,
            "budget": budget,
        }])

    async def remove_portfolio_budget(self, portfolio_id: str) -> JSONData:
        """移除Portfolio预算限制"""
        return await self.update_portfolios([{
            "portfolioId": portfolio_id,
            "budget": None,
        }])

    async def pause_portfolio(self, portfolio_id: str) -> JSONData:
        """暂停Portfolio（会暂停其下所有Campaign）"""
        return await self.update_portfolios([{"portfolioId": portfolio_id, "state": "PAUSED"}])

    async def enable_portfolio(self, portfolio_id: str) -> JSONData:
        """启用Portfolio"""
        return await self.update_portfolios([{"portfolioId": portfolio_id, "state": "ENABLED"}])

    async def rename_portfolio(self, portfolio_id: str, new_name: str) -> JSONData:
        """重命名Portfolio"""
        return await self.update_portfolios([{"portfolioId": portfolio_id, "name": new_name}])

    async def get_portfolio_by_name(self, name: str) -> JSONData | None:
        """根据名称获取Portfolio"""
        result = await self.list_portfolios(name_filter=name)
        portfolios = result.get("portfolios", [])
        for portfolio in portfolios:
            if portfolio.get("name") == name:
                return portfolio
        return None

    async def create_portfolio(
        self,
        name: str,
        budget_amount: float | None = None,
        budget_policy: str = "DATE_RANGE",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> JSONData:
        """
        创建单个Portfolio（简化版）
        """
        portfolio: JSONData = {
            "name": name,
            "state": "ENABLED",
        }

        if budget_amount:
            portfolio["budget"] = {
                "amount": budget_amount,
                "policy": budget_policy,
            }
            if budget_policy == "DATE_RANGE":
                portfolio["budget"]["startDate"] = start_date
                portfolio["budget"]["endDate"] = end_date

        result = await self.create_portfolios([portfolio])
        success = result.get("portfolios", {}).get("success", [])
        return success[0] if success else {}

    # ============ 兼容 v2 API 的方法（已废弃）============
    
    async def list_portfolios_extended(self) -> JSONList:
        """
        [已废弃] 使用 list_portfolios(include_extended=True) 代替
        """
        result = await self.list_portfolios(include_extended=True)
        return result.get("portfolios", [])
    
    async def get_portfolio_extended(self, portfolio_id: str) -> JSONData:
        """
        [已废弃] 使用 get_portfolio() 代替，v3 API 默认包含扩展字段
        """
        return await self.get_portfolio(portfolio_id)
