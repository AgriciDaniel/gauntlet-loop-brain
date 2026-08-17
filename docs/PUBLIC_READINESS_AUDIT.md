# Public-Readiness Audit

**Audit date:** 2026-08-17

**Scope:** current working candidate, all reachable Git blobs and commits,
ignored release archives, project metadata, dependencies, and GitHub governance.

## Verdict

No API keys, access tokens, private keys, personal email addresses, client data,
local home paths, requested credit-system markers, sensitive filenames, unsafe
ZIP paths, or symlinks were found in the tracked repository, reachable history,
or release archives.

The repository uses the Apache License 2.0. It is not yet approved for public
visibility because private vulnerability reporting is unavailable while the
repository remains private. A public tag must also be bound to one exact clean
commit and its matching release artifacts.

Market readiness is a separate, stronger gate. Buyer demand, retention, and
equal-budget advantage remain unvalidated.

## Evidence

- Scanned 324 reachable Git blobs across six commits with credential, email,
  private-key, token, and local-path patterns. No findings.
- Reviewed Git author and committer metadata. It contains GitHub noreply or
  known GitHub service addresses, not personal email addresses.
- Scanned the complete working tree. Ignored Python bytecode caches were the
  only files containing local build paths, and those generated caches were
  removed.
- Scanned three ignored release ZIP archives. No credentials, personal paths,
  symlinks, traversal paths, or sensitive entry names were found.
- Reviewed six `detect-secrets` findings. Five are SHA-256 or commit hashes and
  one is the word `secretary` in a role name. None is a credential.
- Verified all current release checksums.
- Found no sensitive filenames, `.env` files, key files, deploy keys,
  repository Actions secrets, Actions variables, or GitHub environments.
- `pip-audit` found no known Python dependency vulnerabilities. The static site
  declares no npm dependencies.
- The hero PNG contains no text or EXIF metadata. Repository SVGs contain no
  script or external-resource references.

## Repository Governance Review

- Repository visibility: private.
- Default branch: `main`.
- Required status check: `test`, strict mode.
- Admin enforcement, linear history, resolved conversations, force-push
  blocking, and deletion blocking are enabled.
- Current workflow token default is read-only, and the checked-in workflow pins
  third-party actions to immutable commit SHAs.
- The repository-wide Actions policy now allows only GitHub-owned actions. The
  current workflow uses only SHA-pinned GitHub-owned actions.
- Dependabot vulnerability alerts and automated security fixes are enabled.
- Required approvals are currently zero, and code-owner review is not required.
- Private vulnerability reporting is not currently available.
- Secret scanning and code scanning are not currently available while the
  repository is private.

## Required Before Public Visibility

1. Enable and verify private vulnerability reporting.
2. Review and commit this exact candidate, then rerun the full pipeline on the
   clean commit.
3. Produce an `experimental` release manifest with matching checksums.
4. Enable secret scanning and code scanning when the repository plan and
   visibility allow them.

Required approvals remain zero because the owner is currently the only
collaborator. Requiring another approval would deadlock every pull request.
Require an approving review and code-owner review after a second trusted
collaborator is available.

## Release Tag Contract

- Prerelease: `vMAJOR.MINOR.PATCH-rc.N`
- Stable: `vMAJOR.MINOR.PATCH`
- First planned prerelease: `v0.1.0-rc.1`
- First planned stable release: `v0.1.0`

No tag or GitHub release has been created. A tag must point to the exact clean
commit represented by its release manifest, checksums, notes, and license.

## Verification Commands

```bash
python -m compileall scripts gauntlet_loop_brain tests
python tests/test_pipeline.py
python scripts/build_demo_vault.py
python scripts/hash_sample_vault.py --check
python scripts/audit_brain.py --json
brainstein audit-brain . --json
pip-audit .
detect-secrets scan --all-files --no-verify .
```

The release pipeline was also rehearsed successfully in an isolated clean Git
copy so packaging provenance and dirty-worktree checks remained active.

The dated state in `references/publication-readiness.json` keeps public
packaging fail-closed until private vulnerability reporting is verified enabled.
