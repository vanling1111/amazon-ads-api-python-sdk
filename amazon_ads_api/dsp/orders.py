"""
Amazon DSP - Orders API (异步版本)
DSP订单管理（Campaign级别）
"""

from ..base import BaseAdsClient, JSONData, JSONList


class DSPOrdersAPI(BaseAdsClient):
    """DSP Orders API (全异步)"""

    # ============ Orders (Campaigns) ============

    async def list_orders(
        self,
        advertiser_id: str,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Order列表"""
        params: JSONData = {
            "advertiserId": advertiser_id,
            "maxResults": max_results,
        }
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/dsp/orders", params=params)
        return result if isinstance(result, dict) else {"orders": []}

    async def get_order(self, order_id: str, advertiser_id: str) -> JSONData:
        """获取单个Order详情"""
        result = await self.get(f"/dsp/orders/{order_id}", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    async def create_order(
        self,
        advertiser_id: str,
        name: str,
        budget: float,
        start_date: str,
        end_date: str,
        budget_type: str = "LIFETIME",
        goal: str = "AWARENESS",
        frequency_cap: JSONData | None = None,
    ) -> JSONData:
        """创建Order"""
        body: JSONData = {
            "advertiserId": advertiser_id,
            "name": name,
            "budget": budget,
            "budgetType": budget_type,
            "startDate": start_date,
            "endDate": end_date,
            "goal": goal,
        }
        if frequency_cap:
            body["frequencyCap"] = frequency_cap

        result = await self.post("/dsp/orders", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_order(
        self,
        order_id: str,
        advertiser_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新Order"""
        body = {"advertiserId": advertiser_id, **updates}
        result = await self.put(f"/dsp/orders/{order_id}", json_data=body)
        return result if isinstance(result, dict) else {}

    async def delete_order(self, order_id: str, advertiser_id: str) -> JSONData:
        """删除Order"""
        return await self.delete(f"/dsp/orders/{order_id}?advertiserId={advertiser_id}")

    # ============ Order Budget ============

    async def get_order_budget_usage(
        self,
        order_id: str,
        advertiser_id: str,
    ) -> JSONData:
        """获取Order预算使用情况"""
        result = await self.get(f"/dsp/orders/{order_id}/budget", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    async def update_order_budget(
        self,
        order_id: str,
        advertiser_id: str,
        budget: float,
        budget_type: str | None = None,
    ) -> JSONData:
        """更新Order预算"""
        body: JSONData = {
            "advertiserId": advertiser_id,
            "budget": budget,
        }
        if budget_type:
            body["budgetType"] = budget_type

        result = await self.put(f"/dsp/orders/{order_id}/budget", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Order Pacing ============

    async def get_order_pacing(self, order_id: str, advertiser_id: str) -> JSONData:
        """获取Order投放节奏"""
        result = await self.get(f"/dsp/orders/{order_id}/pacing", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    async def update_order_pacing(
        self,
        order_id: str,
        advertiser_id: str,
        pacing_type: str,
        daily_budget: float | None = None,
    ) -> JSONData:
        """更新Order投放节奏"""
        body: JSONData = {
            "advertiserId": advertiser_id,
            "pacingType": pacing_type,
        }
        if daily_budget:
            body["dailyBudget"] = daily_budget

        result = await self.put(f"/dsp/orders/{order_id}/pacing", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Order Performance ============

    async def get_order_performance(
        self,
        order_id: str,
        advertiser_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取Order效果数据"""
        result = await self.get(f"/dsp/orders/{order_id}/performance", params={
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def pause_order(self, order_id: str, advertiser_id: str) -> JSONData:
        """暂停Order"""
        return await self.update_order(order_id, advertiser_id, {"state": "PAUSED"})

    async def resume_order(self, order_id: str, advertiser_id: str) -> JSONData:
        """恢复Order"""
        return await self.update_order(order_id, advertiser_id, {"state": "DELIVERING"})

    async def list_all_orders(
        self,
        advertiser_id: str,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有Order（自动分页）"""
        all_orders = []
        next_token = None

        while True:
            result = await self.list_orders(
                advertiser_id=advertiser_id,
                state_filter=state_filter,
                max_results=100,
                next_token=next_token,
            )
            orders = result.get("orders", [])
            all_orders.extend(orders)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_orders

    async def get_active_orders(self, advertiser_id: str) -> JSONList:
        """获取所有活跃Order"""
        return await self.list_all_orders(advertiser_id, state_filter="DELIVERING")
