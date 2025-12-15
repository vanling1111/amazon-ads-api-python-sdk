"""
Amazon Ads Hashed Records API (异步版本)

官方文档: https://advertising.amazon.com/API/docs/en-us/data-provider/hashed-records
验证日期: 2024-12-15

端点:
- POST /dp/records/hashed - 上传哈希记录
"""

from typing import Any
from amazon_ads_api.base import BaseAdsClient, JSONData

# 官方 Content-Type (V3)
HASHED_RECORDS_CONTENT_TYPE = "application/vnd.dpuploadhashedrecordsrequest.v3+json"


class HashedRecordsAPI(BaseAdsClient):
    """Hashed Records API (全异步)
    
    官方验证: 1个端点
    
    用于匹配 Amazon 购物者与其哈希客户记录，包括姓名、电子邮件、
    手机号码、地址和邮编。
    """

    # ==================== 哈希记录上传 ====================

    async def upload_hashed_records(
        self,
        records: list[dict[str, Any]],
    ) -> JSONData:
        """上传哈希记录批次进行匹配
        
        官方端点: POST /dp/records/hashed
        Content-Type: application/vnd.dpuploadhashedrecordsrequest.v3+json
        最大负载: 5MB
        
        所有输入必须按照文档正确规范化并使用 SHA-256 哈希:
        https://advertising.amazon.com/help/GCCXMZYCK4RXWS6C
        
        Args:
            records: 哈希记录列表，每条记录可包含:
                - hashedEmail: SHA-256 哈希的电子邮件
                - hashedPhone: SHA-256 哈希的手机号码
                - hashedFirstName: SHA-256 哈希的名字
                - hashedLastName: SHA-256 哈希的姓氏
                - hashedAddress: SHA-256 哈希的地址
                - hashedCity: SHA-256 哈希的城市
                - hashedState: SHA-256 哈希的州/省
                - hashedPostalCode: SHA-256 哈希的邮编
                - externalId: 外部标识符
        
        Returns:
            上传结果，包含 requestId
        
        Example:
            ```python
            import hashlib
            
            # 规范化并哈希数据
            email = "user@example.com".lower().strip()
            hashed_email = hashlib.sha256(email.encode()).hexdigest()
            
            records = [{
                "hashedEmail": hashed_email,
                "externalId": "user123"
            }]
            
            result = await client.reference.data_provider.hashed_records.upload_hashed_records(records)
            ```
        """
        data = {"records": records}
        
        # 使用官方 Content-Type
        headers = {"Content-Type": HASHED_RECORDS_CONTENT_TYPE}
        result = await self.post("/dp/records/hashed", json_data=data, headers=headers)
        return result if isinstance(result, dict) else {}
