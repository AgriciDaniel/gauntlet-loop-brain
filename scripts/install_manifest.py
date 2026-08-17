#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import sys
from pathlib import Path


MANIFEST_NAME = ".gauntlet-loop-brain-manifest.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(root: Path) -> dict[str, object]:
    files: dict[str, str] = {}
    directories: list[str] = []
    for current, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        for name in sorted(dirnames):
            path = current_path / name
            rel = path.relative_to(root).as_posix()
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                raise ValueError(f"symlink is not allowed in an installation: {rel}")
            if not stat.S_ISDIR(mode):
                raise ValueError(f"non-directory entry found where a directory was expected: {rel}")
            directories.append(rel)
        for name in sorted(filenames):
            path = current_path / name
            rel = path.relative_to(root).as_posix()
            if rel == MANIFEST_NAME:
                continue
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                raise ValueError(f"symlink is not allowed in an installation: {rel}")
            if not stat.S_ISREG(mode):
                raise ValueError(f"non-regular file is not allowed in an installation: {rel}")
            files[rel] = sha256_file(path)
    return {
        "version": 1,
        "directories": sorted(directories),
        "files": dict(sorted(files.items())),
    }


def create(root: Path) -> None:
    root = root.resolve(strict=True)
    manifest = root / MANIFEST_NAME
    data = inventory(root)
    manifest.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest.chmod(0o600)


def verify(root: Path) -> None:
    if root.is_symlink() or not root.is_dir():
        raise ValueError(f"installation root must be a real directory: {root}")
    manifest = root / MANIFEST_NAME
    if manifest.is_symlink() or not manifest.is_file():
        raise ValueError(f"missing regular ownership manifest: {manifest}")
    try:
        expected = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError(f"invalid ownership manifest: {exc}") from exc
    actual = inventory(root)
    if expected != actual:
        expected_files = set(expected.get("files", {})) if isinstance(expected, dict) else set()
        actual_files = set(actual["files"])
        added = sorted(actual_files - expected_files)
        removed = sorted(expected_files - actual_files)
        changed = sorted(
            path
            for path in expected_files & actual_files
            if expected["files"].get(path) != actual["files"].get(path)
        )
        expected_dirs = set(expected.get("directories", [])) if isinstance(expected, dict) else set()
        actual_dirs = set(actual["directories"])
        detail = []
        if added:
            detail.append("added files: " + ", ".join(added[:5]))
        if removed:
            detail.append("missing files: " + ", ".join(removed[:5]))
        if changed:
            detail.append("changed files: " + ", ".join(changed[:5]))
        if actual_dirs - expected_dirs:
            detail.append("added directories: " + ", ".join(sorted(actual_dirs - expected_dirs)[:5]))
        if expected_dirs - actual_dirs:
            detail.append("missing directories: " + ", ".join(sorted(expected_dirs - actual_dirs)[:5]))
        raise ValueError("installation differs from its ownership manifest" + (": " + "; ".join(detail) if detail else ""))


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or verify an exact Gauntlet installation inventory.")
    parser.add_argument("command", choices=["create", "verify"])
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "create":
            create(args.root)
        else:
            verify(args.root)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
