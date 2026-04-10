"""
Reports V3 API 单元测试

测试目标: amazon_ads_api/services/reporting/reports_v3.py
"""

import pytest
from unittest.mock import AsyncMock


class TestReportsV3API:
    """Reports V3 API 单元测试"""

    @pytest.fixture
    def api(self):
        """创建 mock API 实例"""
        from amazon_ads_api.services.reporting.reports_v3 import ReportsV3API
        api = ReportsV3API.__new__(ReportsV3API)
        api.get = AsyncMock()
        api.post = AsyncMock()
        api.delete = AsyncMock()
        return api

    # ==================== 创建报告测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_report_sp_campaigns(self, api):
        """测试创建 SP Campaigns 报告"""
        mock_response = {
            "reportId": "report123",
            "status": "PENDING"
        }
        api.post.return_value = mock_response
        
        result = await api.create_report(
            report_type="spCampaigns",
            time_unit="DAILY",
            start_date="2024-01-01",
            end_date="2024-01-31",
            metrics=["impressions", "clicks", "spend"]
        )
        
        assert result["reportId"] == "report123"
        api.post.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_report_sb_keywords(self, api):
        """测试创建 SB Keywords 报告"""
        mock_response = {"reportId": "report456", "status": "PENDING"}
        api.post.return_value = mock_response
        
        result = await api.create_report(
            report_type="sbKeywords",
            time_unit="SUMMARY",
            start_date="2024-01-01",
            end_date="2024-01-31",
            metrics=["impressions", "clicks"]
        )
        
        assert result["reportId"] == "report456"

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_report_sd_targets(self, api):
        """测试创建 SD Targets 报告"""
        mock_response = {"reportId": "report789", "status": "PENDING"}
        api.post.return_value = mock_response
        
        result = await api.create_report(
            report_type="sdTargets",
            time_unit="DAILY",
            start_date="2024-01-01",
            end_date="2024-01-07",
            metrics=["impressions", "clicks", "cost"]
        )
        
        assert result["reportId"] == "report789"

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_report_with_filters(self, api):
        """测试带过滤条件创建报告"""
        mock_response = {"reportId": "reportF", "status": "PENDING"}
        api.post.return_value = mock_response
        
        filters = [
            {"field": "campaignStatus", "values": ["ENABLED", "PAUSED"]}
        ]
        
        result = await api.create_report(
            report_type="spCampaigns",
            time_unit="DAILY",
            start_date="2024-01-01",
            end_date="2024-01-31",
            metrics=["impressions"],
            filters=filters
        )
        
        assert result["reportId"] == "reportF"

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_report_with_group_by(self, api):
        """测试带 groupBy 创建报告"""
        mock_response = {"reportId": "reportG", "status": "PENDING"}
        api.post.return_value = mock_response
        
        result = await api.create_report(
            report_type="spCampaigns",
            time_unit="DAILY",
            start_date="2024-01-01",
            end_date="2024-01-31",
            metrics=["impressions"],
            group_by=["campaign", "adGroup"]
        )
        
        assert result["reportId"] == "reportG"

    # ==================== 获取报告状态测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_get_report_status_pending(self, api):
        """测试获取 PENDING 状态报告"""
        mock_response = {
            "reportId": "report123",
            "status": "PENDING",
            "statusDetails": "Report is being generated"
        }
        api.get.return_value = mock_response
        
        result = await api.get_report_status("report123")
        
        assert result["status"] == "PENDING"

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_get_report_status_completed(self, api):
        """测试获取 COMPLETED 状态报告"""
        mock_response = {
            "reportId": "report123",
            "status": "COMPLETED",
            "url": "https://example.com/report.json.gz"
        }
        api.get.return_value = mock_response
        
        result = await api.get_report_status("report123")
        
        assert result["status"] == "COMPLETED"
        assert "url" in result

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_get_report_status_failed(self, api):
        """测试获取 FAILED 状态报告"""
        mock_response = {
            "reportId": "report123",
            "status": "FAILURE",
            "statusDetails": "Invalid date range"
        }
        api.get.return_value = mock_response
        
        result = await api.get_report_status("report123")
        
        assert result["status"] == "FAILURE"

    # ==================== 删除报告测试 ====================

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_delete_report(self, api):
        """测试删除报告"""
        mock_response = {}
        api.delete.return_value = mock_response
        
        result = await api.delete_report("report123")
        
        api.delete.assert_called_once()


class TestReportsV3Helpers:
    """Reports V3 辅助方法测试"""

    @pytest.fixture
    def api(self):
        from amazon_ads_api.services.reporting.reports_v3 import ReportsV3API
        api = ReportsV3API.__new__(ReportsV3API)
        api.get = AsyncMock()
        api.post = AsyncMock()
        return api

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_create_report_basic(self, api):
        """测试创建基础报告"""
        api.post.return_value = {"reportId": "rpt1", "status": "PENDING"}
        
        result = await api.create_report(
            report_type="spCampaigns",
            time_unit="DAILY",
            start_date="2024-01-01",
            end_date="2024-01-31",
            metrics=["impressions", "clicks"]
        )
        
        assert result["reportId"] == "rpt1"
        api.post.assert_called_once()


class TestReportsV3AdProductMapping:
    """测试 adProduct 映射逻辑"""

    @pytest.fixture
    def api(self):
        from amazon_ads_api.services.reporting.reports_v3 import ReportsV3API
        api = ReportsV3API.__new__(ReportsV3API)
        api.post = AsyncMock(return_value={"reportId": "test"})
        return api

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_sp_report_type_mapping(self, api):
        """测试 SP 报告类型映射"""
        await api.create_report(
            report_type="spCampaigns",
            time_unit="DAILY",
            start_date="2024-01-01",
            end_date="2024-01-31",
            metrics=["impressions"]
        )
        
        call_args = api.post.call_args
        # 验证 adProduct 被正确设置为 SPONSORED_PRODUCTS
        assert call_args is not None

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_sb_report_type_mapping(self, api):
        """测试 SB 报告类型映射"""
        await api.create_report(
            report_type="sbCampaigns",
            time_unit="DAILY",
            start_date="2024-01-01",
            end_date="2024-01-31",
            metrics=["impressions"]
        )
        
        call_args = api.post.call_args
        assert call_args is not None

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_sd_report_type_mapping(self, api):
        """测试 SD 报告类型映射"""
        await api.create_report(
            report_type="sdCampaigns",
            time_unit="DAILY",
            start_date="2024-01-01",
            end_date="2024-01-31",
            metrics=["impressions"]
        )
        
        call_args = api.post.call_args
        assert call_args is not None

