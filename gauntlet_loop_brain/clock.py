from __future__ import annotations

import os
from datetime import date


DATE_OVERRIDE_ENV = "GAUNTLET_LOOP_BRAIN_DATE_OVERRIDE"


def reference_date() -> str:
    value = os.environ.get(DATE_OVERRIDE_ENV, "").strip()
    if not value:
        return date.today().isoformat()
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"ERROR: {DATE_OVERRIDE_ENV} must be an ISO date: {value}") from exc
    if parsed.isoformat() != value:
        raise SystemExit(f"ERROR: {DATE_OVERRIDE_ENV} must use YYYY-MM-DD: {value}")
    return value
