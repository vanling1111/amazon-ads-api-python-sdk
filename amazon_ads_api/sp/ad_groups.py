"""
Sponsored Products - Ad Groups API
SP广告组管理
"""

from ..base import BaseAdsClient, JSONData, JSONList


class SPAdGroupsAPI(BaseAdsClient):
    """SP Ad Groups API"""

    def list_ad_groups(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取Ad Group列表
        
        Args:
            campaign_id: 过滤特定Campaign
            state_filter: enabled, paused, archived
            max_results: 最大结果数
            next_token: 分页token
        """
        params: JSONData = {"maxResults": max_results}
        if campaign_id:
            params["campaignIdFilter"] = [campaign_id]
        if state_filter:
            params["stateFilter"] = state_filter
        if next_token:
            params["nextToken"] = next_token

        result = self.post("/sp/adGroups/list", json_data=params)
        return result if isinstance(result, dict) else {"adGroups": []}

    def get_ad_group(self, ad_group_id: str) -> JSONData:
        """获取单个Ad Group详情"""
        result = self.get(f"/sp/adGroups/{ad_group_id}")
        return result if isinstance(result, dict) else {}

    def create_ad_groups(self, ad_groups: JSONList) -> JSONData:
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
        result = self.post("/sp/adGroups", json_data={"adGroups": ad_groups})
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    def update_ad_groups(self, ad_groups: JSONList) -> JSONData:
        """
        批量更新Ad Group
        
        Args:
            ad_groups: 包含adGroupId的更新数据
            [{"adGroupId": "xxx", "state": "paused", "defaultBid": 1.5}]
        """
        result = self.put("/sp/adGroups", json_data={"adGroups": ad_groups})
        return result if isinstance(result, dict) else {"adGroups": {"success": [], "error": []}}

    def delete_ad_group(self, ad_group_id: str) -> JSONData:
        """归档Ad Group"""
        return self.delete(f"/sp/adGroups/{ad_group_id}")

    # ============ 便捷方法 ============

    def pause_ad_group(self, ad_group_id: str) -> JSONData:
        """暂停Ad Group"""
        return self.update_ad_groups([{"adGroupId": ad_group_id, "state": "paused"}])

    def enable_ad_group(self, ad_group_id: str) -> JSONData:
        """启用Ad Group"""
        return self.update_ad_groups([{"adGroupId": ad_group_id, "state": "enabled"}])

    def update_default_bid(self, ad_group_id: str, bid: float) -> JSONData:
        """更新Ad Group默认竞价"""
        return self.update_ad_groups([{"adGroupId": ad_group_id, "defaultBid": bid}])

    def list_all_ad_groups(
        self,
        campaign_id: str | None = None,
        state_filter: str | None = None,
    ) -> JSONList:
        """获取所有Ad Group（自动分页）"""
        all_ad_groups = []
        next_token = None

        while True:
            result = self.list_ad_groups(
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

