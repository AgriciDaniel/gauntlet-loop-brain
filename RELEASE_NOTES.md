# Release Notes

## 0.1.0 Public Review Candidate, 2026-08-17

Gauntlet Loop Brain is ready for private review as a demo-verified research
prototype. This candidate focuses on understandable documentation, reproducible
vault behavior, and honest release boundaries.

### Highlights

- A new gauntlet, brain, and infinity-circuit identity across the README and
  generated vault maps.
- Two plain-language Mermaid diagrams explain the controlled loop and its
  evidence-linked memory.
- A source-cited Obsidian template, sample vault, agent skill, job contract,
  release packager, and installation safeguards.
- Expanded secret and sensitive-data scanning for source files and packaged
  artifacts.
- CI with read-only permissions, immutable action pins, branch protection, and
  required review before `main` changes.

### Honest Limits

- This is an experimental research tool, not a market-ready product.
- Buyer demand, retention, and equal-budget advantage over simpler workflows
  remain unvalidated.
- The current repository remains private while the owner reviews the candidate.
- Public release still requires the owner-selected final license and enabled
  private vulnerability reporting.

### Verification Contract

```bash
python -m compileall scripts gauntlet_loop_brain tests
python tests/test_pipeline.py
python scripts/audit_brain.py --json
python scripts/package_release.py --version 0.1.0
```

The experimental public artifact must additionally pass:

```bash
python scripts/package_release.py --version 0.1.0 --release-type experimental
```
