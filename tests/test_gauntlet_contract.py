from __future__ import annotations

import json
import unittest
from pathlib import Path

from gauntlet_loop_brain.contract import load_job, validate_job


REPO = Path(__file__).resolve().parent.parent


class GauntletContractTests(unittest.TestCase):
    def test_example_contract_is_valid(self) -> None:
        job = load_job(REPO / "tests" / "fixtures" / "gauntlet-job.json")
        errors, warnings = validate_job(job)
        self.assertEqual([], errors)
        self.assertEqual([], warnings)

    def test_unbounded_all_judge_contract_is_rejected_or_warned(self) -> None:
        job = json.loads((REPO / "tests" / "fixtures" / "gauntlet-job.json").read_text(encoding="utf-8"))
        del job["budget"]["max_iterations"]
        job["gates"] = [
            {
                "id": "taste",
                "kind": "judge",
                "authority": "blocking",
                "criterion": "Looks good",
            }
        ]
        errors, warnings = validate_job(job)
        self.assertTrue(any("max_iterations" in error for error in errors))
        self.assertTrue(any("all gates are model judges" in warning for warning in warnings))

    def test_human_stop_is_required(self) -> None:
        job = load_job(REPO / "tests" / "fixtures" / "gauntlet-job.json")
        job["stop_policy"]["human_can_stop"] = False
        errors, _ = validate_job(job)
        self.assertIn("stop_policy.human_can_stop must be true", errors)

    def test_every_resource_ceiling_is_required(self) -> None:
        for name in ["max_minutes", "max_tokens", "max_cost_usd", "max_retries"]:
            with self.subTest(name=name):
                job = load_job(REPO / "tests" / "fixtures" / "gauntlet-job.json")
                job["budget"].pop(name)
                errors, _ = validate_job(job)
                self.assertTrue(any(name in error for error in errors), errors)

    def test_zero_cost_and_zero_retries_are_valid_explicit_ceilings(self) -> None:
        job = load_job(REPO / "tests" / "fixtures" / "gauntlet-job.json")
        job["budget"]["max_cost_usd"] = 0
        job["budget"]["max_retries"] = 0
        errors, _ = validate_job(job)
        self.assertEqual([], errors)

    def test_schema_requires_each_resource_ceiling(self) -> None:
        schema = json.loads((REPO / "schemas" / "gauntlet-job.v1.schema.json").read_text(encoding="utf-8"))
        required = set(schema["properties"]["budget"]["required"])
        self.assertTrue({"max_iterations", "max_parallel_agents", "max_minutes", "max_tokens", "max_cost_usd", "max_retries"}.issubset(required))

    def test_every_gate_is_protected(self) -> None:
        job = load_job(REPO / "tests" / "fixtures" / "gauntlet-job.json")
        job["gates"][0]["protected"] = False
        errors, _ = validate_job(job)
        self.assertIn("gates[1].protected must be true", errors)


if __name__ == "__main__":
    unittest.main()
