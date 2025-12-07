"""
Unit tests for all API modules
"""
import pytest
from unittest.mock import patch, MagicMock


class TestSBModule:
    """Test SB (Sponsored Brands) module imports"""
    
    @pytest.mark.unit
    def test_sb_imports(self):
        """Test all SB classes can be imported"""
        from amazon_ads_api.sb import (
            SBCampaignsAPI, SBAdsAPI, SBKeywordsAPI, 
            SBCreativesAPI, SBBrandVideoAPI, SBModerationAPI
        )
        assert SBCampaignsAPI is not None
        assert SBAdsAPI is not None
        assert SBKeywordsAPI is not None
        assert SBCreativesAPI is not None
        assert SBBrandVideoAPI is not None
        assert SBModerationAPI is not None


class TestSDModule:
    """Test SD (Sponsored Display) module imports"""
    
    @pytest.mark.unit
    def test_sd_imports(self):
        """Test all SD classes can be imported"""
        from amazon_ads_api.sd import (
            SDCampaignsAPI, SDTargetingAPI, SDCreativesAPI,
            SDAudiencesAPI, SDModerationAPI
        )
        assert SDCampaignsAPI is not None
        assert SDTargetingAPI is not None
        assert SDCreativesAPI is not None
        assert SDAudiencesAPI is not None
        assert SDModerationAPI is not None


class TestDSPModule:
    """Test DSP module imports"""
    
    @pytest.mark.unit
    def test_dsp_imports(self):
        """Test all DSP classes can be imported"""
        from amazon_ads_api.dsp import (
            DSPAudiencesAPI, DSPAdvertisersAPI, DSPOrdersAPI, DSPLineItemsAPI,
            DSPCreativesAPI, DSPInventoryAPI, DSPMeasurementAPI,
            DSPConversionsAPI, DSPTargetKPIAPI
        )
        assert DSPAudiencesAPI is not None
        assert DSPAdvertisersAPI is not None
        assert DSPOrdersAPI is not None
        assert DSPLineItemsAPI is not None
        assert DSPCreativesAPI is not None
        assert DSPInventoryAPI is not None
        assert DSPMeasurementAPI is not None
        assert DSPConversionsAPI is not None
        assert DSPTargetKPIAPI is not None


class TestReportingModule:
    """Test Reporting module imports"""
    
    @pytest.mark.unit
    def test_reporting_imports(self):
        """Test all Reporting classes can be imported"""
        from amazon_ads_api.reporting import (
            ReportsV3API, BrandMetricsAPI, StoresAnalyticsAPI, MarketingMixModelingAPI
        )
        assert ReportsV3API is not None
        assert BrandMetricsAPI is not None
        assert StoresAnalyticsAPI is not None
        assert MarketingMixModelingAPI is not None


class TestAccountsModule:
    """Test Accounts module imports"""
    
    @pytest.mark.unit
    def test_accounts_imports(self):
        """Test all Accounts classes can be imported"""
        from amazon_ads_api.accounts import (
            ProfilesAPI, PortfoliosAPI, BillingAPI, AccountBudgetsAPI, TestAccountsAPI
        )
        assert ProfilesAPI is not None
        assert PortfoliosAPI is not None
        assert BillingAPI is not None
        assert AccountBudgetsAPI is not None
        assert TestAccountsAPI is not None


class TestInsightsModule:
    """Test Insights module imports"""
    
    @pytest.mark.unit
    def test_insights_imports(self):
        """Test all Insights classes can be imported"""
        from amazon_ads_api.insights import (
            CategoryInsightsAPI, KeywordInsightsAPI, AudienceInsightsAPI
        )
        assert CategoryInsightsAPI is not None
        assert KeywordInsightsAPI is not None
        assert AudienceInsightsAPI is not None


