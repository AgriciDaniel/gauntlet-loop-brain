# Publishing Notice

Gauntlet Loop Brain is operator-owned research infrastructure. Publication
readiness and market readiness are separate verdicts. A public experimental
release may be safe to publish while buyer demand, retention, and equal-budget
advantage remain unvalidated. It must not imply that those studies passed.

## Release Types

- `scaffold` and `demo` are internal-only and can never set
  `publication_ready: true`.
- `experimental` is the only public path before market validation. It requires
  the Apache License 2.0, a clean Git commit, a configured repository
  target, the exact matching private-reporting URL, and all archive safety gates.
- `market-ready` requires the same publication gates plus the unchanged
  market-ready audit. Experimental publication does not weaken that gate.

## Rights Boundary

Public availability of a source does not automatically create permission to redistribute it. Treat copied source excerpts, screenshots, account exports, prompt text, private notes, and third-party documentation as restricted evidence unless a clear license permits reuse.

Public content policy: publish only source-linked synthesis, compliant short quotes, templates, and synthetic examples; exclude private run evidence and third-party artifacts.

## What Can Be Public

- Original summaries.
- Operating doctrine.
- Links to official public sources.
- Short compliant quotations within the quote policy.
- Sanitized visuals and reports that do not expose raw captures or private data.

## What Must Stay Private

- Real `.raw/` source captures and client manifests.
- Credentials, tokens, cookies, OAuth material, private user data, and local paths.
- Full third-party documents or large source excerpts.
- Internal ledgers excluded by public policy.
- Unreviewed generated archives in `dist/`.

The source repository contains only an empty template manifest and a synthetic
sample fixture under `.raw/`. Those exact paths are allowlisted and scanned.
Any additional tracked `.raw/` path blocks release packaging. Public website
and ZIP outputs still exclude every `.raw/` path.

## Website and ZIP Exclusions

- `.raw`
- `.obsidian`
- `hot.md`
- `log.md`
- `references/source-ledger.json`
- `references/claim-ledger.md`
- `runs`
- `private`

## Review Checklist

1. Run `python scripts/lint_vault.py --vault examples/sample-vault`.
2. Run `python scripts/audit_brain.py --json`.
3. Run a secret scan across tracked and untracked files.
4. Confirm `.raw/` is absent from public artifacts.
5. Run `node site/scripts/sanitize-public.mjs` after a Quartz build.
6. Confirm repository visibility and Pages visibility separately.
7. Enable private vulnerability reporting and record the exact advisory URL in `SECURITY.md`.
8. Confirm `dist/RELEASE_MANIFEST.json` says `publication_ready: true`, names a
   Git commit, and records the configured private-reporting URL.
9. For an experimental release, confirm the manifest says `market_ready: false`
   and records buyer demand, retention, and equal-budget advantage as false.
10. Confirm no release prose claims validated demand, retention, or equal-budget
    advantage unless the market-ready evidence gate has actually passed.
