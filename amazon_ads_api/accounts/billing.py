"""
Amazon Ads Billing API (异步版本)
账单和支付管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class BillingAPI(BaseAdsClient):
    """Billing API (全异步)"""

    # ============ Invoices ============

    async def list_invoices(
        self,
        start_date: str,
        end_date: str,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取账单列表"""
        params: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
            "maxResults": max_results,
        }
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/billing/invoices", params=params)
        return result if isinstance(result, dict) else {"invoices": []}

    async def get_invoice(self, invoice_id: str) -> JSONData:
        """获取账单详情"""
        result = await self.get(f"/billing/invoices/{invoice_id}")
        return result if isinstance(result, dict) else {}

    async def download_invoice(self, invoice_id: str) -> JSONData:
        """下载账单PDF"""
        result = await self.get(f"/billing/invoices/{invoice_id}/document")
        return result if isinstance(result, dict) else {}

    # ============ Spend History ============

    async def get_spend_history(
        self,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> JSONData:
        """获取花费历史"""
        result = await self.get("/billing/spend", params={
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        })
        return result if isinstance(result, dict) else {"spend": []}

    async def get_spend_by_campaign(
        self,
        start_date: str,
        end_date: str,
        campaign_ids: list[str] | None = None,
    ) -> JSONData:
        """获取按Campaign分组的花费"""
        params: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
        }
        if campaign_ids:
            params["campaignIds"] = ",".join(campaign_ids)

        result = await self.get("/billing/spend/campaigns", params=params)
        return result if isinstance(result, dict) else {"spend": []}

    # ============ Payment Methods ============

    async def list_payment_methods(self) -> JSONList:
        """获取支付方式列表"""
        result = await self.get("/billing/paymentMethods")
        return result if isinstance(result, list) else []

    async def get_default_payment_method(self) -> JSONData:
        """获取默认支付方式"""
        result = await self.get("/billing/paymentMethods/default")
        return result if isinstance(result, dict) else {}

    async def set_default_payment_method(self, payment_method_id: str) -> JSONData:
        """设置默认支付方式"""
        result = await self.put("/billing/paymentMethods/default", json_data={
            "paymentMethodId": payment_method_id,
        })
        return result if isinstance(result, dict) else {}

    # ============ Account Balance ============

    async def get_account_balance(self) -> JSONData:
        """获取账户余额"""
        result = await self.get("/billing/balance")
        return result if isinstance(result, dict) else {}

    # ============ Budget Notifications ============

    async def get_budget_alerts(self) -> JSONList:
        """获取预算告警"""
        result = await self.get("/billing/alerts")
        return result if isinstance(result, list) else []

    async def create_budget_alert(
        self,
        threshold_amount: float,
        notification_email: str,
    ) -> JSONData:
        """创建预算告警"""
        result = await self.post("/billing/alerts", json_data={
            "thresholdAmount": threshold_amount,
            "notificationEmail": notification_email,
        })
        return result if isinstance(result, dict) else {}

    async def delete_budget_alert(self, alert_id: str) -> JSONData:
        """删除预算告警"""
        result = await self.delete(f"/billing/alerts/{alert_id}")
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def get_total_spend(self, start_date: str, end_date: str) -> float:
        """获取指定时间段总花费"""
        spend_data = await self.get_spend_history(start_date, end_date, "DAILY")
        spend_list = spend_data.get("spend", [])
        return sum(item.get("amount", 0) for item in spend_list)

    async def get_monthly_spend(self, year: int, month: int) -> float:
        """获取指定月份总花费"""
        start_date = f"{year}-{month:02d}-01"
        if month == 12:
            end_date = f"{year + 1}-01-01"
        else:
            end_date = f"{year}-{month + 1:02d}-01"

        return await self.get_total_spend(start_date, end_date)

    async def list_all_invoices(
        self,
        start_date: str,
        end_date: str,
    ) -> JSONList:
        """获取所有账单（自动分页）"""
        all_invoices: JSONList = []
        next_token = None

        while True:
            result = await self.list_invoices(
                start_date=start_date,
                end_date=end_date,
                max_results=100,
                next_token=next_token,
            )
            invoices = result.get("invoices", [])
            all_invoices.extend(invoices)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_invoices
