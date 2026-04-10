"""
Sponsored Display Campaigns API 单元测试

测试目标: amazon_ads_api/core/sd/campaigns.py
"""

import pytest
from unittest.mock import AsyncMock


class TestSDCampaignsAPI:
    """SD Campaigns API 单元测试"""

    @pytest.fixture
    def api(self):
        """创建 mock API 实例"""
        from amazon_ads_api.core.sd.campaigns import SDCampaignsAPI
        api = SDCampaignsAPI.__new__(SDCampaignsAPI)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.put = AsyncMock()
        api.delete = AsyncMock()
        return api

    # ==================== 创建测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_campaigns_success(self, api):
        """测试成功创建 SD campaigns"""
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "sd123", "index": 0}],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        campaigns = [{
            "name": "SD Test Campaign",
            "state": "PAUSED",
            "budget": 50.0,
            "budgetType": "daily",
            "costType": "cpc",
            "tactic": "T00020",
            "startDate": "2024-01-01"
        }]
        
        result = await api.create_campaigns(campaigns)
        
        assert result == mock_response
        api.post.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_campaigns_with_tactic(self, api):
        """测试不同 tactic 创建 SD campaign"""
        mock_response = {"campaigns": {"success": [{"campaignId": "sd1"}], "error": []}}
        api.post.return_value = mock_response
        
        # T00020 = 受众定向
        campaigns = [{
            "name": "Audience Campaign",
            "tactic": "T00020",
            "state": "PAUSED",
            "budget": 50.0
        }]
        
        result = await api.create_campaigns(campaigns)
        
        assert result["campaigns"]["success"][0]["campaignId"] == "sd1"

    # ==================== 更新测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_update_campaigns_budget(self, api):
        """测试更新 SD campaign 预算"""
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "sd1", "index": 0}],
                "error": []
            }
        }
        api.put.return_value = mock_response
        
        campaigns = [{"campaignId": "sd1", "budget": 100.0}]
        
        result = await api.update_campaigns(campaigns)
        
        assert result == mock_response

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_update_campaigns_state(self, api):
        """测试更新 SD campaign 状态"""
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "sd1"}],
                "error": []
            }
        }
        api.put.return_value = mock_response
        
        campaigns = [{"campaignId": "sd1", "state": "paused"}]
        
        result = await api.update_campaigns(campaigns)
        
        assert len(result["campaigns"]["success"]) == 1


class TestSDCampaignsAdGroups:
    """SD Ad Groups 相关测试"""

    @pytest.fixture
    def api(self):
        from amazon_ads_api.core.sd.campaigns import SDCampaignsAPI
        api = SDCampaignsAPI.__new__(SDCampaignsAPI)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.put = AsyncMock()
        api.delete = AsyncMock()
        return api

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_ad_groups(self, api):
        """测试创建 SD ad groups"""
        mock_response = {
            "adGroups": {
                "success": [{"adGroupId": "ag1", "index": 0}],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        ad_groups = [{
            "campaignId": "sd1",
            "name": "Test Ad Group",
            "state": "enabled",
            "defaultBid": 1.0
        }]
        
        result = await api.create_ad_groups(ad_groups)
        
        assert result == mock_response

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_ad_groups(self, api):
        """测试列出 SD ad groups"""
        mock_response = {
            "adGroups": [
                {"adGroupId": "ag1", "name": "Group 1"}
            ]
        }
        api.post.return_value = mock_response
        
        result = await api.list_ad_groups()
        
        assert "adGroups" in result
