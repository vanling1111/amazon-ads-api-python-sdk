#!/usr/bin/env python
"""
测试运行脚本

Usage:
    python scripts/run_tests.py              # 运行所有单元测试
    python scripts/run_tests.py --unit       # 只运行单元测试
    python scripts/run_tests.py --integration # 只运行集成测试
    python scripts/run_tests.py --coverage   # 运行测试并生成覆盖率报告
    python scripts/run_tests.py --all        # 运行所有测试
"""

import subprocess
import sys
import argparse
from pathlib import Path


def run_command(cmd: list[str]) -> int:
    """运行命令并返回退出码"""
    print(f"Running: {' '.join(cmd)}")
    print("-" * 60)
    result = subprocess.run(cmd)
    print("-" * 60)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Run SDK tests")
    parser.add_argument("--unit", action="store_true", help="Run unit tests only")
    parser.add_argument("--integration", action="store_true", help="Run integration tests only")
    parser.add_argument("--e2e", action="store_true", help="Run E2E tests only")
    parser.add_argument("--coverage", action="store_true", help="Generate coverage report")
    parser.add_argument("--all", action="store_true", help="Run all tests")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("-k", "--keyword", type=str, help="Run tests matching keyword")
    
    args = parser.parse_args()
    
    # 基础命令
    cmd = ["pytest"]
    
    # 添加详细输出
    if args.verbose:
        cmd.append("-v")
    
    # 添加关键字过滤
    if args.keyword:
        cmd.extend(["-k", args.keyword])
    
    # 测试类型选择
    if args.unit:
        cmd.extend(["-m", "unit", "tests/unit/"])
    elif args.integration:
        cmd.extend(["-m", "integration", "tests/integration/"])
    elif args.e2e:
        cmd.extend(["-m", "e2e", "tests/e2e/"])
    elif args.all:
        cmd.append("tests/")
    else:
        # 默认只运行单元测试
        cmd.extend(["-m", "unit", "tests/unit/"])
    
    # 添加覆盖率
    if args.coverage:
        cmd.extend([
            "--cov=amazon_ads_api",
            "--cov-report=html:htmlcov",
            "--cov-report=term-missing",
            "--cov-fail-under=50"  # 最低覆盖率要求
        ])
    
    # 添加通用选项
    cmd.extend([
        "--tb=short",  # 简短的 traceback
        "--strict-markers",  # 严格检查 markers
    ])
    
    # 运行测试
    exit_code = run_command(cmd)
    
    if args.coverage and exit_code == 0:
        print("\n✅ Coverage report generated: htmlcov/index.html")
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())

