"""
Amazon DSP - Line Items API (异步版本)
DSP广告行项目管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class DSPLineItemsAPI(BaseAdsClient):
    """DSP Line Items API (全异步)"""

    # ============ Line Items ============

    async def list_line_items(
        self,
        advertiser_id: str,
        order_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Line Item列表"""
        params: JSONData = {
            "advertiserId": advertiser_id,
            "maxResults": max_results,
        }
        if order_id:
            params["orderId"] = order_id
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/dsp/lineItems", params=params)
        return result if isinstance(result, dict) else {"lineItems": []}

    async def get_line_item(self, line_item_id: str, advertiser_id: str) -> JSONData:
        """获取单个Line Item详情"""
        result = await self.get(f"/dsp/lineItems/{line_item_id}", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    async def create_line_item(
        self,
        advertiser_id: str,
        order_id: str,
        name: str,
        line_item_type: str,
        budget: float,
        bid: float,
        start_date: str,
        end_date: str,
        targeting: JSONData | None = None,
        creative_ids: list[str] | None = None,
    ) -> JSONData:
        """创建Line Item"""
        body: JSONData = {
            "advertiserId": advertiser_id,
            "orderId": order_id,
            "name": name,
            "lineItemType": line_item_type,
            "budget": budget,
            "bid": bid,
            "startDate": start_date,
            "endDate": end_date,
        }
        if targeting:
            body["targeting"] = targeting
        if creative_ids:
            body["creativeIds"] = creative_ids

        result = await self.post("/dsp/lineItems", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_line_item(
        self,
        line_item_id: str,
        advertiser_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新Line Item"""
        body = {"advertiserId": advertiser_id, **updates}
        result = await self.put(f"/dsp/lineItems/{line_item_id}", json_data=body)
        return result if isinstance(result, dict) else {}

    async def delete_line_item(self, line_item_id: str, advertiser_id: str) -> JSONData:
        """删除Line Item"""
        return await self.delete(f"/dsp/lineItems/{line_item_id}?advertiserId={advertiser_id}")

    # ============ Line Item Targeting ============

    async def get_line_item_targeting(
        self,
        line_item_id: str,
        advertiser_id: str,
    ) -> JSONData:
        """获取Line Item定向设置"""
        result = await self.get(f"/dsp/lineItems/{line_item_id}/targeting", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    async def update_line_item_targeting(
        self,
        line_item_id: str,
        advertiser_id: str,
        targeting: JSONData,
    ) -> JSONData:
        """更新Line Item定向"""
        body = {"advertiserId": advertiser_id, "targeting": targeting}
        result = await self.put(f"/dsp/lineItems/{line_item_id}/targeting", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Line Item Bid ============

    async def get_line_item_bid(self, line_item_id: str, advertiser_id: str) -> JSONData:
        """获取Line Item竞价设置"""
        result = await self.get(f"/dsp/lineItems/{line_item_id}/bid", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    async def update_line_item_bid(
        self,
        line_item_id: str,
        advertiser_id: str,
        bid: float,
        bid_type: str = "CPM",
        optimization_goal: str | None = None,
    ) -> JSONData:
        """更新Line Item竞价"""
        body: JSONData = {
            "advertiserId": advertiser_id,
            "bid": bid,
            "bidType": bid_type,
        }
        if optimization_goal:
            body["optimizationGoal"] = optimization_goal

        result = await self.put(f"/dsp/lineItems/{line_item_id}/bid", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Line Item Creatives ============

    async def get_line_item_creatives(
        self,
        line_item_id: str,
        advertiser_id: str,
    ) -> JSONList:
        """获取Line Item关联的创意"""
        result = await self.get(f"/dsp/lineItems/{line_item_id}/creatives", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, list) else []

    async def associate_creatives(
        self,
        line_item_id: str,
        advertiser_id: str,
        creative_ids: list[str],
    ) -> JSONData:
        """关联创意到Line Item"""
        result = await self.post(f"/dsp/lineItems/{line_item_id}/creatives", json_data={
            "advertiserId": advertiser_id,
            "creativeIds": creative_ids,
        })
        return result if isinstance(result, dict) else {}

    async def remove_creative(
        self,
        line_item_id: str,
        creative_id: str,
        advertiser_id: str,
    ) -> JSONData:
        """从Line Item移除创意"""
        return await self.delete(
            f"/dsp/lineItems/{line_item_id}/creatives/{creative_id}"
            f"?advertiserId={advertiser_id}"
        )

    # ============ Line Item Performance ============

    async def get_line_item_performance(
        self,
        line_item_id: str,
        advertiser_id: str,
        start_date: str,
        end_date: str,
        granularity: str = "DAILY",
    ) -> JSONData:
        """获取Line Item效果数据"""
        result = await self.get(f"/dsp/lineItems/{line_item_id}/performance", params={
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        })
        return result if isinstance(result, dict) else {}

    # ============ Line Item Forecast ============

    async def get_line_item_forecast(
        self,
        advertiser_id: str,
        line_item_type: str,
        targeting: JSONData,
        budget: float,
        bid: float,
    ) -> JSONData:
        """获取Line Item预测"""
        result = await self.post("/dsp/lineItems/forecast", json_data={
            "advertiserId": advertiser_id,
            "lineItemType": line_item_type,
            "targeting": targeting,
            "budget": budget,
            "bid": bid,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def pause_line_item(self, line_item_id: str, advertiser_id: str) -> JSONData:
        """暂停Line Item"""
        return await self.update_line_item(line_item_id, advertiser_id, {"state": "PAUSED"})

    async def resume_line_item(self, line_item_id: str, advertiser_id: str) -> JSONData:
        """恢复Line Item"""
        return await self.update_line_item(line_item_id, advertiser_id, {"state": "DELIVERING"})

    async def list_all_line_items(
        self,
        advertiser_id: str,
        order_id: str | None = None,
    ) -> JSONList:
        """获取所有Line Item（自动分页）"""
        all_items = []
        next_token = None

        while True:
            result = await self.list_line_items(
                advertiser_id=advertiser_id,
                order_id=order_id,
                max_results=100,
                next_token=next_token,
            )
            items = result.get("lineItems", [])
            all_items.extend(items)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_items

    async def create_display_line_item(
        self,
        advertiser_id: str,
        order_id: str,
        name: str,
        budget: float,
        cpm_bid: float,
        audiences: list[str],
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """快速创建展示广告Line Item"""
        return await self.create_line_item(
            advertiser_id=advertiser_id,
            order_id=order_id,
            name=name,
            line_item_type="DISPLAY",
            budget=budget,
            bid=cpm_bid,
            start_date=start_date,
            end_date=end_date,
            targeting={"audiences": audiences},
        )

    async def create_video_line_item(
        self,
        advertiser_id: str,
        order_id: str,
        name: str,
        budget: float,
        cpm_bid: float,
        audiences: list[str],
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """快速创建视频广告Line Item"""
        return await self.create_line_item(
            advertiser_id=advertiser_id,
            order_id=order_id,
            name=name,
            line_item_type="VIDEO",
            budget=budget,
            bid=cpm_bid,
            start_date=start_date,
            end_date=end_date,
            targeting={"audiences": audiences},
        )
