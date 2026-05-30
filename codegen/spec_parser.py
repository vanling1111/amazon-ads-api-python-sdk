"""
OpenAPI spec parser for Amazon Ads API.

Loads JSON/YAML spec files and extracts paths, schemas, and resolves $ref
references into a normalized intermediate representation used by the
model and client generators.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Parameter:
    name: str
    location: str  # query, path, header, cookie
    required: bool = False
    schema: dict[str, Any] = field(default_factory=dict)
    description: str = ""


@dataclass
class Operation:
    method: str  # GET, POST, PUT, DELETE, PATCH
    path: str
    operation_id: str = ""
    summary: str = ""
    description: str = ""
    parameters: list[Parameter] = field(default_factory=list)
    request_body_ref: str | None = None
    request_body_schema: dict[str, Any] = field(default_factory=dict)
    request_content_type: str = "application/json"
    response_ref: str | None = None
    response_schema: dict[str, Any] = field(default_factory=dict)
    response_content_type: str = "application/json"
    tags: list[str] = field(default_factory=list)


@dataclass
class SchemaProperty:
    name: str
    type_info: dict[str, Any]
    required: bool = False
    description: str = ""


@dataclass
class SchemaDefinition:
    name: str
    properties: list[SchemaProperty] = field(default_factory=list)
    required_fields: list[str] = field(default_factory=list)
    enum_values: list[str] | None = None
    description: str = ""
    all_of: list[dict[str, Any]] = field(default_factory=list)
    one_of: list[dict[str, Any]] = field(default_factory=list)
    any_of: list[dict[str, Any]] = field(default_factory=list)
    additional_properties: dict[str, Any] | bool | None = None
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class ParsedSpec:
    title: str
    version: str
    description: str
    operations: list[Operation]
    schemas: dict[str, SchemaDefinition]
    raw: dict[str, Any]
    source_file: str


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except ImportError:
        raise RuntimeError(
            "PyYAML is required to parse YAML specs. "
            "Install it with: pip install pyyaml"
        )


def _load_json(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    cleaned = text.replace("\t", " ").replace("\r", "").replace("\x00", "")
    return json.loads(cleaned, strict=False)


def load_spec_file(path: Path) -> dict[str, Any]:
    """Load an OpenAPI spec from JSON or YAML."""
    suffix = path.suffix.lower()
    if suffix in (".yaml", ".yml"):
        return _load_yaml(path)
    return _load_json(path)


def resolve_ref(spec: dict[str, Any], ref: str) -> dict[str, Any]:
    """Resolve a $ref pointer like '#/components/schemas/Foo'."""
    if not ref.startswith("#/"):
        return {}
    parts = ref[2:].split("/")
    current: Any = spec
    for part in parts:
        if isinstance(current, dict):
            current = current.get(part, {})
        else:
            return {}
    return current if isinstance(current, dict) else {}


def ref_to_name(ref: str) -> str:
    """Extract the schema name from a $ref string."""
    return ref.rsplit("/", 1)[-1] if ref else ""


def _extract_schema_from_content(content: dict[str, Any]) -> tuple[str, dict, str | None]:
    """Extract schema and content-type from a requestBody/response content block."""
    for ct, ct_data in content.items():
        schema = ct_data.get("schema", {})
        ref = schema.get("$ref")
        return ct, schema, ref
    return "application/json", {}, None


def _parse_parameters(
    raw_params: list[dict[str, Any]], spec: dict[str, Any]
) -> list[Parameter]:
    params = []
    for p in raw_params:
        if "$ref" in p:
            p = resolve_ref(spec, p["$ref"])
        if not p:
            continue
        params.append(Parameter(
            name=p.get("name", ""),
            location=p.get("in", "query"),
            required=p.get("required", False),
            schema=p.get("schema", {}),
            description=p.get("description", ""),
        ))
    return params


def _parse_operations(spec: dict[str, Any]) -> list[Operation]:
    ops: list[Operation] = []
    paths = spec.get("paths", {})
    http_methods = {"get", "post", "put", "delete", "patch"}

    for path, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        path_params = _parse_parameters(path_item.get("parameters", []), spec)

        for method_str, op_data in path_item.items():
            if method_str.lower() not in http_methods:
                continue
            if not isinstance(op_data, dict):
                continue

            method = method_str.upper()
            op_params = _parse_parameters(op_data.get("parameters", []), spec)
            all_params = path_params + op_params

            req_ct = "application/json"
            req_schema: dict[str, Any] = {}
            req_ref: str | None = None
            rb = op_data.get("requestBody", {})
            if "$ref" in rb:
                rb = resolve_ref(spec, rb["$ref"])
            content = rb.get("content", {})
            if content:
                req_ct, req_schema, req_ref = _extract_schema_from_content(content)

            resp_ct = "application/json"
            resp_schema: dict[str, Any] = {}
            resp_ref: str | None = None
            responses = op_data.get("responses", {})
            for code in ("200", "201", "202", "207"):
                if code in responses:
                    resp_data = responses[code]
                    if "$ref" in resp_data:
                        resp_data = resolve_ref(spec, resp_data["$ref"])
                    resp_content = resp_data.get("content", {})
                    if resp_content:
                        resp_ct, resp_schema, resp_ref = _extract_schema_from_content(resp_content)
                    break

            ops.append(Operation(
                method=method,
                path=path,
                operation_id=op_data.get("operationId", ""),
                summary=op_data.get("summary", ""),
                description=op_data.get("description", ""),
                parameters=all_params,
                request_body_ref=req_ref,
                request_body_schema=req_schema,
                request_content_type=req_ct,
                response_ref=resp_ref,
                response_schema=resp_schema,
                response_content_type=resp_ct,
                tags=op_data.get("tags", []),
            ))

    return ops


def _parse_schema(name: str, raw: dict[str, Any]) -> SchemaDefinition:
    required_fields = raw.get("required", [])
    if not isinstance(required_fields, list):
        required_fields = []

    properties = []
    for prop_name, prop_data in raw.get("properties", {}).items():
        if not isinstance(prop_data, dict):
            continue
        properties.append(SchemaProperty(
            name=prop_name,
            type_info=prop_data,
            required=prop_name in required_fields,
            description=prop_data.get("description", ""),
        ))

    enum_values = raw.get("enum")
    if enum_values is not None and not isinstance(enum_values, list):
        enum_values = None

    return SchemaDefinition(
        name=name,
        properties=properties,
        required_fields=required_fields,
        enum_values=enum_values,
        description=raw.get("description", ""),
        all_of=raw.get("allOf", []),
        one_of=raw.get("oneOf", []),
        any_of=raw.get("anyOf", []),
        additional_properties=raw.get("additionalProperties"),
        raw=raw,
    )


def _parse_schemas(spec: dict[str, Any]) -> dict[str, SchemaDefinition]:
    schemas: dict[str, SchemaDefinition] = {}
    components = spec.get("components", {})
    raw_schemas = components.get("schemas", {})
    for name, raw in raw_schemas.items():
        if not isinstance(raw, dict):
            continue
        schemas[name] = _parse_schema(name, raw)
    return schemas


def parse_spec(path: Path) -> ParsedSpec:
    """Parse an OpenAPI spec file into our intermediate representation."""
    raw = load_spec_file(path)
    info = raw.get("info", {})
    return ParsedSpec(
        title=info.get("title", ""),
        version=info.get("version", ""),
        description=info.get("description", ""),
        operations=_parse_operations(raw),
        schemas=_parse_schemas(raw),
        raw=raw,
        source_file=path.name,
    )


def load_config(config_path: Path) -> list[dict[str, Any]]:
    """Load spec_config.yaml and return the specs list."""
    data = _load_yaml(config_path)
    return data.get("specs", [])


def get_active_specs(config_path: Path, specs_dir: Path) -> list[tuple[dict, ParsedSpec]]:
    """Load config and parse all specs marked generate: true."""
    entries = load_config(config_path)
    results: list[tuple[dict, ParsedSpec]] = []
    for entry in entries:
        if entry.get("generate") is not True:
            continue
        spec_file = specs_dir / entry["file"]
        if not spec_file.exists():
            print(f"[WARN] Spec file not found: {spec_file}")
            continue
        parsed = parse_spec(spec_file)
        if not parsed.operations and not parsed.schemas:
            print(f"[WARN] Empty spec: {spec_file}")
            continue
        results.append((entry, parsed))
    return results
