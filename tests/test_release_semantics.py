from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import package_release


class ExperimentalReleaseGateTests(unittest.TestCase):
    def run_experimental(self, repo: Path) -> str:
        with patch.object(package_release, "REPO", repo):
            with self.assertRaises(SystemExit) as raised:
                package_release.main(
                    ["--version", "0.1.0", "--release-type", "experimental"]
                )
        return str(raised.exception)

    def test_experimental_release_cannot_pass_without_owner_license(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gauntlet-license-gate-") as tmp:
            repo = Path(tmp)
            (repo / "LICENSE").write_text(
                "Replace this file with the final license before distribution.\n",
                encoding="utf-8",
            )
            expected_url = "https://github.com/owner/repository/security/advisories/new"
            with (
                patch.object(package_release, "git_commit", return_value="a" * 40),
                patch.object(
                    package_release,
                    "git_remote_origin",
                    return_value="https://github.com/owner/repository.git",
                ),
                patch.object(
                    package_release,
                    "configured_security_url",
                    return_value=expected_url,
                ),
            ):
                error = self.run_experimental(repo)
            self.assertIn("experimental public release blocked", error)
            self.assertIn("final license has not been selected by the owner", error)
            self.assertNotIn("release provenance is not bound to a Git commit", error)

    def test_experimental_release_is_publication_ready_but_not_market_ready(self) -> None:
        semantics = package_release.describe_release_type("experimental")
        self.assertIs(semantics["publication_ready"], True)
        self.assertIs(semantics["market_ready"], False)
        self.assertEqual(
            semantics["market_validation"],
            {
                "buyer_demand_validated": False,
                "equal_budget_advantage_validated": False,
                "retention_validated": False,
            },
        )

    def test_default_scaffold_is_always_internal(self) -> None:
        semantics = package_release.describe_release_type("scaffold")
        self.assertIs(semantics["publication_ready"], False)
        self.assertEqual(semantics["distribution_status"], "internal-review-only")

    def test_experimental_release_cannot_pass_without_git_commit(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gauntlet-git-gate-") as tmp:
            repo = Path(tmp)
            (repo / "LICENSE").write_text(
                "Owner-selected test license text.\n",
                encoding="utf-8",
            )
            expected_url = "https://github.com/owner/repository/security/advisories/new"
            with (
                patch.object(package_release, "git_commit", return_value=None),
                patch.object(
                    package_release,
                    "git_remote_origin",
                    return_value="https://github.com/owner/repository.git",
                ),
                patch.object(
                    package_release,
                    "configured_security_url",
                    return_value=expected_url,
                ),
            ):
                error = self.run_experimental(repo)
            self.assertIn("experimental public release blocked", error)
            self.assertIn("release provenance is not bound to a Git commit", error)
            self.assertNotIn("final license has not been selected by the owner", error)

    def test_positive_market_claim_is_rejected(self) -> None:
        with self.assertRaisesRegex(SystemExit, "validated buyer demand"):
            package_release.scan_public_market_claims(
                b"Buyer demand is validated.", "public.md"
            )

    def test_explicitly_unvalidated_market_claim_is_allowed(self) -> None:
        package_release.scan_public_market_claims(
            b"Buyer demand is not validated.", "public.md"
        )

    def test_unrelated_negative_claim_does_not_launder_positive_claim(self) -> None:
        with self.assertRaisesRegex(SystemExit, "validated buyer demand"):
            package_release.scan_public_market_claims(
                b"Buyer demand is validated, but retention is not validated.",
                "public.md",
            )

    def test_security_url_must_match_github_origin(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gauntlet-security-gate-") as tmp:
            repo = Path(tmp)
            (repo / "LICENSE").write_text(
                "Owner-selected test license text.\n",
                encoding="utf-8",
            )
            (repo / "SECURITY.md").write_text(
                "Private vulnerability reporting URL: "
                "https://github.com/other/repository/security/advisories/new\n",
                encoding="utf-8",
            )
            with (
                patch.object(package_release, "REPO", repo),
                patch.object(package_release, "git_commit", return_value="a" * 40),
                patch.object(
                    package_release,
                    "git_remote_origin",
                    return_value="https://github.com/owner/repository.git",
                ),
            ):
                blockers = package_release.publication_blockers()
            self.assertIn(
                "private vulnerability-reporting URL does not match Git remote origin",
                blockers,
            )


if __name__ == "__main__":
    unittest.main()