class TestAMCModule:
    """Test AMC module imports"""
    
    @pytest.mark.unit
    def test_amc_imports(self):
        """Test all AMC classes can be imported"""
        from amazon_ads_api.amc import (
            AMCQueriesAPI, AMCAudiencesAPI, AMCWorkflowsAPI
        )
        assert AMCQueriesAPI is not None
        assert AMCAudiencesAPI is not None
        assert AMCWorkflowsAPI is not None


class TestSponsoredTVModule:
    """Test Sponsored TV module imports"""
    
    @pytest.mark.unit
    def test_sponsored_tv_imports(self):
        """Test all Sponsored TV classes can be imported"""
        from amazon_ads_api.sponsored_tv import (
            SponsoredTVCampaignsAPI, SponsoredTVAdGroupsAPI, SponsoredTVAdsAPI,
            SponsoredTVCreativesAPI, SponsoredTVTargetingAPI
        )
        assert SponsoredTVCampaignsAPI is not None
        assert SponsoredTVAdGroupsAPI is not None
        assert SponsoredTVAdsAPI is not None
        assert SponsoredTVCreativesAPI is not None
        assert SponsoredTVTargetingAPI is not None


class TestRASModule:
    """Test Retail Ad Service module imports"""
    
    @pytest.mark.unit
    def test_ras_imports(self):
        """Test all RAS classes can be imported"""
        from amazon_ads_api.retail_ad_service import (
            RASCampaignsAPI, RASAdGroupsAPI, RASProductAdsAPI, RASTargetsAPI
        )
        assert RASCampaignsAPI is not None
        assert RASAdGroupsAPI is not None
        assert RASProductAdsAPI is not None
        assert RASTargetsAPI is not None


class TestAmazonAdsV1Module:
    """Test Amazon Ads V1 module imports"""
    
    @pytest.mark.unit
    def test_ads_v1_imports(self):
        """Test all Amazon Ads V1 classes can be imported"""
        from amazon_ads_api.amazon_ads_v1 import (
            AmazonAdsV1API, AdAssociationsAPI, AdGroupsAPI, AdsAPI, CampaignsAPI,
            TargetsAPI, RecommendationsAPI, AdvertisingDealsAPI, AdvertisingDealTargetsAPI,
            BrandedKeywordsPricingsAPI, CampaignForecastsAPI, CommitmentsAPI,
            CommitmentSpendsAPI, KeywordReservationValidationsAPI, RecommendationTypesAPI
        )
        assert AmazonAdsV1API is not None
        assert AdAssociationsAPI is not None
        assert AdGroupsAPI is not None
        assert AdsAPI is not None
        assert CampaignsAPI is not None
        assert TargetsAPI is not None
        assert RecommendationsAPI is not None
        assert AdvertisingDealsAPI is not None
        assert AdvertisingDealTargetsAPI is not None
        assert BrandedKeywordsPricingsAPI is not None
        assert CampaignForecastsAPI is not None
        assert CommitmentsAPI is not None
        assert CommitmentSpendsAPI is not None
        assert KeywordReservationValidationsAPI is not None
        assert RecommendationTypesAPI is not None


