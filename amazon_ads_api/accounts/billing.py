"""
Billing API
账单和支付管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class BillingAPI(BaseAdsClient):
    """Billing API"""

    # ============ Invoices ============

    def list_invoices(
        self,
        start_date: str,
        end_date: str,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取账单列表
        
        Args:
            start_date: YYYY-MM-DD
            end_date: YYYY-MM-DD
        """
        params: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
            "maxResults": max_results,
        }
        if next_token:
            params["nextToken"] = next_token

        result = self.get("/billing/invoices", params=params)
        return result if isinstance(result, dict) else {"invoices": []}

    def get_invoice(self, invoice_id: str) -> JSONData:
        """获取账单详情"""
        result = self.get(f"/billing/invoices/{invoice_id}")
        return result if isinstance(result, dict) else {}

    def download_invoice(self, invoice_id: str) -> bytes:
        """下载账单PDF"""
        # 这个API返回二进制数据
        response = self.session.get(
            f"{self.base_url}/billing/invoices/{invoice_id}/document",
            headers=self._get_headers(),
            timeout=self.timeout,
        )
        return response.content if response.ok else b""

    # ============ Spend History ============

    def get_spend_history(
        self,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> JSONData:
        """
        获取花费历史
        
        Args:
            granularity: DAILY | MONTHLY
        """
        result = self.get("/billing/spend", params={
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        })
        return result if isinstance(result, dict) else {"spend": []}

    def get_spend_by_campaign(
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

        result = self.get("/billing/spend/campaigns", params=params)
        return result if isinstance(result, dict) else {"spend": []}

    # ============ Payment Methods ============

    def list_payment_methods(self) -> JSONList:
        """获取支付方式列表"""
        result = self.get("/billing/paymentMethods")
        return result if isinstance(result, list) else []

    def get_default_payment_method(self) -> JSONData:
        """获取默认支付方式"""
        result = self.get("/billing/paymentMethods/default")
        return result if isinstance(result, dict) else {}

    def set_default_payment_method(self, payment_method_id: str) -> JSONData:
        """设置默认支付方式"""
        result = self.put("/billing/paymentMethods/default", json_data={
            "paymentMethodId": payment_method_id,
        })
        return result if isinstance(result, dict) else {}

    # ============ Account Balance ============

    def get_account_balance(self) -> JSONData:
        """
        获取账户余额
        
        返回当前余额、信用额度等
        """
        result = self.get("/billing/balance")
        return result if isinstance(result, dict) else {}

    # ============ Budget Notifications ============

    def get_budget_alerts(self) -> JSONList:
        """获取预算告警"""
        result = self.get("/billing/alerts")
        return result if isinstance(result, list) else []

    def create_budget_alert(
        self,
        threshold_amount: float,
        notification_email: str,
    ) -> JSONData:
        """
        创建预算告警
        
        当花费达到阈值时发送邮件通知
        """
        result = self.post("/billing/alerts", json_data={
            "thresholdAmount": threshold_amount,
            "notificationEmail": notification_email,
        })
        return result if isinstance(result, dict) else {}

    def delete_budget_alert(self, alert_id: str) -> JSONData:
        """删除预算告警"""
        return self.delete(f"/billing/alerts/{alert_id}")

    # ============ 便捷方法 ============

    def get_total_spend(self, start_date: str, end_date: str) -> float:
        """获取指定时间段总花费"""
        spend_data = self.get_spend_history(start_date, end_date, "DAILY")
        spend_list = spend_data.get("spend", [])
        return sum(item.get("amount", 0) for item in spend_list)

    def get_monthly_spend(self, year: int, month: int) -> float:
        """获取指定月份总花费"""
        start_date = f"{year}-{month:02d}-01"
        if month == 12:
            end_date = f"{year + 1}-01-01"
        else:
            end_date = f"{year}-{month + 1:02d}-01"

        return self.get_total_spend(start_date, end_date)

    def list_all_invoices(
        self,
        start_date: str,
        end_date: str,
    ) -> JSONList:
        """获取所有账单（自动分页）"""
        all_invoices = []
        next_token = None

        while True:
            result = self.list_invoices(
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

