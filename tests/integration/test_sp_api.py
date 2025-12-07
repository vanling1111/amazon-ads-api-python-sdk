"""
Integration tests for SP (Sponsored Products) API
Note: These tests require valid credentials and profile ID:
  - AMAZON_ADS_CLIENT_ID
  - AMAZON_ADS_CLIENT_SECRET
  - AMAZON_ADS_REFRESH_TOKEN
  - AMAZON_ADS_PROFILE_ID
"""
import os
import pytest
import time
from amazon_ads_api import AmazonAdsClient, AdsRegion
from amazon_ads_api.base import AmazonAdsError


def has_valid_credentials():
    """Check if valid credentials are available"""
    client_id = os.environ.get("AMAZON_ADS_CLIENT_ID", "")
    profile_id = os.environ.get("AMAZON_ADS_PROFILE_ID", "")
    return (client_id and client_id != "test_client_id" and 
            profile_id and profile_id != "1234567890")


requires_credentials = pytest.mark.skipif(
    not has_valid_credentials(),
    reason="Requires valid Amazon Ads API credentials and profile ID"
)


@pytest.fixture
def client():
    """Create authenticated client with profile ID"""
    if not has_valid_credentials():
        pytest.skip("Missing credentials")
    
    client = AmazonAdsClient(
        client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
        client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
        refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
        region=AdsRegion.NA,
    )
    client.with_profile(os.environ["AMAZON_ADS_PROFILE_ID"])
    return client


class TestSPCampaignsIntegration:
    """Integration tests for SP Campaigns API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_campaigns(self, client):
        """Test listing SP campaigns"""
        result = client.sp.campaigns.list_campaigns()
        
        assert isinstance(result, dict)
        assert "campaigns" in result
        assert isinstance(result["campaigns"], list)
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_campaigns_with_state_filter(self, client):
        """Test listing SP campaigns with state filter"""
        result = client.sp.campaigns.list_campaigns(state_filter="enabled")
        
        assert isinstance(result, dict)
        assert "campaigns" in result
        # All returned campaigns should be enabled
        for campaign in result["campaigns"]:
            assert campaign.get("state") == "enabled"
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_campaigns_with_max_results(self, client):
        """Test listing SP campaigns with max results"""
        result = client.sp.campaigns.list_campaigns(max_results=5)
        
        assert isinstance(result, dict)
        assert "campaigns" in result
        assert len(result["campaigns"]) <= 5
    
    @requires_credentials
    @pytest.mark.integration
    def test_get_campaign(self, client):
        """Test getting a specific campaign"""
        # First, list campaigns to get an ID
        list_result = client.sp.campaigns.list_campaigns(max_results=1)
        
        if not list_result.get("campaigns"):
            pytest.skip("No campaigns found to test")
        
        campaign_id = list_result["campaigns"][0]["campaignId"]
        campaign = client.sp.campaigns.get_campaign(campaign_id)
        
        assert isinstance(campaign, dict)
        assert campaign.get("campaignId") == campaign_id
    
    @requires_credentials
    @pytest.mark.integration
    def test_get_nonexistent_campaign(self, client):
        """Test getting a campaign that doesn't exist"""
        with pytest.raises(AmazonAdsError) as exc_info:
            client.sp.campaigns.get_campaign("nonexistent_campaign_id")
        
        # Should be 404 or 400
        assert exc_info.value.status_code in [400, 404]


