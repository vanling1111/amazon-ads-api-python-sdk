"""
Product Metadata API - 产品元数据

端点: /product/metadata
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class ProductMetadataAPI(BaseAdsClient):
    """
    Product Metadata API
    
    允许获取产品目录中SKU或ASIN的产品元数据，
    包括库存状态、价格、资格状态和产品详情，
    用于启动、管理或优化SP、SB、SD广告活动。
    """
    
    async def get_product_metadata(
        self,
        *,
        asins: Optional[List[str]] = None,
        skus: Optional[List[str]] = None,
        include_inventory_status: bool = True,
        include_price: bool = True,
        include_eligibility: bool = True,
        include_product_details: bool = True,
    ) -> Dict[str, Any]:
        """
        获取产品元数据
        
        Args:
            asins: ASIN列表 (与skus二选一)
            skus: SKU列表 (与asins二选一)
            include_inventory_status: 是否包含库存状态
            include_price: 是否包含价格信息
            include_eligibility: 是否包含广告资格状态
            include_product_details: 是否包含产品详情
            
        Returns:
            产品元数据响应
        """
        request_body: Dict[str, Any] = {}
        
        if asins:
            request_body["asins"] = asins
        elif skus:
            request_body["skus"] = skus
        else:
            raise ValueError("Must provide either asins or skus")
        
        # 构建返回字段
        return_fields = []
        if include_inventory_status:
            return_fields.append("inventoryStatus")
        if include_price:
            return_fields.append("price")
        if include_eligibility:
            return_fields.append("eligibility")
        if include_product_details:
            return_fields.append("productDetails")
            
        if return_fields:
            request_body["returnFields"] = return_fields
            
        return await self._request(
            "POST",
            "/product/metadata",
            json=request_body
        )

