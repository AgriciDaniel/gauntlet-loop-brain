#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable


def run(args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run([PY, *args], cwd=REPO, text=True, capture_output=True, env={**os.environ, **(env or {})}, check=False)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise AssertionError(f"command failed: {' '.join(args)}")
    return proc


def run_cmd(args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(args, cwd=REPO, text=True, capture_output=True, env={**os.environ, **(env or {})}, check=False)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise AssertionError(f"command failed: {' '.join(args)}")
    return proc


def main() -> int:
    run(["-m", "compileall", "scripts", "gauntlet_loop_brain", "tests"])
    run(["-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"])
    run(["scripts/lint_vault.py", "--vault", "assets/template-brain", "--template"])
    with tempfile.TemporaryDirectory(prefix="gauntlet-loop-brain-test-") as tmp:
        out_dir = Path(tmp) / "vaults"
        run(["scripts/scaffold_vault.py", "--client", "acme", "--client-name", "Acme Co", "--owner", "Test Owner", "--out-dir", str(out_dir)])
        vault = out_dir / "acme"
        run(["scripts/ingest_source.py", "--vault", str(vault), "--file", "tests/fixtures/sample-source.md"])
        run(["scripts/synthesize_brain.py", "--vault", str(vault)])
        run(["scripts/generate_vault_visuals.py", "--vault", str(vault)])
        run(["scripts/render_brain_report.py", "--vault", str(vault), "--html-only"])
        run(["scripts/lint_vault.py", "--vault", str(vault)])
        assert (vault / "weekly-report.html").exists()
    run(["scripts/build_demo_vault.py"])
    audit = run(["scripts/audit_brain.py", "--json", "--report-only"])
    audit_result = json.loads(audit.stdout)
    market_ready = audit_result.get("market_ready") is True or audit_result.get("status") == "market-ready"
    assert audit_result["publication_ready"] is False
    assert "release manifest" in audit_result["publication_readiness_scope"]
    gated = subprocess.run([PY, "scripts/package_release.py", "--version", "0.1.0", "--release-type", "market-ready"], cwd=REPO, text=True, capture_output=True, check=False)
    if market_ready:
        if gated.returncode:
            print(gated.stdout)
            print(gated.stderr, file=sys.stderr)
        assert gated.returncode == 0
        manifest = REPO / "dist" / "RELEASE_MANIFEST.json"
        assert manifest.exists()
        assert json.loads(manifest.read_text(encoding="utf-8")).get("release_type") == "market-ready"
    else:
        assert gated.returncode != 0
        assert "market-ready release blocked" in gated.stderr
    run(["scripts/package_release.py", "--version", "0.1.0"])
    release_manifest = json.loads((REPO / "dist" / "RELEASE_MANIFEST.json").read_text(encoding="utf-8"))
    assert release_manifest["publication_ready"] is False
    assert release_manifest["market_ready"] is False
    assert release_manifest["distribution_status"] == "internal-review-only"
    assert release_manifest["market_validation"] == {
        "buyer_demand_validated": False,
        "equal_budget_advantage_validated": False,
        "retention_validated": False,
    }
    assert "release type is internal-only" in release_manifest["publication_blockers"]
    assert "final license has not been selected by the owner" in release_manifest["publication_blockers"]
    provenance_blocker = "release provenance is not bound to a Git commit"
    if (REPO / ".git").exists():
        expected_commit = run_cmd(["git", "rev-parse", "HEAD"]).stdout.strip()
        assert release_manifest["git_commit"] == expected_commit
        assert provenance_blocker not in release_manifest["publication_blockers"]
    else:
        assert release_manifest["git_commit"] is None
        assert provenance_blocker in release_manifest["publication_blockers"]
    excluded_parts = {".raw", ".obsidian", "runs", "private"}
    excluded_names = {"hot.md", "log.md"}
    excluded_paths = {"references/source-ledger.json", "references/claim-ledger.md"}
    for archive in (REPO / "dist").glob("*.zip"):
        with zipfile.ZipFile(archive) as zf:
            for name in zf.namelist():
                parts = Path(name).parts[1:]
                payload = Path(*parts)
                assert not (set(parts) & excluded_parts), (archive.name, name)
                assert payload.name not in excluded_names, (archive.name, name)
                assert payload.as_posix() not in excluded_paths, (archive.name, name)
    source_archive = REPO / "dist" / "gauntlet-loop-brain-source-v0.1.0.zip"
    with tempfile.TemporaryDirectory(prefix="gauntlet-public-source-") as extracted:
        with zipfile.ZipFile(source_archive) as zf:
            zf.extractall(extracted)
        public_source = Path(extracted) / "gauntlet-loop-brain-v0.1.0"
        public_lint = subprocess.run([PY, "scripts/lint_vault.py", "--vault", "assets/template-brain", "--template"], cwd=public_source, text=True, capture_output=True, check=False)
        assert public_lint.returncode == 0, public_lint.stdout + public_lint.stderr
        public_vaults = Path(extracted) / "public-vaults"
        public_scaffold = subprocess.run([PY, "scripts/scaffold_vault.py", "--client", "public-smoke", "--owner", "Test Owner", "--out-dir", str(public_vaults)], cwd=public_source, text=True, capture_output=True, check=False)
        assert public_scaffold.returncode == 0, public_scaffold.stdout + public_scaffold.stderr
        public_vault = public_vaults / "public-smoke"
        public_vault_lint = subprocess.run([PY, "scripts/lint_vault.py", "--vault", str(public_vault)], cwd=public_source, text=True, capture_output=True, check=False)
        assert public_vault_lint.returncode == 0, public_vault_lint.stdout + public_vault_lint.stderr
    for archive_name, root_name in [
        ("gauntlet-loop-brain-template-v0.1.0.zip", "gauntlet-loop-brain-template"),
        ("gauntlet-loop-brain-sample-vault-v0.1.0.zip", "gauntlet-loop-brain-sample-vault"),
    ]:
        with tempfile.TemporaryDirectory(prefix="gauntlet-public-vault-") as extracted:
            with zipfile.ZipFile(REPO / "dist" / archive_name) as zf:
                zf.extractall(extracted)
            public_vault = Path(extracted) / root_name
            public_lint = subprocess.run([PY, "scripts/lint_vault.py", "--vault", str(public_vault), "--template"], cwd=REPO, text=True, capture_output=True, check=False)
            assert public_lint.returncode == 0, public_lint.stdout + public_lint.stderr
    with tempfile.TemporaryDirectory(prefix="gauntlet-loop-brain-install-") as tmp:
        env = {"GAUNTLET_LOOP_BRAIN_INSTALL_HOME": tmp}
        run_cmd(["bash", "install.sh", "--target", "all"], env=env)
        assert (Path(tmp) / ".codex" / "skills" / "gauntlet-loop-brain" / "SKILL.md").exists()
        assert (Path(tmp) / ".openclaw" / "skills" / "gauntlet-loop-brain" / "SKILL.md").exists()
        assert (Path(tmp) / ".agent-skills" / "gauntlet-loop-brain" / "SKILL.md").exists()
        assert (Path(tmp) / ".gemini" / "gauntlet-loop-brain" / "GEMINI.md").exists()
        assert "gauntlet-loop-brain-install:start" in (Path(tmp) / ".gemini" / "GEMINI.md").read_text(encoding="utf-8")
        custom_root = Path(tmp) / "custom-skills"
        run_cmd(["bash", "install.sh", "--target", "custom", "--path", str(custom_root)], env=env)
        assert (custom_root / "gauntlet-loop-brain" / "SKILL.md").exists()
        assert (custom_root / "gauntlet-loop-brain" / ".gauntlet-loop-brain-owned").read_text(encoding="utf-8").strip() == "gauntlet-loop-brain-owned:v1"
        assert (custom_root / "gauntlet-loop-brain" / ".gauntlet-loop-brain-manifest.json").exists()
        user_added = custom_root / "gauntlet-loop-brain" / "user-added.txt"
        user_added.write_text("preserve me\n", encoding="utf-8")
        refused_upgrade = subprocess.run(["bash", "install.sh", "--target", "custom", "--path", str(custom_root)], cwd=REPO, text=True, capture_output=True, env={**os.environ, **env}, check=False)
        assert refused_upgrade.returncode != 0
        assert "changed or user-added content" in refused_upgrade.stderr
        refused_owned_remove = subprocess.run(["bash", "uninstall.sh", "--target", "custom", "--path", str(custom_root)], cwd=REPO, text=True, capture_output=True, env={**os.environ, **env}, check=False)
        assert refused_owned_remove.returncode != 0
        assert user_added.exists()
        user_added.unlink()
        collision_root = Path(tmp) / "collision-skills"
        collision = collision_root / "gauntlet-loop-brain"
        collision.mkdir(parents=True)
        (collision / "user.txt").write_text("user owned\n", encoding="utf-8")
        refused = subprocess.run(["bash", "install.sh", "--target", "custom", "--path", str(collision_root)], cwd=REPO, text=True, capture_output=True, env={**os.environ, **env}, check=False)
        assert refused.returncode != 0
        assert "refusing to replace unowned installation" in refused.stderr
        refused_remove = subprocess.run(["bash", "uninstall.sh", "--target", "custom", "--path", str(collision_root)], cwd=REPO, text=True, capture_output=True, env={**os.environ, **env}, check=False)
        assert refused_remove.returncode != 0
        assert (collision / "user.txt").exists()
        external_loader = Path(tmp) / "external-loader.md"
        external_loader.write_text("keep me\n", encoding="utf-8")
        gemini_loader = Path(tmp) / ".gemini" / "GEMINI.md"
        run_cmd(["bash", "uninstall.sh", "--target", "gemini"], env=env)
        gemini_loader.parent.mkdir(parents=True, exist_ok=True)
        gemini_loader.symlink_to(external_loader)
        refused_loader = subprocess.run(["bash", "install.sh", "--target", "gemini"], cwd=REPO, text=True, capture_output=True, env={**os.environ, **env}, check=False)
        assert refused_loader.returncode != 0
        assert "symlink Gemini loader" in refused_loader.stderr
        assert external_loader.read_text(encoding="utf-8") == "keep me\n"
        gemini_loader.unlink()
        run_cmd(["bash", "install.sh", "--target", "gemini"], env=env)
        gemini_loader.unlink()
        gemini_loader.symlink_to(external_loader)
        refused_loader_remove = subprocess.run(["bash", "uninstall.sh", "--target", "gemini"], cwd=REPO, text=True, capture_output=True, env={**os.environ, **env}, check=False)
        assert refused_loader_remove.returncode != 0
        assert "symlink Gemini loader" in refused_loader_remove.stderr
        assert (Path(tmp) / ".gemini" / "gauntlet-loop-brain").exists()
        assert external_loader.read_text(encoding="utf-8") == "keep me\n"
        gemini_loader.unlink()
        run_cmd(["bash", "install.sh", "--target", "gemini"], env=env)
        run_cmd(["bash", "uninstall.sh", "--target", "all"], env=env)
        assert not (Path(tmp) / ".codex" / "skills" / "gauntlet-loop-brain").exists()
        assert not (Path(tmp) / ".gemini" / "gauntlet-loop-brain").exists()
        assert not (Path(tmp) / ".gemini" / "GEMINI.md").exists()
        run_cmd(["bash", "uninstall.sh", "--target", "custom", "--path", str(custom_root)], env=env)
        assert not (custom_root / "gauntlet-loop-brain").exists()
    print("Pipeline tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
