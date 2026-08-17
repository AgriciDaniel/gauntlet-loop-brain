---
type: "concept"
title: "Protected Graders"
domain: "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
status: "active"
created: "2026-08-17"
updated: "2026-08-17"
tags:
  - "#domain/designing-running-evaluating-and-governing-one-prompt-multi-agen"
  - "#type/concept"
  - "#confidence/practitioner"
confidence: "practitioner"
related:
  - "[[Index]]"
  - "[[CONVENTIONS]]"
  - "[[Best Practices Kernel]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Synthesis Workflow]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[Dashboard]]"
  - "[[Tag Taxonomy]]"
  - "[[Claim Verification Flow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
  - "[[wiki/flows/_index|Flows Hub]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[wiki/decisions/_index|Decisions Hub]]"
  - "[[wiki/deliverables/_index|Deliverables Hub]]"
  - "[[wiki/reports/_index|Reports Hub]]"
  - "[[wiki/questions/_index|Questions Hub]]"
  - "[[wiki/gaps/_index|Gaps Hub]]"
  - "[[wiki/experiments/_index|Experiments Hub]]"
source_urls: []
---

# Protected Graders

A protected grader is owned outside the builder's optimization surface. The builder may inspect a failure and propose a fix, but cannot edit, skip, relabel, or waive the grader without an authorized contract change.

## Grader Layers

1. **Policy and authority:** permissions, privacy, legal or ethical boundaries, external actions, protected paths.
2. **Deterministic outcome:** tests, schemas, invariants, accessibility checks, security checks, performance budgets, environment state.
3. **Evidence:** source support, provenance, freshness, coverage, contradiction handling.
4. **Semantic quality:** calibrated model or expert rubric, blind comparison, domain coherence.
5. **User outcome:** real task completion, adoption, satisfaction, or business measure.

Lower-numbered layers can block higher-layer preference. A beautiful candidate with a security failure is `critic_failed`, not a weighted average pass.

## Protection Rules

- Keep held-out tests and judge calibration examples outside builder context.
- Hash or version grader definitions and reference snapshots.
- Record who can change each grader and what approval is required.
- Detect attempts to edit tests, narrow scope, hide failures, or substitute transcript claims for environment outcomes.
- Re-run pass-to-pass and regression tests after every accepted change.

## Evidence Status

- **Evidence-based:** Anthropic separates code-based, model-based, and human graders, and distinguishes transcript from outcome.
- **Evidence-based:** specification gaming research shows literal objective satisfaction can miss intended outcomes.
- **Practitioner:** the blocking precedence and protection mechanics are governance adaptations.

## Sources

- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), official vendor guidance.
- [Specification gaming](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/), official research explainer.

## Related

- [[Index]]
- [[Judge Calibration]]
- [[Stop and Escalation Policy]]
- [[Integration Regression and Smoothing]]
- [[wiki/concepts/_index|Concepts Hub]]
