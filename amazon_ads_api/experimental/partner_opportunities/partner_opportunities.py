"""
Amazon Ads Partner Opportunities API (异步版本)

官方 Spec: PartnerOpportunities.json
验证日期: 2024-12-15

官方端点数: 5
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class PartnerOpportunitiesAPI(BaseAdsClient):
    """
    Partner Opportunities API (全异步)
    
    API Tier: L1
    Source: OpenAPI
    OpenAPI_SPEC: PartnerOpportunities.json
    Stability: Beta
    
    用于管理合作伙伴机会，包括查询、申请和状态管理。
    官方验证: 5个端点
    """

    async def list_opportunities(
        self,
        status: str | None = None,
        opportunity_type: str | None = None,
        max_results: int = 100,
        next_token: str | None = None,
    ) -> JSONData:
        """
        获取合作伙伴机会列表
        
        官方端点: GET /partnerOpportunities
        
        Args:
            status: 状态过滤 (PENDING, APPROVED, REJECTED, EXPIRED)
            opportunity_type: 机会类型过滤
            max_results: 每页数量 (1-100)
            next_token: 分页令牌
            
        Returns:
            {
                "partnerOpportunities": [...],
                "nextToken": "..."
            }
        """
        params: dict[str, Any] = {"maxResults": max_results}
        
        if status:
            params["status"] = status
        if opportunity_type:
            params["opportunityType"] = opportunity_type
        if next_token:
            params["nextToken"] = next_token
        
        result = await self.get("/partnerOpportunities", params=params)
        return result if isinstance(result, dict) else {"partnerOpportunities": []}

    async def get_summary(self) -> JSONData:
        """
        获取合作伙伴机会摘要
        
        官方端点: GET /partnerOpportunities/summary
        
        Returns:
            {
                "totalOpportunities": 10,
                "pendingCount": 5,
                "approvedCount": 3,
                "rejectedCount": 2
            }
        """
        result = await self.get("/partnerOpportunities/summary")
        return result if isinstance(result, dict) else {}

    async def apply_for_opportunity(
        self,
        partner_opportunity_id: str,
        application_data: dict[str, Any],
    ) -> JSONData:
        """
        申请合作伙伴机会
        
        官方端点: POST /partnerOpportunities/{partnerOpportunityId}/apply
        
        Args:
            partner_opportunity_id: 机会 ID
            application_data: 申请数据
        """
        result = await self.post(
            f"/partnerOpportunities/{partner_opportunity_id}/apply",
            json_data=application_data,
        )
        return result if isinstance(result, dict) else {}

    async def update_application_status(
        self,
        partner_opportunity_id: str,
        status_data: dict[str, Any],
    ) -> JSONData:
        """
        更新申请状态
        
        官方端点: POST /partnerOpportunities/{partnerOpportunityId}/applicationStatus
        
        Args:
            partner_opportunity_id: 机会 ID
            status_data: 状态更新数据
        """
        result = await self.post(
            f"/partnerOpportunities/{partner_opportunity_id}/applicationStatus",
            json_data=status_data,
        )
        return result if isinstance(result, dict) else {}

    async def get_opportunity_file(
        self,
        partner_opportunity_id: str,
    ) -> JSONData:
        """
        获取机会相关文件
        
        官方端点: GET /partnerOpportunities/{partnerOpportunityId}/file
        
        Args:
            partner_opportunity_id: 机会 ID
            
        Returns:
            文件下载链接或文件内容
        """
        result = await self.get(
            f"/partnerOpportunities/{partner_opportunity_id}/file"
        )
        return result if isinstance(result, dict) else {}

    # ============ 便捷方法 ============

    async def list_all_opportunities(
        self,
        status: str | None = None,
    ) -> JSONList:
        """获取所有机会（自动分页）"""
        all_opportunities: JSONList = []
        next_token = None
        
        while True:
            result = await self.list_opportunities(
                status=status,
                max_results=100,
                next_token=next_token,
            )
            opportunities = result.get("partnerOpportunities", [])
            all_opportunities.extend(opportunities)
            
            next_token = result.get("nextToken")
            if not next_token:
                break
        
        return all_opportunities

    async def get_pending_opportunities(self) -> JSONList:
        """获取待处理的机会"""
        return await self.list_all_opportunities(status="PENDING")

    async def get_approved_opportunities(self) -> JSONList:
        """获取已批准的机会"""
        return await self.list_all_opportunities(status="APPROVED")

