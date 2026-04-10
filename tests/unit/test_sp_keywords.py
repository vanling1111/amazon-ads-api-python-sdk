"""
Sponsored Products Keywords API 单元测试

测试目标: amazon_ads_api/core/sp/keywords.py
"""

import pytest
from unittest.mock import AsyncMock


class TestSPKeywordsAPI:
    """SP Keywords API 单元测试"""

    @pytest.fixture
    def api(self):
        """创建 mock API 实例"""
        from amazon_ads_api.core.sp.keywords import SPKeywordsAPI
        api = SPKeywordsAPI.__new__(SPKeywordsAPI)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.put = AsyncMock()
        api.delete = AsyncMock()
        return api

    # ==================== 创建测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_keywords_success(self, api):
        """测试成功创建 keywords"""
        mock_response = {
            "keywords": {
                "success": [{"keywordId": "kw123", "index": 0}],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        keywords = [{
            "campaignId": "camp123",
            "adGroupId": "ag123",
            "keywordText": "test keyword",
            "matchType": "BROAD",
            "bid": 0.75,
            "state": "ENABLED"
        }]
        
        result = await api.create_keywords(keywords)
        
        assert result == mock_response
        api.post.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_keywords_multiple(self, api):
        """测试批量创建 keywords"""
        mock_response = {
            "keywords": {
                "success": [
                    {"keywordId": "kw1", "index": 0},
                    {"keywordId": "kw2", "index": 1}
                ],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        keywords = [
            {"campaignId": "c1", "adGroupId": "a1", "keywordText": "kw1", "matchType": "BROAD"},
            {"campaignId": "c1", "adGroupId": "a1", "keywordText": "kw2", "matchType": "EXACT"}
        ]
        
        result = await api.create_keywords(keywords)
        
        assert len(result["keywords"]["success"]) == 2

    # ==================== 列表测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_keywords_default(self, api):
        """测试默认参数列出 keywords"""
        mock_response = {
            "keywords": [
                {"keywordId": "kw1", "keywordText": "test1"},
                {"keywordId": "kw2", "keywordText": "test2"}
            ]
        }
        api.post.return_value = mock_response
        
        result = await api.list_keywords()
        
        assert result == mock_response
        api.post.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_keywords_by_campaign(self, api):
        """测试按 campaign 过滤 keywords"""
        mock_response = {"keywords": [{"keywordId": "kw1", "campaignId": "camp123"}]}
        api.post.return_value = mock_response
        
        result = await api.list_keywords(campaign_id="camp123")
        
        assert result["keywords"][0]["campaignId"] == "camp123"

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_keywords_by_state(self, api):
        """测试按 state 过滤 keywords"""
        mock_response = {"keywords": [{"keywordId": "kw1", "state": "ENABLED"}]}
        api.post.return_value = mock_response
        
        result = await api.list_keywords(state_filter=["ENABLED"])
        
        assert result["keywords"][0]["state"] == "ENABLED"

    # ==================== 更新测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_update_keywords_bid(self, api):
        """测试更新 keyword bid"""
        mock_response = {
            "keywords": {
                "success": [{"keywordId": "kw123", "index": 0}],
                "error": []
            }
        }
        api.put.return_value = mock_response
        
        keywords = [{"keywordId": "kw123", "bid": 1.50}]
        
        result = await api.update_keywords(keywords)
        
        assert result == mock_response

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_update_keywords_state(self, api):
        """测试更新 keyword state"""
        mock_response = {
            "keywords": {
                "success": [{"keywordId": "kw123", "index": 0}],
                "error": []
            }
        }
        api.put.return_value = mock_response
        
        keywords = [{"keywordId": "kw123", "state": "PAUSED"}]
        
        result = await api.update_keywords(keywords)
        
        assert result["keywords"]["success"][0]["keywordId"] == "kw123"

    # ==================== 删除测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_delete_keywords_success(self, api):
        """测试成功删除 keywords"""
        mock_response = {
            "keywords": {
                "success": [{"keywordId": "kw123", "index": 0}],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        result = await api.delete_keywords(["kw123"])
        
        # delete_keywords 内部使用 POST
        api.post.assert_called()


class TestSPNegativeKeywordsAPI:
    """SP Negative Keywords API 单元测试"""

    @pytest.fixture
    def api(self):
        from amazon_ads_api.core.sp.keywords import SPKeywordsAPI
        api = SPKeywordsAPI.__new__(SPKeywordsAPI)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.put = AsyncMock()
        api.delete = AsyncMock()
        return api

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_negative_keywords(self, api):
        """测试创建 negative keywords"""
        mock_response = {
            "negativeKeywords": {
                "success": [{"keywordId": "nk123", "index": 0}],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        neg_keywords = [{
            "campaignId": "camp123",
            "adGroupId": "ag123",
            "keywordText": "negative term",
            "matchType": "NEGATIVE_EXACT"
        }]
        
        result = await api.create_negative_keywords(neg_keywords)
        
        assert result == mock_response

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_list_negative_keywords(self, api):
        """测试列出 negative keywords"""
        mock_response = {
            "negativeKeywords": [
                {"keywordId": "nk1", "keywordText": "bad term"}
            ]
        }
        api.post.return_value = mock_response
        
        result = await api.list_negative_keywords()
        
        assert "negativeKeywords" in result


class TestSPCampaignNegativeKeywordsAPI:
    """SP Campaign-level Negative Keywords 测试"""

    @pytest.fixture
    def api(self):
        from amazon_ads_api.core.sp.keywords import SPKeywordsAPI
        api = SPKeywordsAPI.__new__(SPKeywordsAPI)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.put = AsyncMock()
        api.delete = AsyncMock()
        return api

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_campaign_negative_keywords(self, api):
        """测试创建 campaign 级别 negative keywords"""
        mock_response = {
            "campaignNegativeKeywords": {
                "success": [{"keywordId": "cnk123"}],
                "error": []
            }
        }
        api.post.return_value = mock_response
        
        keywords = [{
            "campaignId": "camp123",
            "keywordText": "exclude this",
            "matchType": "NEGATIVE_EXACT"
        }]
        
        result = await api.create_campaign_negative_keywords(keywords)
        
        assert result == mock_response

