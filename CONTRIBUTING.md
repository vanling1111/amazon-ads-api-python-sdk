# Contributing to Amazon Ads API Python SDK

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [API Coverage Verification](#api-coverage-verification)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## Getting Started

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/vanling1111/amazon-ads-api-python-sdk.git
   cd amazon-ads-api-python-sdk
   ```
3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

### Prerequisites

- Python 3.8+
- pip or poetry
- Git

### Install Dependencies

```bash
# Install in development mode
pip install -e ".[dev]"

# Or with poetry
poetry install
```

### Environment Variables

Create a `.env` file for testing (never commit this):

```env
AMAZON_ADS_CLIENT_ID=your_client_id
AMAZON_ADS_CLIENT_SECRET=your_client_secret
AMAZON_ADS_REFRESH_TOKEN=your_refresh_token
AMAZON_ADS_PROFILE_ID=your_profile_id
AMAZON_ADS_REGION=NA
```

## Project Structure

```
amazon-ads-api-python-sdk/
├── amazon_ads_api/          # SDK source code
│   ├── core/               # L1: OpenAPI-verified APIs
│   ├── reference/          # L2: Official documentation APIs
│   ├── services/           # L3: Product-level aggregation
│   └── experimental/       # L4: Beta/experimental APIs
├── tests/
│   ├── unit/              # Unit tests (mock responses)
│   ├── integration/       # Integration tests (real API)
│   └── e2e/               # End-to-end tests (full workflows)
├── scripts/               # Maintenance scripts
└── specs/                 # Official OpenAPI specifications
```

## Coding Standards

### Python Style

- **PEP 8**: Follow PEP 8 style guidelines
- **Type Hints**: Use type hints for all functions
- **Docstrings**: Google-style docstrings for all public APIs
- **Async/Await**: Use async/await for all I/O operations

### Example

```python
async def create_campaign(
    self,
    campaign: Dict[str, Any],
    *,
    profile_id: Optional[str] = None
) -> Dict[str, Any]:
    """Create a new Sponsored Products campaign.
    
    Args:
        campaign: Campaign configuration dictionary
        profile_id: Optional profile ID to use instead of default
        
    Returns:
        Created campaign response with campaign ID
        
    Raises:
        AmazonAdsError: If API request fails
        
    Example:
        >>> campaign = {
        ...     "name": "My Campaign",
        ...     "budget": {"budgetType": "DAILY", "budget": 100.0},
        ...     "state": "ENABLED"
        ... }
        >>> result = await client.sp.campaigns.create_campaign(campaign)
    """
    # Implementation
```

### Code Quality

- **No TODO/FIXME**: Complete implementations only
- **No Hardcoding**: Use configuration for all environment-specific values
- **Error Handling**: Comprehensive error handling with proper exceptions
- **Logging**: Use structured logging for debugging

## Testing Requirements

### Test Coverage

- **Unit Tests**: >80% coverage
- **All New Features**: Must include tests
- **Integration Tests**: For API interactions
- **E2E Tests**: For complete workflows

### Running Tests

```bash
# Run all tests
pytest

# Run unit tests only
pytest tests/unit/ -v

# Run integration tests (requires credentials)
pytest tests/integration/ -v

# Run E2E tests
pytest tests/e2e/ -v -m e2e

# Run with coverage
pytest --cov=amazon_ads_api --cov-report=html
```

### Writing Tests

```python
import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
@pytest.mark.unit
async def test_create_campaign(mock_client):
    """Test campaign creation"""
    # Arrange
    mock_response = {"campaignId": "123", "code": "SUCCESS"}
    mock_client._client.post = AsyncMock(return_value=mock_response)
    
    # Act
    result = await mock_client.sp.campaigns.create_campaign({"name": "Test"})
    
    # Assert
    assert result["campaignId"] == "123"
    mock_client._client.post.assert_called_once()
```

## Pull Request Process

### Before Submitting

1. **Update Documentation**: Update README, API docs if needed
2. **Run Tests**: Ensure all tests pass
3. **Check Coverage**: Verify coverage remains >80%
4. **Lint Code**: Run linters (`ruff`, `mypy`, `black`)
5. **Verify APIs**: Run coverage verification scripts

```bash
# Format code
black amazon_ads_api/ tests/

# Lint code
ruff amazon_ads_api/ tests/

# Type check
mypy amazon_ads_api/

# Verify API coverage
python scripts/verify_coverage.py
python scripts/deep_verify.py
```

### PR Checklist

- [ ] Code follows PEP 8 style guidelines
- [ ] All tests pass (`pytest`)
- [ ] Coverage >80% (`pytest --cov`)
- [ ] Type hints added (`mypy` passes)
- [ ] Docstrings added (Google style)
- [ ] API verification passes (if adding/modifying APIs)
- [ ] CHANGELOG.md updated
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)

### PR Title Format

```
<type>(<scope>): <subject>

Types: feat, fix, docs, style, refactor, test, chore
Scope: sp, sb, sd, dsp, core, tests, docs, etc.

Examples:
- feat(sp): add budget rules API support
- fix(auth): handle token refresh race condition
- docs(readme): update installation instructions
```

### PR Description Template

```markdown
## Description
[Clear description of changes]

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to break)
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] All tests pass locally

## Verification
- [ ] API coverage verified with scripts
- [ ] No duplicate implementations detected
- [ ] OpenAPI specs up to date

## Checklist
- [ ] Code formatted with `black`
- [ ] Linted with `ruff`
- [ ] Type checked with `mypy`
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
```

## API Coverage Verification

When adding or modifying APIs:

### 1. Download Latest OpenAPI Specs

```bash
cd specs/
python download_all_specs.py
```

### 2. Verify Coverage

```bash
# Verify all APIs against OpenAPI specs
python scripts/verify_coverage.py

# Check for duplicates and compliance issues
python scripts/deep_verify.py
```

### 3. Expected Output

```
✅ API Coverage: 100% (543/543 endpoints)
✅ No duplicate implementations
✅ All HTTP methods correct
✅ All paths match OpenAPI specs
```

### Adding New APIs

1. **Download Official Spec**: Get the latest OpenAPI spec from Amazon
2. **Implement API**: Follow existing patterns in `core/`, `reference/`, etc.
3. **Add Tests**: Unit tests (mock) + integration tests (real API)
4. **Verify Coverage**: Run verification scripts
5. **Update Docs**: Add to README.md API list

## Reporting Issues

### Bug Reports

Include:
- Python version
- SDK version
- Minimal reproduction code
- Expected vs actual behavior
- Error messages/stack traces

### Feature Requests

Include:
- Use case description
- Proposed API design
- Alternative solutions considered
- Official Amazon documentation links

## Questions?

- **Issues**: [GitHub Issues](https://github.com/vanling1111/amazon-ads-api-python-sdk/issues)
- **Discussions**: [GitHub Discussions](https://github.com/vanling1111/amazon-ads-api-python-sdk/discussions)
- **Email**: your.email@example.com

---

**Thank you for contributing!** 🎉

