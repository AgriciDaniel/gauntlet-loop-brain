#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from gauntlet_loop_brain.integrity import hash_tree


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Hash the deterministic sample vault.")
    parser.add_argument("--vault", default="examples/sample-vault")
    parser.add_argument("--fixture", default="tests/fixtures/sample-vault.sha256")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    vault = (REPO / args.vault).resolve()
    fixture = (REPO / args.fixture).resolve()
    digest = hash_tree(vault)
    if not args.check:
        print(digest)
        return 0
    if not fixture.is_file():
        print(f"ERROR: sample-vault hash fixture missing: {fixture}", file=sys.stderr)
        return 1
    fields = fixture.read_text(encoding="utf-8").strip().split()
    expected = fields[0] if fields else ""
    if not re.fullmatch(r"[0-9a-f]{64}", expected):
        print(f"ERROR: invalid sample-vault hash fixture: {fixture}", file=sys.stderr)
        return 1
    if digest != expected:
        print("ERROR: sample-vault tree hash drift", file=sys.stderr)
        print(f"expected: {expected}", file=sys.stderr)
        print(f"actual:   {digest}", file=sys.stderr)
        return 1
    print(f"Sample-vault tree hash passed: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
