# Product Boundaries

Gauntlet Loop Brain is an advisory-by-default Obsidian brain for designing,
running, evaluating, and governing one-prompt multi-agent improvement loops.

## It Does

- Preserve raw sources under `.raw/`.
- Synthesize source-cited notes and deliverables.
- Maintain action queues, reports, and next actions.
- Keep decisions auditable through source links and rollback notes.
- Gate maturity through `references/source-ledger.json`,
  `references/adapter-manifest.json`, and `scripts/audit_brain.py`.
- Validate a frozen `gauntlet.job.v1` contract before execution.
- Permit ordinary reversible workspace edits only when the user's task requests
  building or fixing.

## It Does Not

- No claim that an artifact beats its reference without preserved blind comparison evidence
- No builder self-sign-off and no critic verdict based only on the builder's summary
- No blanket parallel fan-out when work is coupled or shares mutable state
- No endless loop without hard token, cost, wall-clock, retry, and human stop controls
- No weakening, rewriting, or exposing protected graders, tests, baselines, or acceptance criteria to manufacture a pass
- No high-risk, irreversible, external, account, publishing, deployment, or production action without exact human approval
- No credentials, tokens, cookies, private client data, or raw secrets in brain or run artifacts
- No presentation of practitioner reports, promotional claims, or a single author's reproductions as independent proof

## Safety Risks

- The critic optimizes visible polish while missing correctness, security, accessibility, maintainability, or user value
- A reference is irrelevant, inaccessible, legally unsuitable, or not actually better for the intended audience
- Same-model builders and critics share correlated blind spots or self-preference
- Position, verbosity, style, and familiarity biases distort pairwise judging
- Parallel workers overwrite each other or break assumptions in coupled systems
- Repeated local improvements regress the integrated artifact
- The loop games the rubric, held-out tests, or proxy metric without achieving the intended outcome
- Context growth, lossy handoffs, and stale memory cause drift over long runs
- Unreachable quality language triggers runaway cost without meaningful progress
- One initiating prompt is misrepresented as one completion, low cost, or production readiness

## Maturity Boundary

This repo is a `demo-verified` research prototype. Current research, the generic
domain adapter, demo generation, source citations, Obsidian graph hygiene,
packaging, and release scans pass. Market-ready status remains blocked until a
cross-date sample-vault hash is pinned and buyer demand, retention, and
equal-budget advantage over simpler workflows are validated.
