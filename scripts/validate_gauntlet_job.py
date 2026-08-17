#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from gauntlet_loop_brain.contract import load_job, validate_job


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Gauntlet Loop job contract.")
    parser.add_argument("job", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        data = load_job(args.job)
        errors, warnings = validate_job(data)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors, warnings = [str(exc)], []

    result = {"ok": not errors, "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("PASS" if result["ok"] else "FAIL")
        for message in errors:
            print(f"ERROR: {message}")
        for message in warnings:
            print(f"WARNING: {message}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
