"""Auto-generated async API client. Do not edit manually.

Source: SponsoredProducts_prod_3p.json
Title:  Sponsored Products
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_sp import *  # noqa: F403
except ImportError:
    pass


class SpClient(BaseAdsClient):
    """Auto-generated from SponsoredProducts_prod_3p.json (80 operations)"""

    async def create_sponsored_products_ad_groups(self, body: SponsoredProductsCreateSponsoredProductsAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/adGroups

        Create ad groups  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/adGroups"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spAdGroup.v3+json")

    async def update_sponsored_products_ad_groups(self, body: SponsoredProductsUpdateSponsoredProductsAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /sp/adGroups

        Update ad groups  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/adGroups"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spAdGroup.v3+json")

    async def delete_sponsored_products_ad_groups(self, body: SponsoredProductsDeleteSponsoredProductsAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/adGroups/delete

        Delete ad groups  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/adGroups/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spAdGroup.v3+json")

    async def list_sponsored_products_ad_groups(self, body: SponsoredProductsListSponsoredProductsAdGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/adGroups/list

        List ad groups  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/sp/adGroups/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spAdGroup.v3+json")

    async def get_sp_budget_rules_for_advertiser(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_token: str | None = None, page_size: str | None = None) -> JSONData | JSONList:
        """GET /sp/budgetRules

        Get all budget rules created by an advertiser
        """
        endpoint = "/sp/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_token is not None:
            params["nextToken"] = next_token
        if page_size is not None:
            params["pageSize"] = page_size
        return await self.get(endpoint, params=params)

    async def create_budget_rules_for_sp_campaigns(self, body: CreateSPBudgetRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/budgetRules

        Creates one or more budget rules.
        """
        endpoint = "/sp/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def update_budget_rules_for_sp_campaigns(self, body: UpdateSPBudgetRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sp/budgetRules

        Updates one or more budget rules.
        """
        endpoint = "/sp/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params)

    async def get_budget_rule_by_rule_id_for_sp_campaigns(self, budget_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sp/budgetRules/{budgetRuleId}

        Gets a budget rule specified by identifier.
        """
        endpoint = f"/sp/budgetRules/{budget_rule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def get_campaigns_associated_with_sp_budget_rule(self, budget_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_token: str | None = None, page_size: str | None = None) -> JSONData | JSONList:
        """GET /sp/budgetRules/{budgetRuleId}/campaigns

        Gets all the campaigns associated with a budget rule
        """
        endpoint = f"/sp/budgetRules/{budget_rule_id}/campaigns"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_token is not None:
            params["nextToken"] = next_token
        if page_size is not None:
            params["pageSize"] = page_size
        return await self.get(endpoint, params=params)

    async def bulk_budget_rules_association_for_sp(self, body: BulkBudgetRulesAssociationRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/budgetRulesAssociation

        Associates budget rules to one or more campaigns.
        """
        endpoint = "/sp/budgetRulesAssociation"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def bulk_budget_rules_dis_association_for_sp(self, body: BulkBudgetRulesDisAssociationRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/budgetRulesAssociation/delete

        DisAssociates budget rules from one or more campaigns
        """
        endpoint = "/sp/budgetRulesAssociation/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def get_campaign_recommendations(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, campaign_ids: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /sp/campaign/recommendations

        Gets the top consolidated recommendations across bid, budget, targeting for SP campaigns given an advertiser profile id.
        """
        endpoint = "/sp/campaign/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if campaign_ids is not None:
            params["campaignIds"] = campaign_ids
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def fetch_campaign_recommendations(self, body: GetCampaignRecommendationsRequestV2 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaign/recommendations

        Gets the top consolidated recommendations across bid, budget, targeting for SP campaigns given an advertiser profile id.
        """
        endpoint = "/sp/campaign/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spgetcampaignrecommendationsrequest.v2+json")

    async def create_sponsored_products_campaign_negative_keywords(self, body: SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaignNegativeKeywords

        Create campaign negative keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed
        """
        endpoint = "/sp/campaignNegativeKeywords"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaignNegativeKeyword.v3+json")

    async def update_sponsored_products_campaign_negative_keywords(self, body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /sp/campaignNegativeKeywords

        Update campaign negative keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed
        """
        endpoint = "/sp/campaignNegativeKeywords"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaignNegativeKeyword.v3+json")

    async def delete_sponsored_products_campaign_negative_keywords(self, body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaignNegativeKeywords/delete

        Delete campaign negative keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed
        """
        endpoint = "/sp/campaignNegativeKeywords/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaignNegativeKeyword.v3+json")

    async def list_sponsored_products_campaign_negative_keywords(self, body: SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaignNegativeKeywords/list

        List campaign negative keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign
        """
        endpoint = "/sp/campaignNegativeKeywords/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaignNegativeKeyword.v3+json")

    async def create_sponsored_products_campaign_negative_targeting_clauses(self, body: SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaignNegativeTargets

        Create campaign negative targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign
        """
        endpoint = "/sp/campaignNegativeTargets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaignNegativeTargetingClause.v3+json")

    async def update_sponsored_products_campaign_negative_targeting_clauses(self, body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /sp/campaignNegativeTargets

        Update campaign negative targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign
        """
        endpoint = "/sp/campaignNegativeTargets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaignNegativeTargetingClause.v3+json")

    async def delete_sponsored_products_campaign_negative_targeting_clauses(self, body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaignNegativeTargets/delete

        Delete campaign negative targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign
        """
        endpoint = "/sp/campaignNegativeTargets/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaignNegativeTargetingClause.v3+json")

    async def list_sponsored_products_campaign_negative_targeting_clauses(self, body: SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaignNegativeTargets/list

        List campaign negative targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser
        """
        endpoint = "/sp/campaignNegativeTargets/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaignNegativeTargetingClause.v3+json")

    async def create_sponsored_products_campaigns(self, body: SponsoredProductsCreateSponsoredProductsCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaigns

        Create campaigns  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/campaigns"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaign.v3+json")

    async def update_sponsored_products_campaigns(self, body: SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /sp/campaigns

        Update campaigns  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/campaigns"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaign.v3+json")

    async def sp_campaigns_budget_usage(self, body: BudgetUsageCampaignRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaigns/budget/usage

        Budget usage API for SP campaigns
        """
        endpoint = "/sp/campaigns/budget/usage"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spcampaignbudgetusage.v1+json")

    async def get_budget_recommendations(self, body: BudgetRecommendationRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaigns/budgetRecommendations

        Get recommended daily budget and estimated missed opportunities for campaigns.
        """
        endpoint = "/sp/campaigns/budgetRecommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.budgetrecommendation.v3+json")

    async def sp_get_budget_rules_recommendation(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaigns/budgetRules/recommendations

        Gets a list of special events with suggested date range and suggested budget increase for a campaign specified by identi
        """
        endpoint = "/sp/campaigns/budgetRules/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spbudgetrulesrecommendation.v3+json")

    async def delete_sponsored_products_campaigns(self, body: SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaigns/delete

        Delete campaigns  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/campaigns/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaign.v3+json")

    async def get_budget_recommendation(self, body: InitialBudgetRecommendationRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaigns/initialBudgetRecommendation

        Creates daily budget recommendation along with benchmark metrics when creating a new campaign.
        """
        endpoint = "/sp/campaigns/initialBudgetRecommendation"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spinitialbudgetrecommendation.v3.4+json")

    async def list_sponsored_products_campaigns(self, body: SponsoredProductsListSponsoredProductsCampaignsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaigns/list

        List campaigns  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/sp/campaigns/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spCampaign.v3+json")

    async def list_associated_budget_rules_for_sp_campaigns(self, campaign_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sp/campaigns/{campaignId}/budgetRules

        Gets a list of budget rules associated to a campaign specified by identifier.
        """
        endpoint = f"/sp/campaigns/{campaign_id}/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def create_associated_budget_rules_for_sp_campaigns(self, campaign_id: str, body: CreateAssociatedBudgetRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaigns/{campaignId}/budgetRules

        Associates one or more budget rules to a campaign specified by identifer.
        """
        endpoint = f"/sp/campaigns/{campaign_id}/budgetRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def disassociate_associated_budget_rule_for_sp_campaigns(self, campaign_id: str, budget_rule_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sp/campaigns/{campaignId}/budgetRules/{budgetRuleId}

        Disassociates a budget rule specified by identifier from a campaign specified by identifier.
        """
        endpoint = f"/sp/campaigns/{campaign_id}/budgetRules/{budget_rule_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def associate_optimization_rules_to_campaign(self, campaign_id: str, body: OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/campaigns/{campaignId}/optimizationRules

        Associates one or multiple optimization rules with a campaign.
        """
        endpoint = f"/sp/campaigns/{campaign_id}/optimizationRules"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spoptimizationrules.v1+json")

    async def get_multi_country_theme_based_bid_recommendation_for_ad_group_v1(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /sp/global/targets/bid/recommendations

        Get bid recommendations for multi-country ad groups
        """
        endpoint = "/sp/global/targets/bid/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

    async def get_global_ranked_keyword_recommendation(self, body: dict[str, Any] | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /sp/global/targets/keywords/recommendations/list

        Get global keyword recommendations
        """
        endpoint = "/sp/global/targets/keywords/recommendations/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spkeywordsrecommendation.v5+json")

    async def create_sponsored_products_keywords(self, body: SponsoredProductsCreateSponsoredProductsKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/keywords

        Create keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/keywords"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spKeyword.v3+json")

    async def update_sponsored_products_keywords(self, body: SponsoredProductsUpdateSponsoredProductsKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /sp/keywords

        Update keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/keywords"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spKeyword.v3+json")

    async def delete_sponsored_products_keywords(self, body: SponsoredProductsDeleteSponsoredProductsKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/keywords/delete

        Delete keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/keywords/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spKeyword.v3+json")

    async def list_sponsored_products_keywords(self, body: SponsoredProductsListSponsoredProductsKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/keywords/list

        List keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/keywords/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spKeyword.v3+json")

    async def create_sponsored_products_negative_keywords(self, body: SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/negativeKeywords

        Create negative keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/negativeKeywords"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spNegativeKeyword.v3+json")

    async def update_sponsored_products_negative_keywords(self, body: SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /sp/negativeKeywords

        Update negative keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/negativeKeywords"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spNegativeKeyword.v3+json")

    async def delete_sponsored_products_negative_keywords(self, body: SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/negativeKeywords/delete

        Delete negative keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/negativeKeywords/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spNegativeKeyword.v3+json")

    async def list_sponsored_products_negative_keywords(self, body: SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/negativeKeywords/list

        List negative keywords  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/sp/negativeKeywords/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spNegativeKeyword.v3+json")

    async def create_sponsored_products_negative_targeting_clauses(self, body: SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/negativeTargets

        Create negative targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed
        """
        endpoint = "/sp/negativeTargets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spNegativeTargetingClause.v3+json")

    async def update_sponsored_products_negative_targeting_clauses(self, body: SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /sp/negativeTargets

        Update negative targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed
        """
        endpoint = "/sp/negativeTargets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spNegativeTargetingClause.v3+json")

    async def get_negative_brands(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """GET /sp/negativeTargets/brands/recommendations

        Returns brands recommended for negative targeting.
        """
        endpoint = "/sp/negativeTargets/brands/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        return await self.get(endpoint, params=params)

    async def search_brands(self, body: SearchBrandsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/negativeTargets/brands/search

        Returns brands related to keyword input for negative targeting.
        """
        endpoint = "/sp/negativeTargets/brands/search"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spproducttargeting.v3+json")

    async def delete_sponsored_products_negative_targeting_clauses(self, body: SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/negativeTargets/delete

        Delete negative targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed
        """
        endpoint = "/sp/negativeTargets/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spNegativeTargetingClause.v3+json")

    async def list_sponsored_products_negative_targeting_clauses(self, body: SponsoredProductsListSponsoredProductsNegativeTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/negativeTargets/list

        List negative targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign
        """
        endpoint = "/sp/negativeTargets/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spNegativeTargetingClause.v3+json")

    async def create_sponsored_products_product_ads(self, body: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/productAds

        Create product ads  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/productAds"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spProductAd.v3+json")

    async def update_sponsored_products_product_ads(self, body: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /sp/productAds

        Update product ads  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/productAds"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spProductAd.v3+json")

    async def delete_sponsored_products_product_ads(self, body: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/productAds/delete

        Delete product ads  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/productAds/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spProductAd.v3+json")

    async def list_sponsored_products_product_ads(self, body: SponsoredProductsListSponsoredProductsProductAdsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/productAds/list

        List product ads  **Requires one of these permissions**: ['advertiser_campaign_edit','advertiser_campaign_view']
        """
        endpoint = "/sp/productAds/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spProductAd.v3+json")

    async def create_optimization_rule(self, body: CreateSPCampaignOptimizationRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/rules/campaignOptimization

        Creates a campaign optimization rule.
        """
        endpoint = "/sp/rules/campaignOptimization"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.optimizationrules.v1+json")

    async def update_optimization_rule(self, body: UpdateSPCampaignOptimizationRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sp/rules/campaignOptimization

        Updates a campaign optimization rule.
        """
        endpoint = "/sp/rules/campaignOptimization"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.optimizationrules.v1+json")

    async def get_optimization_rule_eligibility(self, body: SPCampaignOptimizationRecommendationsAPIRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/rules/campaignOptimization/eligibility

        Gets a campaign optimization rule eligibility for SP campaigns.
        """
        endpoint = "/sp/rules/campaignOptimization/eligibility"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.optimizationrules.v1+json")

    async def get_rule_notification(self, body: SPCampaignOptimizationNotificationAPIRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/rules/campaignOptimization/state

        Gets campaign optimization rule state. Recommended refresh frequency is once a day.
        """
        endpoint = "/sp/rules/campaignOptimization/state"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.optimizationrules.v1+json")

    async def delete_campaign_optimization_rule(self, campaign_optimization_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """DELETE /sp/rules/campaignOptimization/{campaignOptimizationId}

        Deletes a campaign optimization rule specified by identifier.
        """
        endpoint = f"/sp/rules/campaignOptimization/{campaign_optimization_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.delete(endpoint, params=params)

    async def get_campaign_optimization_rule(self, campaign_optimization_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """GET /sp/rules/campaignOptimization/{campaignOptimizationId}

        Gets a campaign optimization rule specified by identifier.
        """
        endpoint = f"/sp/rules/campaignOptimization/{campaign_optimization_id}"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        return await self.get(endpoint, params=params)

    async def create_optimization_rules(self, body: OptimizationRulesAPISwaggerCreateOptimizationRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/rules/optimization

        Creates one or more optimization rules.
        """
        endpoint = "/sp/rules/optimization"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spoptimizationrules.v1+json")

    async def update_optimization_rules(self, body: OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /sp/rules/optimization

        Updates one or more optimization rules.
        """
        endpoint = "/sp/rules/optimization"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spoptimizationrules.v1+json")

    async def search_optimization_rules(self, body: OptimizationRulesAPISwaggerSearchOptimizationRulesRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/rules/optimization/search

        Searches optimization rules based on optional filters.
        """
        endpoint = "/sp/rules/optimization/search"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spoptimizationrules.v1+json")

    async def create_target_promotion_groups(self, body: SponsoredProductsCreateTargetPromotionGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targetPromotionGroups

        Creates a target promotion group, by grouping the auto-targeting adGroupId and manual-targeting adGroups, divided by key
        """
        endpoint = "/sp/targetPromotionGroups"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sptargetpromotiongroup.v1+json")

    async def list_target_promotion_groups(self, body: SponsoredProductsListTargetPromotionGroupsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targetPromotionGroups/list

        Returns the target promotion groups for an advertiser and / or adGroupId, and / or target promotion group id.  **Require
        """
        endpoint = "/sp/targetPromotionGroups/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sptargetpromotiongroup.v1+json")

    async def get_target_promotion_groups_recommendations(self, body: SponsoredProductsGetTargetPromotionGroupsRecommendationsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targetPromotionGroups/recommendations

        Retrieves keyword and product targets of an auto-targeting campaign as recommendations for promoting to a manual-targeti
        """
        endpoint = "/sp/targetPromotionGroups/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spTargetPromotionGroupsRecommendations.v1+json")

    async def create_target_promotion_group_targets(self, body: SponsoredProductsCreateTargetPromotionGroupTargetsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targetPromotionGroups/targets

        Creates keyword and/or product targets in the manual adGroup that are part of the target promotion group  **Requires one
        """
        endpoint = "/sp/targetPromotionGroups/targets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sptargetpromotiongrouptarget.v1+json")

    async def list_target_promotion_group_targets(self, body: SponsoredProductsListTargetPromotionGroupTargetsRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targetPromotionGroups/targets/list

        Returns the targets created through target promotion groups for an advertiser and / or given target promotion group.  **
        """
        endpoint = "/sp/targetPromotionGroups/targets/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.sptargetpromotiongrouptarget.v1+json")

    async def get_keyword_group_recommendations(self, body: KeywordGroupsRecommendationsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, locale: str | None = None) -> JSONData | JSONList:
        """POST /sp/targeting/recommendations/keywordGroups

        This API (currently beta) recommends Keyword Group targets for a given list of Ad ASINs. Keyword Groups is a new control
        """
        endpoint = "/sp/targeting/recommendations/keywordGroups"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if locale is not None:
            params["locale"] = locale
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spkeywordgroupsrecommendations.v1.0+json")

    async def create_sponsored_products_targeting_clauses(self, body: SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/targets

        Create targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/targets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spTargetingClause.v3+json")

    async def update_sponsored_products_targeting_clauses(self, body: SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """PUT /sp/targets

        Update targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/targets"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.spTargetingClause.v3+json")

    async def get_theme_based_bid_recommendation_for_ad_group_v1(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targets/bid/recommendations

        Get bid recommendations for ad groups
        """
        endpoint = "/sp/targets/bid/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spthemebasedbidrecommendation.v3+json")

    async def get_targetable_categories(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None, locale: str | None = None) -> JSONData | JSONList:
        """GET /sp/targets/categories

        Returns all targetable categories.
        """
        endpoint = "/sp/targets/categories"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        if locale is not None:
            params["locale"] = locale
        return await self.get(endpoint, params=params)

    async def get_category_recommendations_for_asi_ns(self, body: GetCategoryRecommendationsForAsinsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None, locale: str | None = None) -> JSONData | JSONList:
        """POST /sp/targets/categories/recommendations

        Returns a list of category recommendations for the input list of ASINs.
        """
        endpoint = "/sp/targets/categories/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        if locale is not None:
            params["locale"] = locale
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spproducttargeting.v3+json")

    async def get_refinements_for_category(self, category_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None, locale: str | None = None) -> JSONData | JSONList:
        """GET /sp/targets/category/{categoryId}/refinements

        Returns refinements according to category input.
        """
        endpoint = f"/sp/targets/category/{category_id}/refinements"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        if locale is not None:
            params["locale"] = locale
        return await self.get(endpoint, params=params)

    async def delete_sponsored_products_targeting_clauses(self, body: SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targets/delete

        Delete targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/targets/delete"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spTargetingClause.v3+json")

    async def get_ranked_keyword_recommendation(self, body: dict[str, Any] | None = None, amazon_advertising_api_marketplace_id: str | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targets/keywords/recommendations

        Get keyword recommendations
        """
        endpoint = "/sp/targets/keywords/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_marketplace_id is not None:
            params["Amazon-Advertising-API-MarketplaceId"] = amazon_advertising_api_marketplace_id
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spkeywordsrecommendation.v3+json")

    async def list_sponsored_products_targeting_clauses(self, body: SponsoredProductsListSponsoredProductsTargetingClausesRequestContent | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targets/list

        List targeting clauses  **Requires one of these permissions**: ['advertiser_campaign_edit','campaign_proposed']
        """
        endpoint = "/sp/targets/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spTargetingClause.v3+json")

    async def get_targetable_asin_counts(self, body: GetTargetableAsinCountsRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, prefer: str | None = None) -> JSONData | JSONList:
        """POST /sp/targets/products/count

        Get number of targetable asins based on refinements provided by the user.
        """
        endpoint = "/sp/targets/products/count"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if prefer is not None:
            params["Prefer"] = prefer
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spproducttargeting.v3+json")

    async def get_product_recommendations(self, body: GetProductRecommendationsRequest | dict[str, Any] | None = None, amazon_advertising_api_advertiser_id: str | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/targets/products/recommendations

        Suggested target ASINs for your advertised product
        """
        endpoint = "/sp/targets/products/recommendations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_advertiser_id is not None:
            params["Amazon-Advertising-API-AdvertiserId"] = amazon_advertising_api_advertiser_id
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.spproductrecommendation.v3+json")

    async def sp_get_all_rule_events(self, body: SPGetAllRuleEventRequest | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /sp/v1/events

        Gets all special individual and grouped events with suggested date range in advertiser's marketplace.
        """
        endpoint = "/sp/v1/events"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params)

