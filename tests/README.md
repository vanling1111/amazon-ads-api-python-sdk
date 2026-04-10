# Amazon Ads API SDK 测试指南

## 测试架构

```
tests/
├── conftest.py              # 共享 fixtures
├── pytest.ini               # Pytest 配置
├── unit/                    # 单元测试
│   └── test_sp_campaigns.py
├── integration/             # 集成测试
│   └── test_api_integration.py
└── e2e/                     # 端到端测试
    └── test_campaign_flow.py
```

## 测试类型

### 1. 单元测试 (Unit Tests)

**特点：**
- 不需要网络连接
- 使用 Mock 对象
- 快速执行
- 覆盖率目标 >80%

**运行：**
```bash
# 运行所有单元测试
pytest -m unit

# 运行特定文件
pytest tests/unit/test_sp_campaigns.py

# 带覆盖率
pytest -m unit --cov=amazon_ads_api --cov-report=html
```

### 2. 集成测试 (Integration Tests)

**特点：**
- 需要真实 Amazon Ads 凭证
- 测试真实 API 调用
- 只读操作（不创建资源）

**环境变量：**
```bash
export AMAZON_ADS_CLIENT_ID="your_client_id"
export AMAZON_ADS_CLIENT_SECRET="your_client_secret"
export AMAZON_ADS_REFRESH_TOKEN="your_refresh_token"
export AMAZON_ADS_PROFILE_ID="your_profile_id"
```

**运行：**
```bash
pytest -m integration
```

### 3. 端到端测试 (E2E Tests)

**特点：**
- 测试完整业务流程
- 会创建真实广告资源
- 需要测试账号或沙盒环境
- **谨慎使用！**

**环境变量：**
```bash
# 除了集成测试的环境变量外，还需要：
export AMAZON_ADS_TEST_MODE="true"  # 必须显式启用
```

**运行：**
```bash
pytest -m e2e
```

## 常用命令

```bash
# 运行所有测试
pytest

# 只运行单元测试（默认）
pytest -m unit

# 运行单元+集成测试
pytest -m "unit or integration"

# 排除慢速测试
pytest -m "not slow"

# 并行运行
pytest -n auto

# 详细输出
pytest -v --tb=long

# 生成覆盖率报告
pytest --cov=amazon_ads_api --cov-report=html
open htmlcov/index.html

# 只运行失败的测试
pytest --lf

# 失败时停止
pytest -x
```

## 编写新测试

### 单元测试模板

```python
import pytest
from unittest.mock import AsyncMock

@pytest.fixture
def api_client():
    """创建 mock API 客户端"""
    client = YourAPI.__new__(YourAPI)
    client.get = AsyncMock()
    client.post = AsyncMock()
    return client

class TestYourAPI:
    
    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_your_method(self, api_client):
        """测试描述"""
        # Arrange
        api_client.get.return_value = {"expected": "response"}
        
        # Act
        result = await api_client.your_method()
        
        # Assert
        assert result == {"expected": "response"}
        api_client.get.assert_called_once()
```

### 集成测试模板

```python
import os
import pytest

SKIP = not os.getenv("AMAZON_ADS_CLIENT_ID")

@pytest.mark.integration
@pytest.mark.skipif(SKIP, reason="需要凭证")
class TestIntegration:
    
    @pytest.mark.asyncio
    async def test_real_api_call(self):
        """测试真实 API"""
        from amazon_ads_api import AmazonAdsClient
        
        client = AmazonAdsClient(
            client_id=os.getenv("AMAZON_ADS_CLIENT_ID"),
            # ...
        )
        
        result = await client.some_api.some_method()
        assert result is not None
```

## CI/CD 配置

### GitHub Actions

```yaml
name: Tests

on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -e ".[dev]"
      - run: pytest -m unit --cov=amazon_ads_api
      
  integration-tests:
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -e ".[dev]"
      - run: pytest -m integration
        env:
          AMAZON_ADS_CLIENT_ID: ${{ secrets.AMAZON_ADS_CLIENT_ID }}
          AMAZON_ADS_CLIENT_SECRET: ${{ secrets.AMAZON_ADS_CLIENT_SECRET }}
          AMAZON_ADS_REFRESH_TOKEN: ${{ secrets.AMAZON_ADS_REFRESH_TOKEN }}
          AMAZON_ADS_PROFILE_ID: ${{ secrets.AMAZON_ADS_PROFILE_ID }}
```

## 覆盖率目标

| 模块 | 目标覆盖率 |
|------|-----------|
| core/sp/ | >85% |
| core/sb/ | >85% |
| core/sd/ | >85% |
| core/dsp/ | >80% |
| services/ | >75% |
| experimental/ | >60% |
| **总体** | **>80%** |

## 测试数据

测试使用的 Mock 数据定义在 `conftest.py` 中，包括：
- `MOCK_PROFILE`
- `MOCK_CAMPAIGN`
- `MOCK_AD_GROUP`
- `MOCK_KEYWORD`
- `MOCK_REPORT`

## 故障排除

### 测试无法导入模块

```bash
# 确保在开发模式安装
pip install -e .
```

### 异步测试失败

```bash
# 确保安装 pytest-asyncio
pip install pytest-asyncio
```

### 集成测试跳过

检查环境变量是否正确设置：
```bash
echo $AMAZON_ADS_CLIENT_ID
```

