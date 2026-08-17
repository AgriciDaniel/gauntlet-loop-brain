#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


REPO = Path(__file__).resolve().parent.parent
TEXT_SUFFIXES = {".base", ".canvas", ".css", ".csv", ".html", ".json", ".md", ".py", ".sh", ".toml", ".txt", ".yaml", ".yml"}
SKIP_PARTS = {".git", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "__pycache__", "build", "dist", "venv"}
SKIP_SUFFIXES = {".pyc", ".pyo", ".log"}
FORBIDDEN_ENTRY_NAMES = {".env", ".env.local", ".env.production", ".DS_Store", "Thumbs.db", "workspace.json"}
PUBLIC_EXCLUDED_PARTS = {".raw", ".obsidian", "runs", "private"}
PUBLIC_EXCLUDED_NAMES = {"hot.md", "log.md"}
PUBLIC_EXCLUDED_PATHS = {"references/source-ledger.json", "references/claim-ledger.md"}
MAX_SCAN_BYTES = 25 * 1024 * 1024
FORBIDDEN_TEXT_PATTERNS = {
    "local home path": re.compile(rb"/(?:var/)?home/(?!\.\.\.)[A-Za-z0-9_.-]+"),
    "private key": re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "openai api key": re.compile(rb"sk-[A-Za-z0-9_-]{20,}"),
    "anthropic api key": re.compile(rb"sk-ant-[A-Za-z0-9_-]{20,}"),
    "github token": re.compile(rb"(ghp|github_pat)_[A-Za-z0-9_]{20,}"),
    "aws key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "google api key": re.compile(rb"AIza[0-9A-Za-z_-]{20,}"),
    "bearer literal": re.compile(rb"Bearer\s+[A-Za-z0-9._-]{24,}"),
}
PUBLIC_MARKET_CLAIM_PATTERNS = {
    "validated buyer demand": re.compile(r"\b(?:validated buyer demand|buyer demand (?:is|has been) validated)\b", re.I),
    "validated retention": re.compile(r"\b(?:validated retention|retention (?:is|has been) validated)\b", re.I),
    "validated equal-budget advantage": re.compile(
        r"\b(?:validated equal-budget advantage|equal-budget advantage (?:is|has been) (?:validated|proven)|proven to outperform)\b",
        re.I,
    ),
}
NEGATED_MARKET_CLAIM_CONTEXT = re.compile(
    r"\b(?:not|never|unvalidated|cannot|do not|does not|must not|no claim|no public surface|blocked until|remain unavailable|forbid)\b",
    re.I,
)
SECURITY_URL_PREFIX = "Private vulnerability reporting URL:"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build verified release ZIP artifacts.")
    parser.add_argument("--version", required=True)
    parser.add_argument("--dist-dir", default="dist")
    parser.add_argument(
        "--release-type",
        default="scaffold",
        choices=["scaffold", "demo", "experimental", "market-ready"],
    )
    args = parser.parse_args(argv)
    version = normalize_version(args.version)
    dist = (REPO / args.dist_dir).resolve()
    if dist != REPO and not dist.is_relative_to(REPO):
        raise SystemExit(f"ERROR: --dist-dir must resolve inside the repo: {dist}")
    if args.release_type == "experimental":
        enforce_publication_gate("experimental public")
    if args.release_type == "market-ready":
        enforce_market_ready_gate()
    dist.mkdir(parents=True, exist_ok=True)
    scan_source_tree()
    artifacts = [
        build_zip(dist / f"gauntlet-loop-brain-template-v{version}.zip", REPO / "assets" / "template-brain", "gauntlet-loop-brain-template"),
        build_zip(dist / f"gauntlet-loop-brain-sample-vault-v{version}.zip", REPO / "examples" / "sample-vault", "gauntlet-loop-brain-sample-vault"),
        build_source_zip(dist / f"gauntlet-loop-brain-source-v{version}.zip", version),
    ]
    for artifact in artifacts:
        validate_zip(artifact["path"])
    release_semantics = describe_release_type(args.release_type)
    public_release = release_semantics["publication_ready"]
    blockers = [] if public_release else publication_blockers()
    if not public_release:
        blockers.append("release type is internal-only")
    manifest = {
        "product": "gauntlet-loop-brain",
        "version": version,
        "release_type": args.release_type,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "git_commit": git_commit(),
        **release_semantics,
        "publication_blockers": blockers,
        "security_reporting_url": configured_security_url() if public_release else None,
        "artifacts": [{"file": a["path"].name, "sha256": sha256_file(a["path"]), "bytes": a["path"].stat().st_size, "entries": a["entries"]} for a in artifacts],
        "checks": [
            "repo source scan passed",
            "zip entry scan passed",
            "zip content secret scan passed",
            "zip content local-path scan passed",
            "public exclusion policy passed",
            "public market-claim overstatement scan passed",
        ],
    }
    manifest_path = dist / "RELEASE_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sums = dist / "SHA256SUMS"
    write_sha256s(sums, [*(a["path"] for a in artifacts), manifest_path])
    validate_sha256s(sums)
    print(f"Release package built in {dist}")
    return 0


