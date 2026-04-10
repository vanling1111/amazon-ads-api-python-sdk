#!/usr/bin/env python3
"""
Amazon Ads API SDK 覆盖率验证脚本

此脚本自动对比官方 spec 文件和 SDK 实现，生成详细的覆盖率报告。

使用方法:
    python scripts/verify_coverage.py

输出:
    - 控制台显示验证结果
    - 生成 COVERAGE_REPORT.md 详细报告
"""

import json
import os
import re
import ast
from pathlib import Path
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass, field
import yaml


@dataclass
class Endpoint:
    """API 端点"""
    method: str
    path: str
    operation_id: str = ""
    
    def __hash__(self):
        return hash((self.method.upper(), self.path))
    
    def __eq__(self, other):
        if isinstance(other, Endpoint):
            return self.method.upper() == other.method.upper() and self.path == other.path
        return False


@dataclass
class SpecFile:
    """Spec 文件信息"""
    name: str
    endpoints: List[Endpoint] = field(default_factory=list)
    

@dataclass
class SDKImplementation:
    """SDK 实现信息"""
    file_path: str
    endpoints: List[Endpoint] = field(default_factory=list)
    methods: List[str] = field(default_factory=list)


def load_json_spec(file_path: str) -> List[Endpoint]:
    """加载 JSON spec 文件"""
    endpoints = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        paths = data.get('paths', {})
        for path, methods in paths.items():
            for method, details in methods.items():
                if method.lower() in ['get', 'post', 'put', 'delete', 'patch']:
                    op_id = details.get('operationId', '') if isinstance(details, dict) else ''
                    endpoints.append(Endpoint(
                        method=method.upper(),
                        path=path,
                        operation_id=op_id
                    ))
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
    
    return endpoints


def load_yaml_spec(file_path: str) -> List[Endpoint]:
    """加载 YAML spec 文件"""
    endpoints = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        paths = data.get('paths', {})
        for path, methods in paths.items():
            for method, details in methods.items():
                if method.lower() in ['get', 'post', 'put', 'delete', 'patch']:
                    op_id = details.get('operationId', '') if isinstance(details, dict) else ''
                    endpoints.append(Endpoint(
                        method=method.upper(),
                        path=path,
                        operation_id=op_id
                    ))
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
    
    return endpoints


def extract_sdk_endpoints(file_path: str) -> Tuple[List[Endpoint], List[str]]:
    """从 SDK 源码提取实现的端点"""
    endpoints = []
    methods = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取所有 async def 方法
        method_pattern = r'async def (\w+)\s*\('
        methods = re.findall(method_pattern, content)
        
        # 提取端点路径
        # 模式1: await self.get("/path"
        # 模式2: await self.post("/path"
        # 模式3: f"/path/{var}"
        endpoint_patterns = [
            r'await self\.(get|post|put|delete|patch)\s*\(\s*[f]?"([^"]+)"',
            r'await self\.(get|post|put|delete|patch)\s*\(\s*f"([^"]+)"',
        ]
        
        for pattern in endpoint_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                method, path = match
                # 标准化路径（移除 f-string 变量）
                normalized_path = re.sub(r'\{[^}]+\}', '{id}', path)
                endpoints.append(Endpoint(method=method.upper(), path=path))
        
    except Exception as e:
        print(f"Error extracting from {file_path}: {e}")
    
    return endpoints, methods


def find_sdk_files(sdk_root: str) -> List[str]:
    """查找所有 SDK 实现文件"""
    files = []
    for root, dirs, filenames in os.walk(sdk_root):
        # 跳过 __pycache__ 和测试目录
        dirs[:] = [d for d in dirs if d not in ['__pycache__', 'tests', '.git']]
        
        for filename in filenames:
            if filename.endswith('.py') and filename not in ['__init__.py', 'base.py', 'client.py']:
                files.append(os.path.join(root, filename))
    
    return files


def normalize_path(path: str) -> str:
    """标准化路径用于比较"""
    # 将所有路径参数替换为通用占位符
    return re.sub(r'\{[^}]+\}', '{id}', path)


def endpoints_match(ep1: Endpoint, ep2: Endpoint) -> bool:
    """检查两个端点是否匹配"""
    if ep1.method.upper() != ep2.method.upper():
        return False
    # 精确匹配或标准化匹配
    if ep1.path == ep2.path:
        return True
    return normalize_path(ep1.path) == normalize_path(ep2.path)


def is_endpoint_covered(endpoint: Endpoint, sdk_endpoints: Set[Endpoint]) -> bool:
    """检查端点是否被 SDK 覆盖"""
    for sdk_ep in sdk_endpoints:
        if endpoints_match(endpoint, sdk_ep):
            return True
    return False


