#!/usr/bin/env python3
"""
Check for Amazon Ads API spec updates.

Compares remote spec files against local copies by downloading headers
(Content-Length, ETag, Last-Modified) and optionally full content.
Outputs a JSON report of changes suitable for CI consumption.

Usage:
    python scripts/check_spec_updates.py              # Quick header-only check
    python scripts/check_spec_updates.py --full        # Full content diff
    python scripts/check_spec_updates.py --json        # JSON output for CI
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import ssl
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

SDK_ROOT = Path(__file__).resolve().parent.parent
SPECS_DIR = SDK_ROOT / "specs"

sys.path.insert(0, str(SDK_ROOT))
from download_specs import SPEC_MAP


def _get_ssl_context() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def _local_hash(path: Path) -> str:
    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _remote_hash(url: str) -> tuple[str, int, str | None]:
    """Download a spec and return (sha256, size, error)."""
    ctx = _get_ssl_context()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "AmazonAdsSDK/1.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = resp.read()
            return hashlib.sha256(data).hexdigest(), len(data), None
    except Exception as e:
        return "", 0, str(e)


def _spec_filename(url: str, custom_name: str | None) -> str:
    if custom_name:
        return custom_name
    return url.rsplit("/", 1)[-1]


def check_updates(full_check: bool = False) -> list[dict]:
    """Check all specs for updates. Returns list of change records."""
    changes: list[dict] = []
    items = list(SPEC_MAP.items())

    if not full_check:
        # Quick check: compare file sizes only via HEAD request
        ctx = _get_ssl_context()
        for url, custom_name in items:
            filename = _spec_filename(url, custom_name)
            local_path = SPECS_DIR / filename

            if not local_path.exists():
                changes.append({
                    "file": filename,
                    "url": url,
                    "status": "new",
                    "detail": "File not found locally",
                })
                continue

            try:
                req = urllib.request.Request(url, method="HEAD",
                                            headers={"User-Agent": "AmazonAdsSDK/1.0"})
                with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                    remote_size = int(resp.headers.get("Content-Length", 0))
                    local_size = local_path.stat().st_size
                    if remote_size > 0 and abs(remote_size - local_size) > 10:
                        changes.append({
                            "file": filename,
                            "url": url,
                            "status": "size_changed",
                            "detail": f"local={local_size} remote={remote_size}",
                        })
            except Exception as e:
                if "403" not in str(e) and "404" not in str(e):
                    changes.append({
                        "file": filename,
                        "url": url,
                        "status": "error",
                        "detail": str(e),
                    })
        return changes

    # Full check: download and hash compare
    def _check_one(url: str, custom_name: str | None) -> dict | None:
        filename = _spec_filename(url, custom_name)
        local_path = SPECS_DIR / filename

        if not local_path.exists():
            return {
                "file": filename,
                "url": url,
                "status": "new",
                "detail": "File not found locally",
            }

        local_h = _local_hash(local_path)
        remote_h, remote_size, err = _remote_hash(url)

        if err:
            if "403" not in err and "404" not in err:
                return {
                    "file": filename,
                    "url": url,
                    "status": "error",
                    "detail": err,
                }
            return None

        if remote_h and remote_h != local_h:
            return {
                "file": filename,
                "url": url,
                "status": "content_changed",
                "detail": f"hash changed, remote_size={remote_size}",
            }
        return None

    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {
            pool.submit(_check_one, url, name): (url, name)
            for url, name in items
        }
        for future in as_completed(futures):
            result = future.result()
            if result:
                changes.append(result)

    return changes


def main():
    parser = argparse.ArgumentParser(description="Check for Amazon Ads API spec updates")
    parser.add_argument("--full", action="store_true", help="Full content hash comparison")
    parser.add_argument("--json", action="store_true", help="Output JSON for CI")
    args = parser.parse_args()

    changes = check_updates(full_check=args.full)

    if args.json:
        output = {
            "has_updates": len(changes) > 0,
            "changes": changes,
            "total_specs": len(SPEC_MAP),
        }
        print(json.dumps(output, indent=2))
    else:
        if not changes:
            print(f"All {len(SPEC_MAP)} specs are up to date.")
        else:
            print(f"Found {len(changes)} changes:")
            for c in changes:
                print(f"  [{c['status']}] {c['file']}: {c['detail']}")

    sys.exit(1 if changes else 0)


if __name__ == "__main__":
    main()
