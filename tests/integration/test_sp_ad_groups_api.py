"""
SP Ad Groups API 完整性测试

目标：测试所有SP Ad Groups API方法（11个）

覆盖的API：
1. list_ad_groups
2. get_ad_group (通过list_ad_groups实现)
3. create_ad_groups
4. update_ad_groups
5. archive_ad_group
6. list_ad_groups with filters
7. list_ad_groups with pagination
"""

import pytest
import pytest_asyncio
import os
from dotenv import load_dotenv
from amazon_ads_api import AmazonAdsClient

# 加载后端的.env文件
backend_env = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'amazon-ads-ai', 'backend', '.env')
if os.path.exists(backend_env):
    load_dotenv(backend_env)
else:
    load_dotenv()  # Fallback to default


@pytest_asyncio.fixture
async def ads_client():
    """Amazon Ads客户端"""
    client = AmazonAdsClient(
        client_id=os.getenv('AMAZON_ADS_CLIENT_ID'),
        client_secret=os.getenv('AMAZON_ADS_CLIENT_SECRET'),
        refresh_token=os.getenv('AMAZON_ADS_REFRESH_TOKEN'),
        profile_id=os.getenv('AMAZON_ADS_PROFILE_ID'),
    )
    yield client
    # Cleanup
    await client.close() if hasattr(client, 'close') else None


@pytest.mark.integration
@pytest.mark.sp_ad_groups
class TestSPAdGroupsListAPI:
    """测试Ad Groups List相关API"""
    
    @pytest.mark.asyncio
    async def test_list_ad_groups_basic(self, ads_client):
        """测试基本的list_ad_groups"""
        result = await ads_client.sp.ad_groups.list_ad_groups(max_results=10)
        
        # 验证返回结构
        assert isinstance(result, dict), "返回值应该是dict"
        assert "adGroups" in result, "应包含adGroups字段"
        assert isinstance(result["adGroups"], list), "adGroups应该是list"
        
        print(f"✓ list_ad_groups返回{len(result['adGroups'])}个ad groups")
    
    @pytest.mark.asyncio
    async def test_list_ad_groups_with_state_filter(self, ads_client):
        """测试state过滤"""
        result = await ads_client.sp.ad_groups.list_ad_groups(
            state_filter=["enabled"],
            max_results=10
        )
        
        assert "adGroups" in result
        # 验证返回的ad groups状态正确
        if result["adGroups"]:
            for ad_group in result["adGroups"]:
                assert ad_group["state"].upper() == "ENABLED"
        
        print(f"✓ 过滤后返回{len(result['adGroups'])}个enabled ad groups")
    
    @pytest.mark.asyncio
    async def test_list_ad_groups_with_campaign_filter(self, ads_client):
        """测试campaign_id过滤"""
        # 先获取一个campaign
        campaigns = await ads_client.sp.campaigns.list_campaigns(max_results=1)
        if not campaigns.get("campaigns"):
            pytest.skip("No campaigns found")
        
        campaign_id = campaigns["campaigns"][0]["campaignId"]
        
        result = await ads_client.sp.ad_groups.list_ad_groups(
            campaign_id=campaign_id,
            max_results=10
        )
        
        assert "adGroups" in result
        # 验证返回的ad groups属于该campaign
        if result["adGroups"]:
            for ag in result["adGroups"]:
                assert ag.get("campaignId") == campaign_id
        
        print(f"✓ Campaign {campaign_id}有{len(result['adGroups'])}个ad groups")
    
    @pytest.mark.asyncio
    async def test_list_ad_groups_with_ad_group_ids(self, ads_client):
        """测试ad_group_ids过滤"""
        # 先获取一些ad groups
        all_ad_groups = await ads_client.sp.ad_groups.list_ad_groups(max_results=5)
        if not all_ad_groups.get("adGroups"):
            pytest.skip("No ad groups found")
        
        # 获取前2个ad group的ID
        ad_group_ids = [ag["adGroupId"] for ag in all_ad_groups["adGroups"][:2]]
        
        result = await ads_client.sp.ad_groups.list_ad_groups(
            ad_group_ids=ad_group_ids,
            max_results=10
        )
        
        assert "adGroups" in result
        # 验证返回的ad groups是我们请求的
        returned_ids = {ag["adGroupId"] for ag in result["adGroups"]}
        for ag_id in ad_group_ids:
            assert ag_id in returned_ids
        
        print(f"✓ 请求{len(ad_group_ids)}个ad groups，返回{len(result['adGroups'])}个")
    
    @pytest.mark.asyncio
    async def test_list_ad_groups_pagination(self, ads_client):
        """测试分页功能"""
        # 第一页
        page1 = await ads_client.sp.ad_groups.list_ad_groups(max_results=5)
        
        assert "adGroups" in page1
        
        # 如果有nextToken，测试第二页
        if page1.get("nextToken"):
            page2 = await ads_client.sp.ad_groups.list_ad_groups(
                max_results=5,
                next_token=page1["nextToken"]
            )
            
            assert "adGroups" in page2
            # 验证两页数据不重复
            if page1["adGroups"] and page2["adGroups"]:
                page1_ids = {ag["adGroupId"] for ag in page1["adGroups"]}
                page2_ids = {ag["adGroupId"] for ag in page2["adGroups"]}
                assert page1_ids.isdisjoint(page2_ids), "分页数据不应重复"
            
            print(f"✓ 分页正常：第1页{len(page1['adGroups'])}个，第2页{len(page2['adGroups'])}个")
        else:
            print("✓ 无需分页（数据量较少）")


