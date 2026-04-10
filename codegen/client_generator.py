"""
Generate async API client classes from OpenAPI paths.

Each spec produces a client class inheriting from BaseAdsClient with one
async method per operation. Methods accept typed request models and return
typed response models (from the generated models module).
"""

from __future__ import annotations

import re

from .spec_parser import ParsedSpec, Operation, ref_to_name
from .model_generator import _safe_class_name, _camel_to_snake, _sanitize_str

CLIENT_HEADER = '''"""Auto-generated async API client. Do not edit manually.

Source: {source_file}
Title:  {title}
"""

from __future__ import annotations

from typing import Any

from amazon_ads_api.base import BaseAdsClient, JSONData, JSONList

try:
    from .{models_module} import *  # noqa: F403
except ImportError:
    pass


'''


def _operation_to_method_name(op: Operation) -> str:
    """Derive a Python method name from an operation."""
    if op.operation_id:
        name = _camel_to_snake(op.operation_id)
    else:
        parts = op.path.strip("/").split("/")
        safe_parts = [re.sub(r"\{[^}]+\}", "by_id", p) for p in parts]
        name = f"{op.method.lower()}_{'_'.join(safe_parts)}"

    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    if not name:
        name = "unknown_operation"
    return name


def _has_path_params(path: str) -> bool:
    return "{" in path


def _extract_path_params(op: Operation) -> list[str]:
    return [p.name for p in op.parameters if p.location == "path"]


def _extract_query_params(op: Operation) -> list[tuple[str, str]]:
    """Return list of (original_name, safe_python_name) for query/header params."""
    result = []
    for p in op.parameters:
        if p.location in ("query", "header"):
            safe = _safe_param_name(p.name)
            result.append((p.name, safe))
    return result


def _safe_param_name(name: str) -> str:
    """Make a parameter name safe for use as a Python identifier."""
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    safe = _camel_to_snake(safe).strip("_")
    safe = re.sub(r"_+", "_", safe)
    if not safe or safe[0].isdigit():
        safe = f"p_{safe}"
    import keyword
    if keyword.iskeyword(safe):
        safe = f"{safe}_"
    return safe


def _generate_method(op: Operation, models_module: str) -> list[str]:
    """Generate a single async method for an operation."""
    method_name = _operation_to_method_name(op)
    method_lower = op.method.lower()
    lines: list[str] = []

    path_params = _extract_path_params(op)
    query_params = _extract_query_params(op)

    has_body = op.method in ("POST", "PUT", "PATCH") and (
        op.request_body_ref or op.request_body_schema
    )

    req_type = None
    if has_body and op.request_body_ref:
        req_type = _safe_class_name(ref_to_name(op.request_body_ref))

    sig_parts = ["self"]
    for pp in path_params:
        sig_parts.append(f"{_camel_to_snake(pp)}: str")

    if has_body:
        if req_type:
            sig_parts.append(f"body: {req_type} | dict[str, Any] | None = None")
        else:
            sig_parts.append("body: dict[str, Any] | None = None")

    for orig_name, safe_name in query_params:
        sig_parts.append(f"{safe_name}: str | None = None")

    return_type = "JSONData | JSONList"
    sig = ", ".join(sig_parts)

    desc = _sanitize_str(op.summary or op.description or "")[:120]
    lines.append(f"    async def {method_name}({sig}) -> {return_type}:")
    lines.append(f'        """{op.method} {op.path}')
    if desc:
        lines.append("")
        lines.append(f"        {desc}")
    lines.append('        """')

    path_expr = op.path
    if path_params:
        for pp in path_params:
            placeholder = "{" + pp + "}"
            snake_pp = _camel_to_snake(pp)
            path_expr = path_expr.replace(placeholder, "{" + snake_pp + "}")
        lines.append(f'        endpoint = f"{path_expr}"')
    else:
        lines.append(f'        endpoint = "{path_expr}"')

    if query_params:
        lines.append("        params: dict[str, Any] = {}")
        for orig_name, safe_name in query_params:
            lines.append(f'        if {safe_name} is not None:')
            lines.append(f'            params["{orig_name}"] = {safe_name}')

    if has_body:
        lines.append("        json_data = None")
        lines.append("        if body is not None:")
        lines.append("            if hasattr(body, 'model_dump'):")
        lines.append("                json_data = body.model_dump(by_alias=True, exclude_none=True)")
        lines.append("            else:")
        lines.append("                json_data = body")

    call_args = ["endpoint"]
    if has_body:
        call_args.append("json_data=json_data")
    if query_params:
        call_args.append("params=params")

    ct = op.request_content_type
    if ct and ct != "application/json":
        call_args.append(f'content_type="{ct}"')

    call_str = ", ".join(call_args)

    if method_lower == "get":
        lines.append(f"        return await self.get({call_str})")
    elif method_lower == "delete":
        lines.append(f"        return await self.delete({call_str})")
    elif method_lower == "put":
        lines.append(f"        return await self.put({call_str})")
    elif method_lower == "patch":
        if not hasattr(None, '_'):
            lines.append(f"        return await self._request('PATCH', {call_str})")
    else:
        lines.append(f"        return await self.post({call_str})")

    lines.append("")
    return lines


def generate_client(spec: ParsedSpec, module_name: str) -> str:
    """Generate the full client module for a spec."""
    models_module = f"models_{module_name}"
    class_name = "".join(
        word.capitalize() for word in module_name.split("_")
    ) + "Client"

    header = CLIENT_HEADER.format(
        source_file=spec.source_file,
        title=spec.title,
        models_module=models_module,
    )

    lines = [f"class {class_name}(BaseAdsClient):"]
    lines.append(f'    """Auto-generated from {spec.source_file} ({len(spec.operations)} operations)"""')
    lines.append("")

    seen_methods: set[str] = set()
    for op in spec.operations:
        method_name = _operation_to_method_name(op)
        if method_name in seen_methods:
            method_name = f"{method_name}_{op.method.lower()}"
        seen_methods.add(method_name)

        method_lines = _generate_method(op, models_module)
        for ml in method_lines:
            original_name = _operation_to_method_name(op)
            lines.append(ml.replace(f"def {original_name}(", f"def {method_name}(")
                         if original_name != method_name and f"def {original_name}(" in ml
                         else ml)

    if len(spec.operations) == 0:
        lines.append("    pass")
        lines.append("")

    return header + "\n".join(lines) + "\n"
