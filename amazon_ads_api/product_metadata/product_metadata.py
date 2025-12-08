"""
Product Metadata API (异步版本) - 产品元数据

端点: /product/metadata
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient, JSONData


class ProductMetadataAPI(BaseAdsClient):
    """
    Product Metadata API (全异步)
    
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
            
        result = await self.post("/product/metadata", json_data=request_body)
        return result if isinstance(result, dict) else {}
    
    async def get_product_by_asin(self, asin: str) -> Dict[str, Any]:
        """获取单个ASIN的产品元数据"""
        result = await self.get_product_metadata(asins=[asin])
        products = result.get("products", [])
        return products[0] if products else {}
    
    async def get_products_by_asins(self, asins: List[str]) -> List[Dict[str, Any]]:
        """批量获取ASIN的产品元数据"""
        result = await self.get_product_metadata(asins=asins)
        return result.get("products", [])
    
    async def check_product_eligibility(
        self,
        asins: List[str],
        ad_type: str = "SP",
    ) -> Dict[str, Any]:
        """
        检查产品广告资格
        
        Args:
            asins: ASIN列表
            ad_type: 广告类型 SP | SB | SD
            
        Returns:
            资格检查结果
        """
        result = await self.get_product_metadata(
            asins=asins,
            include_eligibility=True,
            include_inventory_status=False,
            include_price=False,
            include_product_details=False,
        )
        
        eligible = []
        ineligible = []
        
        for product in result.get("products", []):
            asin = product.get("asin")
            eligibility = product.get("eligibility", {})
            
            is_eligible = eligibility.get(f"{ad_type.lower()}Eligible", False)
            if is_eligible:
                eligible.append(asin)
            else:
                ineligible.append({
                    "asin": asin,
                    "reason": eligibility.get("ineligibilityReason", "Unknown"),
                })
        
        return {
            "eligible": eligible,
            "ineligible": ineligible,
        }
    
    async def get_product_prices(self, asins: List[str]) -> Dict[str, float]:
        """获取产品价格"""
        result = await self.get_product_metadata(
            asins=asins,
            include_price=True,
            include_inventory_status=False,
            include_eligibility=False,
            include_product_details=False,
        )
        
        prices = {}
        for product in result.get("products", []):
            asin = product.get("asin")
            price_info = product.get("price", {})
            prices[asin] = price_info.get("listPrice", 0)
        
        return prices
    
    async def get_product_inventory(self, asins: List[str]) -> Dict[str, Dict[str, Any]]:
        """获取产品库存状态"""
        result = await self.get_product_metadata(
            asins=asins,
            include_inventory_status=True,
            include_price=False,
            include_eligibility=False,
            include_product_details=False,
        )
        
        inventory = {}
        for product in result.get("products", []):
            asin = product.get("asin")
            inv_status = product.get("inventoryStatus", {})
            inventory[asin] = {
                "inStock": inv_status.get("inStock", False),
                "fulfillmentType": inv_status.get("fulfillmentType", "Unknown"),
                "quantity": inv_status.get("quantity", 0),
            }
        
        return inventory
