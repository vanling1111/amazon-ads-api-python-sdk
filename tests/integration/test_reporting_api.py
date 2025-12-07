"""
Integration tests for Reporting API
Note: These tests require valid credentials:
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


class TestReportsV3Integration:
    """Integration tests for Reports V3 API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_create_report(self, client):
        """Test creating a report"""
        # Create a simple SP campaigns report
        try:
            result = client.reporting.reports.create_report(
                report_type="spCampaigns",
                time_unit="SUMMARY",
                start_date="20240101",
                end_date="20240131",
                metrics=["impressions", "clicks", "spend"],
            )
            
            assert isinstance(result, dict)
            assert "reportId" in result or "status" in result
        except AmazonAdsError as e:
            # 400 might happen if no data for date range
            assert e.status_code == 400
    
    @requires_credentials
    @pytest.mark.integration
    @pytest.mark.slow
    def test_create_and_check_report_status(self, client):
        """Test creating a report and checking its status"""
        # Create report
        try:
            create_result = client.reporting.reports.create_report(
                report_type="spCampaigns",
                time_unit="SUMMARY",
                start_date="20240101",
                end_date="20240131",
                metrics=["impressions", "clicks", "spend"],
            )
            
            if "reportId" not in create_result:
                pytest.skip("Report creation did not return reportId")
            
            report_id = create_result["reportId"]
            
            # Check status
            status_result = client.reporting.reports.get_report(report_id)
            
            assert isinstance(status_result, dict)
            assert "status" in status_result
            assert status_result["status"] in ["IN_PROGRESS", "COMPLETED", "FAILED"]
            
        except AmazonAdsError as e:
            # 400 might happen if no data
            if e.status_code != 400:
                raise


class TestBrandMetricsIntegration:
    """Integration tests for Brand Metrics API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_brand_metrics_api_accessible(self, client):
        """Test that Brand Metrics API is accessible"""
        # Just verify we can call the API without auth errors
        try:
            result = client.reporting.brand_metrics.get_brand_metrics(
                brand_entity_id="test",
                start_date="2024-01-01",
                end_date="2024-01-31",
            )
            assert isinstance(result, dict)
        except AmazonAdsError as e:
            # 400/404 is expected for invalid brand entity
            assert e.status_code in [400, 404]


class TestStoresAnalyticsIntegration:
    """Integration tests for Stores Analytics API"""
    
    @requires_credentials
    @pytest.mark.integration
    def test_stores_analytics_api_accessible(self, client):
        """Test that Stores Analytics API is accessible"""
        try:
            result = client.reporting.stores_analytics.get_stores_report(
                store_id="test",
                start_date="2024-01-01",
                end_date="2024-01-31",
            )
            assert isinstance(result, dict)
        except AmazonAdsError as e:
            # 400/404 is expected for invalid store
            assert e.status_code in [400, 404]

