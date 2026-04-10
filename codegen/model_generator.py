"""
Generate Pydantic v2 models from OpenAPI schemas.

Handles:
- $ref resolution to Python class references
- camelCase -> snake_case with Field(alias=...)
- enum -> StrEnum
- allOf composition (merged properties)
- oneOf / anyOf -> Union types
- nested objects -> inline or referenced classes
- additionalProperties -> dict fields
"""

from __future__ import annotations

import keyword
import re
from dataclasses import dataclass
from typing import Any

from .spec_parser import ParsedSpec, ref_to_name, resolve_ref

HEADER = '''"""Auto-generated Pydantic models. Do not edit manually.

Source: {source_file}
Title:  {title}
"""

from __future__ import annotations

from enum import StrEnum  # noqa: F401
from typing import Any, Optional, Union  # noqa: F401

from pydantic import BaseModel, Field  # noqa: F401


'''

RESERVED = set(keyword.kwlist) | {"type", "list", "dict", "set", "id", "format", "input", "filter"}


def _sanitize_str(s: str) -> str:
    """Remove newlines and problematic chars from a string used in code."""
    return s.replace("\n", " ").replace("\r", "").replace('"', "'").replace("\\", "\\\\").strip()


def _camel_to_snake(name: str) -> str:
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    return s2.lower()


def _safe_field_name(name: str) -> str:
    snake = _camel_to_snake(name)
    if snake in RESERVED or snake.startswith("__"):
        snake = f"{snake}_"
    snake = re.sub(r"[^a-zA-Z0-9_]", "_", snake)
    if snake and snake[0].isdigit():
        snake = f"f_{snake}"
    return snake


