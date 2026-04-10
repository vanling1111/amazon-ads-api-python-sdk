"""
Sponsored Products API 集成测试

需要真实的 Amazon Ads 凭证才能运行
设置环境变量:
- AMAZON_ADS_CLIENT_ID
- AMAZON_ADS_CLIENT_SECRET
- AMAZON_ADS_REFRESH_TOKEN
- AMAZON_ADS_PROFILE_ID
"""

import os
import pytest
from datetime import datetime, timedelta

from amazon_ads_api.base import AdsRegion

# 标记所有测试为集成测试
pytestmark = [pytest.mark.integration, pytest.mark.slow]


# Region 映射
REGION_MAP = {
    "NA": AdsRegion.NA,
    "EU": AdsRegion.EU,
    "FE": AdsRegion.FE,
}


def get_credentials():
    """从环境变量获取凭证"""
    region_str = os.getenv("AMAZON_ADS_REGION", "NA")
    return {
        "client_id": os.getenv("AMAZON_ADS_CLIENT_ID"),
        "client_secret": os.getenv("AMAZON_ADS_CLIENT_SECRET"),
        "refresh_token": os.getenv("AMAZON_ADS_REFRESH_TOKEN"),
        "profile_id": os.getenv("AMAZON_ADS_PROFILE_ID"),
        "region": REGION_MAP.get(region_str, AdsRegion.NA),
    }


def skip_if_no_credentials():
    """如果没有凭证则跳过测试"""
    creds = get_credentials()
    if not all([creds["client_id"], creds["client_secret"], creds["refresh_token"]]):
        pytest.skip("Missing Amazon Ads credentials")


class TestProfilesIntegration:
    """Profiles API 集成测试 - 必须首先测试，获取有效的 profile_id"""

    @pytest.fixture
    def client(self):
        """创建真实 API 客户端（同步 fixture）"""
        skip_if_no_credentials()
        
        from amazon_ads_api import AmazonAdsClient
        
        creds = get_credentials()
        client = AmazonAdsClient(
            client_id=creds["client_id"],
            client_secret=creds["client_secret"],
            refresh_token=creds["refresh_token"],
            profile_id=creds["profile_id"],
            region=creds["region"],
        )
        
        return client

    @pytest.mark.asyncio
    async def test_list_profiles(self, client):
        """测试列出 profiles - 这是基础测试，验证凭证有效"""
        result = await client.accounts.profiles.list_profiles()
        
        print(f"\n获取到 {len(result)} 个 profiles")
        for profile in result:
            print(f"  - Profile ID: {profile.get('profileId')}, "
                  f"Country: {profile.get('countryCode')}, "
                  f"Type: {profile.get('accountInfo', {}).get('type')}")
        
        assert isinstance(result, list)
        if result:
            assert "profileId" in result[0]


class TestSPCampaignsIntegration:
    """SP Campaigns API 集成测试"""

    @pytest.fixture
    def client(self):
        """创建真实 API 客户端"""
        skip_if_no_credentials()
        
        from amazon_ads_api import AmazonAdsClient
        
        creds = get_credentials()
        client = AmazonAdsClient(
            client_id=creds["client_id"],
            client_secret=creds["client_secret"],
            refresh_token=creds["refresh_token"],
            profile_id=creds["profile_id"],
            region=creds["region"],
        )
        
        return client

    @pytest.mark.asyncio
    async def test_list_campaigns(self, client):
        """测试列出真实 campaigns"""
        result = await client.sp.campaigns.list_campaigns(max_results=10)
        
        print(f"\n获取到 SP Campaigns: {result}")
        
        # 结果可能是列表或包含 campaigns 键的字典
        if isinstance(result, dict):
            campaigns = result.get("campaigns", [])
        else:
            campaigns = result if isinstance(result, list) else []
        
        assert isinstance(campaigns, list)
        print(f"共 {len(campaigns)} 个 campaigns")


