"""
History API (异步版本)
变更历史记录
"""

from ..base import BaseAdsClient, JSONData, JSONList


class HistoryAPI(BaseAdsClient):
    """History API (全异步)"""

    # ============ Change History ============

    async def get_change_history(
        self,
        start_date: str,
        end_date: str,
        entity_type: str | None = None,
        entity_id: str | None = None,
        change_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取变更历史
        
        Args:
            entity_type: CAMPAIGN | AD_GROUP | KEYWORD | TARGET | ...
            entity_id: 特定实体ID
            change_type: CREATE | UPDATE | DELETE | STATE_CHANGE
        """
        body: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
            "maxResults": max_results,
        }
        if entity_type:
            body["entityType"] = entity_type
        if entity_id:
            body["entityId"] = entity_id
        if change_type:
            body["changeType"] = change_type
        if next_token:
            body["nextToken"] = next_token

        result = await self.post("/history/changes", json_data=body)
        return result if isinstance(result, dict) else {"changes": []}

    # ============ Entity Snapshots ============

    async def get_entity_snapshot(
        self,
        entity_type: str,
        entity_id: str,
        snapshot_date: str,
    ) -> JSONData:
        """
        获取实体历史快照
        
        查看某个实体在特定日期的状态
        """
        result = await self.get(f"/history/snapshot/{entity_type}/{entity_id}", params={
            "snapshotDate": snapshot_date,
        })
        return result if isinstance(result, dict) else {}

    # ============ Bid History ============

    async def get_bid_history(
        self,
        entity_type: str,
        entity_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONList:
        """
        获取竞价变更历史
        
        Args:
            entity_type: KEYWORD | TARGET
            entity_id: 关键词或Target ID
        """
        result = await self.post("/history/bids", json_data={
            "entityType": entity_type,
            "entityId": entity_id,
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, list) else []

    # ============ Budget History ============

    async def get_budget_history(
        self,
        campaign_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONList:
        """获取预算变更历史"""
        result = await self.post("/history/budgets", json_data={
            "campaignId": campaign_id,
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, list) else []

    # ============ State History ============

    async def get_state_history(
        self,
        entity_type: str,
        entity_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONList:
        """
        获取状态变更历史
        
        追踪enabled/paused/archived状态变化
        """
        result = await self.post("/history/states", json_data={
            "entityType": entity_type,
            "entityId": entity_id,
            "startDate": start_date,
            "endDate": end_date,
        })
        return result if isinstance(result, list) else []

    # ============ Audit Log ============

    async def get_audit_log(
        self,
        start_date: str,
        end_date: str,
        user_id: str | None = None,
        action_type: str | None = None,
        max_results: int = 100,
    ) -> JSONData:
        """
        获取审计日志
        
        记录所有API操作
        
        Args:
            user_id: 筛选特定用户
            action_type: CREATE | UPDATE | DELETE | READ
        """
        body: JSONData = {
            "startDate": start_date,
            "endDate": end_date,
            "maxResults": max_results,
        }
        if user_id:
            body["userId"] = user_id
        if action_type:
            body["actionType"] = action_type

        result = await self.post("/history/audit", json_data=body)
        return result if isinstance(result, dict) else {"logs": []}

    # ============ 便捷方法 ============

    async def get_campaign_history(
        self,
        campaign_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取Campaign完整变更历史"""
        changes = await self.get_change_history(
            start_date=start_date,
            end_date=end_date,
            entity_type="CAMPAIGN",
            entity_id=campaign_id,
        )
        budget = await self.get_budget_history(campaign_id, start_date, end_date)
        state = await self.get_state_history("CAMPAIGN", campaign_id, start_date, end_date)

        return {
            "changes": changes.get("changes", []),
            "budgetHistory": budget,
            "stateHistory": state,
        }

    async def get_keyword_history(
        self,
        keyword_id: str,
        start_date: str,
        end_date: str,
    ) -> JSONData:
        """获取Keyword完整变更历史"""
        changes = await self.get_change_history(
            start_date=start_date,
            end_date=end_date,
            entity_type="KEYWORD",
            entity_id=keyword_id,
        )
        bids = await self.get_bid_history("KEYWORD", keyword_id, start_date, end_date)
        state = await self.get_state_history("KEYWORD", keyword_id, start_date, end_date)

        return {
            "changes": changes.get("changes", []),
            "bidHistory": bids,
            "stateHistory": state,
        }

    async def list_all_changes(
        self,
        start_date: str,
        end_date: str,
        entity_type: str | None = None,
    ) -> JSONList:
        """获取所有变更（自动分页）"""
        all_changes = []
        next_token = None

        while True:
            result = await self.get_change_history(
                start_date=start_date,
                end_date=end_date,
                entity_type=entity_type,
                max_results=100,
                next_token=next_token,
            )
            changes = result.get("changes", [])
            all_changes.extend(changes)

            next_token = result.get("nextToken")
            if not next_token:
                break

        return all_changes

    async def get_recent_changes(self, days: int = 7) -> JSONList:
        """获取最近N天的变更"""
        from datetime import datetime, timedelta

        end_date = datetime.now().strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        return await self.list_all_changes(start_date, end_date)
