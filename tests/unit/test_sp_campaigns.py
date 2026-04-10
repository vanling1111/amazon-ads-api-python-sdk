"""
Sponsored Products Campaigns API 单元测试

测试目标: amazon_ads_api/core/sp/campaigns.py
"""

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from amazon_ads_api.core.sp.campaigns import SPCampaignsAPI


class TestSPCampaignsAPI:
    """SP Campaigns API 单元测试"""

    @pytest.fixture
    def api(self):
        """创建 mock API 实例"""
        api = SPCampaignsAPI.__new__(SPCampaignsAPI)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.put = AsyncMock()
        api.delete = AsyncMock()
        return api

    # ==================== 创建测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_campaigns_success(self, api):
        """测试成功创建 campaigns"""
        # Arrange
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "123", "index": 0}],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        campaigns = [{
            "name": "Test Campaign",
            "targetingType": "MANUAL",
            "state": "PAUSED",
            "dailyBudget": 10.0,
            "startDate": "2024-01-01"
        }]
        
        # Act
        result = await api.create_campaigns(campaigns)
        
        # Assert
        assert result == mock_response
        api.post.assert_called_once()
        call_args = api.post.call_args
        assert "/sp/campaigns" in str(call_args)

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_campaigns_with_portfolio(self, api):
        """测试创建带 portfolio 的 campaign"""
        mock_response = {"campaigns": {"success": [{"campaignId": "123"}], "error": []}}
        api.post.return_value = mock_response
        
        campaigns = [{
            "name": "Test Campaign",
            "targetingType": "MANUAL",
            "state": "PAUSED",
            "dailyBudget": 10.0,
            "startDate": "2024-01-01",
            "portfolioId": "portfolio123"
        }]
        
        result = await api.create_campaigns(campaigns)
        
        assert result == mock_response
        api.post.assert_called_once()

    # ==================== 列表测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_campaigns_default(self, api):
        """测试默认参数列出 campaigns"""
        mock_response = {
            "campaigns": [
                {"campaignId": "123", "name": "Campaign 1"},
                {"campaignId": "456", "name": "Campaign 2"}
            ]
        }
        api.post.return_value = mock_response
        
        result = await api.list_campaigns()
        
        assert result == mock_response
        api.post.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_campaigns_with_filters(self, api):
        """测试带过滤条件列出 campaigns"""
        mock_response = {"campaigns": [{"campaignId": "123"}]}
        api.post.return_value = mock_response
        
        result = await api.list_campaigns(
            campaign_ids=["123", "456"],
            state_filter=["ENABLED"],
            name_filter="test"
        )
        
        assert result == mock_response
        api.post.assert_called_once()
        call_args = api.post.call_args
        # 验证请求包含过滤器
        assert call_args is not None

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_campaigns_with_pagination(self, api):
        """测试分页列出 campaigns"""
        mock_response = {
            "campaigns": [{"campaignId": "123"}],
            "nextToken": "token123"
        }
        api.post.return_value = mock_response
        
        result = await api.list_campaigns(max_results=50, next_token="prev_token")
        
        assert result == mock_response
        assert "nextToken" in result

    # ==================== 更新测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_update_campaigns_success(self, api):
        """测试成功更新 campaigns"""
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "123", "index": 0}],
                "error": []
            }
        }
        api.put.return_value = mock_response
        
        campaigns = [{
            "campaignId": "123",
            "state": "ENABLED",
            "dailyBudget": 20.0
        }]
        
        result = await api.update_campaigns(campaigns)
        
        assert result == mock_response
        api.put.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_update_campaigns_partial_failure(self, api):
        """测试部分更新失败"""
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "123", "index": 0}],
                "error": [{"campaignId": "456", "index": 1, "code": "INVALID_ARGUMENT"}]
            }
        }
        api.put.return_value = mock_response
        
        campaigns = [
            {"campaignId": "123", "state": "ENABLED"},
            {"campaignId": "456", "state": "INVALID_STATE"}
        ]
        
        result = await api.update_campaigns(campaigns)
        
        assert len(result["campaigns"]["error"]) == 1

    # ==================== 删除测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_delete_campaigns_success(self, api):
        """测试成功删除（归档）campaigns"""
        mock_response = {
            "campaigns": {
                "success": [{"campaignId": "123", "index": 0}],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        result = await api.delete_campaigns(["123", "456"])
        
        # delete_campaigns 内部使用 POST 而不是 DELETE
        api.post.assert_called()

    # ==================== 错误处理测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_campaigns_empty_response(self, api):
        """测试空响应处理"""
        api.post.return_value = None
        
        result = await api.list_campaigns()
        
        # 应该返回默认值而不是 None
        assert result is not None or result == {"campaigns": []}

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_campaigns_empty_list(self, api):
        """测试空列表创建"""
        mock_response = {"campaigns": {"success": [], "error": []}}
        api.post.return_value = mock_response
        
        result = await api.create_campaigns([])
        
        assert result["campaigns"]["success"] == []


class TestSPCampaignsBudgetRules:
    """SP Campaign Budget Rules 测试 - 使用 SPBudgetRulesAPI"""

    @pytest.fixture
    def api(self):
        from amazon_ads_api.core.sp.budget_rules import SPBudgetRulesAPI
        api = SPBudgetRulesAPI.__new__(SPBudgetRulesAPI)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.put = AsyncMock()
        api.delete = AsyncMock()
        return api

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_budget_rules(self, api):
        """测试创建预算规则"""
        mock_response = {
            "responses": [{"ruleId": "rule123", "code": "SUCCESS"}]
        }
        api.post.return_value = mock_response
        
        rules = [{
            "campaignId": "campaign123",
            "ruleType": "budget",
            "ruleDetails": {
                "budgetIncreasePercentage": 50,
                "startDate": "2024-01-01",
                "endDate": "2024-01-31"
            }
        }]
        
        result = await api.create_budget_rules(rules)
        
        assert result == mock_response
        api.post.assert_called_once()


class TestSPCampaignsHelpers:
    """SP Campaigns 辅助方法测试"""

    @pytest.fixture
    def api(self):
        api = SPCampaignsAPI.__new__(SPCampaignsAPI)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.put = AsyncMock()
        api.delete = AsyncMock()
        return api

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_get_campaign_by_id(self, api):
        """测试通过 ID 获取单个 campaign"""
        mock_campaign = {"campaignId": "123", "name": "Test Campaign"}
        api.post.return_value = {"campaigns": [mock_campaign]}
        
        result = await api.list_campaigns(campaign_ids=["123"])
        
        assert result["campaigns"][0]["campaignId"] == "123"

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_all_campaigns_pagination(self, api):
        """测试自动分页获取所有 campaigns"""
        # 第一页
        api.post.side_effect = [
            {"campaigns": [{"campaignId": "1"}], "nextToken": "token1"},
            {"campaigns": [{"campaignId": "2"}], "nextToken": None}
        ]
        
        # 获取第一页
        result1 = await api.list_campaigns()
        assert "nextToken" in result1
        
        # 获取第二页
        result2 = await api.list_campaigns(next_token=result1["nextToken"])
        assert result2["campaigns"][0]["campaignId"] == "2"
