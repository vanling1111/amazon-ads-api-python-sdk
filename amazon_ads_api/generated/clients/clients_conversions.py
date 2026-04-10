"""Auto-generated async API client. Do not edit manually.

Source: ConversionsAPI_prod_3p.json
Title:  Conversions API
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .models_conversions import *  # noqa: F403
except ImportError:
    pass


class ConversionsClient(BaseAdsClient):
    """Auto-generated from ConversionsAPI_prod_3p.json (17 operations)"""

    async def dsp_amazon_ad_tag_get_events_by_ad_tag_id(self, account_id: str, ad_tag_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None, search_term: str | None = None, start_date_time: str | None = None, next_token: str | None = None, max_results: str | None = None, end_date_time: str | None = None) -> JSONData | JSONList:
        """GET /accounts/{accountId}/dsp/adTagEvents/{adTagId}/list

        Gets a list of available event metadata for the given ad tag.
        """
        endpoint = f"/accounts/{account_id}/dsp/adTagEvents/{ad_tag_id}/list"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        if search_term is not None:
            params["searchTerm"] = search_term
        if start_date_time is not None:
            params["startDateTime"] = start_date_time
        if next_token is not None:
            params["nextToken"] = next_token
        if max_results is not None:
            params["maxResults"] = max_results
        if end_date_time is not None:
            params["endDateTime"] = end_date_time
        return await self.get(endpoint, params=params)

    async def dsp_amazon_ad_tag_get_ad_tag_by_advertiser_id(self, account_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None) -> JSONData | JSONList:
        """GET /accounts/{accountId}/dsp/amazonAdTag

        Gets an Amazon Ad Tag for a given advertiser
        """
        endpoint = f"/accounts/{account_id}/dsp/amazonAdTag"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        return await self.get(endpoint, params=params)

    async def dsp_amazon_batch_get_conversion_definitions_for_orders(self, account_id: str, body: BatchGetConversionDefinitionsAssociatedForOrdersRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/batchOrders/conversionDefinitionAssociations

        Retrieve associated conversion definitions for orders.
        """
        endpoint = f"/accounts/{account_id}/dsp/batchOrders/conversionDefinitionAssociations"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspbatchgetconversiondefinitions.v1+json")

    async def dsp_amazon_create_conversion_definitions(self, account_id: str, body: BatchCreateConversionDefinitionsRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/conversionDefinitions

        Batch create conversion definitions.
        """
        endpoint = f"/accounts/{account_id}/dsp/conversionDefinitions"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspconversiondefinition.v1+json")

    async def dsp_amazon_update_conversion_definitions(self, account_id: str, body: BatchUpdateConversionDefinitionsRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None) -> JSONData | JSONList:
        """PUT /accounts/{accountId}/dsp/conversionDefinitions

        Batch update conversion definitions.
        """
        endpoint = f"/accounts/{account_id}/dsp/conversionDefinitions"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspconversiondefinition.v1+json")

    async def dsp_amazon_deletion_request(self, account_id: str, body: BatchDeleteUserEventsRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/conversionDefinitions/delete

        Deletes existing event data associated with user(s). Supply all match keys associated with the user. Events processed be
        """
        endpoint = f"/accounts/{account_id}/dsp/conversionDefinitions/delete"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspuserdeletionrequest.v1+json")

    async def dsp_amazon_ingest_conversion_data(self, account_id: str, body: BatchImportConversionEventDataRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/conversionDefinitions/eventData

        Import conversion event data. This API expects one source per request across all conversion event data and supports part
        """
        endpoint = f"/accounts/{account_id}/dsp/conversionDefinitions/eventData"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspconversioneventimport.v1+json")

    async def dsp_amazon_list_conversion_definitions(self, account_id: str, body: ListConversionDefinitionsRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/conversionDefinitions/list

        Retrieve a list of conversion definitions based on filters.
        """
        endpoint = f"/accounts/{account_id}/dsp/conversionDefinitions/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspconversiondefinition.v1+json")

    async def dsp_amazon_get_ad_tag_associated_event(self, account_id: str, conversion_definition_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """GET /accounts/{accountId}/dsp/conversionDefinitions/{conversionDefinitionId}/adTagEventAssociations

        Retrieve associated Amazon adTag event for a ConversionDefinition.
        """
        endpoint = f"/accounts/{account_id}/dsp/conversionDefinitions/{conversion_definition_id}/adTagEventAssociations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        return await self.get(endpoint, params=params)

    async def dsp_amazon_update_ad_tag_associated_event(self, account_id: str, conversion_definition_id: str, body: ConversionDefinitionAdTagEventAssociationRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, amazon_ads_manager_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/conversionDefinitions/{conversionDefinitionId}/adTagEventAssociations

        Associate/Dissociate an Amazon adTag event to a ConversionDefinition.
        """
        endpoint = f"/accounts/{account_id}/dsp/conversionDefinitions/{conversion_definition_id}/adTagEventAssociations"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        if amazon_ads_manager_account_id is not None:
            params["Amazon-Ads-Manager-Account-ID"] = amazon_ads_manager_account_id
        json_data = None
        if body is not None:
            if hasattr(body, 'model_dump'):
                json_data = body.model_dump(by_alias=True, exclude_none=True)
            else:
                json_data = body
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspconversionadtageventassociation.v1+json")

    async def dsp_amazon_get_associated_mobile_app_for_conversion_definition(self, account_id: str, conversion_definition_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """GET /accounts/{accountId}/dsp/conversionDefinitions/{conversionDefinitionId}/mobileMeasurementPartnerAppRegistration

        Retrieve associated Mobile Measurement Partner App for a ConversionDefinition.
        """
        endpoint = f"/accounts/{account_id}/dsp/conversionDefinitions/{conversion_definition_id}/mobileMeasurementPartnerAppRegistration"
        params: dict[str, Any] = {}
        if amazon_advertising_api_client_id is not None:
            params["Amazon-Advertising-API-ClientId"] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            params["Amazon-Advertising-API-Scope"] = amazon_advertising_api_scope
        if amazon_ads_account_id is not None:
            params["Amazon-Ads-AccountId"] = amazon_ads_account_id
        return await self.get(endpoint, params=params)

    async def dsp_amazon_batch_create_mobile_measurement_partner_app_registration(self, account_id: str, body: BatchCreateMobileMeasurementPartnerAppRegistrationRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/mobileMeasurementPartners

        Create a new Mobile Measurement Partner app registration.
        """
        endpoint = f"/accounts/{account_id}/dsp/mobileMeasurementPartners"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspmobilemeasurementpartnerappregistration.v1+json")

    async def dsp_amazon_batch_update_mobile_measurement_partner_app_registration(self, account_id: str, body: BatchUpdateMobileMeasurementPartnerAppRegistrationRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """PUT /accounts/{accountId}/dsp/mobileMeasurementPartners

        Update a Mobile Measurement Partner app registration. Updates may sever the data connection between the Mobile Measureme
        """
        endpoint = f"/accounts/{account_id}/dsp/mobileMeasurementPartners"
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
        return await self.put(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspmobilemeasurementpartnerappregistration.v1+json")

    async def dsp_amazon_delete_measurement_partner_app_registrations(self, account_id: str, body: BatchDeleteMobileMeasurementPartnerAppRegistrationRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/mobileMeasurementPartners/delete

        Marks a Mobile Measurement Partner app registration as deleted. Deleted Mobile Measurement Partner app registrations wil
        """
        endpoint = f"/accounts/{account_id}/dsp/mobileMeasurementPartners/delete"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspmobilemeasurementpartnerappregistration.v1+json")

    async def dsp_amazon_list_mobile_measurement_partner_app_registrations(self, account_id: str, body: ListMobileMeasurementPartnerAppRegistrationsRequestV1 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/mobileMeasurementPartners/list

        List Mobile Measurement Partner App Registrations
        """
        endpoint = f"/accounts/{account_id}/dsp/mobileMeasurementPartners/list"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspmobilemeasurementpartnerappregistration.v1+json")

    async def dsp_amazon_get_associated_conversion_definitions_for_order(self, account_id: str, order_id: str, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None, next_token: str | None = None, max_results: str | None = None) -> JSONData | JSONList:
        """GET /accounts/{accountId}/dsp/orders/{orderId}/conversionDefinitionAssociations

        Retrieve associated conversion definitions for an order.
        """
        endpoint = f"/accounts/{account_id}/dsp/orders/{order_id}/conversionDefinitionAssociations"
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
        return await self.get(endpoint, params=params)

    async def dsp_amazon_update_associated_conversion_definitions_for_order(self, account_id: str, order_id: str, body: BatchAssociateConversionDefinitionsRequestV3 | dict[str, Any] | None = None, amazon_advertising_api_client_id: str | None = None, amazon_advertising_api_scope: str | None = None, amazon_ads_account_id: str | None = None) -> JSONData | JSONList:
        """POST /accounts/{accountId}/dsp/orders/{orderId}/conversionDefinitionAssociations

        Associate/Dissociate conversion definitions to an order.
        """
        endpoint = f"/accounts/{account_id}/dsp/orders/{order_id}/conversionDefinitionAssociations"
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
        return await self.post(endpoint, json_data=json_data, params=params, content_type="application/vnd.dspcampaignconversionassociation.v3+json")

