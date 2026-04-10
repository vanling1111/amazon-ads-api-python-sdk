"""Auto-generated async API client. Do not edit manually.

Source: Measurement_prod_3p.json
Title:  Measurement
"""

from __future__ import annotations

from typing import Any  # noqa: F401

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList  # noqa: F401

try:
    from .models_dsp_measurement import *  # noqa: F403
except ImportError:
    pass


class DspMeasurementClient(BaseAdsClient):
    """Auto-generated from Measurement_prod_3p.json (30 operations)"""

    async def check_dsp_audience_research_eligibility(self, body: DSPAudienceResearchEligibilityRequestV1M2 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /dsp/measurement/eligibility/audienceResearch

        Checks the DSP AUDIENCE_RESEARCH study type eligibility against vendor products.
        """
        endpoint = "/dsp/measurement/eligibility/audienceResearch"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.measurementeligibility.v1.2+json")

    async def check_dsp_brand_lift_eligibility(self, body: DSPBrandLiftEligibilityRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /dsp/measurement/eligibility/brandLift

        Checks the DSP BRAND_LIFT study type eligibility against vendor products.
        """
        endpoint = "/dsp/measurement/eligibility/brandLift"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.measurementeligibility.v1+json")

    async def check_dsp_creative_testing_eligibility(self, body: DSPCreativeTestingEligibilityRequestV1M2 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /dsp/measurement/eligibility/creativeTesting

        Checks the DSP CREATIVE_TESTING study type eligibility against vendor products.
        """
        endpoint = "/dsp/measurement/eligibility/creativeTesting"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.measurementeligibility.v1.2+json")

    async def check_dsp_omnichannel_metrics_eligibility(self, body: DSPOmnichannelMetricsEligibilityRequestV1M2 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /dsp/measurement/eligibility/omnichannelMetrics

        Checks the DSP OMNICHANNEL_METRICS study type eligibility against vendor products.
        """
        endpoint = "/dsp/measurement/eligibility/omnichannelMetrics"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.measurementeligibility.v1.2+json")

    async def get_dsp_audience_research_studies(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, study_ids: str | None = None, advertiser_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /dsp/measurement/studies/audienceResearch

        Gets one or more DSP AUDIENCE_RESEARCH studies with requested study identifiers or an advertiser identifier.
        """
        endpoint = "/dsp/measurement/studies/audienceResearch"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if study_ids is not None:
            params["studyIds"] = study_ids
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def create_dsp_audience_research_study(self, body: CreateDSPAudienceResearchStudyV1M2 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/measurement/studies/audienceResearch

        Create new DSP AUDIENCE_RESEARCH study.
        """
        endpoint = "/dsp/measurement/studies/audienceResearch"
        params: dict[str, Any] = {}
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1.2+json")

    async def update_dsp_audience_research_study(self, study_id: str, body: UpdateDSPAudienceResearchStudyV1M2 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/measurement/studies/audienceResearch/{studyId}

        Update DSP AUDIENCE_RESEARCH study. This will be a full update.
        """
        endpoint = f"/dsp/measurement/studies/audienceResearch/{study_id}"
        params: dict[str, Any] = {}
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1.2+json")

    async def get_dsp_audience_research_study_result(self, study_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, accept: str | None = None) -> JSONData | JSONList:
        """GET /dsp/measurement/studies/audienceResearch/{studyId}/result

        Get result of a DSP AUDIENCE_RESEARCH study.
        """
        endpoint = f"/dsp/measurement/studies/audienceResearch/{study_id}/result"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if accept is not None:
            params["Accept"] = accept
        return await self.get(endpoint, params=params)

    async def get_dsp_brand_lift_studies(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, study_id_filters: str | None = None, advertiser_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /dsp/measurement/studies/brandLift

        Gets one or more DSP BRAND_LIFT studies with requested study identifiers or an advertiser identifier.
        """
        endpoint = "/dsp/measurement/studies/brandLift"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if study_id_filters is not None:
            params["studyIdFilters"] = study_id_filters
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def create_dsp_brand_lift_studies(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /dsp/measurement/studies/brandLift

        Create new DSP BRAND_LIFT studies.
        """
        endpoint = "/dsp/measurement/studies/brandLift"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1+json")

    async def update_dsp_brand_lift_studies(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/measurement/studies/brandLift

        Update DSP BRAND_LIFT studies. This will be a full update.
        """
        endpoint = "/dsp/measurement/studies/brandLift"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1+json")

    async def get_dsp_creative_testing_studies(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, study_ids: str | None = None, advertiser_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /dsp/measurement/studies/creativeTesting

        Gets one or more DSP CREATIVE_TESTING studies with requested study identifiers or an advertiser identifier.
        """
        endpoint = "/dsp/measurement/studies/creativeTesting"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if study_ids is not None:
            params["studyIds"] = study_ids
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def create_dsp_creative_testing_study(self, body: CreateDSPCreativeTestingStudyV1M2 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/measurement/studies/creativeTesting

        Create new DSP CREATIVE_TESTING study.
        """
        endpoint = "/dsp/measurement/studies/creativeTesting"
        params: dict[str, Any] = {}
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1.2+json")

    async def update_dsp_creative_testing_study(self, study_id: str, body: UpdateDSPCreativeTestingStudyV1M2 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/measurement/studies/creativeTesting/{studyId}

        Update DSP CREATIVE_TESTING study. This will be a full update.
        """
        endpoint = f"/dsp/measurement/studies/creativeTesting/{study_id}"
        params: dict[str, Any] = {}
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1.2+json")

    async def get_dsp_creative_testing_study_result(self, study_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, accept: str | None = None) -> JSONData | JSONList:
        """GET /dsp/measurement/studies/creativeTesting/{studyId}/result

        Get result of a DSP CREATIVE_TESTING study.
        """
        endpoint = f"/dsp/measurement/studies/creativeTesting/{study_id}/result"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if accept is not None:
            params["Accept"] = accept
        return await self.get(endpoint, params=params)

    async def get_dsp_omnichannel_metrics_studies(self, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, study_ids: str | None = None, advertiser_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /dsp/measurement/studies/omnichannelMetrics

        Gets one or more DSP OMNICHANNEL_METRICS studies with requested study identifiers or an advertiser identifier.
        """
        endpoint = "/dsp/measurement/studies/omnichannelMetrics"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if study_ids is not None:
            params["studyIds"] = study_ids
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def create_dsp_omnichannel_metrics_studies(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /dsp/measurement/studies/omnichannelMetrics

        Create new DSP OMNICHANNEL_METRICS studies.
        """
        endpoint = "/dsp/measurement/studies/omnichannelMetrics"
        params: dict[str, Any] = {}
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1.2+json")

    async def update_dsp_omnichannel_metrics_studies(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """PUT /dsp/measurement/studies/omnichannelMetrics

        Update DSP OMNICHANNEL_METRICS studies. This will be a full update.
        """
        endpoint = "/dsp/measurement/studies/omnichannelMetrics"
        params: dict[str, Any] = {}
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1.2+json")

    async def get_dsp_omnichannel_metrics_study_result(self, study_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, accept: str | None = None) -> JSONData | JSONList:
        """GET /dsp/measurement/studies/omnichannelMetrics/{studyId}/result

        Get result of a DSP OMNICHANNEL_METRICS study.
        """
        endpoint = f"/dsp/measurement/studies/omnichannelMetrics/{study_id}/result"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if accept is not None:
            params["Accept"] = accept
        return await self.get(endpoint, params=params)

    async def check_planning_eligibility(self, body: PlanningEligibilityRequestV1M3 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /measurement/planning/eligibility

        Checks eligibility against all vendor products.
        """
        endpoint = "/measurement/planning/eligibility"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.measurementeligibility.v1.1+json")

    async def cancel_measurement_studies(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, study_ids: str | None = None) -> JSONData | JSONList:
        """DELETE /measurement/studies

        Cancel existing studies. Once a study is cancelled it can not be resumed again.
        """
        endpoint = "/measurement/studies"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if study_ids is not None:
            params["studyIds"] = study_ids
        return await self.delete(endpoint, params=params)

    async def get_studies(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, study_ids: str | None = None, advertiser_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /measurement/studies

        Gets base study objects given a list of studyIds or a list of advertiserIds.
        """
        endpoint = "/measurement/studies"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if study_ids is not None:
            params["studyIds"] = study_ids
        if advertiser_id is not None:
            params["advertiserId"] = advertiser_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def get_dsp_brand_lift_study_result(self, study_id: str, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, accept: str | None = None) -> JSONData | JSONList:
        """GET /measurement/studies/brandLift/{studyId}/result

        Get result of a DSP BRAND_LIFT study.
        """
        endpoint = f"/measurement/studies/brandLift/{study_id}/result"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if accept is not None:
            params["Accept"] = accept
        return await self.get(endpoint, params=params)

    async def get_surveys(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, survey_ids: str | None = None, study_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /measurement/studies/surveys

        Gets one or more study surveys with requested survey identifiers or a study identifier.
        """
        endpoint = "/measurement/studies/surveys"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if survey_ids is not None:
            params["surveyIds"] = survey_ids
        if study_id is not None:
            params["studyId"] = study_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def create_surveys(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """POST /measurement/studies/surveys

        Create new study surveys.
        """
        endpoint = "/measurement/studies/surveys"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1+json")

    async def update_surveys(self, body: dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None) -> JSONData | JSONList:
        """PUT /measurement/studies/surveys

        Update measurement surveys. This will be a full update.
        """
        endpoint = "/measurement/studies/surveys"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.studymanagement.v1+json")

    async def vendor_product(self, body: VendorProductRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /measurement/vendorProducts/list

        Lists the supported measurement vendor products.
        """
        endpoint = "/measurement/vendorProducts/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.measurementvendor.v1+json")

    async def omnichannel_metrics_brand_search(self, body: OmnichannelMetricsBrandSearchRequestV1M2 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """POST /measurement/vendorProducts/omnichannelMetrics/brands/list

        Search for brands to be used in the OMNICHANNEL_METRICS vendor product.
        """
        endpoint = "/measurement/vendorProducts/omnichannelMetrics/brands/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.ocmbrands.v1.2+json")

    async def vendor_product_policy(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, vendor_product_ids: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /measurement/vendorProducts/policies

        Gets the policies for the specific vendor product(s).
        """
        endpoint = "/measurement/vendorProducts/policies"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if vendor_product_ids is not None:
            params["vendorProductIds"] = vendor_product_ids
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

    async def vendor_product_survey_question_templates(self, amazon_advertising_api_client_id: str | None = None, amazon_ads_account_id: str | None = None, amazon_advertising_api_scope: str | None = None, vendor_product_ids: str | None = None, survey_question_template_ids: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /measurement/vendorProducts/surveyQuestionTemplates

        Gets the survey question templates for the specific vendor product(s).
        """
        endpoint = "/measurement/vendorProducts/surveyQuestionTemplates"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if vendor_product_ids is not None:
            params["vendorProductIds"] = vendor_product_ids
        if survey_question_template_ids is not None:
            params["surveyQuestionTemplateIds"] = survey_question_template_ids
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        return await self.get(endpoint, params=params)