def _safe_class_name(name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", name)
    if not cleaned or cleaned[0].isdigit():
        cleaned = f"Schema{cleaned}"
    return cleaned


def _is_simple_type(schema: dict[str, Any]) -> bool:
    """Check if schema maps to a simple Python type (no class needed)."""
    if "$ref" in schema:
        return False
    t = schema.get("type", "")
    if t in ("string", "integer", "number", "boolean"):
        return True
    if t == "array" and "items" in schema:
        return _is_simple_type(schema["items"])
    return False


@dataclass
class _TypeMapping:
    python_type: str
    needs_import: str | None = None


class ModelGenerator:
    def __init__(self, spec: ParsedSpec):
        self.spec = spec
        self._generated_enums: set[str] = set()
        self._generated_classes: set[str] = set()
        self._output_lines: list[str] = []
        self._forward_refs: set[str] = set()

    def _resolve_type(
        self,
        schema: dict[str, Any],
        field_name: str = "",
        parent_name: str = "",
    ) -> str:
        """Convert an OpenAPI schema to a Python type annotation string."""
        if "$ref" in schema:
            ref_name = ref_to_name(schema["$ref"])
            class_name = _safe_class_name(ref_name)
            self._forward_refs.add(class_name)
            return f'"{class_name}"'

        t = schema.get("type", "")
        fmt = schema.get("format", "")

        if "enum" in schema and t == "string":
            enum_name = _safe_class_name(
                f"{parent_name}{field_name.title()}" if field_name else parent_name
            )
            if enum_name not in self._generated_enums:
                self._generate_enum(enum_name, schema["enum"])
            return enum_name

        if t == "string":
            return "str"
        if t == "integer":
            return "int"
        if t == "number":
            if fmt == "integer":
                return "int"
            return "float"
        if t == "boolean":
            return "bool"

        if t == "array":
            items = schema.get("items", {})
            item_type = self._resolve_type(items, field_name, parent_name)
            return f"list[{item_type}]"

        if t == "object":
            if "properties" in schema:
                inline_name = _safe_class_name(
                    f"{parent_name}{field_name.title()}" if field_name else f"{parent_name}Inline"
                )
                if inline_name not in self._generated_classes:
                    self._generate_model_class(inline_name, schema)
                return f'"{inline_name}"'
            ap = schema.get("additionalProperties")
            if isinstance(ap, dict) and ap:
                val_type = self._resolve_type(ap, field_name, parent_name)
                return f"dict[str, {val_type}]"
            return "dict[str, Any]"

        if "allOf" in schema:
            return self._resolve_allof(schema["allOf"], parent_name, field_name)
        if "oneOf" in schema:
            return self._resolve_union(schema["oneOf"], parent_name, field_name)
        if "anyOf" in schema:
            return self._resolve_union(schema["anyOf"], parent_name, field_name)

        return "Any"

    def _resolve_allof(
        self, items: list[dict], parent_name: str, field_name: str
    ) -> str:
        """allOf -> merged model or a single $ref."""
        refs = [i for i in items if "$ref" in i]
        props = {}
        required: list[str] = []
        for item in items:
            if "$ref" in item:
                resolved = resolve_ref(self.spec.raw, item["$ref"])
                props.update(resolved.get("properties", {}))
                required.extend(resolved.get("required", []))
            else:
                props.update(item.get("properties", {}))
                required.extend(item.get("required", []))

        if len(refs) == 1 and not any("properties" in i for i in items if "$ref" not in i):
            return self._resolve_type(refs[0], field_name, parent_name)

        if props:
            merged_name = _safe_class_name(
                f"{parent_name}{field_name.title()}" if field_name else f"{parent_name}AllOf"
            )
            if merged_name not in self._generated_classes:
                merged_schema = {"type": "object", "properties": props, "required": required}
                self._generate_model_class(merged_name, merged_schema)
            return f'"{merged_name}"'

        if refs:
            return self._resolve_type(refs[0], field_name, parent_name)
        return "Any"

    def _resolve_union(
        self, items: list[dict], parent_name: str, field_name: str
    ) -> str:
        types = []
        for item in items:
            t = self._resolve_type(item, field_name, parent_name)
            if t not in types:
                types.append(t)
        if len(types) == 1:
            return types[0]
        return f"Union[{', '.join(types)}]"

    def _generate_enum(self, name: str, values: list) -> None:
        self._generated_enums.add(name)
        lines = [f"\nclass {name}(StrEnum):"]
        for val in values:
            if not isinstance(val, str):
                val = str(val)
            member = re.sub(r"[^a-zA-Z0-9_]", "_", val.upper())
            if not member or member[0].isdigit():
                member = f"V_{member}"
            if member in ("", "_"):
                member = "EMPTY"
            safe_val = _sanitize_str(val)
            lines.append(f'    {member} = "{safe_val}"')
        if len(values) == 0:
            lines.append("    pass")
        lines.append("")
        self._output_lines.extend(lines)

    def _generate_model_class(self, name: str, schema: dict[str, Any]) -> None:
        self._generated_classes.add(name)
        required_fields = set(schema.get("required", []))
        properties = schema.get("properties", {})
        desc = schema.get("description", "")

        lines = [f"\nclass {name}(BaseModel):"]
        if desc:
            escaped = _sanitize_str(desc)[:200]
            lines.append(f'    """{escaped}"""')

        if not properties:
            if schema.get("additionalProperties"):
                ap = schema["additionalProperties"]
                val_type = "Any"
                if isinstance(ap, dict):
                    val_type = self._resolve_type(ap, "", name)
                lines.append(
                    f"    __root__: dict[str, {val_type}] = {{}}"
                )
            else:
                lines.append("    pass")
            lines.append("")
            self._output_lines.extend(lines)
            return

        for prop_name, prop_schema in properties.items():
            if not isinstance(prop_schema, dict):
                continue
            snake = _safe_field_name(prop_name)
            py_type = self._resolve_type(prop_schema, prop_name, name)
            is_required = prop_name in required_fields
            prop_desc = prop_schema.get("description", "")

            field_args = []
            if snake != prop_name:
                field_args.append(f'alias="{prop_name}"')
            if prop_desc:
                short_desc = _sanitize_str(prop_desc)[:120]
                field_args.append(f'description="{short_desc}"')

            if is_required:
                if field_args:
                    lines.append(f"    {snake}: {py_type} = Field(..., {', '.join(field_args)})")
                else:
                    lines.append(f"    {snake}: {py_type}")
            else:
                default = "None"
                if field_args:
                    lines.append(
                        f"    {snake}: Optional[{py_type}] = Field({default}, {', '.join(field_args)})"
                    )
                else:
                    lines.append(f"    {snake}: Optional[{py_type}] = {default}")

        lines.append("")
        lines.append("    model_config = {'populate_by_name': True}")
        lines.append("")
        self._output_lines.extend(lines)

    def generate(self) -> str:
        """Generate the full Python module string for all schemas."""
        self._output_lines = []
        self._generated_enums = set()
        self._generated_classes = set()
        self._forward_refs = set()

        sorted_schemas = self._topological_sort()

        for name in sorted_schemas:
            schema_def = self.spec.schemas[name]
            class_name = _safe_class_name(name)

            if schema_def.enum_values is not None:
                if class_name not in self._generated_enums:
                    self._generate_enum(class_name, schema_def.enum_values)
                continue

            if class_name not in self._generated_classes:
                self._generate_model_class(class_name, schema_def.raw)

        header = HEADER.format(
            source_file=self.spec.source_file,
            title=self.spec.title,
        )
        return header + "\n".join(self._output_lines) + "\n"

    def _topological_sort(self) -> list[str]:
        """Sort schemas so dependencies come before dependents."""
        visited: set[str] = set()
        order: list[str] = []
        in_stack: set[str] = set()

        def _get_deps(name: str) -> set[str]:
            schema = self.spec.schemas.get(name)
            if not schema:
                return set()
            deps: set[str] = set()
            raw_str = str(schema.raw)
            for match in re.finditer(r'#/components/schemas/([^"\'}\s,]+)', raw_str):
                dep_name = match.group(1)
                if dep_name in self.spec.schemas and dep_name != name:
                    deps.add(dep_name)
            return deps

        def visit(name: str) -> None:
            if name in visited:
                return
            if name in in_stack:
                visited.add(name)
                order.append(name)
                return
            in_stack.add(name)
            for dep in _get_deps(name):
                visit(dep)
            in_stack.discard(name)
            visited.add(name)
            order.append(name)

        for name in self.spec.schemas:
            visit(name)

        return order


def generate_models(spec: ParsedSpec) -> str:
    """Public API: generate Pydantic model code from a parsed spec."""
    gen = ModelGenerator(spec)
    return gen.generate()
