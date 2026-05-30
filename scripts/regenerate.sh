#!/usr/bin/env bash
# Regenerate all models and clients from OpenAPI specs.
# Usage: ./scripts/regenerate.sh [-v] [--spec MODULE]
set -euo pipefail

cd "$(dirname "$0")/.."
python3 -m codegen.generate "$@"
