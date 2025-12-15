"""
Audiences Discovery API - 受众发现 (异步版本)

官方端点 (共4个):
- POST /audiences/list - 获取受众列表
- POST /audiences/taxonomy/list - 获取分类树
- PUT /dsp/audiences/edit - 编辑 DSP 受众
- POST /dsp/audiences/delete - 删除 DSP 受众

官方规范: Audiences.json
参考文档: https://advertising.amazon.com/API/docs/en-us/audiences
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList
import uuid


class AudiencesDiscoveryAPI(BaseAdsClient):
    """
    Audiences Discovery API (全异步)
    
    官方端点 (共4个):
    - POST /audiences/list - 获取受众列表
    - POST /audiences/taxonomy/list - 获取分类树
    - PUT /dsp/audiences/edit - 编辑 DSP 受众
    - POST /dsp/audiences/delete - 删除 DSP 受众
    """
    
    # ==================== Discovery ====================
    
    async def fetch_taxonomy(
        self,
        ad_type: str,
        category_path: list[str] | None = None,
        countries: list[str] | None = None,
        advertiser_id: str | None = None,
        next_token: str | None = None,
        max_results: int = 250,
    ) -> JSONData:
        """
        浏览受众类别分类树
        
        官方端点: POST /audiences/taxonomy/list
        官方规范: Audiences.json
        
        Args:
            ad_type: 广告类型 (必填)
                - "DSP": DSP 广告
                - "SD": Sponsored Display
                - "ST": Sponsored TV
            category_path: 分类路径，用于获取子分类 (可选)
                Example: ["In-market", "Electronics"]
            countries: ISO Alpha-2 国家代码列表 (可选，当前仅支持单个国家)
                Example: ["US"]
            advertiser_id: 广告商ID (DSP 类型必填，SD 类型可选)
            next_token: 分页令牌
            max_results: 每页最大数量 (1-250, 默认250)
        
        Returns:
            {
                "categories": [{"category": "string", "audienceCount": 100}],
                "categoryPath": ["path", "to", "category"],
                "nextToken": "..."
            }
        """
        request_body: JSONData = {
            "adType": ad_type,
        }
        
        if category_path:
            request_body["categoryPath"] = category_path
        if countries:
            request_body["countries"] = countries
        
        params: dict[str, Any] = {"maxResults": max_results}
        if advertiser_id:
            params["advertiserId"] = advertiser_id
        if next_token:
            params["nextToken"] = next_token
            
        result = await self.post(
            "/audiences/taxonomy/list", 
            json_data=request_body,
            params=params,
        )
        return result if isinstance(result, dict) else {"categories": []}
    
    async def list_audiences(
        self,
        ad_type: str,
        filters: JSONList | None = None,
        countries: list[str] | None = None,
        advertiser_id: str | None = None,
        can_target: bool = False,
        max_results: int = 10,
        next_token: str | None = None,
    ) -> JSONData:
        """
        根据筛选条件获取受众片段列表
        
        官方端点: POST /audiences/list
        官方规范: Audiences.json
        
        Args:
            ad_type: 广告类型 (必填)
                - "DSP": DSP 广告
                - "SD": Sponsored Display
                - "ST": Sponsored TV
            filters: 过滤条件列表 (可选)
                支持的字段: audienceName, category, categoryPath, audienceId, status
                Example: [
                    {"field": "audienceName", "operator": "EQ", "values": ["My Audience"]},
                    {"field": "status", "operator": "EQ", "values": ["Active"]}
                ]
                operator: "EQ" 或 "NOT_EQ"
            countries: ISO Alpha-2 国家代码列表 (可选，当前仅支持单个国家)
            advertiser_id: 广告商ID (DSP 类型必填，SD 类型可选)
            can_target: 仅返回可定向的受众 (默认 false)
            max_results: 每页最大数量 (1-250, 默认10)
            next_token: 分页令牌
        
        Returns:
            {
                "audiences": [...],
                "matchCount": 100,
                "nextToken": "..."
            }
        """
        request_body: JSONData = {
            "adType": ad_type,
        }
        
        if filters:
            request_body["filters"] = filters
        if countries:
            request_body["countries"] = countries
        
        params: dict[str, Any] = {
            "maxResults": max_results,
            "canTarget": str(can_target).lower(),
        }
        if advertiser_id:
            params["advertiserId"] = advertiser_id
        if next_token:
            params["nextToken"] = next_token
            
        result = await self.post(
            "/audiences/list", 
            json_data=request_body,
            params=params,
        )
        return result if isinstance(result, dict) else {"audiences": []}
    
    # ==================== DSP Audiences Management ====================
    
    async def edit_dsp_audience(
        self,
        advertiser_id: str,
        audience_id: str,
        audience_type: str,
        idempotency_key: str | None = None,
        name: str | None = None,
        description: str | None = None,
        lookback: int | None = None,
        rules: JSONList | None = None,
    ) -> JSONData:
        """
        编辑 DSP 受众
        
        官方端点: PUT /dsp/audiences/edit
        官方规范: Audiences.json
        
        Args:
            advertiser_id: 广告商ID (Header: AdvertiserId)
            audience_id: 受众ID (必填)
            audience_type: 受众类型 (必填)
                - PRODUCT_PURCHASES
                - PRODUCT_SEARCH
                - PRODUCT_SIMS
                - PRODUCT_VIEWS
            idempotency_key: 请求的唯一标识 (可选，自动生成)
            name: 受众名称 (可选, maxLength: 128)
            description: 受众描述 (可选, maxLength: 1000)
            lookback: 回溯天数 (可选)
                - PRODUCT_PURCHASES: 1-365
                - 其他: 1-90
            rules: 定义受众的规则集 (可选)
                Example: [{
                    "attributeType": "ASIN",
                    "attributeValues": ["B08V4T57R2"],
                    "clause": "INCLUDE",
                    "operator": "ONE_OF"
                }]
        
        Returns:
            {
                "failed": [...],
                "success": [{"audienceId": "...", "idempotencyKey": "...", "index": 0}]
            }
        """
        edit_item: JSONData = {
            "audienceId": audience_id,
            "audienceType": audience_type,
            "idempotencyKey": idempotency_key or str(uuid.uuid4()),
        }
        
        if name:
            edit_item["name"] = name
        if description:
            edit_item["description"] = description
        if lookback is not None:
            edit_item["lookback"] = lookback
        if rules:
            edit_item["rules"] = rules
        
        request_body: JSONData = {
            "dspAudienceEditRequestItems": [edit_item]
        }
        
        result = await self.put(
            "/dsp/audiences/edit", 
            json_data=request_body,
            content_type="application/vnd.dspaudiences.v1+json",
            headers={"AdvertiserId": advertiser_id},
        )
        return result if isinstance(result, dict) else {"success": [], "failed": []}
    
    async def delete_dsp_audience(
        self,
        advertiser_id: str,
        audience_id: str,
        idempotency_key: str | None = None,
    ) -> JSONData:
        """
        删除 DSP 受众
        
        官方端点: POST /dsp/audiences/delete
        官方规范: Audiences.json
        
        仅支持以下类型的受众:
        - PRODUCT_PURCHASES
        - PRODUCT_VIEWS
        - PRODUCT_SIMS
        - PRODUCT_SEARCH
        - COMBINED_AUDIENCE
        
        Args:
            advertiser_id: 广告商ID (Header: AdvertiserId)
            audience_id: 要删除的受众ID
            idempotency_key: 请求的唯一标识 (可选，自动生成)
        
        Returns:
            {
                "failed": [...],
                "success": [{"audienceId": "...", "idempotencyKey": "...", "index": 0}]
            }
        """
        delete_item: JSONData = {
            "audienceId": audience_id,
            "idempotencyKey": idempotency_key or str(uuid.uuid4()),
        }
        
        request_body: JSONData = {
            "dspAudienceDeleteRequestItems": [delete_item]
        }
        
        result = await self.post(
            "/dsp/audiences/delete", 
            json_data=request_body,
            content_type="application/vnd.dspaudiences.v1+json",
            headers={"AdvertiserId": advertiser_id},
        )
        return result if isinstance(result, dict) else {"success": [], "failed": []}
    
    # ==================== 便捷方法 ====================
    
    async def list_all_audiences(
        self,
        ad_type: str,
        filters: JSONList | None = None,
        countries: list[str] | None = None,
        advertiser_id: str | None = None,
        can_target: bool = False,
        max_items: int = 1000,
    ) -> JSONList:
        """
        获取所有受众（自动分页）
        
        Args:
            ad_type: 广告类型 ("DSP", "SD", "ST")
            filters: 过滤条件
            countries: 国家代码列表
            advertiser_id: 广告商ID
            can_target: 仅返回可定向受众
            max_items: 最大返回数量
        
        Returns:
            所有受众的列表
        """
        all_audiences: JSONList = []
        next_token = None
        
        while len(all_audiences) < max_items:
            result = await self.list_audiences(
                ad_type=ad_type,
                filters=filters,
                countries=countries,
                advertiser_id=advertiser_id,
                can_target=can_target,
                max_results=min(250, max_items - len(all_audiences)),
                next_token=next_token,
            )
            
            audiences = result.get("audiences", [])
            all_audiences.extend(audiences)
            
            next_token = result.get("nextToken")
            if not next_token or not audiences:
                break
        
        return all_audiences[:max_items]
    
    async def search_audiences_by_name(
        self,
        ad_type: str,
        name: str,
        countries: list[str] | None = None,
        advertiser_id: str | None = None,
    ) -> JSONList:
        """
        按名称搜索受众（广泛匹配，非精确匹配）
        
        Args:
            ad_type: 广告类型
            name: 受众名称（广泛匹配）
            countries: 国家代码列表
            advertiser_id: 广告商ID
        
        Returns:
            匹配的受众列表
        """
        filters = [{"field": "audienceName", "operator": "EQ", "values": [name]}]
        result = await self.list_audiences(
            ad_type=ad_type,
            filters=filters,
            countries=countries,
            advertiser_id=advertiser_id,
        )
        return result.get("audiences", [])
    
    async def get_audience_by_id(
        self,
        ad_type: str,
        audience_id: str,
        advertiser_id: str | None = None,
    ) -> JSONData | None:
        """
        按ID获取受众
        
        Args:
            ad_type: 广告类型
            audience_id: 受众ID
            advertiser_id: 广告商ID
        
        Returns:
            受众详情或 None
        """
        filters = [{"field": "audienceId", "operator": "EQ", "values": [audience_id]}]
        result = await self.list_audiences(
            ad_type=ad_type,
            filters=filters,
            advertiser_id=advertiser_id,
        )
        audiences = result.get("audiences", [])
        return audiences[0] if audiences else None
