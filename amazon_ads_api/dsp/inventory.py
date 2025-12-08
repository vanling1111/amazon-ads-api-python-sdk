"""
Amazon DSP - Inventory API (异步版本)
DSP库存源和交易管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class DSPInventoryAPI(BaseAdsClient):
    """DSP Inventory API (全异步)"""

    # ============ Inventory Sources ============

    async def list_inventory_sources(
        self,
        advertiser_id: str,
        inventory_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取库存源列表"""
        params: JSONData = {
            "advertiserId": advertiser_id,
            "maxResults": max_results,
        }
        if inventory_type:
            params["inventoryType"] = inventory_type
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/dsp/inventory/sources", params=params)
        return result if isinstance(result, dict) else {"sources": []}

    async def get_inventory_source(
        self,
        source_id: str,
        advertiser_id: str,
    ) -> JSONData:
        """获取库存源详情"""
        result = await self.get(f"/dsp/inventory/sources/{source_id}", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    # ============ Deals (Private Marketplace) ============

    async def list_deals(
        self,
        advertiser_id: str,
        deal_type: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """获取Deal列表"""
        params: JSONData = {
            "advertiserId": advertiser_id,
            "maxResults": max_results,
        }
        if deal_type:
            params["dealType"] = deal_type
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = await self.get("/dsp/inventory/deals", params=params)
        return result if isinstance(result, dict) else {"deals": []}

    async def get_deal(self, deal_id: str, advertiser_id: str) -> JSONData:
        """获取Deal详情"""
        result = await self.get(f"/dsp/inventory/deals/{deal_id}", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, dict) else {}

    async def create_deal(
        self,
        advertiser_id: str,
        name: str,
        deal_type: str,
        publisher_id: str,
        floor_price: float,
        start_date: str,
        end_date: str,
        inventory_format: str | None = None,
    ) -> JSONData:
        """创建Deal"""
        body: JSONData = {
            "advertiserId": advertiser_id,
            "name": name,
            "dealType": deal_type,
            "publisherId": publisher_id,
            "floorPrice": floor_price,
            "startDate": start_date,
            "endDate": end_date,
        }
        if inventory_format:
            body["inventoryFormat"] = inventory_format

        result = await self.post("/dsp/inventory/deals", json_data=body)
        return result if isinstance(result, dict) else {}

    async def update_deal(
        self,
        deal_id: str,
        advertiser_id: str,
        updates: JSONData,
    ) -> JSONData:
        """更新Deal"""
        body = {"advertiserId": advertiser_id, **updates}
        result = await self.put(f"/dsp/inventory/deals/{deal_id}", json_data=body)
        return result if isinstance(result, dict) else {}

    async def delete_deal(self, deal_id: str, advertiser_id: str) -> JSONData:
        """删除Deal"""
        return await self.delete(f"/dsp/inventory/deals/{deal_id}?advertiserId={advertiser_id}")

    # ============ Deal Discovery ============

    async def discover_deals(
        self,
        advertiser_id: str,
        inventory_format: str | None = None,
        publisher_categories: list[str] | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """发现可用Deal"""
        body: JSONData = {
            "advertiserId": advertiser_id,
            "maxResults": max_results,
        }
        if inventory_format:
            body["inventoryFormat"] = inventory_format
        if publisher_categories:
            body["publisherCategories"] = publisher_categories

        result = await self.post("/dsp/inventory/deals/discover", json_data=body)
        return result if isinstance(result, dict) else {"deals": []}

    async def request_deal_access(
        self,
        deal_id: str,
        advertiser_id: str,
        message: str | None = None,
    ) -> JSONData:
        """请求访问Deal"""
        body: JSONData = {"advertiserId": advertiser_id}
        if message:
            body["message"] = message

        result = await self.post(f"/dsp/inventory/deals/{deal_id}/request", json_data=body)
        return result if isinstance(result, dict) else {}

    # ============ Supply Sources ============

    async def list_supply_sources(self, advertiser_id: str) -> JSONList:
        """获取供应源列表"""
        result = await self.get("/dsp/inventory/supplySources", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, list) else []

    async def get_supply_source_performance(
        self,
        source_id: str,
        advertiser_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取供应源效果数据"""
        result = await self.get(f"/dsp/inventory/supplySources/{source_id}/performance", params={
            "advertiserId": advertiser_id,
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ Domain Lists ============

    async def list_domain_lists(self, advertiser_id: str) -> JSONList:
        """获取域名列表（白名单/黑名单）"""
        result = await self.get("/dsp/inventory/domainLists", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, list) else []

    async def create_domain_list(
        self,
        advertiser_id: str,
        name: str,
        list_type: str,
        domains: list[str],
    ) -> JSONData:
        """创建域名列表"""
        result = await self.post("/dsp/inventory/domainLists", json_data={
            "advertiserId": advertiser_id,
            "name": name,
            "listType": list_type,
            "domains": domains,
        })
        return result if isinstance(result, dict) else {}

    async def update_domain_list(
        self,
        list_id: str,
        advertiser_id: str,
        domains: list[str],
        action: str = "ADD",
    ) -> JSONData:
        """更新域名列表"""
        result = await self.put(f"/dsp/inventory/domainLists/{list_id}", json_data={
            "advertiserId": advertiser_id,
            "domains": domains,
            "action": action,
        })
        return result if isinstance(result, dict) else {}

    async def delete_domain_list(self, list_id: str, advertiser_id: str) -> JSONData:
        """删除域名列表"""
        return await self.delete(
            f"/dsp/inventory/domainLists/{list_id}?advertiserId={advertiser_id}"
        )

    # ============ App Lists ============

    async def list_app_lists(self, advertiser_id: str) -> JSONList:
        """获取App列表"""
        result = await self.get("/dsp/inventory/appLists", params={
            "advertiserId": advertiser_id
        })
        return result if isinstance(result, list) else []

    async def create_app_list(
        self,
        advertiser_id: str,
        name: str,
        list_type: str,
        app_ids: list[str],
    ) -> JSONData:
        """创建App列表"""
        result = await self.post("/dsp/inventory/appLists", json_data={
            "advertiserId": advertiser_id,
            "name": name,
            "listType": list_type,
            "appIds": app_ids,
        })
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def list_all_deals(
        self,
        advertiser_id: str,
        deal_type: str | None = None,
    ) -> JSONList:
        """获取所有Deal（自动分页）"""
        all_deals = []
        next_token = None

        while True:
            result = await self.list_deals(
                advertiser_id=advertiser_id,
                deal_type=deal_type,
                max_results=100,
                next_token=next_token,
            )
            deals = result.get("deals", [])
            all_deals.extend(deals)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_deals

    async def get_active_deals(self, advertiser_id: str) -> JSONList:
        """获取所有活跃Deal"""
        all_deals = await self.list_all_deals(advertiser_id)
        return [deal for deal in all_deals if deal.get("state") == "ACTIVE"]

    async def create_whitelist(
        self,
        advertiser_id: str,
        name: str,
        domains: list[str],
    ) -> JSONData:
        """快速创建域名白名单"""
        return await self.create_domain_list(
            advertiser_id=advertiser_id,
            name=name,
            list_type="WHITELIST",
            domains=domains,
        )

    async def create_blacklist(
        self,
        advertiser_id: str,
        name: str,
        domains: list[str],
    ) -> JSONData:
        """快速创建域名黑名单"""
        return await self.create_domain_list(
            advertiser_id=advertiser_id,
            name=name,
            list_type="BLACKLIST",
            domains=domains,
        )
