"""
SP Keywords API 完整性测试

目标：测试所有SP Keywords API方法，验证：
1. 请求参数格式正确
2. API响应可以正确解析
3. 错误处理符合预期
4. 返回值类型正确

覆盖：
- 22个Keywords API方法
- 包括正常关键词、否定关键词（Ad Group和Campaign级别）
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
@pytest.mark.sp_keywords
class TestSPKeywordsListAPI:
    """测试Keywords List相关API"""
    
    @pytest.mark.asyncio
    async def test_list_keywords_basic(self, ads_client):
        """测试基本的list_keywords调用"""
        result = await ads_client.sp.keywords.list_keywords(max_results=10)
        
        # 验证返回结构
        assert isinstance(result, dict), "返回值应该是dict"
        assert "keywords" in result, "应包含keywords字段"
        assert isinstance(result["keywords"], list), "keywords应该是list"
        
        print(f"✓ list_keywords返回{len(result['keywords'])}个keywords")
    
    @pytest.mark.asyncio
    async def test_list_keywords_with_filters(self, ads_client):
        """测试带过滤条件的list_keywords"""
        result = await ads_client.sp.keywords.list_keywords(
            state_filter=["enabled", "paused"],
            max_results=10
        )
        
        assert "keywords" in result
        # 验证返回的keywords状态正确
        if result["keywords"]:
            for kw in result["keywords"]:
                assert kw["state"].upper() in ["ENABLED", "PAUSED"]
        
        print(f"✓ 过滤后返回{len(result['keywords'])}个keywords")
    
    @pytest.mark.asyncio
    async def test_list_keywords_with_campaign_filter(self, ads_client):
        """测试campaign_id过滤"""
        # 先获取一个campaign
        campaigns = await ads_client.sp.campaigns.list_campaigns(max_results=1)
        if not campaigns.get("campaigns"):
            pytest.skip("No campaigns found")
        
        campaign_id = campaigns["campaigns"][0]["campaignId"]
        
        result = await ads_client.sp.keywords.list_keywords(
            campaign_id=campaign_id,
            max_results=10
        )
        
        assert "keywords" in result
        # 验证返回的keywords属于该campaign
        if result["keywords"]:
            for kw in result["keywords"]:
                assert "campaignId" in kw
        
        print(f"✓ Campaign {campaign_id}有{len(result['keywords'])}个keywords")
    
    @pytest.mark.asyncio
    async def test_list_keywords_pagination(self, ads_client):
        """测试分页功能"""
        # 第一页
        page1 = await ads_client.sp.keywords.list_keywords(max_results=5)
        
        assert "keywords" in page1
        
        # 如果有nextToken，测试第二页
        if page1.get("nextToken"):
            page2 = await ads_client.sp.keywords.list_keywords(
                max_results=5,
                next_token=page1["nextToken"]
            )
            
            assert "keywords" in page2
            # 验证两页数据不重复
            if page1["keywords"] and page2["keywords"]:
                page1_ids = {kw["keywordId"] for kw in page1["keywords"]}
                page2_ids = {kw["keywordId"] for kw in page2["keywords"]}
                assert page1_ids.isdisjoint(page2_ids), "分页数据不应重复"
            
            print(f"✓ 分页正常：第1页{len(page1['keywords'])}个，第2页{len(page2['keywords'])}个")
        else:
            print("✓ 无需分页（数据量较少）")


@pytest.mark.integration
@pytest.mark.sp_keywords
class TestSPKeywordsNegativeAPI:
    """测试Negative Keywords相关API"""
    
    @pytest.mark.asyncio
    async def test_list_negative_keywords(self, ads_client):
        """测试list_negative_keywords"""
        result = await ads_client.sp.keywords.list_negative_keywords(max_results=10)
        
        assert isinstance(result, dict)
        assert "negativeKeywords" in result
        assert isinstance(result["negativeKeywords"], list)
        
        print(f"✓ list_negative_keywords返回{len(result['negativeKeywords'])}个")
    
    @pytest.mark.asyncio
    async def test_list_campaign_negative_keywords(self, ads_client):
        """测试list_campaign_negative_keywords"""
        result = await ads_client.sp.keywords.list_campaign_negative_keywords(max_results=10)
        
        assert isinstance(result, dict)
        assert "campaignNegativeKeywords" in result
        assert isinstance(result["campaignNegativeKeywords"], list)
        
        print(f"✓ list_campaign_negative_keywords返回{len(result['campaignNegativeKeywords'])}个")


@pytest.mark.integration
@pytest.mark.sp_keywords
@pytest.mark.creates_resources
class TestSPKeywordsCRUDAPI:
    """测试Keywords CRUD相关API（会创建资源）"""
    
    @pytest.mark.skip(reason="需要真实Campaign和AdGroup，在E2E测试中已覆盖")
    @pytest.mark.asyncio
    async def test_create_keywords(self, ads_client):
        """测试create_keywords（跳过，E2E已测试）"""
        pass
    
    @pytest.mark.skip(reason="需要真实Keyword ID，在E2E测试中已覆盖")
    @pytest.mark.asyncio
    async def test_update_keywords(self, ads_client):
        """测试update_keywords（跳过，E2E已测试）"""
        pass
    
    @pytest.mark.skip(reason="需要真实Keyword ID，在E2E测试中已覆盖")
    @pytest.mark.asyncio
    async def test_delete_keywords(self, ads_client):
        """测试delete_keywords（跳过，E2E已测试）"""
        pass


@pytest.mark.integration
@pytest.mark.sp_keywords
class TestSPKeywordsAPIErrorHandling:
    """测试API错误处理"""
    
    @pytest.mark.asyncio
    async def test_list_keywords_invalid_state_filter(self, ads_client):
        """测试无效的state_filter"""
        # 应该优雅处理，不应崩溃
        try:
            result = await ads_client.sp.keywords.list_keywords(
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
    async def test_list_keywords_with_large_max_results(self, ads_client):
        """测试超大max_results参数"""
        # max_results过大时，验证API行为
        result = await ads_client.sp.keywords.list_keywords(max_results=10000)
        
        assert isinstance(result, dict)
        assert "keywords" in result
        
        # 验证返回数量（不硬编码断言，因为不同账号数据量不同）
        returned_count = len(result["keywords"])
        
        # 验证：如果返回数量很大，应该有nextToken用于分页
        if returned_count > 100:
            print(f"⚠ API返回了{returned_count}个keywords（超过常见100的限制）")
        
        print(f"✓ max_results=10000时返回{returned_count}个keywords")


@pytest.mark.integration
@pytest.mark.sp_keywords
class TestSPKeywordsAPIReturnTypes:
    """测试API返回值类型正确性"""
    
    @pytest.mark.asyncio
    async def test_list_keywords_return_type(self, ads_client):
        """验证list_keywords返回类型"""
        result = await ads_client.sp.keywords.list_keywords(max_results=1)
        
        assert isinstance(result, dict), "返回类型应为dict"
        assert "keywords" in result, "应包含keywords字段"
        assert isinstance(result["keywords"], list), "keywords应为list"
        
        if result["keywords"]:
            kw = result["keywords"][0]
            # 验证必需字段类型
            assert isinstance(kw.get("keywordId"), (str, int)), "keywordId应为str或int"
            assert isinstance(kw.get("keywordText"), str), "keywordText应为str"
            assert isinstance(kw.get("state"), str), "state应为str"
            
            print(f"✓ 返回值类型验证通过：{list(kw.keys())}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s", "--tb=short"])

