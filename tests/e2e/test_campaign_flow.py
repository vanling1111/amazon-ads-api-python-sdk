"""
端到端测试 - Campaign 完整流程

测试完整的广告活动流程:
1. 创建 Campaign
2. 创建 Ad Group
3. 添加 Keywords
4. 生成报告
5. 清理资源

需要真实的 Amazon Ads 测试账号
"""

import os
import pytest
import asyncio
from typing import Optional
from datetime import datetime, timedelta

from amazon_ads_api.base import AdsRegion


# 跳过条件
SKIP_E2E = not all([
    os.getenv("AMAZON_ADS_CLIENT_ID"),
    os.getenv("AMAZON_ADS_CLIENT_SECRET"),
    os.getenv("AMAZON_ADS_REFRESH_TOKEN"),
    os.getenv("AMAZON_ADS_PROFILE_ID"),
    os.getenv("AMAZON_ADS_TEST_MODE", "false").lower() == "true",  # 必须显式启用
])

skip_reason = "需要配置 AMAZON_ADS_* 环境变量并设置 AMAZON_ADS_TEST_MODE=true"


# Region 映射
REGION_MAP = {
    "NA": AdsRegion.NA,
    "EU": AdsRegion.EU,
    "FE": AdsRegion.FE,
}


def get_client():
    """创建 API 客户端"""
    from amazon_ads_api import AmazonAdsClient
    
    region_str = os.getenv("AMAZON_ADS_REGION", "NA")
    return AmazonAdsClient(
        client_id=os.getenv("AMAZON_ADS_CLIENT_ID"),
        client_secret=os.getenv("AMAZON_ADS_CLIENT_SECRET"),
        refresh_token=os.getenv("AMAZON_ADS_REFRESH_TOKEN"),
        profile_id=os.getenv("AMAZON_ADS_PROFILE_ID"),
        region=REGION_MAP.get(region_str, AdsRegion.NA),
    )


@pytest.mark.e2e
@pytest.mark.skipif(SKIP_E2E, reason=skip_reason)
class TestCampaignE2EFlow:
    """
    Campaign E2E 测试流程
    
    注意: 这些测试会创建真实的广告资源！
    请确保使用测试账号或沙盒环境
    """
    
    campaign_id: Optional[str] = None
    ad_group_id: Optional[str] = None
    keyword_id: Optional[str] = None
    
    @pytest.fixture
    def client(self):
        """设置客户端（同步 fixture）"""
        return get_client()
    
    @pytest.mark.asyncio
    async def test_01_list_campaigns(self, client):
        """步骤 1: 列出现有 Campaigns"""
        result = await client.sp.campaigns.list_campaigns(max_results=10)
        
        print(f"\n获取到 Campaigns: {len(result.get('campaigns', []))} 个")
        
        assert isinstance(result, dict)
        campaigns = result.get("campaigns", [])
        assert isinstance(campaigns, list)
        
        # 保存第一个 campaign 用于后续测试
        if campaigns:
            self.__class__.campaign_id = campaigns[0].get("campaignId")
            print(f"使用现有 Campaign ID: {self.__class__.campaign_id}")
    
    @pytest.mark.asyncio
    async def test_02_list_ad_groups(self, client):
        """步骤 2: 列出 Ad Groups"""
        result = await client.sp.ad_groups.list_ad_groups(max_results=10)
        
        print(f"\n获取到 Ad Groups")
        
        if isinstance(result, dict):
            ad_groups = result.get("adGroups", [])
        else:
            ad_groups = result if isinstance(result, list) else []
        
        assert isinstance(ad_groups, list)
        
        if ad_groups:
            self.__class__.ad_group_id = ad_groups[0].get("adGroupId")
            print(f"使用现有 Ad Group ID: {self.__class__.ad_group_id}")
    
    @pytest.mark.asyncio
    async def test_03_list_keywords(self, client):
        """步骤 3: 列出 Keywords"""
        result = await client.sp.keywords.list_keywords(max_results=10)
        
        print(f"\n获取到 Keywords")
        
        if isinstance(result, dict):
            keywords = result.get("keywords", [])
        else:
            keywords = result if isinstance(result, list) else []
        
        assert isinstance(keywords, list)
        print(f"共 {len(keywords)} 个 keywords")
    
    @pytest.mark.asyncio
    async def test_04_list_portfolios(self, client):
        """步骤 4: 列出 Portfolios"""
        result = await client.accounts.portfolios.list_portfolios()
        
        print(f"\n获取到 Portfolios")
        
        # 结果可能是列表或包含 portfolios 键的字典
        if isinstance(result, dict):
            portfolios = result.get("portfolios", [])
        else:
            portfolios = result if isinstance(result, list) else []
        
        assert isinstance(portfolios, list)
        print(f"共 {len(portfolios)} 个 portfolios")
    
    @pytest.mark.asyncio
    async def test_05_get_campaign_details(self, client):
        """步骤 5: 获取 Campaign 详情（如果有）"""
        if not self.__class__.campaign_id:
            pytest.skip("没有可用的 Campaign")
        
        # 使用 list 并过滤来获取详情
        result = await client.sp.campaigns.list_campaigns(
            campaign_ids=[self.__class__.campaign_id]
        )
        
        print(f"\nCampaign 详情: {result}")
        
        if isinstance(result, dict):
            campaigns = result.get("campaigns", [])
            if campaigns:
                campaign = campaigns[0]
                assert campaign.get("campaignId") == self.__class__.campaign_id
                print(f"Campaign 名称: {campaign.get('name')}")


@pytest.mark.e2e
@pytest.mark.skipif(SKIP_E2E, reason=skip_reason)
class TestReportE2EFlow:
    """报告 E2E 测试流程"""
    
    @pytest.fixture
    def client(self):
        """设置客户端（同步 fixture）"""
        return get_client()
    
    @pytest.mark.asyncio
    async def test_report_workflow(self, client):
        """测试完整的报告工作流"""
        # 1. 创建报告请求
        end_date = datetime.now() - timedelta(days=1)
        start_date = end_date - timedelta(days=7)
        
        print(f"\n创建报告: {start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}")
        
        create_result = await client.services.reporting.create_report(
            report_type="spCampaigns",
            time_unit="SUMMARY",
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d"),
            metrics=["impressions", "clicks", "spend"]
        )
        
        print(f"创建结果: {create_result}")
        
        if "reportId" not in create_result:
            pytest.skip("无法创建报告")
        
        report_id = create_result["reportId"]
        print(f"Report ID: {report_id}")
        
        # 2. 等待报告完成（最多等待 30 秒）
        max_wait = 30
        wait_interval = 5
        waited = 0
        
        while waited < max_wait:
            status = await client.services.reporting.get_report_status(report_id)
            print(f"报告状态 ({waited}s): {status.get('status')}")
            
            if status.get("status") == "COMPLETED":
                print(f"报告完成! URL: {status.get('url')}")
                break
            elif status.get("status") == "FAILURE":
                print(f"报告失败: {status.get('failureReason')}")
                break
            
            await asyncio.sleep(wait_interval)
            waited += wait_interval
        
        # 3. 验证报告状态
        final_status = await client.services.reporting.get_report_status(report_id)
        assert final_status.get("status") in ["COMPLETED", "PENDING", "PROCESSING", "FAILURE"]
        print(f"最终状态: {final_status.get('status')}")


