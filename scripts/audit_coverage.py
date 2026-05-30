#!/usr/bin/env python3
"""Audit OpenAPI spec coverage vs generated clients and client.generated registry."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SDK_ROOT = Path(__file__).resolve().parent.parent
SPECS_DIR = SDK_ROOT / "specs"
CONFIG_PATH = SDK_ROOT / "codegen" / "spec_config.yaml"
CLIENTS_DIR = SDK_ROOT / "amazon_ads_api" / "generated" / "clients"
REGISTRY_PATH = SDK_ROOT / "amazon_ads_api" / "generated" / "registry.py"

sys.path.insert(0, str(SDK_ROOT))
from codegen.spec_parser import get_active_specs  # noqa: E402


def audit() -> dict:
    active = get_active_specs(CONFIG_PATH, SPECS_DIR)
    active_modules = [config["module"] for config, parsed in active]
    client_files = {
        path.stem.replace("clients_", "")
        for path in CLIENTS_DIR.glob("clients_*.py")
    }
    missing_clients = sorted(set(active_modules) - client_files)
    extra_clients = sorted(client_files - set(active_modules))

    operation_counts: dict[str, int] = {}
    for config, parsed in active:
        operation_counts[config["module"]] = len(parsed.operations)

    modules_with_zero_ops = sorted(
        module for module, count in operation_counts.items() if count == 0
    )
    total_operations = sum(operation_counts.values())

    registry_modules: tuple[str, ...] = ()
    if REGISTRY_PATH.exists():
        from amazon_ads_api.generated.registry import GeneratedAPIs

        registry_modules = GeneratedAPIs.module_names()

    registry_missing = sorted(set(client_files) - set(registry_modules))
    registry_extra = sorted(set(registry_modules) - client_files)

    return {
        "active_specs": len(active),
        "generated_client_modules": len(client_files),
        "registry_modules": len(registry_modules),
        "total_operations": total_operations,
        "missing_client_modules": missing_clients,
        "extra_client_modules": extra_clients,
        "modules_with_zero_operations": modules_with_zero_ops,
        "registry_missing": registry_missing,
        "registry_extra": registry_extra,
        "complete": (
            not missing_clients
            and not extra_clients
            and not registry_missing
            and not registry_extra
        ),
    }


def main() -> int:
    report = audit()
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
