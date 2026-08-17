# Release Notes

## v0.1.0, Public Experimental Preview (planned)

**Status:** public source repository, not tagged and without a GitHub release.

Gauntlet Loop Brain is a demo-verified research prototype. This candidate
focuses on understandable documentation, reproducible vault behavior, and
honest release boundaries.

### Highlights

- A new gauntlet, brain, and infinity-circuit identity across the README and
  generated vault maps.
- Two plain-language Mermaid diagrams explain the controlled loop and its
  evidence-linked memory.
- A source-cited Obsidian template, sample vault, agent skill, job contract,
  release packager, and installation safeguards.
- A pinned deterministic sample-vault tree hash with a mutation-sensitive
  negative test.
- Expanded secret and sensitive-data scanning for source files and packaged
  artifacts.
- CI with read-only permissions, immutable action pins, and protected `main`.
- Simple Free and Pro AI Marketing Hub community links.

### Honest Limits

- This is an experimental research tool, not a market-ready product.
- Buyer demand, retention, and equal-budget advantage over simpler workflows
  remain unvalidated.
- The owner selected the Apache License 2.0 for source distribution.
- Private vulnerability reporting, secret scanning, push protection, Dependabot,
  and CodeQL default setup are enabled.

### Tag Policy

- Stable releases: `vMAJOR.MINOR.PATCH`, beginning with `v0.1.0`.
- Prereleases: `vMAJOR.MINOR.PATCH-rc.N`, beginning with `v0.1.0-rc.1`.
- A tag identifies one reviewed clean commit and its matching release artifacts.
- An experimental tag never implies market readiness.
- No tag or GitHub release exists yet.

### Verification Contract

```bash
python -m compileall scripts gauntlet_loop_brain tests
python tests/test_pipeline.py
python scripts/build_demo_vault.py
python scripts/hash_sample_vault.py --check
python scripts/audit_brain.py --json
python scripts/package_release.py --version 0.1.0
```

The experimental public artifact must additionally pass:

```bash
python scripts/package_release.py --version 0.1.0 --release-type experimental
```
