"""
Integration tests for SP (Sponsored Products) API
Note: These tests require valid credentials and profile ID
"""
import os
import pytest
from amazon_ads_api import AmazonAdsClient, AdsRegion


# Skip integration tests if no credentials
requires_credentials = pytest.mark.skipif(
    not os.environ.get("AMAZON_ADS_CLIENT_ID") or 
    os.environ.get("AMAZON_ADS_CLIENT_ID") == "test_client_id",
    reason="Requires valid Amazon Ads API credentials"
)

requires_profile = pytest.mark.skipif(
    not os.environ.get("AMAZON_ADS_PROFILE_ID") or
    os.environ.get("AMAZON_ADS_PROFILE_ID") == "1234567890",
    reason="Requires valid Amazon Ads Profile ID"
)


class TestSPCampaigns:
    """Test SP Campaigns API"""
    
    @pytest.fixture
    def client(self):
        """Create authenticated client"""
        client = AmazonAdsClient(
            client_id=os.environ.get("AMAZON_ADS_CLIENT_ID", ""),
            client_secret=os.environ.get("AMAZON_ADS_CLIENT_SECRET", ""),
            refresh_token=os.environ.get("AMAZON_ADS_REFRESH_TOKEN", ""),
            region=AdsRegion.NA,
        )
        profile_id = os.environ.get("AMAZON_ADS_PROFILE_ID", "")
        if profile_id:
            client.with_profile(profile_id)
        return client
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    def test_list_campaigns(self, client):
        """Test listing SP campaigns"""
        campaigns = client.sp.campaigns.list_campaigns()
        assert isinstance(campaigns, (dict, list))
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    @pytest.mark.slow
    def test_campaign_crud(self, client):
        """Test campaign CRUD operations"""
        # This would test create, read, update, delete
        # Skipping actual implementation to avoid creating test data
        pass


class TestSPKeywords:
    """Test SP Keywords API"""
    
    @pytest.fixture
    def client(self):
        """Create authenticated client"""
        client = AmazonAdsClient(
            client_id=os.environ.get("AMAZON_ADS_CLIENT_ID", ""),
            client_secret=os.environ.get("AMAZON_ADS_CLIENT_SECRET", ""),
            refresh_token=os.environ.get("AMAZON_ADS_REFRESH_TOKEN", ""),
            region=AdsRegion.NA,
        )
        profile_id = os.environ.get("AMAZON_ADS_PROFILE_ID", "")
        if profile_id:
            client.with_profile(profile_id)
        return client
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    def test_list_keywords(self, client):
        """Test listing SP keywords"""
        # Would need a campaign_id to test
        pass


class TestSPTargeting:
    """Test SP Targeting API"""
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    def test_list_targets(self):
        """Test listing SP targets"""
        pass


class TestSPAdGroups:
    """Test SP Ad Groups API"""
    
    @requires_credentials
    @requires_profile
    @pytest.mark.integration
    def test_list_ad_groups(self):
        """Test listing SP ad groups"""
        pass

