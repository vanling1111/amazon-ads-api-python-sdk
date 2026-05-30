"""
Resolve conflicts when the same endpoint path appears in multiple specs.

Strategy:
- Each spec entry in spec_config.yaml can have a `priority` (lower = higher priority).
- When the same method+path pair appears in specs with different modules,
  only the highest-priority spec generates that endpoint.
- Within the same module, all operations are kept (no dedup needed since
  they come from the same logical API).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .spec_parser import ParsedSpec, Operation


@dataclass
class ConflictReport:
    total_operations: int
    kept_operations: int
    dropped_operations: int
    conflicts: list[dict[str, Any]]


def resolve_conflicts(
    specs: list[tuple[dict[str, Any], ParsedSpec]],
) -> tuple[list[tuple[dict, ParsedSpec]], ConflictReport]:
    """
    Resolve endpoint conflicts across multiple specs.

    Each entry is (config_dict, parsed_spec). Returns a new list where
    conflicting operations have been removed from lower-priority specs.
    """
    endpoint_owners: dict[tuple[str, str], tuple[int, str, str]] = {}
    conflicts: list[dict[str, Any]] = []

    for config, parsed in specs:
        priority = config.get("priority", 100)
        module = config.get("module", "unknown")
        for op in parsed.operations:
            key = (op.method, op.path)
            if key in endpoint_owners:
                existing_pri, existing_mod, existing_file = endpoint_owners[key]
                if module == existing_mod:
                    continue
                if priority < existing_pri:
                    conflicts.append({
                        "method": op.method,
                        "path": op.path,
                        "winner": f"{module} (pri={priority})",
                        "loser": f"{existing_mod} (pri={existing_pri})",
                    })
                    endpoint_owners[key] = (priority, module, parsed.source_file)
                else:
                    conflicts.append({
                        "method": op.method,
                        "path": op.path,
                        "winner": f"{existing_mod} (pri={existing_pri})",
                        "loser": f"{module} (pri={priority})",
                    })
            else:
                endpoint_owners[key] = (priority, module, parsed.source_file)

    total = 0
    kept = 0
    result: list[tuple[dict, ParsedSpec]] = []

    for config, parsed in specs:
        module = config.get("module", "unknown")
        filtered_ops: list[Operation] = []

        for op in parsed.operations:
            total += 1
            key = (op.method, op.path)
            _, owner_module, owner_file = endpoint_owners.get(key, (999, "", ""))
            if owner_module == module:
                filtered_ops.append(op)
                kept += 1

        filtered_spec = ParsedSpec(
            title=parsed.title,
            version=parsed.version,
            description=parsed.description,
            operations=filtered_ops,
            schemas=parsed.schemas,
            raw=parsed.raw,
            source_file=parsed.source_file,
        )
        result.append((config, filtered_spec))

    report = ConflictReport(
        total_operations=total,
        kept_operations=kept,
        dropped_operations=total - kept,
        conflicts=conflicts,
    )
    return result, report
