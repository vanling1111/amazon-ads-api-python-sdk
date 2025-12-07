"""
Integration tests for authentication
Note: These tests require valid credentials
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


class TestAuthentication:
    """Test authentication flow"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_token_refresh(self):
        """Test that token can be refreshed with valid credentials"""
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        
        # If we get here without exception, auth succeeded
        assert client is not None
    
    @requires_credentials
    @pytest.mark.integration
    def test_get_profiles(self):
        """Test getting profiles list"""
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        
        profiles = client.accounts.profiles.list_profiles()
        assert isinstance(profiles, list)


class TestRegions:
    """Test different regions"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_na_region(self):
        """Test North America region"""
        client = AmazonAdsClient(
            client_id=os.environ["AMAZON_ADS_CLIENT_ID"],
            client_secret=os.environ["AMAZON_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["AMAZON_ADS_REFRESH_TOKEN"],
            region=AdsRegion.NA,
        )
        assert client.region == AdsRegion.NA
    
    @pytest.mark.integration
    @pytest.mark.skip(reason="Requires EU credentials")
    def test_eu_region(self):
        """Test Europe region"""
        # Would require EU-specific credentials
        pass
    
    @pytest.mark.integration
    @pytest.mark.skip(reason="Requires FE credentials")
    def test_fe_region(self):
        """Test Far East region"""
        # Would require FE-specific credentials
        pass