def generate_coverage_report(
    specs: Dict[str, SpecFile],
    sdk_impls: Dict[str, SDKImplementation],
    output_file: str
):
    """生成覆盖率报告"""
    
    # 收集所有 SDK 端点
    all_sdk_endpoints: Set[Endpoint] = set()
    for impl in sdk_impls.values():
        all_sdk_endpoints.update(impl.endpoints)
    
    # 计算覆盖情况（使用改进的匹配逻辑）
    total_spec = 0
    total_covered = 0
    missing_endpoints = []
    
    for spec in specs.values():
        for endpoint in spec.endpoints:
            total_spec += 1
            if is_endpoint_covered(endpoint, all_sdk_endpoints):
                total_covered += 1
            else:
                missing_endpoints.append(endpoint)
    
    coverage_pct = (total_covered / total_spec * 100) if total_spec > 0 else 0
    
    # 生成报告
    report = []
    report.append("# Amazon Ads API SDK 覆盖率报告\n")
    report.append(f"生成时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append("\n## 📊 总体统计\n")
    report.append(f"| 指标 | 数量 |")
    report.append(f"|------|------|")
    report.append(f"| 官方 Spec 文件 | {len(specs)} |")
    report.append(f"| SDK 实现文件 | {len(sdk_impls)} |")
    report.append(f"| 官方端点总数 | {total_spec} |")
    report.append(f"| SDK 已实现端点 | {len(all_sdk_endpoints)} |")
    report.append(f"| 已覆盖端点 | {total_covered} |")
    report.append(f"| **覆盖率** | **{coverage_pct:.1f}%** |")
    report.append("")
    
    # 按 Spec 文件详细报告
    report.append("\n## 📋 按 Spec 文件详细覆盖\n")
    report.append("| Spec 文件 | 端点数 | 已实现 | 覆盖率 |")
    report.append("|-----------|--------|--------|--------|")
    
    for spec_name, spec in sorted(specs.items()):
        total = len(spec.endpoints)
        impl_count = sum(1 for ep in spec.endpoints if is_endpoint_covered(ep, all_sdk_endpoints))
        pct = (impl_count / total * 100) if total > 0 else 0
        status = "[OK]" if pct >= 100 else "[WARN]" if pct >= 80 else "[MISS]"
        report.append(f"| {status} {spec_name} | {total} | {impl_count} | {pct:.0f}% |")
    
    report.append("")
    
    # 所有端点详细列表
    report.append("\n## 📝 所有官方端点验证\n")
    
    for spec_name, spec in sorted(specs.items()):
        report.append(f"\n### {spec_name}\n")
        report.append("| Method | Endpoint | Status |")
        report.append("|--------|----------|--------|")
        
        for endpoint in sorted(spec.endpoints, key=lambda e: (e.path, e.method)):
            is_covered = is_endpoint_covered(endpoint, all_sdk_endpoints)
            status = "[OK] Implemented" if is_covered else "[MISS] Missing"
            report.append(f"| {endpoint.method} | `{endpoint.path}` | {status} |")
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    return {
        'total_specs': len(specs),
        'total_spec_endpoints': total_spec,
        'total_sdk_endpoints': len(all_sdk_endpoints),
        'covered': total_covered,
        'missing': len(missing_endpoints),
        'coverage_pct': coverage_pct,
        'missing_endpoints': missing_endpoints
    }


def main():
    # 项目根目录
    project_root = Path(__file__).parent.parent
    specs_dir = project_root / 'specs'
    sdk_dir = project_root / 'amazon_ads_api'
    
    print("=" * 60)
    print("Amazon Ads API SDK Coverage Verification")
    print("=" * 60)
    
    # 1. 加载所有 spec 文件
    print("\n[1] Loading Spec files...")
    specs: Dict[str, SpecFile] = {}
    
    for spec_file in specs_dir.glob('*.json'):
        endpoints = load_json_spec(str(spec_file))
        if endpoints:
            specs[spec_file.name] = SpecFile(name=spec_file.name, endpoints=endpoints)
            print(f"  [OK] {spec_file.name}: {len(endpoints)} endpoints")
    
    for spec_file in specs_dir.glob('*.yaml'):
        endpoints = load_yaml_spec(str(spec_file))
        if endpoints:
            specs[spec_file.name] = SpecFile(name=spec_file.name, endpoints=endpoints)
            print(f"  [OK] {spec_file.name}: {len(endpoints)} endpoints")
    
    # 2. 扫描 SDK 实现
    print("\n[2] Scanning SDK implementations...")
    sdk_impls: Dict[str, SDKImplementation] = {}
    
    sdk_files = find_sdk_files(str(sdk_dir))
    for sdk_file in sdk_files:
        endpoints, methods = extract_sdk_endpoints(sdk_file)
        rel_path = os.path.relpath(sdk_file, str(sdk_dir))
        if endpoints:
            sdk_impls[rel_path] = SDKImplementation(
                file_path=rel_path,
                endpoints=endpoints,
                methods=methods
            )
            print(f"  [OK] {rel_path}: {len(endpoints)} endpoints, {len(methods)} methods")
    
    # 3. 生成覆盖率报告
    print("\n[3] Generating coverage report...")
    output_file = project_root / 'COVERAGE_REPORT.md'
    results = generate_coverage_report(specs, sdk_impls, str(output_file))
    
    # 4. 打印结果
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"  Spec files: {results['total_specs']}")
    print(f"  Official endpoints: {results['total_spec_endpoints']}")
    print(f"  SDK endpoints: {results['total_sdk_endpoints']}")
    print(f"  Covered: {results['covered']}")
    print(f"  Coverage: {results['coverage_pct']:.1f}%")
    
    if results['missing_endpoints']:
        print(f"\n[WARNING] Missing endpoints ({results['missing']}):")
        for ep in sorted(results['missing_endpoints'], key=lambda e: (e.path, e.method))[:20]:
            print(f"    - {ep.method} {ep.path}")
        if results['missing'] > 20:
            print(f"    ... and {results['missing'] - 20} more")
    else:
        print("\n[SUCCESS] All official endpoints are implemented!")
    
    print(f"\nDetailed report saved to: {output_file}")
    
    return results


if __name__ == '__main__':
    main()

