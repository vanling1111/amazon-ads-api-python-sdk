"""
Amazon DSP - Conversions API (异步版本)

官方端点 (17个):
- Ad Tag Events (2个)
- Conversion Definitions (6个)
- Mobile Measurement Partners (4个)
- Order Associations (2个)
- Batch Operations (3个)

官方规范: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ConversionsAPI_prod_3p.json
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class DSPConversionsAPI(BaseAdsClient):
    """
    DSP Conversions API (全异步)
    
    用于管理 DSP 转化定义和追踪。
    """

    # ============ Ad Tag Events ============

    async def list_ad_tag_events(
        self,
        account_id: str,
        ad_tag_id: str,
    ) -> JSONData:
        """
        列出广告标签事件
        
        官方端点: GET /accounts/{accountId}/dsp/adTagEvents/{adTagId}/list
        """
        result = await self.get(f"/accounts/{account_id}/dsp/adTagEvents/{ad_tag_id}/list")
        return result if isinstance(result, dict) else {"events": []}

    async def get_amazon_ad_tag(self, account_id: str) -> JSONData:
        """
        获取 Amazon 广告标签
        
        官方端点: GET /accounts/{accountId}/dsp/amazonAdTag
        """
        result = await self.get(f"/accounts/{account_id}/dsp/amazonAdTag")
        return result if isinstance(result, dict) else {}

    # ============ Conversion Definitions ============

    async def list_conversion_definitions(
        self,
        account_id: str,
        **kwargs,
    ) -> JSONData:
        """
        列出转化定义
        
        官方端点: POST /accounts/{accountId}/dsp/conversionDefinitions/list
        """
        result = await self.post(
            f"/accounts/{account_id}/dsp/conversionDefinitions/list",
            json_data=kwargs
        )
        return result if isinstance(result, dict) else {"conversionDefinitions": []}

    async def create_conversion_definitions(
        self,
        account_id: str,
        definitions: JSONList,
    ) -> JSONData:
        """
        创建转化定义
        
        官方端点: POST /accounts/{accountId}/dsp/conversionDefinitions
        """
        body: JSONData = {"conversionDefinitions": definitions}
        result = await self.post(
            f"/accounts/{account_id}/dsp/conversionDefinitions",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    async def update_conversion_definitions(
        self,
        account_id: str,
        definitions: JSONList,
    ) -> JSONData:
        """
        更新转化定义
        
        官方端点: PUT /accounts/{accountId}/dsp/conversionDefinitions
        """
        body: JSONData = {"conversionDefinitions": definitions}
        result = await self.put(
            f"/accounts/{account_id}/dsp/conversionDefinitions",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    async def delete_conversion_definitions(
        self,
        account_id: str,
        definition_ids: list[str],
    ) -> JSONData:
        """
        删除转化定义
        
        官方端点: POST /accounts/{accountId}/dsp/conversionDefinitions/delete
        """
        body: JSONData = {"conversionDefinitionIds": definition_ids}
        result = await self.post(
            f"/accounts/{account_id}/dsp/conversionDefinitions/delete",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    async def get_conversion_event_data(
        self,
        account_id: str,
        **kwargs,
    ) -> JSONData:
        """
        获取转化事件数据
        
        官方端点: POST /accounts/{accountId}/dsp/conversionDefinitions/eventData
        """
        result = await self.post(
            f"/accounts/{account_id}/dsp/conversionDefinitions/eventData",
            json_data=kwargs
        )
        return result if isinstance(result, dict) else {}

    async def get_ad_tag_event_associations(
        self,
        account_id: str,
        conversion_definition_id: str,
    ) -> JSONData:
        """
        获取广告标签事件关联
        
        官方端点: GET /accounts/{accountId}/dsp/conversionDefinitions/{conversionDefinitionId}/adTagEventAssociations
        """
        result = await self.get(
            f"/accounts/{account_id}/dsp/conversionDefinitions/{conversion_definition_id}/adTagEventAssociations"
        )
        return result if isinstance(result, dict) else {"associations": []}

    async def create_ad_tag_event_associations(
        self,
        account_id: str,
        conversion_definition_id: str,
        associations: JSONList,
    ) -> JSONData:
        """
        创建广告标签事件关联
        
        官方端点: POST /accounts/{accountId}/dsp/conversionDefinitions/{conversionDefinitionId}/adTagEventAssociations
        """
        body: JSONData = {"associations": associations}
        result = await self.post(
            f"/accounts/{account_id}/dsp/conversionDefinitions/{conversion_definition_id}/adTagEventAssociations",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    async def get_mobile_measurement_partner_registration(
        self,
        account_id: str,
        conversion_definition_id: str,
    ) -> JSONData:
        """
        获取移动测量合作伙伴注册信息
        
        官方端点: GET /accounts/{accountId}/dsp/conversionDefinitions/{conversionDefinitionId}/mobileMeasurementPartnerAppRegistration
        """
        result = await self.get(
            f"/accounts/{account_id}/dsp/conversionDefinitions/{conversion_definition_id}/mobileMeasurementPartnerAppRegistration"
        )
        return result if isinstance(result, dict) else {}

    # ============ Mobile Measurement Partners ============

    async def list_mobile_measurement_partners(
        self,
        account_id: str,
        **kwargs,
    ) -> JSONData:
        """
        列出移动测量合作伙伴
        
        官方端点: POST /accounts/{accountId}/dsp/mobileMeasurementPartners/list
        """
        result = await self.post(
            f"/accounts/{account_id}/dsp/mobileMeasurementPartners/list",
            json_data=kwargs
        )
        return result if isinstance(result, dict) else {"partners": []}

    async def create_mobile_measurement_partners(
        self,
        account_id: str,
        partners: JSONList,
    ) -> JSONData:
        """
        创建移动测量合作伙伴
        
        官方端点: POST /accounts/{accountId}/dsp/mobileMeasurementPartners
        """
        body: JSONData = {"partners": partners}
        result = await self.post(
            f"/accounts/{account_id}/dsp/mobileMeasurementPartners",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    async def update_mobile_measurement_partners(
        self,
        account_id: str,
        partners: JSONList,
    ) -> JSONData:
        """
        更新移动测量合作伙伴
        
        官方端点: PUT /accounts/{accountId}/dsp/mobileMeasurementPartners
        """
        body: JSONData = {"partners": partners}
        result = await self.put(
            f"/accounts/{account_id}/dsp/mobileMeasurementPartners",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    async def delete_mobile_measurement_partners(
        self,
        account_id: str,
        partner_ids: list[str],
    ) -> JSONData:
        """
        删除移动测量合作伙伴
        
        官方端点: POST /accounts/{accountId}/dsp/mobileMeasurementPartners/delete
        """
        body: JSONData = {"partnerIds": partner_ids}
        result = await self.post(
            f"/accounts/{account_id}/dsp/mobileMeasurementPartners/delete",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    # ============ Order Associations ============

    async def get_order_conversion_associations(
        self,
        account_id: str,
        order_id: str,
    ) -> JSONData:
        """
        获取订单转化关联
        
        官方端点: GET /accounts/{accountId}/dsp/orders/{orderId}/conversionDefinitionAssociations
        """
        result = await self.get(
            f"/accounts/{account_id}/dsp/orders/{order_id}/conversionDefinitionAssociations"
        )
        return result if isinstance(result, dict) else {"associations": []}

    async def create_order_conversion_associations(
        self,
        account_id: str,
        order_id: str,
        associations: JSONList,
    ) -> JSONData:
        """
        创建订单转化关联
        
        官方端点: POST /accounts/{accountId}/dsp/orders/{orderId}/conversionDefinitionAssociations
        """
        body: JSONData = {"associations": associations}
        result = await self.post(
            f"/accounts/{account_id}/dsp/orders/{order_id}/conversionDefinitionAssociations",
            json_data=body
        )
        return result if isinstance(result, dict) else {}

    # ============ Batch Operations ============

    async def batch_create_order_conversion_associations(
        self,
        account_id: str,
        associations: JSONList,
    ) -> JSONData:
        """
        批量创建订单转化关联
        
        官方端点: POST /accounts/{accountId}/dsp/batchOrders/conversionDefinitionAssociations
        """
        body: JSONData = {"associations": associations}
        result = await self.post(
            f"/accounts/{account_id}/dsp/batchOrders/conversionDefinitionAssociations",
            json_data=body
        )
        return result if isinstance(result, dict) else {}
