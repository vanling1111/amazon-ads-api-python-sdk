"""
Main code generation entry point.

Usage:
    python -m codegen.generate                    # generate all active specs
    python -m codegen.generate --spec sp          # generate only the 'sp' module
    python -m codegen.generate --dry-run          # parse + resolve, no file output
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from .spec_parser import get_active_specs
from .conflict_resolver import resolve_conflicts
from .model_generator import generate_models
from .client_generator import generate_client

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SPECS_DIR = PROJECT_ROOT / "specs"
CONFIG_PATH = PROJECT_ROOT / "codegen" / "spec_config.yaml"
OUTPUT_DIR = PROJECT_ROOT / "amazon_ads_api" / "generated"


def _write_if_changed(path: Path, content: str) -> bool:
    """Write file only if content changed. Returns True if written."""
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def _generate_init(output_dir: Path, modules: list[str], subdir: str) -> None:
    """Generate __init__.py that re-exports from all submodules."""
    init_path = output_dir / subdir / "__init__.py"
    lines = [f'"""Auto-generated {subdir}. Do not edit manually."""', ""]
    for mod in sorted(modules):
        lines.append(f"from .{subdir}_{mod} import *  # noqa: F401,F403")
    lines.append("")
    _write_if_changed(init_path, "\n".join(lines))


def run(
    spec_filter: str | None = None,
    dry_run: bool = False,
    verbose: bool = False,
) -> dict:
    """Run code generation."""
    t0 = time.time()

    print("=" * 60)
    print("Amazon Ads API SDK Code Generator")
    print("=" * 60)

    # 1. Load and parse active specs
    print("\n[1/4] Loading specs...")
    active_specs = get_active_specs(CONFIG_PATH, SPECS_DIR)
    print(f"  Loaded {len(active_specs)} active specs")

    # Filter if requested
    if spec_filter:
        active_specs = [
            (c, s) for c, s in active_specs
            if c.get("module") == spec_filter
        ]
        print(f"  Filtered to {len(active_specs)} specs (module={spec_filter})")

    if not active_specs:
        print("  No specs to process.")
        return {"status": "empty"}

    # 2. Resolve conflicts
    print("\n[2/4] Resolving conflicts...")
    resolved, report = resolve_conflicts(active_specs)
    print(f"  Total operations: {report.total_operations}")
    print(f"  Kept: {report.kept_operations}")
    print(f"  Dropped (conflicts): {report.dropped_operations}")
    if report.conflicts and verbose:
        for c in report.conflicts[:20]:
            print(f"    {c['method']} {c['path']}: {c['winner']} > {c['loser']}")

    if dry_run:
        print("\n[DRY RUN] No files written.")
        elapsed = time.time() - t0
        print(f"\nDone in {elapsed:.1f}s")
        return {
            "status": "dry_run",
            "specs": len(resolved),
            "operations": report.kept_operations,
            "conflicts": report.dropped_operations,
        }

    # 3. Generate models
    print("\n[3/4] Generating models...")
    models_dir = OUTPUT_DIR / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    model_modules: list[str] = []
    model_stats: dict[str, int] = {}

    for config, parsed in resolved:
        module_name = config["module"]
        if not parsed.schemas:
            continue

        code = generate_models(parsed)
        filename = f"models_{module_name}.py"
        out_path = models_dir / filename
        written = _write_if_changed(out_path, code)
        model_modules.append(module_name)

        import ast
        try:
            tree = ast.parse(code)
            n_classes = sum(1 for n in ast.walk(tree) if isinstance(n, ast.ClassDef))
        except SyntaxError:
            n_classes = -1

        model_stats[module_name] = n_classes
        status = "written" if written else "unchanged"
        if verbose:
            print(f"  [{status}] {filename}: {n_classes} classes")

    print(f"  Generated {len(model_modules)} model files")

    # 4. Generate clients
    print("\n[4/4] Generating clients...")
    clients_dir = OUTPUT_DIR / "clients"
    clients_dir.mkdir(parents=True, exist_ok=True)
    client_modules: list[str] = []
    client_stats: dict[str, int] = {}

    for config, parsed in resolved:
        module_name = config["module"]
        if not parsed.operations:
            continue

        code = generate_client(parsed, module_name)
        filename = f"clients_{module_name}.py"
        out_path = clients_dir / filename
        written = _write_if_changed(out_path, code)
        client_modules.append(module_name)

        client_stats[module_name] = len(parsed.operations)
        status = "written" if written else "unchanged"
        if verbose:
            print(f"  [{status}] {filename}: {len(parsed.operations)} operations")

    print(f"  Generated {len(client_modules)} client files")

    # Generate __init__.py files
    _generate_init(OUTPUT_DIR, model_modules, "models")
    _generate_init(OUTPUT_DIR, client_modules, "clients")

    # Summary
    elapsed = time.time() - t0
    total_classes = sum(model_stats.values())
    total_ops = sum(client_stats.values())
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Specs processed:  {len(resolved)}")
    print(f"  Model files:      {len(model_modules)} ({total_classes} classes)")
    print(f"  Client files:     {len(client_modules)} ({total_ops} operations)")
    print(f"  Conflicts resolved: {report.dropped_operations}")
    print(f"  Time:             {elapsed:.1f}s")
    print(f"  Output:           {OUTPUT_DIR}")

    return {
        "status": "ok",
        "specs": len(resolved),
        "model_files": len(model_modules),
        "client_files": len(client_modules),
        "total_classes": total_classes,
        "total_operations": total_ops,
        "conflicts_dropped": report.dropped_operations,
        "elapsed": elapsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Amazon Ads API SDK Code Generator")
    parser.add_argument("--spec", help="Generate only this module (e.g. 'sp')")
    parser.add_argument("--dry-run", action="store_true", help="Parse only, no file output")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    result = run(spec_filter=args.spec, dry_run=args.dry_run, verbose=args.verbose)
    if result.get("status") == "ok":
        sys.exit(0)
    elif result.get("status") == "dry_run":
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