def enforce_market_ready_gate() -> None:
    enforce_publication_gate("market-ready")
    audit = REPO / "scripts" / "audit_brain.py"
    if not audit.exists():
        raise SystemExit("ERROR: market-ready release blocked: missing scripts/audit_brain.py")
    proc = subprocess.run(
        [sys.executable, str(audit), "--require", "market-ready", "--json"],
        cwd=REPO,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode:
        detail = "\n".join(part for part in [proc.stdout.strip(), proc.stderr.strip()] if part)
        raise SystemExit("ERROR: market-ready release blocked by audit:\n" + detail)


def enforce_publication_gate(label: str) -> None:
    blockers = publication_blockers()
    if blockers:
        raise SystemExit(f"ERROR: {label} release blocked: " + "; ".join(blockers))


def describe_release_type(release_type: str) -> dict[str, object]:
    market_ready = release_type == "market-ready"
    publication_ready = release_type in {"experimental", "market-ready"}
    distribution_status = {
        "scaffold": "internal-review-only",
        "demo": "internal-review-only",
        "experimental": "public-experimental-release",
        "market-ready": "public-market-ready-release",
    }[release_type]
    return {
        "publication_ready": publication_ready,
        "market_ready": market_ready,
        "distribution_status": distribution_status,
        "market_validation": {
            "buyer_demand_validated": market_ready,
            "retention_validated": market_ready,
            "equal_budget_advantage_validated": market_ready,
        },
    }


def normalize_version(value: str) -> str:
    version = value.strip().removeprefix("v")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise SystemExit("ERROR: --version must look like 0.1.0")
    return version


def should_skip(path: Path) -> bool:
    if set(path.parts) & SKIP_PARTS:
        return True
    if any(part.endswith(".egg-info") for part in path.parts):
        return True
    return path.suffix in SKIP_SUFFIXES


def reject_forbidden_entry(path: Path) -> None:
    if path.name in FORBIDDEN_ENTRY_NAMES:
        raise SystemExit(f"ERROR: forbidden release entry: {path.as_posix()}")
    if path.is_absolute() or ".." in path.parts:
        raise SystemExit(f"ERROR: unsafe release entry: {path.as_posix()}")


def is_public_excluded(path: Path) -> bool:
    return bool(set(path.parts) & PUBLIC_EXCLUDED_PARTS) or path.name in PUBLIC_EXCLUDED_NAMES or path.as_posix() in PUBLIC_EXCLUDED_PATHS


def iter_tree(root: Path, *, public: bool = False) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if should_skip(rel):
            continue
        if public and is_public_excluded(rel):
            continue
        reject_forbidden_entry(rel)
        if path.is_symlink():
            raise SystemExit(f"ERROR: symlink not allowed: {rel.as_posix()}")
        if path.is_file():
            files.append(path)
    return sorted(files)


def source_files() -> list[Path]:
    if (REPO / ".git").exists():
        reject_dirty_tracked_files()
        reject_untracked_files()
        proc = subprocess.run(["git", "ls-files", "-z", "--cached"], cwd=REPO, capture_output=True, check=False)
        if proc.returncode != 0:
            raise SystemExit(proc.stderr.decode("utf-8", "replace"))
        files = []
        for raw in proc.stdout.split(b"\0"):
            if raw:
                rel = Path(raw.decode("utf-8", "replace"))
                if should_skip(rel):
                    continue
                reject_forbidden_entry(rel)
                path = REPO / rel
                if path.is_symlink():
                    raise SystemExit(f"ERROR: symlink not allowed: {rel.as_posix()}")
                if path.is_file():
                    files.append(path)
        return sorted(files)
    return iter_tree(REPO)


def reject_dirty_tracked_files() -> None:
    dirty: set[str] = set()
    for args in (["git", "diff", "--name-only", "-z"], ["git", "diff", "--name-only", "-z", "--cached"]):
        proc = subprocess.run(args, cwd=REPO, capture_output=True, check=False)
        if proc.returncode != 0:
            raise SystemExit(proc.stderr.decode("utf-8", "replace"))
        dirty.update(raw.decode("utf-8", "replace") for raw in proc.stdout.split(b"\0") if raw)
    blocked = sorted(path for path in dirty if not should_skip(Path(path)))
    if blocked:
        raise SystemExit("ERROR: dirty tracked files would make release non-reproducible: " + ", ".join(blocked[:10]))


def reject_untracked_files() -> None:
    proc = subprocess.run(["git", "ls-files", "-z", "--others", "--exclude-standard"], cwd=REPO, capture_output=True, check=False)
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.decode("utf-8", "replace"))
    untracked = sorted(raw.decode("utf-8", "replace") for raw in proc.stdout.split(b"\0") if raw)
    allowed = [p for p in untracked if not should_skip(Path(p))]
    if allowed:
        raise SystemExit("ERROR: untracked files would make release non-reproducible: " + ", ".join(allowed[:10]))


