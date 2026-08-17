---
type: "flow"
title: "AI Marketing Hub Adapter"
domain: "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
status: "active"
created: "2026-08-17"
updated: "2026-08-17"
tags:
  - "#domain/designing-running-evaluating-and-governing-one-prompt-multi-agen"
  - "#type/flow"
  - "#confidence/practitioner"
confidence: "practitioner"
related:
  - "[[Index]]"
  - "[[Dashboard]]"
  - "[[Tag Taxonomy]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Synthesis Workflow]]"
  - "[[Reporting Workflow]]"
  - "[[Best Practices Kernel]]"
  - "[[CONVENTIONS]]"
  - "[[Claim Verification Flow]]"
  - "[[Source Manifest Guide]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
  - "[[wiki/flows/_index|Flows Hub]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[wiki/decisions/_index|Decisions Hub]]"
  - "[[wiki/deliverables/_index|Deliverables Hub]]"
  - "[[wiki/reports/_index|Reports Hub]]"
  - "[[wiki/questions/_index|Questions Hub]]"
  - "[[wiki/gaps/_index|Gaps Hub]]"
  - "[[wiki/experiments/_index|Experiments Hub]]"
source_urls: []
---

# AI Marketing Hub Adapter

Adapt the Gauntlet Loop as an opt-in governance wrapper around one existing AI Marketing Hub workflow or skill. Do not replace the Hub router, duplicate skill-specific gates, or imply external execution.

## Trigger

A routed marketing job has an inspectable artifact, valid reference set, enough value for iterative cost, and a declared operator who wants Gauntlet mode.

## Prerequisites

- Read `${AI_MARKETING_LIBRARY_ROOT}/data/orchestrator.json` and the selected
  workflow in `data/workflows/workflows.json`. Resolve the root from the current
  operator environment.
- Load the exact source skill or brain contract. The Hub remains the routing authority.
- Confirm goal, business context, prerequisites, access, deliverable owner, mutation authority, and rollback.

## Steps

1. Route the goal through the Hub. If routing returns `needs_input` or `blocked`, do not start a loop.
2. Run [[Gauntlet Fit and Reference Gate]] against the routed deliverable.
3. Wrap the selected workflow in [[One-Prompt Job Contract]] without changing its canonical prompt, schema, prerequisites, or delivery gates.
4. Treat research, strategy, copy, visual, channel, and compliance concerns as separate work units only when coupling permits.
5. Use skill-specific tests and delivery contracts as protected graders.
6. Add calibrated comparison criteria for audience fit, brand distinctiveness, factual support, channel constraints, accessibility, and measurable outcome.
7. Integrate through one owner, run all original Hub and source-skill gates, and report the typed outcome.
8. Return a proposal or artifact package. Publishing, account edits, spend, and deployment still require explicit external approval and capable executors.

## Outputs

- Hub route and workflow ID, Gauntlet fit decision, contract hash, reference packet, iteration ledger, original gate results, final state, cost, gaps, and approval queue.

## Gates

- No guessed variables, fabricated market data, invented reviews, unsupported performance claims, or hidden missing prerequisites.
- `no data`, `needs_input`, `blocked`, and `optional_missing` remain honest states.
- Original skill gates outrank Gauntlet preference scores.
- No live account, publishing, spend, or production mutation without exact approval, executor receipt, and rollback where required.

## Failure Modes

- Reference copies a competitor instead of serving the brand: stop and revise the reference packet.
- Parallel copy, design, and strategy drift apart: re-route to one integrator.
- Mechanical gates pass but work is generic: run the local Gogh direction and distinctiveness gates, then obtain human taste review.

## Sources

- Local synthesis: `${AI_MARKETING_LIBRARY_ROOT}/data/orchestrator.json`,
  `references/CONTRACT.md`, and `references/canon/005-seven-verb-brains.md`.
- Local synthesis: `${GOGH_ROOT}/wiki/flows/Aesthetic Direction Commitment.md`,
  `wiki/audits/Distinctiveness Audit.md`, and `wiki/flows/Full Stack Build Flow.md`.
- Local synthesis: `${SECRETARY_ROOT}/docs/evidence-workflow.md` for frozen
  evidence and honest unsupported outcomes.
- Public research basis: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).

## Rollback

Restore the last verified local artifact. External rollback follows the source workflow's explicit executor and approval contract.

## Related

- [[Index]]
- [[Best Practices Kernel]]
- [[Integration Regression and Smoothing]]
- [[Approval Queue]]
