"""
Sponsored Brands Campaigns API 单元测试

测试目标: amazon_ads_api/core/sb/campaigns.py
"""

import pytest
from unittest.mock import AsyncMock


class TestSBCampaignsAPI:
    """SB Campaigns API 单元测试"""

    @pytest.fixture
    def api(self):
        """创建 mock API 实例"""
        from amazon_ads_api.core.sb.campaigns import SBCampaignsAPI
        api = SBCampaignsAPI.__new__(SBCampaignsAPI)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.put = AsyncMock()
        api.delete = AsyncMock()
        return api

    # ==================== 创建测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_campaigns_success(self, api):
        """测试成功创建 SB campaigns"""
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "sb123", "index": 0}],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        campaigns = [{
            "name": "SB Test Campaign",
            "state": "paused",
            "budget": 100.0,
            "budgetType": "daily",
            "startDate": "2024-01-01",
            "brandEntityId": "ENTITY123"
        }]
        
        result = await api.create_campaigns(campaigns)
        
        assert result == mock_response
        api.post.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_campaigns_with_portfolio(self, api):
        """测试创建带 portfolio 的 SB campaign"""
        mock_response = {"campaigns": {"success": [{"campaignId": "sb1"}], "error": []}}
        api.post.return_value = mock_response
        
        campaigns = [{
            "name": "Portfolio Campaign",
            "portfolioId": "port123",
            "state": "paused",
            "budget": 100.0
        }]
        
        result = await api.create_campaigns(campaigns)
        
        assert result["campaigns"]["success"][0]["campaignId"] == "sb1"

    # ==================== 列表测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_campaigns_default(self, api):
        """测试默认参数列出 SB campaigns"""
        mock_response = {
            "campaigns": [
                {"campaignId": "sb1", "name": "Campaign 1"},
                {"campaignId": "sb2", "name": "Campaign 2"}
            ]
        }
        api.post.return_value = mock_response
        
        result = await api.list_campaigns()
        
        assert len(result["campaigns"]) == 2

    # ==================== 更新测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_update_campaigns_budget(self, api):
        """测试更新 SB campaign 预算"""
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "sb1", "index": 0}],
                "error": []
            }
        }
        api.put.return_value = mock_response
        
        campaigns = [{"campaignId": "sb1", "budget": 200.0}]
        
        result = await api.update_campaigns(campaigns)
        
        assert result == mock_response

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_update_campaigns_state(self, api):
        """测试更新 SB campaign 状态"""
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "sb1"}],
                "error": []
            }
        }
        api.put.return_value = mock_response
        
        campaigns = [{"campaignId": "sb1", "state": "enabled"}]
        
        result = await api.update_campaigns(campaigns)
        
        assert len(result["campaigns"]["success"]) == 1
