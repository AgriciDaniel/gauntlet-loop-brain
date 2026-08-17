from __future__ import annotations

import hashlib
import json
from pathlib import Path


DEFAULT_HASH_SKIP = (
    ".git",
    "__pycache__",
    "dist",
    "node_modules",
    "site/public",
    ".obsidian/workspace.json",
    ".obsidian/workspace-mobile.json",
    ".DS_Store",
)


def hash_tree(root: Path, *, skip: tuple[str, ...] = DEFAULT_HASH_SKIP) -> str:
    root = root.expanduser().resolve()
    if not root.exists():
        raise FileNotFoundError(root)
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            rel = path.relative_to(root).as_posix()
            if should_skip_hash_path(rel, skip):
                continue
            digest.update(rel.encode("utf-8"))
            digest.update(b"\x00SYMLINK\x00")
            digest.update(path.readlink().as_posix().encode("utf-8"))
            digest.update(b"\x00")
            continue
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if should_skip_hash_path(rel, skip):
            continue
        digest.update(rel.encode("utf-8"))
        digest.update(b"\x00")
        digest.update(normalize_file_bytes(path))
        digest.update(b"\x00")
    return digest.hexdigest()


def should_skip_hash_path(rel: str, skip: tuple[str, ...]) -> bool:
    if rel.endswith(".pyc"):
        return True
    parts = rel.split("/")
    for item in skip:
        item_parts = item.strip("/").split("/")
        if len(item_parts) == 1:
            if item_parts[0] in parts:
                return True
            continue
        if any(parts[index : index + len(item_parts)] == item_parts for index in range(len(parts) - len(item_parts) + 1)):
            return True
    return False


def normalize_file_bytes(path: Path) -> bytes:
    raw = path.read_bytes()
    if path.suffix.lower() == ".json":
        try:
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            return raw
        return (json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
    if b"\x00" in raw[:8192]:
        return raw
    text = raw.decode("utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
    if text and not text.endswith("\n"):
        text += "\n"
    return text.encode("utf-8")
