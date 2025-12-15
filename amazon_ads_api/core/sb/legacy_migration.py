"""
Sponsored Brands - Legacy Campaign Migration API (异步版本)
SB旧版Campaign迁移

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
"""

from amazon_ads_api.base import BaseAdsClient, JSONData


class SBLegacyMigrationAPI(BaseAdsClient):
    """SB Legacy Campaign Migration API (全异步)"""

    # ============ Migration Job ============

    async def create_migration_job(
        self,
        campaign_ids: list[str],
    ) -> JSONData:
        """
        创建旧版Campaign迁移任务
        
        Args:
            campaign_ids: 要迁移的旧版Campaign ID列表
        """
        result = await self.post(
            "/sb/v4/legacyCampaigns/migrationJob",
            json_data={"campaignIds": campaign_ids}
        )
        return result if isinstance(result, dict) else {}

    async def get_migration_job_status(
        self,
        job_id: str,
    ) -> JSONData:
        """
        获取迁移任务状态
        
        Args:
            job_id: 迁移任务ID
        """
        result = await self.post(
            "/sb/v4/legacyCampaigns/migrationJob/status",
            json_data={"jobId": job_id}
        )
        return result if isinstance(result, dict) else {}

    async def get_migration_job_results(
        self,
        job_id: str,
    ) -> JSONData:
        """
        获取迁移任务结果
        
        Args:
            job_id: 迁移任务ID
        """
        result = await self.post(
            "/sb/v4/legacyCampaigns/migrationJob/results",
            json_data={"jobId": job_id}
        )
        return result if isinstance(result, dict) else {"results": []}

    async def get_overall_migration_results(
        self,
        campaign_ids: list[str] | None = None,
    ) -> JSONData:
        """
        获取整体迁移结果统计
        
        Args:
            campaign_ids: 可选，过滤特定Campaign
        """
        body = {}
        if campaign_ids:
            body["campaignIds"] = campaign_ids

        result = await self.post(
            "/sb/v4/legacyCampaigns/overallMigrationResults",
            json_data=body or None
        )
        return result if isinstance(result, dict) else {"results": []}

    # ============ 便捷方法 ============

    async def migrate_and_wait(
        self,
        campaign_ids: list[str],
        max_wait_seconds: int = 300,
        poll_interval_seconds: int = 5,
    ) -> JSONData:
        """
        创建迁移任务并等待完成
        
        Args:
            campaign_ids: 要迁移的Campaign ID列表
            max_wait_seconds: 最大等待时间（秒）
            poll_interval_seconds: 轮询间隔（秒）
            
        Returns:
            迁移结果
        """
        import asyncio
        
        # 创建迁移任务
        job = await self.create_migration_job(campaign_ids)
        job_id = job.get("jobId")
        if not job_id:
            return {"error": "Failed to create migration job", "job": job}
        
        # 等待完成
        elapsed = 0
        while elapsed < max_wait_seconds:
            status = await self.get_migration_job_status(job_id)
            state = status.get("status", "").upper()
            
            if state == "COMPLETED":
                return await self.get_migration_job_results(job_id)
            elif state == "FAILED":
                return {"error": "Migration job failed", "status": status}
            
            await asyncio.sleep(poll_interval_seconds)
            elapsed += poll_interval_seconds
        
        return {"error": "Migration job timed out", "jobId": job_id}

