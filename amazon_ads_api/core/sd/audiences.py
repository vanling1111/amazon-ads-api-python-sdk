"""
Sponsored Display - Audience Targeting (异步版本)

⚠️ 重要说明：
SD 没有独立的 /sd/audiences/* API 端点！
SD 受众定向是通过 /sd/targets 端点的 targeting 表达式实现的。

官方文档: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi
OpenAPI Spec: SponsoredDisplay_v3.yaml

使用方法:
- 受众定向通过 /sd/targets 端点实现
- 使用 TargetingPredicateNested 类型，设置 type='audience'
- 使用 audienceSameAs 来指定具体受众 ID
- 受众 ID 可通过 Audiences Discovery API 获取

示例:
{
    "adGroupId": "xxx",
    "targetingClause": {
        "expression": [{
            "type": "audience",
            "value": [{
                "type": "audienceSameAs",
                "value": "12345"  # 受众 ID
            }]
        }]
    },
    "bid": 1.0
}
"""

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList


class SDAudienceTargetingAPI(BaseAdsClient):
    """
    SD Audience Targeting API (全异步)
    
    ⚠️ 注意：这不是独立的 audiences API！
    这是通过 /sd/targets 端点实现受众定向的辅助类。
    
    SD 受众定向使用 TargetingPredicateNested 表达式，
    通过 targeting 端点进行配置。
    
    API Tier: L1
    Source: SponsoredDisplay_v3.yaml (targeting 部分)
    """

    # ============ 创建受众定向目标 ============

    async def create_audience_target(
        self,
        ad_group_id: str,
        audience_id: str,
        bid: float,
        state: str = "enabled",
    ) -> JSONData:
        """
        创建受众定向目标
        
        通过 POST /sd/targets 端点实现
        
        Args:
            ad_group_id: 广告组 ID
            audience_id: 受众 ID (通过 Audiences Discovery API 获取)
            bid: 竞价金额
            state: 状态 (enabled, paused, archived)
        
        Returns:
            创建结果
        """
        # 构建受众定向表达式
        targeting_clause = {
            "expression": [{
                "type": "audience",
                "value": [{
                    "type": "audienceSameAs",
                    "value": audience_id
                }]
            }]
        }
        
        body: JSONData = {
            "adGroupId": ad_group_id,
            "targetingClause": targeting_clause,
            "bid": bid,
            "state": state,
        }
        
        result = await self.post("/sd/targets", json_data=[body])
        return result if isinstance(result, (dict, list)) else {}

    async def create_audience_targets_batch(
        self,
        targets: JSONList,
    ) -> JSONData:
        """
        批量创建受众定向目标
        
        Args:
            targets: 目标列表，每个包含:
                - ad_group_id: 广告组 ID
                - audience_id: 受众 ID
                - bid: 竞价金额
                - state: 状态 (可选)
        
        Returns:
            批量创建结果
        """
        formatted_targets = []
        for target in targets:
            targeting_clause = {
                "expression": [{
                    "type": "audience",
                    "value": [{
                        "type": "audienceSameAs",
                        "value": target["audience_id"]
                    }]
                }]
            }
            formatted_targets.append({
                "adGroupId": target["ad_group_id"],
                "targetingClause": targeting_clause,
                "bid": target["bid"],
                "state": target.get("state", "enabled"),
            })
        
        result = await self.post("/sd/targets", json_data=formatted_targets)
        return result if isinstance(result, (dict, list)) else {}

    async def update_audience_target_bid(
        self,
        target_id: str,
        bid: float,
    ) -> JSONData:
        """
        更新受众定向目标的竞价
        
        通过 PUT /sd/targets 端点实现
        
        Args:
            target_id: 目标 ID
            bid: 新竞价金额
        
        Returns:
            更新结果
        """
        result = await self.put("/sd/targets", json_data=[{
            "targetId": target_id,
            "bid": bid,
        }])
        return result if isinstance(result, (dict, list)) else {}

    async def archive_audience_target(
        self,
        target_id: str,
    ) -> JSONData:
        """
        归档受众定向目标
        
        通过 PUT /sd/targets 端点实现
        
        Args:
            target_id: 目标 ID
        
        Returns:
            归档结果
        """
        result = await self.put("/sd/targets", json_data=[{
            "targetId": target_id,
            "state": "archived",
        }])
        return result if isinstance(result, (dict, list)) else {}

    # ============ 创建否定受众定向 ============

    async def create_negative_audience_target(
        self,
        ad_group_id: str,
        audience_id: str,
        state: str = "enabled",
    ) -> JSONData:
        """
        创建否定受众定向
        
        通过 POST /sd/negativeTargets 端点实现
        
        Args:
            ad_group_id: 广告组 ID
            audience_id: 要排除的受众 ID
            state: 状态
        
        Returns:
            创建结果
        """
        targeting_clause = {
            "expression": [{
                "type": "audience",
                "value": [{
                    "type": "audienceSameAs",
                    "value": audience_id
                }]
            }]
        }
        
        body: JSONData = {
            "adGroupId": ad_group_id,
            "targetingClause": targeting_clause,
            "state": state,
        }
        
        result = await self.post("/sd/negativeTargets", json_data=[body])
        return result if isinstance(result, (dict, list)) else {}

    async def archive_negative_audience_target(
        self,
        target_id: str,
    ) -> JSONData:
        """
        归档否定受众定向
        
        通过 PUT /sd/negativeTargets 端点实现
        """
        result = await self.put("/sd/negativeTargets", json_data=[{
            "targetId": target_id,
            "state": "archived",
        }])
        return result if isinstance(result, (dict, list)) else {}

    # ============ Dynamic Segment - Audiences Likely Interested ============

    async def create_dynamic_audience_target(
        self,
        ad_group_id: str,
        bid: float,
        state: str = "enabled",
    ) -> JSONData:
        """
        创建动态受众定向 (Audiences Likely Interested In Ad)
        
        官方文档说明:
        Target audiences that are likely to consider and buy from your business.
        We recommend adding this segment to all campaigns for greater reach.
        
        ⚠️ 注意: 仅当 landingPageType 为 OFF_AMAZON_LINK 时支持
        
        Args:
            ad_group_id: 广告组 ID
            bid: 竞价金额
            state: 状态
        
        Returns:
            创建结果
        """
        targeting_clause = {
            "expression": [{
                "type": "audiencesLikelyInterestedInAd"
            }]
        }
        
        body: JSONData = {
            "adGroupId": ad_group_id,
            "targetingClause": targeting_clause,
            "bid": bid,
            "state": state,
        }
        
        result = await self.post("/sd/targets", json_data=[body])
        return result if isinstance(result, (dict, list)) else {}


# 保持向后兼容的别名
SDAudiencesAPI = SDAudienceTargetingAPI
