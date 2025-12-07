"""
Amazon Ads Test Accounts API

官方文档: https://advertising.amazon.com/API/docs/en-us/guides/account-management/test-accounts/overview
OpenAPI: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingTestAccount_prod_3p.json
"""

from typing import Any, Dict, List, Optional
from ..base import BaseAdsClient


class TestAccountsAPI(BaseAdsClient):
    """Test Accounts API - 测试账户管理
    
    创建和管理用于API集成测试的测试广告账户。
    """
    
    # ==================== 测试账户管理 ====================
    
    async def list_test_accounts(self) -> List[Dict[str, Any]]:
        """获取所有测试账户列表
        
        Returns:
            测试账户列表
        """
        response = await self._make_request(
            "GET",
            "/testAccounts",
        )
        return response.get("testAccounts", [])
    
    async def create_test_account(
        self,
        name: str,
        country_code: str,
        account_type: str = "seller",
        timezone: Optional[str] = None,
    ) -> Dict[str, Any]:
        """创建测试账户
        
        Args:
            name: 测试账户名称
            country_code: 国家代码 (US, UK, DE, etc.)
            account_type: 账户类型 (seller, vendor)
            timezone: 时区
            
        Returns:
            创建的测试账户信息
        """
        data = {
            "name": name,
            "countryCode": country_code,
            "accountType": account_type,
        }
        if timezone:
            data["timezone"] = timezone
            
        return await self._make_request(
            "POST",
            "/testAccounts",
            json=data,
        )
    
    async def get_test_account(
        self,
        test_account_id: str,
    ) -> Dict[str, Any]:
        """获取测试账户详情
        
        Args:
            test_account_id: 测试账户ID
            
        Returns:
            测试账户详情
        """
        return await self._make_request(
            "GET",
            f"/testAccounts/{test_account_id}",
        )
    
    async def delete_test_account(
        self,
        test_account_id: str,
    ) -> None:
        """删除测试账户
        
        Args:
            test_account_id: 测试账户ID
        """
        await self._make_request(
            "DELETE",
            f"/testAccounts/{test_account_id}",
        )
    
    # ==================== 测试数据管理 ====================
    
    async def generate_test_data(
        self,
        test_account_id: str,
        data_type: str,
        config: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """为测试账户生成测试数据
        
        Args:
            test_account_id: 测试账户ID
            data_type: 数据类型 (campaigns, keywords, reports)
            config: 数据生成配置
            
        Returns:
            生成的数据信息
        """
        data = {
            "dataType": data_type,
        }
        if config:
            data["config"] = config
            
        return await self._make_request(
            "POST",
            f"/testAccounts/{test_account_id}/data",
            json=data,
        )
    
    async def reset_test_account(
        self,
        test_account_id: str,
    ) -> Dict[str, Any]:
        """重置测试账户数据
        
        Args:
            test_account_id: 测试账户ID
            
        Returns:
            重置结果
        """
        return await self._make_request(
            "POST",
            f"/testAccounts/{test_account_id}/reset",
        )
    
    # ==================== 测试账户授权 ====================
    
    async def get_test_account_credentials(
        self,
        test_account_id: str,
    ) -> Dict[str, Any]:
        """获取测试账户API凭证
        
        Args:
            test_account_id: 测试账户ID
            
        Returns:
            API凭证信息
        """
        return await self._make_request(
            "GET",
            f"/testAccounts/{test_account_id}/credentials",
        )
    
    async def refresh_test_account_credentials(
        self,
        test_account_id: str,
    ) -> Dict[str, Any]:
        """刷新测试账户API凭证
        
        Args:
            test_account_id: 测试账户ID
            
        Returns:
            新的API凭证
        """
        return await self._make_request(
            "POST",
            f"/testAccounts/{test_account_id}/credentials/refresh",
        )