class TestSPCampaignsCRUD:
    """Test SP Campaigns CRUD operations"""
    
    @requires_credentials
    @pytest.mark.integration
    @pytest.mark.slow
    def test_create_and_delete_campaign(self, client):
        """Test creating and deleting a campaign"""
        # Create campaign
        test_campaign = {
            "name": f"Test Campaign {int(time.time())}",
            "targetingType": "MANUAL",
            "state": "paused",  # Create as paused to avoid spending
            "dailyBudget": 1.0,
            "startDate": "20250101",
            "bidding": {
                "strategy": "LEGACY_FOR_SALES"
            }
        }
        
        create_result = client.sp.campaigns.create_campaigns([test_campaign])
        
        assert isinstance(create_result, dict)
        assert "campaigns" in create_result
        
        # Check if creation succeeded
        if create_result["campaigns"].get("success"):
            campaign_id = create_result["campaigns"]["success"][0]["campaignId"]
            
            # Verify campaign exists
            campaign = client.sp.campaigns.get_campaign(campaign_id)
            assert campaign.get("name") == test_campaign["name"]
            
            # Delete (archive) the campaign
            delete_result = client.sp.campaigns.delete_campaign(campaign_id)
            assert isinstance(delete_result, dict)
        else:
            # Creation failed - check error
            errors = create_result["campaigns"].get("error", [])
            pytest.skip(f"Campaign creation failed: {errors}")


class TestSPAdGroupsIntegration:
    """Integration tests for SP Ad Groups API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_ad_groups(self, client):
        """Test listing SP ad groups"""
        # First get a campaign
        campaigns = client.sp.campaigns.list_campaigns(max_results=1)
        
        if not campaigns.get("campaigns"):
            pytest.skip("No campaigns found")
        
        campaign_id = campaigns["campaigns"][0]["campaignId"]
        
        # List ad groups for that campaign
        result = client.sp.ad_groups.list_ad_groups(campaign_id=campaign_id)
        
        assert isinstance(result, dict)


class TestSPKeywordsIntegration:
    """Integration tests for SP Keywords API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_keywords(self, client):
        """Test listing SP keywords"""
        # First get a campaign
        campaigns = client.sp.campaigns.list_campaigns(max_results=1)
        
        if not campaigns.get("campaigns"):
            pytest.skip("No campaigns found")
        
        campaign_id = campaigns["campaigns"][0]["campaignId"]
        
        # List keywords for that campaign
        result = client.sp.keywords.list_keywords(campaign_id=campaign_id)
        
        assert isinstance(result, dict)


class TestSPTargetingIntegration:
    """Integration tests for SP Targeting API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_list_targets(self, client):
        """Test listing SP targets"""
        # First get a campaign
        campaigns = client.sp.campaigns.list_campaigns(max_results=1)
        
        if not campaigns.get("campaigns"):
            pytest.skip("No campaigns found")
        
        campaign_id = campaigns["campaigns"][0]["campaignId"]
        
        # List targets for that campaign
        result = client.sp.targeting.list_targets(campaign_id=campaign_id)
        
        assert isinstance(result, dict)


class TestSPRecommendationsIntegration:
    """Integration tests for SP Recommendations API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_get_bid_recommendations(self, client):
        """Test getting bid recommendations"""
        # This requires existing keywords, so we just test the API is accessible
        # Without erroring on authentication
        try:
            result = client.sp.recommendations.get_bid_recommendations(
                ad_group_id="test",
                keyword_recommendations=[]
            )
            # If we get here, the API is accessible
            assert True
        except AmazonAdsError as e:
            # 400 is expected for invalid parameters
            # We just want to ensure auth works
            assert e.status_code == 400


class TestRateLimiting:
    """Test rate limiting behavior"""
    
    @requires_credentials
    @pytest.mark.integration
    @pytest.mark.slow
    def test_multiple_requests(self, client):
        """Test that multiple requests don't get rate limited immediately"""
        # Make 5 quick requests
        for i in range(5):
            result = client.sp.campaigns.list_campaigns(max_results=1)
            assert isinstance(result, dict)
        
        # If we get here without 429 error, rate limiting is handled correctly


class TestErrorHandling:
    """Test error handling in integration"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_unauthorized_profile(self, client):
        """Test accessing a profile we don't have access to"""
        # Save original profile
        original_profile = client.profile_id
        
        # Set to a fake profile ID
        client.with_profile("9999999999999")
        
        # This should fail with 403 or similar
        with pytest.raises(AmazonAdsError) as exc_info:
            client.sp.campaigns.list_campaigns()
        
        assert exc_info.value.status_code in [400, 401, 403]
        
        # Restore original profile
        client.with_profile(original_profile)
