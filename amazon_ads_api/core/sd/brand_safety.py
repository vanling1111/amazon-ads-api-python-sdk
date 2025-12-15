"""
Sponsored Display - Brand Safety API (异步版本)
SD品牌安全管理

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SDBrandSafetyAPI(BaseAdsClient):
    """SD Brand Safety API (全异步)"""

    # ============ Deny List ============

    async def list_deny_list(self) -> JSONData:
        """获取品牌安全拒绝列表"""
        result = await self.get("/sd/brandSafety/deny")
        return result if isinstance(result, dict) else {"denyList": []}

    async def add_to_deny_list(self, items: JSONList) -> JSONData:
        """
        添加到拒绝列表
        
        Args:
            items: [{"type": "DOMAIN", "value": "example.com"}, ...]
        """
        result = await self.post("/sd/brandSafety/deny", json_data={"items": items})
        return result if isinstance(result, dict) else {"success": [], "error": []}

    async def remove_from_deny_list(self, items: JSONList) -> JSONData:
        """
        从拒绝列表移除
        
        Args:
            items: [{"type": "DOMAIN", "value": "example.com"}, ...]
        """
        result = await self.delete("/sd/brandSafety/deny")
        return result if isinstance(result, dict) else {"success": [], "error": []}

    # ============ Status ============

    async def get_brand_safety_status(self) -> JSONData:
        """获取品牌安全状态"""
        result = await self.get("/sd/brandSafety/status")
        return result if isinstance(result, dict) else {}

    async def get_job_status(self, job_id: str) -> JSONData:
        """获取品牌安全任务状态"""
        result = await self.get(f"/sd/brandSafety/{job_id}/status")
        return result if isinstance(result, dict) else {}

    async def get_job_results(self, job_id: str) -> JSONData:
        """获取品牌安全任务结果"""
        result = await self.get(f"/sd/brandSafety/{job_id}/results")
        return result if isinstance(result, dict) else {"results": []}

