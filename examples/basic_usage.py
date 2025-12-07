"""
Amazon Ads API SDK 基础使用示例
"""

from amazon_ads_api import AmazonAdsClient, AdsRegion


def main():
    # 创建客户端
    client = AmazonAdsClient(
        client_id="your_client_id",
        client_secret="your_client_secret",
        refresh_token="your_refresh_token",
        region=AdsRegion.NA,  # NA=北美, EU=欧洲, FE=远东
    )

    # 获取所有 Profiles
    profiles = client.accounts.profiles.list_profiles()
    print(f"Found {len(profiles)} profiles")

    if not profiles:
        print("No profiles found. Please check your credentials.")
        return

    # 使用第一个 Profile
    profile = profiles[0]
    profile_id = profile.get("profileId")
    print(f"Using profile: {profile_id}")

    # 设置 Profile ID
    client.with_profile(profile_id)

    # ============ SP (Sponsored Products) ============
    print("\n=== Sponsored Products ===")

    # 获取 Campaigns
    campaigns = client.sp.campaigns.list_campaigns()
    print(f"SP Campaigns: {len(campaigns.get('campaigns', []))}")

    # 获取 Keywords
    keywords = client.sp.keywords.list_keywords()
    print(f"SP Keywords: {len(keywords.get('keywords', []))}")

    # ============ SB (Sponsored Brands) ============
    print("\n=== Sponsored Brands ===")

    # 获取 SB Campaigns
    sb_campaigns = client.sb.campaigns.list_campaigns()
    print(f"SB Campaigns: {len(sb_campaigns.get('campaigns', []))}")

    # ============ SD (Sponsored Display) ============
    print("\n=== Sponsored Display ===")

    # 获取 SD Campaigns
    sd_campaigns = client.sd.campaigns.list_campaigns()
    print(f"SD Campaigns: {len(sd_campaigns.get('campaigns', []))}")

    # ============ Portfolios ============
    print("\n=== Portfolios ===")

    portfolios = client.accounts.portfolios.list_portfolios()
    print(f"Portfolios: {len(portfolios)}")

    # ============ 报告 ============
    print("\n=== Reports ===")

    # 创建并等待报告
    # report = client.reporting.reports.create_and_wait_report(
    #     report_type="spCampaigns",
    #     time_unit="DAILY",
    #     start_date="2024-01-01",
    #     end_date="2024-01-31",
    #     metrics=["impressions", "clicks", "spend", "sales14d"],
    # )
    # print(f"Report rows: {len(report)}")

    print("\n✅ Demo completed!")


if __name__ == "__main__":
    main()

