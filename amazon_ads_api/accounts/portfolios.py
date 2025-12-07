"""
Portfolios API
广告组合管理（Campaign分组）
"""

from ..base import BaseAdsClient, JSONData, JSONList


class PortfoliosAPI(BaseAdsClient):
    """Portfolios API"""

    # ============ Portfolios ============

    def list_portfolios(self) -> JSONList:
        """
        获取Portfolio列表
        
        Portfolio用于将Campaign分组管理和预算控制
        """
        result = self.get("/v2/portfolios")
        return result if isinstance(result, list) else []

    def list_portfolios_extended(self) -> JSONList:
        """获取Portfolio列表（扩展信息）"""
        result = self.get("/v2/portfolios/extended")
        return result if isinstance(result, list) else []

    def get_portfolio(self, portfolio_id: str) -> JSONData:
        """获取单个Portfolio详情"""
        result = self.get(f"/v2/portfolios/{portfolio_id}")
        return result if isinstance(result, dict) else {}

    def get_portfolio_extended(self, portfolio_id: str) -> JSONData:
        """获取Portfolio详情（扩展信息）"""
        result = self.get(f"/v2/portfolios/extended/{portfolio_id}")
        return result if isinstance(result, dict) else {}

    def create_portfolios(self, portfolios: JSONList) -> JSONList:
        """
        批量创建Portfolio
        
        Args:
            portfolios: [
                {
                    "name": "Brand A Campaigns",
                    "budget": {
                        "amount": 1000.0,
                        "policy": "dateRange",  # dateRange | monthlyRecurring
                        "startDate": "20240101",
                        "endDate": "20241231"
                    },
                    "state": "enabled"
                }
            ]
        """
        result = self.post("/v2/portfolios", json_data=portfolios)
        return result if isinstance(result, list) else []

    def update_portfolios(self, portfolios: JSONList) -> JSONList:
        """
        批量更新Portfolio
        
        Args:
            portfolios: [{"portfolioId": "xxx", "name": "New Name", "state": "paused"}]
        """
        result = self.put("/v2/portfolios", json_data=portfolios)
        return result if isinstance(result, list) else []

    # ============ Budget Control ============

    def set_portfolio_budget(
        self,
        portfolio_id: str,
        amount: float,
        policy: str = "dateRange",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> JSONList:
        """
        设置Portfolio预算
        
        Args:
            amount: 预算金额
            policy: dateRange | monthlyRecurring
            start_date: YYYYMMDD（dateRange必填）
            end_date: YYYYMMDD（dateRange必填）
        """
        budget: JSONData = {
            "amount": amount,
            "policy": policy,
        }
        if policy == "dateRange":
            budget["startDate"] = start_date
            budget["endDate"] = end_date

        return self.update_portfolios([{
            "portfolioId": portfolio_id,
            "budget": budget,
        }])

    def remove_portfolio_budget(self, portfolio_id: str) -> JSONList:
        """移除Portfolio预算限制"""
        return self.update_portfolios([{
            "portfolioId": portfolio_id,
            "budget": None,
        }])

    # ============ 便捷方法 ============

    def pause_portfolio(self, portfolio_id: str) -> JSONList:
        """暂停Portfolio（会暂停其下所有Campaign）"""
        return self.update_portfolios([{"portfolioId": portfolio_id, "state": "paused"}])

    def enable_portfolio(self, portfolio_id: str) -> JSONList:
        """启用Portfolio"""
        return self.update_portfolios([{"portfolioId": portfolio_id, "state": "enabled"}])

    def rename_portfolio(self, portfolio_id: str, new_name: str) -> JSONList:
        """重命名Portfolio"""
        return self.update_portfolios([{"portfolioId": portfolio_id, "name": new_name}])

    def get_portfolio_by_name(self, name: str) -> JSONData | None:
        """根据名称获取Portfolio"""
        portfolios = self.list_portfolios()
        for portfolio in portfolios:
            if portfolio.get("name") == name:
                return portfolio
        return None

    def create_portfolio(
        self,
        name: str,
        budget_amount: float | None = None,
        budget_policy: str = "dateRange",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> JSONData:
        """
        创建单个Portfolio
        
        简化版创建方法
        """
        portfolio: JSONData = {
            "name": name,
            "state": "enabled",
        }

        if budget_amount:
            portfolio["budget"] = {
                "amount": budget_amount,
                "policy": budget_policy,
            }
            if budget_policy == "dateRange":
                portfolio["budget"]["startDate"] = start_date
                portfolio["budget"]["endDate"] = end_date

        result = self.create_portfolios([portfolio])
        return result[0] if result else {}

    def get_portfolio_campaigns(self, portfolio_id: str) -> JSONList:
        """
        获取Portfolio下的Campaign列表
        
        注意：需要从Campaign API过滤
        """
        # 这个方法需要调用SP/SB/SD的Campaign API
        # 这里返回空，实际使用时应该在上层服务中实现
        return []

