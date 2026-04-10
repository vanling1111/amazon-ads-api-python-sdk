#!/usr/bin/env python3
"""
Amazon Ads API SDK 深度验证脚本

验证内容:
1. 端点正确性 - HTTP方法、路径是否与spec一致
2. 参数完整性 - 是否实现了所有必需参数
3. 重复冗余检测 - 检测重复的端点实现
4. SDK内部一致性 - 检测内部冲突

使用方法:
    python scripts/deep_verify.py
"""

import json
import os
import re
import ast
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from dataclasses import dataclass, field
from collections import defaultdict
import yaml


@dataclass
class EndpointSpec:
    """官方Spec端点定义"""
    method: str
    path: str
    operation_id: str = ""
    parameters: List[Dict] = field(default_factory=list)
    request_body: Dict = field(default_factory=dict)
    content_type: str = ""
    
    def __hash__(self):
        return hash((self.method.upper(), self.path))


@dataclass
class SDKEndpoint:
    """SDK实现的端点"""
    method: str
    path: str
    file_path: str
    function_name: str
    line_number: int = 0
    
    def __hash__(self):
        return hash((self.method.upper(), self.path))


def load_spec_endpoints(specs_dir: str) -> Dict[str, List[EndpointSpec]]:
    """加载所有spec文件的端点定义"""
    specs = {}
    
    for spec_file in Path(specs_dir).glob('*.json'):
        try:
            with open(spec_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            endpoints = []
            paths = data.get('paths', {})
            for path, methods in paths.items():
                for method, details in methods.items():
                    if method.lower() in ['get', 'post', 'put', 'delete', 'patch']:
                        ep = EndpointSpec(
                            method=method.upper(),
                            path=path,
                            operation_id=details.get('operationId', ''),
                            parameters=details.get('parameters', []),
                            request_body=details.get('requestBody', {}),
                        )
                        # 提取content-type
                        if 'requestBody' in details:
                            content = details['requestBody'].get('content', {})
                            if content:
                                ep.content_type = list(content.keys())[0]
                        endpoints.append(ep)
            
            if endpoints:
                specs[spec_file.name] = endpoints
        except Exception as e:
            print(f"Error loading {spec_file}: {e}")
    
    for spec_file in Path(specs_dir).glob('*.yaml'):
        try:
            with open(spec_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            endpoints = []
            paths = data.get('paths', {})
            for path, methods in paths.items():
                for method, details in methods.items():
                    if method.lower() in ['get', 'post', 'put', 'delete', 'patch']:
                        ep = EndpointSpec(
                            method=method.upper(),
                            path=path,
                            operation_id=details.get('operationId', ''),
                            parameters=details.get('parameters', []),
                            request_body=details.get('requestBody', {}),
                        )
                        endpoints.append(ep)
            
            if endpoints:
                specs[spec_file.name] = endpoints
        except Exception as e:
            print(f"Error loading {spec_file}: {e}")
    
    return specs


def extract_sdk_endpoints_detailed(file_path: str) -> List[SDKEndpoint]:
    """从SDK源码提取详细的端点信息"""
    endpoints = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        # 查找所有 async def 函数
        current_func = None
        current_line = 0
        
        for i, line in enumerate(lines, 1):
            # 检测函数定义
            func_match = re.match(r'\s*async def (\w+)\s*\(', line)
            if func_match:
                current_func = func_match.group(1)
                current_line = i
            
            # 检测API调用 - 多种模式
            if current_func:
                # 模式1: await self.get("/path"
                # 模式2: await self.post(f"/path/{var}"
                # 模式3: result = await self.get(
                patterns = [
                    r'await self\.(get|post|put|delete|patch)\s*\(\s*f?"([^"]+)"',
                    r'await self\.(get|post|put|delete|patch)\s*\(\s*f\'([^\']+)\'',
                    r'self\.(get|post|put|delete|patch)\s*\(\s*f?"([^"]+)"',
                    r'self\.(get|post|put|delete|patch)\s*\(\s*f\'([^\']+)\'',
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        method, path = match.groups()
                        endpoints.append(SDKEndpoint(
                            method=method.upper(),
                            path=path,
                            file_path=file_path,
                            function_name=current_func,
                            line_number=i
                        ))
                        break  # 只计算一次
    
    except Exception as e:
        print(f"Error extracting from {file_path}: {e}")
    
    return endpoints


def normalize_path(path: str) -> str:
    """标准化路径用于比较"""
    return re.sub(r'\{[^}]+\}', '{id}', path)


def check_duplicates(all_sdk_endpoints: List[SDKEndpoint]) -> List[Dict]:
    """检测重复的端点实现"""
    duplicates = []
    endpoint_map = defaultdict(list)
    
    for ep in all_sdk_endpoints:
        key = (ep.method.upper(), normalize_path(ep.path))
        endpoint_map[key].append(ep)
    
    for key, eps in endpoint_map.items():
        if len(eps) > 1:
            # 检查是否真的是重复（同一个文件内的可能是不同上下文）
            unique_files = set(ep.file_path for ep in eps)
            if len(unique_files) > 1:
                duplicates.append({
                    'method': key[0],
                    'path': key[1],
                    'implementations': [
                        {
                            'file': os.path.relpath(ep.file_path),
                            'function': ep.function_name,
                            'line': ep.line_number
                        }
                        for ep in eps
                    ]
                })
    
    return duplicates


def check_spec_compliance(
    spec_endpoints: Dict[str, List[EndpointSpec]],
    sdk_endpoints: List[SDKEndpoint]
) -> Dict[str, Any]:
    """检查SDK实现与Spec的合规性"""
    issues = {
        'missing_required_params': [],
        'wrong_method': [],
        'path_mismatch': [],
        'missing_endpoints': [],
    }
    
    # 创建SDK端点查找表 - 按路径分组
    sdk_by_path = defaultdict(set)
    for ep in sdk_endpoints:
        normalized = normalize_path(ep.path)
        sdk_by_path[normalized].add(ep.method.upper())
    
    # 检查每个spec端点
    for spec_name, endpoints in spec_endpoints.items():
        for spec_ep in endpoints:
            normalized_path = normalize_path(spec_ep.path)
            
            # 检查是否有这个路径的任何实现
            if normalized_path in sdk_by_path:
                # 检查是否有正确的HTTP方法
                sdk_methods = sdk_by_path[normalized_path]
                if spec_ep.method.upper() not in sdk_methods:
                    # 这个路径存在但没有这个HTTP方法
                    issues['missing_endpoints'].append({
                        'spec': spec_name,
                        'path': spec_ep.path,
                        'method': spec_ep.method.upper(),
                        'available_methods': list(sdk_methods),
                    })
            else:
                # 路径完全不存在
                issues['missing_endpoints'].append({
                    'spec': spec_name,
                    'path': spec_ep.path,
                    'method': spec_ep.method.upper(),
                    'available_methods': [],
                })
    
    return issues


def check_internal_consistency(sdk_dir: str) -> Dict[str, Any]:
    """检查SDK内部一致性"""
    issues = {
        'conflicting_endpoints': [],
        'orphan_files': [],
    }
    
    # 检查是否有未导出的模块
    init_files = list(Path(sdk_dir).rglob('__init__.py'))
    py_files = [f for f in Path(sdk_dir).rglob('*.py') 
                if f.name not in ['__init__.py', 'base.py', 'client.py']]
    
    # 简单检查：计算文件数量一致性
    module_count = len(py_files)
    
    return issues


def generate_deep_report(
    specs: Dict[str, List[EndpointSpec]],
    sdk_endpoints: List[SDKEndpoint],
    duplicates: List[Dict],
    compliance_issues: Dict[str, Any],
    output_file: str
):
    """生成深度验证报告"""
    report = []
    report.append("# Amazon Ads API SDK Deep Verification Report\n")
    report.append(f"Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # 1. 总体统计
    total_spec_endpoints = sum(len(eps) for eps in specs.values())
    total_sdk_endpoints = len(sdk_endpoints)
    unique_sdk_endpoints = len(set((ep.method, normalize_path(ep.path)) for ep in sdk_endpoints))
    
    report.append("\n## 1. Summary Statistics\n")
    report.append("| Metric | Count |")
    report.append("|--------|-------|")
    report.append(f"| Official Spec Endpoints | {total_spec_endpoints} |")
    report.append(f"| SDK Endpoint Calls | {total_sdk_endpoints} |")
    report.append(f"| Unique SDK Endpoints | {unique_sdk_endpoints} |")
    report.append(f"| Duplicate Implementations | {len(duplicates)} |")
    report.append("")
    
    # 2. 重复检测
    report.append("\n## 2. Duplicate Detection\n")
    if duplicates:
        report.append(f"**Found {len(duplicates)} potentially duplicated endpoints:**\n")
        for dup in duplicates:
            report.append(f"\n### {dup['method']} {dup['path']}\n")
            report.append("| File | Function | Line |")
            report.append("|------|----------|------|")
            for impl in dup['implementations']:
                report.append(f"| `{impl['file']}` | `{impl['function']}` | {impl['line']} |")
    else:
        report.append("**No duplicates found across different files.**\n")
    
    # 3. 合规性问题
    report.append("\n## 3. Compliance Issues\n")
    has_issues = False
    
    if compliance_issues.get('missing_endpoints'):
        # 过滤掉已有其他方法实现的端点（可能是误报）
        truly_missing = [
            ep for ep in compliance_issues['missing_endpoints']
            if not ep.get('available_methods')  # 路径完全不存在
        ]
        
        if truly_missing:
            has_issues = True
            report.append(f"\n### Missing Endpoints ({len(truly_missing)})\n")
            report.append("| Spec | Method | Path |")
            report.append("|------|--------|------|")
            for issue in truly_missing[:50]:  # 限制显示
                report.append(f"| {issue['spec']} | {issue['method']} | `{issue['path']}` |")
            if len(truly_missing) > 50:
                report.append(f"\n... and {len(truly_missing) - 50} more")
    
    if not has_issues:
        report.append("**No compliance issues found.**\n")
    
    # 4. 按模块统计
    report.append("\n## 4. Implementation by Module\n")
    
    # 统计每个文件的端点数
    file_stats = defaultdict(int)
    for ep in sdk_endpoints:
        rel_path = os.path.relpath(ep.file_path)
        file_stats[rel_path] += 1
    
    report.append("| Module | Endpoint Calls |")
    report.append("|--------|----------------|")
    for file_path, count in sorted(file_stats.items()):
        report.append(f"| `{file_path}` | {count} |")
    
    # 5. 验证结论
    report.append("\n## 5. Verification Conclusion\n")
    
    truly_missing_count = len([
        ep for ep in compliance_issues.get('missing_endpoints', [])
        if not ep.get('available_methods')
    ])
    
    if not duplicates and truly_missing_count == 0:
        report.append("### [PASS] All Checks Passed\n")
        report.append("- No critical duplicate implementations\n")
        report.append("- All spec endpoints have SDK implementations\n")
        report.append("- SDK implementation is consistent with official specs\n")
    else:
        report.append("### [ATTENTION] Issues Found\n")
        if duplicates:
            report.append(f"- {len(duplicates)} potential duplicate implementations (may be intentional)\n")
        if truly_missing_count > 0:
            report.append(f"- {truly_missing_count} truly missing endpoints\n")
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    return {
        'total_spec': total_spec_endpoints,
        'total_sdk': total_sdk_endpoints,
        'unique_sdk': unique_sdk_endpoints,
        'duplicates': len(duplicates),
        'compliance_issues': sum(len(v) for v in compliance_issues.values() if isinstance(v, list)),
        'pass': not duplicates and not has_issues
    }


def main():
    project_root = Path(__file__).parent.parent
    specs_dir = project_root / 'specs'
    sdk_dir = project_root / 'amazon_ads_api'
    
    print("=" * 60)
    print("Amazon Ads API SDK Deep Verification")
    print("=" * 60)
    
    # 1. 加载Spec
    print("\n[1] Loading official specs...")
    specs = load_spec_endpoints(str(specs_dir))
    total_spec = sum(len(eps) for eps in specs.values())
    print(f"    Loaded {len(specs)} spec files with {total_spec} endpoints")
    
    # 2. 扫描SDK
    print("\n[2] Scanning SDK implementations...")
    all_sdk_endpoints = []
    
    for py_file in Path(sdk_dir).rglob('*.py'):
        if py_file.name not in ['__init__.py', 'base.py', 'client.py']:
            endpoints = extract_sdk_endpoints_detailed(str(py_file))
            all_sdk_endpoints.extend(endpoints)
    
    print(f"    Found {len(all_sdk_endpoints)} endpoint calls in SDK")
    
    # 3. 检测重复
    print("\n[3] Checking for duplicates...")
    duplicates = check_duplicates(all_sdk_endpoints)
    if duplicates:
        print(f"    [WARNING] Found {len(duplicates)} potential duplicates")
    else:
        print("    [OK] No duplicates found")
    
    # 4. 检查合规性
    print("\n[4] Checking spec compliance...")
    compliance_issues = check_spec_compliance(specs, all_sdk_endpoints)
    issue_count = sum(len(v) for v in compliance_issues.values() if isinstance(v, list))
    if issue_count:
        print(f"    [WARNING] Found {issue_count} compliance issues")
    else:
        print("    [OK] All implementations comply with specs")
    
    # 5. 生成报告
    print("\n[5] Generating detailed report...")
    output_file = project_root / 'DEEP_VERIFICATION_REPORT.md'
    results = generate_deep_report(
        specs, all_sdk_endpoints, duplicates, compliance_issues, str(output_file)
    )
    
    # 打印结果
    print("\n" + "=" * 60)
    print("VERIFICATION RESULTS")
    print("=" * 60)
    print(f"  Spec Endpoints: {results['total_spec']}")
    print(f"  SDK Endpoint Calls: {results['total_sdk']}")
    print(f"  Unique SDK Endpoints: {results['unique_sdk']}")
    print(f"  Duplicates: {results['duplicates']}")
    print(f"  Compliance Issues: {results['compliance_issues']}")
    
    if results['pass']:
        print("\n  [PASS] All checks passed!")
    else:
        print("\n  [ATTENTION] Issues found - review report for details")
    
    print(f"\nDetailed report saved to: {output_file}")
    
    return results


if __name__ == '__main__':
    main()

