from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = {
    "schema",
    "goal",
    "reference",
    "authority",
    "budget",
    "gates",
    "stop_policy",
}
GATE_KINDS = {"deterministic", "evidence", "judge", "human"}
GATE_AUTHORITIES = {"blocking", "advisory"}
REGRESSION_POLICIES = {"revert", "escalate", "revert_or_escalate"}


def load_job(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("job contract must be a JSON object")
    return data


def validate_job(data: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    missing = sorted(REQUIRED_TOP_LEVEL - data.keys())
    errors.extend(f"missing required field: {name}" for name in missing)
    if missing:
        return errors, warnings

    if data.get("schema") != "gauntlet.job.v1":
        errors.append("schema must equal gauntlet.job.v1")
    if not _nonempty_string(data.get("goal")):
        errors.append("goal must be a non-empty string")

    reference = data.get("reference")
    if not isinstance(reference, dict):
        errors.append("reference must be an object")
    else:
        for name in ["name", "location", "rationale"]:
            if not _nonempty_string(reference.get(name)):
                errors.append(f"reference.{name} must be a non-empty string")
        dimensions = reference.get("observable_dimensions")
        if not _nonempty_string_list(dimensions):
            errors.append("reference.observable_dimensions must contain at least one dimension")

    authority = data.get("authority")
    if not isinstance(authority, dict):
        errors.append("authority must be an object")
    else:
        for name in ["allowed_actions", "disallowed_actions"]:
            if not isinstance(authority.get(name), list):
                errors.append(f"authority.{name} must be a list")
        if not authority.get("disallowed_actions"):
            warnings.append("authority.disallowed_actions is empty; verify the blast radius")

    budget = data.get("budget")
    if not isinstance(budget, dict):
        errors.append("budget must be an object")
    else:
        _positive_int(budget, "max_iterations", errors)
        _positive_int(budget, "max_parallel_agents", errors)
        _positive_int(budget, "max_minutes", errors)
        _positive_int(budget, "max_tokens", errors)
        value = budget.get("max_cost_usd")
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
            errors.append("max_cost_usd must be zero or greater")
        retries = budget.get("max_retries")
        if not isinstance(retries, int) or isinstance(retries, bool) or retries < 0:
            errors.append("max_retries must be an integer zero or greater")

    gates = data.get("gates")
    if not isinstance(gates, list) or not gates:
        errors.append("gates must contain at least one gate")
    else:
        seen: set[str] = set()
        for index, gate in enumerate(gates, start=1):
            prefix = f"gates[{index}]"
            if not isinstance(gate, dict):
                errors.append(f"{prefix} must be an object")
                continue
            gate_id = gate.get("id")
            if not _nonempty_string(gate_id):
                errors.append(f"{prefix}.id must be a non-empty string")
            elif gate_id in seen:
                errors.append(f"duplicate gate id: {gate_id}")
            else:
                seen.add(gate_id)
            if gate.get("kind") not in GATE_KINDS:
                errors.append(f"{prefix}.kind must be one of {sorted(GATE_KINDS)}")
            if gate.get("authority") not in GATE_AUTHORITIES:
                errors.append(f"{prefix}.authority must be blocking or advisory")
            if not _nonempty_string(gate.get("criterion")):
                errors.append(f"{prefix}.criterion must be a non-empty string")
            if gate.get("protected") is not True:
                errors.append(f"{prefix}.protected must be true")
        if not any(isinstance(gate, dict) and gate.get("authority") == "blocking" for gate in gates):
            errors.append("at least one gate must be blocking")
        if all(isinstance(gate, dict) and gate.get("kind") == "judge" for gate in gates):
            warnings.append("all gates are model judges; add deterministic, evidence, or human verification")

    stop = data.get("stop_policy")
    if not isinstance(stop, dict):
        errors.append("stop_policy must be an object")
    else:
        _positive_int(stop, "plateau_window", errors)
        delta = stop.get("minimum_improvement_delta")
        if not isinstance(delta, (int, float)) or isinstance(delta, bool) or delta < 0:
            errors.append("stop_policy.minimum_improvement_delta must be zero or greater")
        if stop.get("regression_policy") not in REGRESSION_POLICIES:
            errors.append("stop_policy.regression_policy is invalid")
        if stop.get("human_can_stop") is not True:
            errors.append("stop_policy.human_can_stop must be true")

    return errors, warnings


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _nonempty_string_list(value: object) -> bool:
    return isinstance(value, list) and bool(value) and all(_nonempty_string(item) for item in value)


def _positive_int(container: dict[str, Any], name: str, errors: list[str]) -> None:
    value = container.get(name)
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        errors.append(f"{name} must be an integer greater than zero")