def scan_source_tree() -> None:
    for path in source_files():
        rel = path.relative_to(REPO)
        if not should_skip(rel):
            scan_file(path, rel.as_posix())


def build_zip(out: Path, source: Path, root_name: str) -> dict[str, object]:
    entries = 0
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in iter_tree(source, public=True):
            zf.write(path, (Path(root_name) / path.relative_to(source)).as_posix())
            entries += 1
    return {"path": out, "entries": entries}


def build_source_zip(out: Path, version: str) -> dict[str, object]:
    entries = 0
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in source_files():
            rel = path.relative_to(REPO)
            if not should_skip(rel) and not is_public_excluded(rel):
                zf.write(path, (Path(f"gauntlet-loop-brain-v{version}") / rel).as_posix())
                entries += 1
    return {"path": out, "entries": entries}


def validate_zip(path: Path) -> None:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        if not names:
            raise SystemExit(f"ERROR: empty artifact: {path.name}")
        for name in names:
            rel = Path(name)
            for part in rel.parts:
                reject_forbidden_entry(Path(part))
            if should_skip(rel) or any(part in SKIP_PARTS for part in rel.parts):
                raise SystemExit(f"ERROR: forbidden zip entry in {path.name}: {name}")
            payload_rel = Path(*rel.parts[1:]) if len(rel.parts) > 1 else Path()
            if is_public_excluded(payload_rel):
                raise SystemExit(f"ERROR: public-excluded zip entry in {path.name}: {name}")
            mode = zf.getinfo(name).external_attr >> 16
            if stat.S_ISLNK(mode):
                raise SystemExit(f"ERROR: symlink entry in {path.name}: {name}")
            scan_bytes(zf.read(name), f"{path.name}:{name}", rel.suffix, public_claims=True)


def scan_file(path: Path, label: str) -> None:
    size = path.stat().st_size
    if size > MAX_SCAN_BYTES:
        raise SystemExit(f"ERROR: file too large for release scan: {label}")
    scan_bytes(path.read_bytes(), label, path.suffix)


