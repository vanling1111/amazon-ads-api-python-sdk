"""
Sponsored Products - Ad Groups API (异步版本)
SP广告组管理
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

# API v3 Content-Type
CONTENT_TYPE_AD_GROUP = "application/vnd.spAdGroup.v3+json"


class SPAdGroupsAPI(BaseAdsClient):
    """SP Ad Groups API (全异步)"""

    async def list_ad_groups(
        self,
        campaign_id: str | None = None,
        ad_group_ids: list[str] | None = None,
        state_filter: list[str] | str | None = None,
        name_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
        include_extended_data: bool = False,
    ) -> JSONData:
        """
        获取Ad Group列表
        
        Args:
            campaign_id: 过滤特定Campaign
            ad_group_ids: Ad Group ID过滤
            state_filter: 状态过滤 ["ENABLED", "PAUSED", "ARCHIVED"]
            name_filter: 名称过滤（模糊匹配）
            max_results: 最大结果数
            next_token: 分页token
            include_extended_data: 是否包含扩展字段
        """
        params: JSONData = {"maxResults": max_results}
        
        # ID过滤 - 官方格式: {"include": [...]}
        if campaign_id:
            params["campaignIdFilter"] = {"include": [campaign_id]}
        if ad_group_ids:
            params["adGroupIdFilter"] = {"include": ad_group_ids}
        
        # 状态过滤
        if state_filter:
            states = [state_filter] if isinstance(state_filter, str) else state_filter
            params["stateFilter"] = {"include": [s.upper() for s in states]}
        
        # 名称过滤
        if name_filter:
            params["nameFilter"] = {
                "queryTermMatchType": "BROAD_MATCH",
                "include": [name_filter]
            }
        
        if next_token:
            params["nextToken"] = next_token
        
        if include_extended_data:
            params["includeExtendedDataFields"] = True

        result = await self.post("/sp/adGroups/list", json_data=params, content_type=CONTENT_TYPE_AD_GROUP)
        return result if isinstance(result, dict) else {"adGroups": []}

    async def get_ad_group(self, ad_group_id: str) -> JSONData:
        """获取单个Ad Group详情"""
        result = await self.get(f"/sp/adGroups/{ad_group_id}", content_type=CONTENT_TYPE_AD_GROUP)
        return result if isinstance(result, dict) else {}

    async def create_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """
        批量创建Ad Group
        
        Args:
            ad_groups: Ad Group列表
            [
                {
                    "campaignId": "xxx",
                    "name": "My Ad Group",
                    "state": "enabled",
                    "defaultBid": 1.0
                }
            ]
        """
        result = await self.post("/sp/adGroups", json_data={"adGroups": ad_groups}, content_type=CONTENT_TYPE_AD_GROUP)
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    async def update_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """
        批量更新Ad Group
        
        Args:
            ad_groups: 包含adGroupId的更新数据
            [{"adGroupId": "xxx", "state": "paused", "defaultBid": 1.5}]
        """
        result = await self.put("/sp/adGroups", json_data={"adGroups": ad_groups}, content_type=CONTENT_TYPE_AD_GROUP)
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    async def delete_ad_groups(self, ad_group_ids: list[str]) -> JSONData:
        """
        批量归档Ad Group（官方 v3 /delete 端点）
        
        注意：Amazon Ads 不支持真正删除广告实体，此操作将 Ad Group 状态设置为 "archived"。
        
        Args:
            ad_group_ids: Ad Group ID列表
            
        Returns:
            {"adGroups": {"success": [...], "error": [...]}}
        """
        # 官方请求格式: {"adGroupIdFilter": {"include": [...]}}
        body = {"adGroupIdFilter": {"include": ad_group_ids}}
        result = await self.post("/sp/adGroups/delete", json_data=body, content_type=CONTENT_TYPE_AD_GROUP)
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    async def delete_ad_group(self, ad_group_id: str) -> JSONData:
        """归档单个Ad Group（状态变为 archived）"""
        return await self.delete_ad_groups([ad_group_id])
    
    # archive_ad_group 是 delete_ad_group 的别名
    async def archive_ad_group(self, ad_group_id: str) -> JSONData:
        """归档Ad Group（等同于 delete_ad_group）"""
        return await self.delete_ad_group(ad_group_id)

    # ============ 便捷方法 ============

    async def pause_ad_group(self, ad_group_id: str) -> JSONData:
        """暂停Ad Group"""
        return await self.update_ad_groups([{"adGroupId": ad_group_id, "state": "paused"}])

    async def enable_ad_group(self, ad_group_id: str) -> JSONData:
        """启用Ad Group"""
        return await self.update_ad_groups([{"adGroupId": ad_group_id, "state": "enabled"}])

    async def update_default_bid(self, ad_group_id: str, bid: float) -> JSONData:
        """更新Ad Group默认竞价"""
        return await self.update_ad_groups([{"adGroupId": ad_group_id, "defaultBid": bid}])

    async def list_all_ad_groups(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有Ad Group（自动分页）"""
        all_ad_groups = []
        next_token = None

        while True:
            result = await self.list_ad_groups(
                campaign_id=campaign_id,
                state_filter=state_filter,
                max_results=100,
                next_token=next_token,
            )
            ad_groups = result.get("adGroups", [])
            all_ad_groups.extend(ad_groups)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_ad_groups
