# Release Checklist

## Product

- [ ] README states buyer, promise, outputs, boundaries, and quick start.
- [ ] `SKILL.md` maps commands accurately.
- [ ] License and distribution stance is explicit.
- [ ] Third-party notices are current.
- [ ] README and support surfaces link to the verified Free and Pro AI Marketing Hub pages.
- [ ] Release notes match the exact version and commit being tagged.

## Research

- [ ] Maturity is documented and not overstated.
- [ ] `references/current-requirements.md` has dated official/primary sources.
- [ ] `references/source-ledger.json` lists dated official/primary sources,
      refresh dates, source types, and supported claims.
- [ ] `references/source-map.md` explains import strategy and source schemas.
- [ ] `references/safety-gates.md` lists refusal rules and failure paths.
- [ ] Stale source claims were browsed and refreshed before release.
- [ ] Market claims follow `docs/MARKET_VALIDATION_PROTOCOL.md`; unrun study
      templates are never described as validation evidence.

## Vault

- [ ] Template vault opens in Obsidian.
- [ ] Hot/Index/Wiki notes and hubs are connected.
- [ ] Raw sources stay immutable under `.raw/`.
- [ ] Deliverables cite source notes or raw-file hashes.
- [ ] `PUBLISHING_NOTICE.md` has been reviewed before public publish or ZIP release.

## Verification

- [ ] `python -m compileall scripts gauntlet_loop_brain tests`
- [ ] `python tests/test_pipeline.py`
- [ ] `python scripts/build_demo_vault.py`
- [ ] `python scripts/hash_sample_vault.py --check`
- [ ] `python scripts/package_release.py --version 0.1.0`
- [ ] The default scaffold manifest says `publication_ready: false` and
      `distribution_status: internal-review-only`.
- [ ] For a public research release, run
      `python scripts/package_release.py --version 0.1.0 --release-type experimental`.
- [ ] The experimental manifest says `publication_ready: true`,
      `market_ready: false`, and all three market-validation fields are false.
- [ ] The final owner-selected license is present, the worktree is clean, and
      the manifest records the exact Git commit.
- [ ] The reviewed tag uses `vMAJOR.MINOR.PATCH` or
      `vMAJOR.MINOR.PATCH-rc.N` and points to that exact commit.
- [ ] The configured Git remote identifies the public repository target and the
      private vulnerability-reporting URL in `SECURITY.md` exactly matches it.
- [ ] `references/publication-readiness.json` records a current verified GitHub
      governance state and private vulnerability reporting is enabled.
- [ ] No secrets, private client data, or local absolute paths in artifacts.
- [ ] Market-ready release is blocked unless audit score is at least 90 with no critical failures.
- [ ] No public surface claims validated buyer demand, validated retention, or
      validated equal-budget advantage while those studies remain pending.
- [ ] `references/adapter-manifest.json` names real schemas, importer paths,
      synthesis modules, report renderers, fixtures, and tests before
      domain-adapted or market-ready release.