def scan_bytes(data: bytes, label: str, suffix: str, *, public_claims: bool = False) -> None:
    if suffix and suffix not in TEXT_SUFFIXES:
        return
    for name, pattern in FORBIDDEN_TEXT_PATTERNS.items():
        if pattern.search(data):
            raise SystemExit(f"ERROR: {name} found in {label}")
    if public_claims and suffix in {".base", ".canvas", ".html", ".md", ".toml", ".yaml", ".yml"}:
        scan_public_market_claims(data, label)


def scan_public_market_claims(data: bytes, label: str) -> None:
    text = data.decode("utf-8", "replace")
    for name, pattern in PUBLIC_MARKET_CLAIM_PATTERNS.items():
        for match in pattern.finditer(text):
            paragraph_boundary = text.rfind("\n\n", 0, match.start())
            if paragraph_boundary >= 0:
                paragraph_boundary += 1
            sentence_start = max(
                text.rfind(".", 0, match.start()),
                text.rfind("!", 0, match.start()),
                text.rfind("?", 0, match.start()),
                paragraph_boundary,
            )
            qualifying_prefix = text[sentence_start + 1 : match.start()]
            if not NEGATED_MARKET_CLAIM_CONTEXT.search(qualifying_prefix):
                raise SystemExit(f"ERROR: unsupported public claim '{name}' found in {label}")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_sha256s(path: Path, artifacts: list[Path]) -> None:
    path.write_text("\n".join(f"{sha256_file(a)}  {a.name}" for a in artifacts) + "\n", encoding="utf-8")


def validate_sha256s(path: Path) -> None:
    for line in path.read_text(encoding="utf-8").splitlines():
        expected, filename = line.split("  ", 1)
        actual = sha256_file(path.parent / filename)
        if expected != actual:
            raise SystemExit(f"ERROR: checksum mismatch for {filename}")


def git_commit() -> str | None:
    if not (REPO / ".git").exists():
        return None
    proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True, check=False)
    return proc.stdout.strip() if proc.returncode == 0 else None


def publication_blockers() -> list[str]:
    blockers: list[str] = []
    license_path = REPO / "LICENSE"
    license_text = license_path.read_text(encoding="utf-8", errors="replace").lower() if license_path.exists() else ""
    if not license_text or "replace this file with the final license" in license_text:
        blockers.append("final license has not been selected by the owner")
    if git_commit() is None:
        blockers.append("release provenance is not bound to a Git commit")
    origin = git_remote_origin()
    if origin is None:
        blockers.append("public repository target is not configured as Git remote origin")
    configured = configured_security_url()
    if configured is None:
        blockers.append("exact private vulnerability-reporting URL is not configured in SECURITY.md")
    elif origin is not None:
        expected = expected_github_security_url(origin)
        if expected is None:
            blockers.append("private vulnerability-reporting URL cannot be verified against Git remote origin")
        elif configured != expected:
            blockers.append("private vulnerability-reporting URL does not match Git remote origin")
    return blockers


def git_remote_origin() -> str | None:
    if not (REPO / ".git").exists():
        return None
    proc = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    value = proc.stdout.strip()
    return value if proc.returncode == 0 and value else None


def expected_github_security_url(origin: str) -> str | None:
    patterns = [
        re.compile(r"^https://github\.com/([^/]+)/([^/]+?)(?:\.git)?$"),
        re.compile(r"^git@github\.com:([^/]+)/([^/]+?)(?:\.git)?$"),
        re.compile(r"^ssh://git@github\.com/([^/]+)/([^/]+?)(?:\.git)?$"),
    ]
    for pattern in patterns:
        match = pattern.fullmatch(origin.strip().rstrip("/"))
        if match:
            owner, repository = match.groups()
            return f"https://github.com/{owner}/{repository}/security/advisories/new"
    return None


def configured_security_url() -> str | None:
    path = REPO / "SECURITY.md"
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith(SECURITY_URL_PREFIX):
            continue
        value = line.removeprefix(SECURITY_URL_PREFIX).strip()
        parsed = urlparse(value)
        if parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment:
            return None
        if any(marker in value.lower() for marker in ["owner_must", "example.com", "tbd", "replace"]):
            return None
        return value
    return None


if __name__ == "__main__":
    raise SystemExit(main())