class TestOtherModules:
    """Test other module imports"""
    
    @pytest.mark.unit
    def test_eligibility_import(self):
        """Test Eligibility API import"""
        from amazon_ads_api.eligibility import EligibilityAPI
        assert EligibilityAPI is not None
    
    @pytest.mark.unit
    def test_locations_import(self):
        """Test Locations API import"""
        from amazon_ads_api.locations import LocationsAPI
        assert LocationsAPI is not None
    
    @pytest.mark.unit
    def test_exports_import(self):
        """Test Exports API import"""
        from amazon_ads_api.exports import ExportsAPI
        assert ExportsAPI is not None
    
    @pytest.mark.unit
    def test_stream_import(self):
        """Test Stream API import"""
        from amazon_ads_api.stream import MarketingStreamAPI
        assert MarketingStreamAPI is not None
    
    @pytest.mark.unit
    def test_media_planning_import(self):
        """Test Media Planning API import"""
        from amazon_ads_api.media_planning import ReachForecastingAPI
        assert ReachForecastingAPI is not None
    
    @pytest.mark.unit
    def test_manager_accounts_import(self):
        """Test Manager Accounts API import"""
        from amazon_ads_api.manager_accounts import ManagerAccountsAPI
        assert ManagerAccountsAPI is not None
    
    @pytest.mark.unit
    def test_posts_import(self):
        """Test Posts API import"""
        from amazon_ads_api.posts import PostsAPI
        assert PostsAPI is not None
    
    @pytest.mark.unit
    def test_product_metadata_import(self):
        """Test Product Metadata API import"""
        from amazon_ads_api.product_metadata import ProductMetadataAPI
        assert ProductMetadataAPI is not None
    
    @pytest.mark.unit
    def test_audiences_discovery_import(self):
        """Test Audiences Discovery API import"""
        from amazon_ads_api.audiences_discovery import AudiencesDiscoveryAPI
        assert AudiencesDiscoveryAPI is not None
    
    @pytest.mark.unit
    def test_ad_library_import(self):
        """Test Ad Library API import"""
        from amazon_ads_api.ad_library import AdLibraryAPI, AdType, NameMatchType
        assert AdLibraryAPI is not None
        assert AdType is not None
        assert NameMatchType is not None
    
    @pytest.mark.unit
    def test_brand_home_import(self):
        """Test Brand Home API import"""
        from amazon_ads_api.brand_home import BrandHomeAPI
        assert BrandHomeAPI is not None
    
    @pytest.mark.unit
    def test_localization_import(self):
        """Test Localization API import"""
        from amazon_ads_api.localization import LocalizationAPI
        assert LocalizationAPI is not None
    
    @pytest.mark.unit
    def test_ads_data_manager_import(self):
        """Test Ads Data Manager API import"""
        from amazon_ads_api.ads_data_manager import AdsDataManagerAPI
        assert AdsDataManagerAPI is not None
    
    @pytest.mark.unit
    def test_brand_associations_import(self):
        """Test Brand Associations API import"""
        from amazon_ads_api.brand_associations import BrandAssociationsAPI
        assert BrandAssociationsAPI is not None
    
    @pytest.mark.unit
    def test_common_module_imports(self):
        """Test Common module imports"""
        from amazon_ads_api.common import (
            AttributionAPI, StoresAPI, AssetsAPI, HistoryAPI
        )
        assert AttributionAPI is not None
        assert StoresAPI is not None
        assert AssetsAPI is not None
        assert HistoryAPI is not None
    
    @pytest.mark.unit
    def test_recommendations_module_imports(self):
        """Test Recommendations module imports"""
        from amazon_ads_api.recommendations import (
            PartnerOpportunitiesAPI, TacticalRecommendationsAPI, PersonaBuilderAPI
        )
        assert PartnerOpportunitiesAPI is not None
        assert TacticalRecommendationsAPI is not None
        assert PersonaBuilderAPI is not None
    
    @pytest.mark.unit
    def test_data_provider_imports(self):
        """Test Data Provider module imports"""
        from amazon_ads_api.data_provider import (
            DataProviderMetadataAPI, DataProviderRecordsAPI, HashedRecordsAPI
        )
        assert DataProviderMetadataAPI is not None
        assert DataProviderRecordsAPI is not None
        assert HashedRecordsAPI is not None
    
    @pytest.mark.unit
    def test_products_import(self):
        """Test Products API import"""
        from amazon_ads_api.products import ProductSelectorAPI
        assert ProductSelectorAPI is not None
    
    @pytest.mark.unit
    def test_moderation_imports(self):
        """Test Moderation module imports"""
        from amazon_ads_api.moderation import PreModerationAPI, UnifiedModerationAPI
        assert PreModerationAPI is not None
        assert UnifiedModerationAPI is not None

