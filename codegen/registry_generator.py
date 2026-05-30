"""Generate a lazy registry exposing every codegen client on AmazonAdsClient.generated."""

from __future__ import annotations

from pathlib import Path


def _client_class_name(module_name: str) -> str:
    parts = module_name.split("_")
    return "".join(p[:1].upper() + p[1:] for p in parts) + "Client"


def generate_registry(module_names: list[str]) -> str:
    sorted_modules = sorted(module_names)
    entries = "\n".join(
        f'    "{name}": ("amazon_ads_api.generated.clients.clients_{name}", "{_client_class_name(name)}"),'
        for name in sorted_modules
    )
    return f'''"""Auto-generated client registry. Do not edit manually."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from amazon_ads_api.client import AmazonAdsClient

_MODULE_CLIENTS: dict[str, tuple[str, str]] = {{
{entries}
}}


class GeneratedAPIs:
    """Lazy access to every OpenAPI-generated client module.

    Example::

        await client.generated.marketing_stream.create_stream_subscription(body={{...}})
        await client.generated.sp.create_campaign(...)
    """

    def __init__(self, client: "AmazonAdsClient") -> None:
        self._client = client
        self._instances: dict[str, Any] = {{}}

    @staticmethod
    def module_names() -> tuple[str, ...]:
        return tuple(sorted(_MODULE_CLIENTS))

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(name)
        if name not in _MODULE_CLIENTS:
            raise AttributeError(
                f"unknown generated module {{name!r}}; "
                f"available: {{', '.join(self.module_names())}}"
            )
        cached = self._instances.get(name)
        if cached is not None:
            return cached
        module_path, class_name = _MODULE_CLIENTS[name]
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        instance = self._client._create_client(cls)
        self._instances[name] = instance
        return instance

    def __dir__(self) -> list[str]:
        return sorted(set(super().__dir__()) | set(_MODULE_CLIENTS))


__all__ = ["GeneratedAPIs", "_MODULE_CLIENTS"]
'''


def write_registry(output_dir: Path, module_names: list[str] | None = None) -> Path:
    clients_dir = output_dir / "clients"
    if module_names is None:
        module_names = sorted(
            path.stem.replace("clients_", "")
            for path in clients_dir.glob("clients_*.py")
        )
    path = output_dir / "registry.py"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(generate_registry(module_names), encoding="utf-8")
    return path