class TestSPKeywordsIntegration:
    """SP Keywords API 集成测试"""

    @pytest.fixture
    def client(self):
        skip_if_no_credentials()
        
        from amazon_ads_api import AmazonAdsClient
        
        creds = get_credentials()
        client = AmazonAdsClient(
            client_id=creds["client_id"],
            client_secret=creds["client_secret"],
            refresh_token=creds["refresh_token"],
            profile_id=creds["profile_id"],
            region=creds["region"],
        )
        
        return client

    @pytest.mark.asyncio
    async def test_list_keywords(self, client):
        """测试列出真实 keywords"""
        result = await client.sp.keywords.list_keywords(max_results=10)
        
        print(f"\n获取到 SP Keywords: {result}")
        
        # 结果可能是列表或包含 keywords 键的字典
        if isinstance(result, dict):
            keywords = result.get("keywords", [])
        else:
            keywords = result if isinstance(result, list) else []
        
        assert isinstance(keywords, list)
        print(f"共 {len(keywords)} 个 keywords")


class TestReportsIntegration:
    """Reports API 集成测试"""

    @pytest.fixture
    def client(self):
        skip_if_no_credentials()
        
        from amazon_ads_api import AmazonAdsClient
        
        creds = get_credentials()
        client = AmazonAdsClient(
            client_id=creds["client_id"],
            client_secret=creds["client_secret"],
            refresh_token=creds["refresh_token"],
            profile_id=creds["profile_id"],
            region=creds["region"],
        )
        
        return client

    @pytest.mark.asyncio
    async def test_create_and_get_report(self, client):
        """测试创建和获取报告"""
        # 使用过去 7 天的日期
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        
        # 创建报告（使用 services.reporting）
        create_result = await client.services.reporting.create_report(
            report_type="spCampaigns",
            time_unit="SUMMARY",
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d"),
            metrics=["impressions", "clicks", "spend"]
        )
        
        print(f"\n创建报告结果: {create_result}")
        
        assert "reportId" in create_result
        report_id = create_result["reportId"]
        
        # 获取报告状态
        status_result = await client.services.reporting.get_report_status(report_id)
        
        print(f"报告状态: {status_result}")
        
        assert status_result["reportId"] == report_id
        assert status_result["status"] in ["PENDING", "PROCESSING", "COMPLETED", "FAILURE"]


class TestSBCampaignsIntegration:
    """Sponsored Brands Campaigns API 集成测试"""

    @pytest.fixture
    def client(self):
        skip_if_no_credentials()
        
        from amazon_ads_api import AmazonAdsClient
        
        creds = get_credentials()
        client = AmazonAdsClient(
            client_id=creds["client_id"],
            client_secret=creds["client_secret"],
            refresh_token=creds["refresh_token"],
            profile_id=creds["profile_id"],
            region=creds["region"],
        )
        
        return client

    @pytest.mark.asyncio
    async def test_list_sb_campaigns(self, client):
        """测试列出 SB campaigns"""
        result = await client.sb.campaigns.list_campaigns(max_results=10)
        
        print(f"\n获取到 SB Campaigns: {result}")
        
        if isinstance(result, dict):
            campaigns = result.get("campaigns", [])
        else:
            campaigns = result if isinstance(result, list) else []
        
        assert isinstance(campaigns, list)
        print(f"共 {len(campaigns)} 个 SB campaigns")


class TestSDCampaignsIntegration:
    """Sponsored Display Campaigns API 集成测试"""

    @pytest.fixture
    def client(self):
        skip_if_no_credentials()
        
        from amazon_ads_api import AmazonAdsClient
        
        creds = get_credentials()
        client = AmazonAdsClient(
            client_id=creds["client_id"],
            client_secret=creds["client_secret"],
            refresh_token=creds["refresh_token"],
            profile_id=creds["profile_id"],
            region=creds["region"],
        )
        
        return client

    @pytest.mark.asyncio
    async def test_list_sd_campaigns(self, client):
        """测试列出 SD campaigns"""
        result = await client.sd.campaigns.list_campaigns(max_results=10)
        
        print(f"\n获取到 SD Campaigns: {result}")
        
        if isinstance(result, dict):
            campaigns = result.get("campaigns", [])
        else:
            campaigns = result if isinstance(result, list) else []
        
        assert isinstance(campaigns, list)
        print(f"共 {len(campaigns)} 个 SD campaigns")

