# Gauntlet Loop Brain Research Plan

Baseline captured 2026-08-17. The origin, public artifact, vendor operating guidance, iterative-refinement literature, judge-bias literature, and safety rationale are represented in the source ledger. Remaining work focuses on refutation, transfer, and market validation.

## Completed Baseline

- [x] Capture the method author's dated guide and original prompt.
- [x] Capture the public repository's tooling, honest assessment, non-monotonic score trace, and sequential-versus-parallel process finding.
- [x] Capture official guidance on evaluator-optimizer, orchestrator-worker, long-running harness, agent evaluation, multi-agent coordination, and human control.
- [x] Capture primary research on Self-Refine, Reflexion, LLM judges, unreliable self-discrimination, self-preference bias, and specification gaming.
- [x] Distinguish controlled research, vendor field evidence, first-party practitioner evidence, and unsupported folklore.
- [x] Exclude viral metrics, unverified costs, unverified agent counts, and repeated press amplification from authoritative claims.

## Open Research Questions

1. At equal model, tool, token, time, and human-review budgets, does the Gauntlet prompt outperform a strong single-agent or fixed-workflow baseline?
2. Which gains come from the prompt, model, agent harness, evaluator quality, extra tokens, or stopping decision?
3. Which artifact dimensions are observable enough for deterministic tests, model graders, domain experts, and real users?
4. How should coupling be measured before scheduling parallel work?
5. When does a fresh same-model critic help, and when is a different model, multi-judge panel, or human required?
6. How well does static visual comparison predict dynamic quality such as gameplay feel, video pacing, accessibility, or interaction latency?
7. Which buyer segment will pay, repeat the workflow, and accept its evidence burden?

## Controlled Experiment Program

### E1: Prompt Contribution

Run the same inspectable task with the same model, harness, tools, references, token budget, wall-clock, and human stop policy under:

- strong one-pass prompt
- evaluator-optimizer without multi-agent fan-out
- full governed Gauntlet workflow

Use hidden deterministic tests, blinded human review, randomized candidate order, at least three trials per condition, and full cost accounting.

### E2: Critic Independence

Compare builder self-review, fresh same-model critic, different-model critic, multi-judge consensus, and human-calibrated critic. Measure reference-choice accuracy, false passes, false failures, order sensitivity, verbosity sensitivity, and downstream improvement.

### E3: Coupling Probe

Select one task with independent components and one with shared mutable state. Compare parallel ownership with sequential single-owner work under equal budgets. Track merge conflicts, regression count, protected scorecard movement, integration time, and rework.

### E4: Dynamic Artifact Observability

Compare screenshot-only grading with scripted interaction traces, recordings, performance telemetry, deterministic checks, and human playtesting. Measure which defects each channel misses.

### E5: Stop Policy

Compare fixed iterations, evidence-threshold stopping, marginal-value stopping, and human acceptance. Record quality, cost, regression, and overshoot.

### E6: Customer and Retention Proof

Interview real operators using their most recent comparable project. Then run paid or commitment-backed pilots, compare against their current workflow, and measure whether they schedule a second use.

## Refresh Work

- 2026-09-17: recheck S001 through S007 and S014 for current model, harness, product-control, and repository changes.
- 2026-11-17: literature scan for replications, contradictions, newer judge-bias results, coordination benchmarks, and objective-integrity work.
- Before each integration or release: verify platform limits, pricing, permissions, subagent behavior, model availability, and every external reference.

## Evidence Rules

- Primary and official sources lead. Practitioner and vendor reports keep their original confidence.
- A second article repeating the same origin is not corroboration.
- Comparative, causal, numeric, safety, cost, current-platform, and production-readiness claims need a second independent source or a controlled local test.
- Contradictions remain visible. Never overwrite the finding that Claude of Duty did not beat Call of Duty, that its score regressed, or that sequential ownership beat parallel directory ownership for coupled concerns.
- No release copy may call the brain market-ready until the product audit and the market-validation work both pass.
