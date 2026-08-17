#!/usr/bin/env python3
"""Safely install or remove the Gauntlet block in Gemini's loader."""

from __future__ import annotations

import argparse
import os
import re
import stat
import tempfile
from pathlib import Path
from typing import Callable


START = "<!-- gauntlet-loop-brain-install:start -->"
END = "<!-- gauntlet-loop-brain-install:end -->"
DEFAULT_IMPORT = "@./gauntlet-loop-brain/GEMINI.md"

BeforeMutation = Callable[[Path], None]


def _read_regular(path: Path, *, missing_ok: bool) -> tuple[str, int] | None:
    try:
        source_fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    except FileNotFoundError:
        if missing_ok:
            return None
        raise
    except OSError as exc:
        raise RuntimeError(f"refusing unsafe Gemini loader {path}: {exc}") from exc

    with os.fdopen(source_fd, "r", encoding="utf-8") as handle:
        source_stat = os.fstat(handle.fileno())
        if not stat.S_ISREG(source_stat.st_mode):
            raise RuntimeError(f"refusing non-regular Gemini loader: {path}")
        return handle.read(), source_stat.st_mode & 0o777


def _atomic_write(
    path: Path,
    text: str,
    mode: int,
    *,
    _before_replace: BeforeMutation | None = None,
) -> None:
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temp_name, mode)
        if _before_replace is not None:
            _before_replace(path)
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def install_block(
    path: Path,
    import_line: str = DEFAULT_IMPORT,
    *,
    _before_replace: BeforeMutation | None = None,
) -> None:
    current = _read_regular(path, missing_ok=True)
    if current is None:
        text = ""
        mode = 0o600
    else:
        text, mode = current

    block = f"{START}\n{import_line}\n{END}"
    pattern = f"{re.escape(START)}.*?{re.escape(END)}"
    if re.search(pattern, text, flags=re.S):
        new_text = re.sub(pattern, block, text, flags=re.S)
    else:
        new_text = (text.rstrip() + "\n\n" + block + "\n").lstrip()
    _atomic_write(path, new_text, mode, _before_replace=_before_replace)


def remove_block(
    path: Path,
    *,
    _before_replace: BeforeMutation | None = None,
) -> bool:
    current = _read_regular(path, missing_ok=True)
    if current is None:
        return False
    text, mode = current
    pattern = f"\n*{re.escape(START)}.*?{re.escape(END)}\n*"
    new_text = re.sub(pattern, "\n", text, flags=re.S).strip()
    if new_text:
        _atomic_write(
            path,
            new_text + "\n",
            mode,
            _before_replace=_before_replace,
        )
    else:
        if _before_replace is not None:
            _before_replace(path)
        os.unlink(path)
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    install = subparsers.add_parser("install")
    install.add_argument("loader", type=Path)
    install.add_argument("--import-line", default=DEFAULT_IMPORT)
    remove = subparsers.add_parser("remove")
    remove.add_argument("loader", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "install":
            install_block(args.loader, args.import_line)
        else:
            remove_block(args.loader)
    except (OSError, RuntimeError) as exc:
        raise SystemExit(f"ERROR: {exc}") from exc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