@pytest.mark.integration
@pytest.mark.sp_ad_groups
class TestSPAdGroupsAPIReturnTypes:
    """测试API返回值类型正确性"""
    
    @pytest.mark.asyncio
    async def test_list_ad_groups_return_structure(self, ads_client):
        """验证list_ad_groups返回结构"""
        result = await ads_client.sp.ad_groups.list_ad_groups(max_results=1)
        
        assert isinstance(result, dict)
        assert "adGroups" in result
        assert isinstance(result["adGroups"], list)
        
        if result["adGroups"]:
            ad_group = result["adGroups"][0]
            # 验证必需字段
            assert "adGroupId" in ad_group
            assert "name" in ad_group
            assert "campaignId" in ad_group
            assert "state" in ad_group
            assert "defaultBid" in ad_group
            
            print(f"✓ Ad Group结构验证通过：{list(ad_group.keys())[:5]}...")


@pytest.mark.integration
@pytest.mark.sp_ad_groups
@pytest.mark.creates_resources
class TestSPAdGroupsCRUDAPI:
    """测试CRUD API（会创建资源，在E2E中已测试）"""
    
    @pytest.mark.skip(reason="在E2E test_03中已完整测试")
    @pytest.mark.asyncio
    async def test_create_ad_groups(self, ads_client):
        """创建Ad Group（跳过）"""
        pass
    
    @pytest.mark.skip(reason="在E2E test_03中已完整测试")
    @pytest.mark.asyncio
    async def test_update_ad_groups(self, ads_client):
        """更新Ad Group（跳过）"""
        pass
    
    @pytest.mark.skip(reason="在E2E test_03中已完整测试")
    @pytest.mark.asyncio
    async def test_archive_ad_group(self, ads_client):
        """归档Ad Group（跳过）"""
        pass


@pytest.mark.integration
@pytest.mark.sp_ad_groups
class TestSPAdGroupsAPIErrorHandling:
    """测试API错误处理"""
    
    @pytest.mark.asyncio
    async def test_list_ad_groups_with_invalid_state(self, ads_client):
        """测试无效的state_filter"""
        # 应该优雅处理，不应崩溃
        try:
            result = await ads_client.sp.ad_groups.list_ad_groups(
                state_filter=["invalid_state"],
                max_results=1
            )
            # 可能返回空列表或API错误
            assert isinstance(result, dict)
        except Exception as e:
            # 如果API返回错误，应该是AmazonAdsError
            from amazon_ads_api.base import AmazonAdsError
            assert isinstance(e, AmazonAdsError)
            print(f"✓ API正确返回错误：{e}")
    
    @pytest.mark.asyncio
    async def test_list_ad_groups_with_large_max_results(self, ads_client):
        """测试超大max_results"""
        result = await ads_client.sp.ad_groups.list_ad_groups(max_results=10000)
        
        assert isinstance(result, dict)
        assert "adGroups" in result
        
        # 验证返回数量
        returned_count = len(result["adGroups"])
        
        if returned_count > 100:
            print(f"⚠ API返回了{returned_count}个ad groups（超过常见100的限制）")
        
        print(f"✓ max_results=10000时返回{returned_count}个ad groups")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s", "--tb=short"])

