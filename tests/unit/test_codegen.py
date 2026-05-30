"""
Code generator unit tests.

Validates that the spec parser, model generator, client generator,
and conflict resolver all work correctly.
"""

import ast
import os
from pathlib import Path

import pytest

SDK_ROOT = Path(__file__).resolve().parent.parent.parent
SPECS_DIR = SDK_ROOT / "specs"
CONFIG_PATH = SDK_ROOT / "codegen" / "spec_config.yaml"


@pytest.mark.unit
class TestSpecParser:

    def test_parse_json_spec(self):
        from codegen.spec_parser import parse_spec
        spec = parse_spec(SPECS_DIR / "SponsoredProducts_prod_3p.json")
        assert spec.title == "Sponsored Products"
        assert len(spec.operations) > 50
        assert len(spec.schemas) > 100

    def test_parse_yaml_spec(self):
        from codegen.spec_parser import parse_spec
        spec = parse_spec(SPECS_DIR / "SponsoredDisplay_v3_openapi.yaml")
        assert spec.title
        assert len(spec.operations) > 0

    def test_load_config(self):
        from codegen.spec_parser import load_config
        entries = load_config(CONFIG_PATH)
        assert len(entries) > 70
        active = [e for e in entries if e.get("generate") is True]
        assert len(active) > 60

    def test_get_active_specs(self):
        from codegen.spec_parser import get_active_specs
        active = get_active_specs(CONFIG_PATH, SPECS_DIR)
        assert len(active) >= 70

    def test_operation_fields(self):
        from codegen.spec_parser import parse_spec
        spec = parse_spec(SPECS_DIR / "SponsoredProducts_prod_3p.json")
        op = spec.operations[0]
        assert op.method in ("GET", "POST", "PUT", "DELETE", "PATCH")
        assert op.path.startswith("/")

    def test_schema_fields(self):
        from codegen.spec_parser import parse_spec
        spec = parse_spec(SPECS_DIR / "SponsoredProducts_prod_3p.json")
        assert len(spec.schemas) > 0
        name, schema = next(iter(spec.schemas.items()))
        assert schema.name == name


@pytest.mark.unit
class TestModelGenerator:

    def test_generate_sp_models(self):
        from codegen.spec_parser import parse_spec
        from codegen.model_generator import generate_models
        spec = parse_spec(SPECS_DIR / "SponsoredProducts_prod_3p.json")
        code = generate_models(spec)
        tree = ast.parse(code)
        classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        assert len(classes) > 500

    def test_generated_models_have_valid_syntax(self):
        from codegen.spec_parser import get_active_specs
        from codegen.model_generator import generate_models
        active = get_active_specs(CONFIG_PATH, SPECS_DIR)
        for config, parsed in active[:5]:
            if not parsed.schemas:
                continue
            code = generate_models(parsed)
            ast.parse(code)

    def test_models_contain_basemodel(self):
        from codegen.spec_parser import parse_spec
        from codegen.model_generator import generate_models
        spec = parse_spec(SPECS_DIR / "SponsoredProducts_prod_3p.json")
        code = generate_models(spec)
        assert "class " in code
        assert "BaseModel" in code
        assert "Field" in code

    def test_enums_generated(self):
        from codegen.spec_parser import parse_spec
        from codegen.model_generator import generate_models
        spec = parse_spec(SPECS_DIR / "SponsoredProducts_prod_3p.json")
        code = generate_models(spec)
        assert "StrEnum" in code


@pytest.mark.unit
class TestClientGenerator:

    def test_generate_sp_client(self):
        from codegen.spec_parser import parse_spec
        from codegen.client_generator import generate_client
        spec = parse_spec(SPECS_DIR / "SponsoredProducts_prod_3p.json")
        code = generate_client(spec, "sp")
        tree = ast.parse(code)
        classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        assert len(classes) == 1
        assert classes[0].name == "SpClient"

    def test_client_has_async_methods(self):
        from codegen.spec_parser import parse_spec
        from codegen.client_generator import generate_client
        spec = parse_spec(SPECS_DIR / "SponsoredProducts_prod_3p.json")
        code = generate_client(spec, "sp")
        tree = ast.parse(code)
        methods = [n for n in ast.walk(tree) if isinstance(n, ast.AsyncFunctionDef)]
        assert len(methods) == len(spec.operations)

    def test_generated_clients_have_valid_syntax(self):
        from codegen.spec_parser import get_active_specs
        from codegen.client_generator import generate_client
        active = get_active_specs(CONFIG_PATH, SPECS_DIR)
        for config, parsed in active:
            if not parsed.operations:
                continue
            code = generate_client(parsed, config["module"])
            ast.parse(code)


@pytest.mark.unit
class TestConflictResolver:

    def test_no_conflicts_single_spec(self):
        from codegen.spec_parser import parse_spec
        from codegen.conflict_resolver import resolve_conflicts
        spec = parse_spec(SPECS_DIR / "SponsoredProducts_prod_3p.json")
        config = {"module": "sp", "priority": 100}
        resolved, report = resolve_conflicts([(config, spec)])
        assert report.dropped_operations == 0
        assert report.kept_operations == len(spec.operations)

    def test_conflicts_resolved_by_priority(self):
        from codegen.spec_parser import parse_spec
        from codegen.conflict_resolver import resolve_conflicts

        spec1 = parse_spec(SPECS_DIR / "SponsoredDisplay_prod_3p.json")
        spec2 = parse_spec(SPECS_DIR / "SponsoredDisplay_v3_openapi.yaml")
        config1 = {"module": "sd", "priority": 1}
        config2 = {"module": "sd_v3", "priority": 100}

        resolved, report = resolve_conflicts([(config1, spec1), (config2, spec2)])
        assert report.dropped_operations > 0


@pytest.mark.unit
class TestFullGeneration:

    def test_all_generated_files_exist(self):
        gen_dir = SDK_ROOT / "amazon_ads_api" / "generated"
        models_dir = gen_dir / "models"
        clients_dir = gen_dir / "clients"
        assert models_dir.exists()
        assert clients_dir.exists()
        model_files = [f for f in os.listdir(models_dir) if f.endswith(".py") and f != "__init__.py"]
        client_files = [f for f in os.listdir(clients_dir) if f.endswith(".py") and f != "__init__.py"]
        assert len(model_files) >= 70
        assert len(client_files) >= 70

    def test_generated_registry_covers_all_clients(self):
        from scripts.audit_coverage import audit

        report = audit()
        assert report["complete"] is True
        assert report["generated_client_modules"] >= 78
        assert report["total_operations"] >= 690

    def test_amazon_ads_client_generated_accessor(self):
        from amazon_ads_api import AmazonAdsClient, AdsRegion

        client = AmazonAdsClient(
            client_id="x",
            client_secret="y",
            refresh_token="z",
            profile_id="123",
            region=AdsRegion.NA,
        )
        assert "marketing_stream" in client.generated.module_names()
        assert hasattr(client.generated.marketing_stream, "create_stream_subscription")
        assert hasattr(client.reference.stream.subscriptions, "create_subscription")

    def test_all_generated_files_valid_syntax(self):
        gen_dir = SDK_ROOT / "amazon_ads_api" / "generated"
        for subdir in ["models", "clients"]:
            d = gen_dir / subdir
            for f in d.iterdir():
                if f.suffix == ".py":
                    ast.parse(f.read_text())
