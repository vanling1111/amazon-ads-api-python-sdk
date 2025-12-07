"""
Amazon Ads Brand Metrics API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/reporting/brand-metrics/overview
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class BrandMetricsAPI(BaseAdsClient):
    """Brand Metrics API - 品牌指标
    
    获取品牌知名度、考虑度和购买意向等品牌健康指标。
    """
    
    # ==================== 品牌指标报告 ====================
    
    async def create_report(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        category_ids: Optional[List[str]] = None,
        metrics: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """创建品牌指标报告
        
        Args:
            brand_entity_id: 品牌实体ID
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            category_ids: 类目ID列表
            metrics: 指标列表
            
        Returns:
            报告创建结果
        """
        data = {
            "brandEntityId": brand_entity_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if category_ids:
            data["categoryIds"] = category_ids
        if metrics:
            data["metrics"] = metrics
            
        return await self._make_request(
            "POST",
            "/brandMetrics/reports",
            json=data,
        )
    
    async def get_report(
        self,
        report_id: str,
    ) -> Dict[str, Any]:
        """获取品牌指标报告状态
        
        Args:
            report_id: 报告ID
            
        Returns:
            报告详情
        """
        return await self._make_request(
            "GET",
            f"/brandMetrics/reports/{report_id}",
        )
    
    async def download_report(
        self,
        report_id: str,
    ) -> bytes:
        """下载品牌指标报告
        
        Args:
            report_id: 报告ID
            
        Returns:
            报告内容
        """
        return await self._make_request(
            "GET",
            f"/brandMetrics/reports/{report_id}/download",
        )
    
    # ==================== 品牌健康指标 ====================
    
    async def get_brand_awareness(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        category_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取品牌知名度指标
        
        Args:
            brand_entity_id: 品牌实体ID
            start_date: 开始日期
            end_date: 结束日期
            category_id: 类目ID
            
        Returns:
            品牌知名度数据
        """
        params = {
            "brandEntityId": brand_entity_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if category_id:
            params["categoryId"] = category_id
            
        return await self._make_request(
            "GET",
            "/brandMetrics/awareness",
            params=params,
        )
    
    async def get_brand_consideration(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        category_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取品牌考虑度指标
        
        Args:
            brand_entity_id: 品牌实体ID
            start_date: 开始日期
            end_date: 结束日期
            category_id: 类目ID
            
        Returns:
            品牌考虑度数据
        """
        params = {
            "brandEntityId": brand_entity_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if category_id:
            params["categoryId"] = category_id
            
        return await self._make_request(
            "GET",
            "/brandMetrics/consideration",
            params=params,
        )
    
    async def get_brand_purchase_intent(
        self,
        brand_entity_id: str,
        start_date: str,
        end_date: str,
        category_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """获取品牌购买意向指标
        
        Args:
            brand_entity_id: 品牌实体ID
            start_date: 开始日期
            end_date: 结束日期
            category_id: 类目ID
            
        Returns:
            品牌购买意向数据
        """
        params = {
            "brandEntityId": brand_entity_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        if category_id:
            params["categoryId"] = category_id
            
        return await self._make_request(
            "GET",
            "/brandMetrics/purchaseIntent",
            params=params,
        )
    
    # ==================== 品牌份额 ====================
    
    async def get_share_of_voice(
        self,
        brand_entity_id: str,
        category_id: str,
        start_date: str,
        end_date: str,
    ) -> Dict[str, Any]:
        """获取品牌声量份额
        
        Args:
            brand_entity_id: 品牌实体ID
            category_id: 类目ID
            start_date: 开始日期
            end_date: 结束日期
            
        Returns:
            声量份额数据
        """
        params = {
            "brandEntityId": brand_entity_id,
            "categoryId": category_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        return await self._make_request(
            "GET",
            "/brandMetrics/shareOfVoice",
            params=params,
        )
    
    async def get_category_benchmark(
        self,
        category_id: str,
        start_date: str,
        end_date: str,
    ) -> Dict[str, Any]:
        """获取类目基准数据
        
        Args:
            category_id: 类目ID
            start_date: 开始日期
            end_date: 结束日期
            
        Returns:
            类目基准数据
        """
        params = {
            "categoryId": category_id,
            "startDate": start_date,
            "endDate": end_date,
        }
        return await self._make_request(
            "GET",
            "/brandMetrics/categoryBenchmark",
            params=params,
        )
    
    # ==================== 可用类目 ====================
    
    async def list_available_categories(
        self,
        brand_entity_id: str,
    ) -> List[Dict[str, Any]]:
        """获取品牌可用类目列表
        
        Args:
            brand_entity_id: 品牌实体ID
            
        Returns:
            可用类目列表
        """
        params = {
            "brandEntityId": brand_entity_id,
        }
        response = await self._make_request(
            "GET",
            "/brandMetrics/categories",
            params=params,
        )
        return response.get("categories", [])
