---
type: "flow"
title: "Builder Critic Evidence Loop"
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

# Builder Critic Evidence Loop

Run one bounded improvement cycle with role separation, evidence, and a typed verdict.

## Trigger

A work unit is owned, observable, budgeted, and has a frozen rubric.

## Prerequisites

- Reproducible baseline evidence and protected gate results.
- Builder write boundary and critic read boundary.

## Steps

1. Builder inspects the baseline and changes only owned surfaces.
2. Builder runs deterministic checks and captures artifact evidence.
3. Orchestrator creates a fresh critic packet without builder rationale or identity cues.
4. Critic observes the real artifact and returns `pass`, `fail`, `uncertain`, or `blocked` with located findings.
5. Orchestrator rejects findings without evidence or outside rubric authority.
6. Builder receives accepted findings, not the critic's hidden chain or desired verdict.
7. Builder makes one bounded repair and re-runs protected gates.
8. Record before and after evidence, cost, regressions, and next state.
9. Continue only if [[Budget Plateau and Human Escalation]] permits another retry.

## Outputs

- Iteration ledger with artifact identity, findings, change set, evidence, verdict, cost, and state transition.
- `critic_failed` when any blocking dimension fails, even if other dimensions improve.

## Gates

- Builder cannot grade or accept its own work.
- Critic cannot edit the artifact or protected graders.
- Model preference cannot waive deterministic, evidence, policy, or human gates.

## Failure Modes

- Critic cannot observe: `blocked`, improve capture.
- Repeated generic feedback: rotate critic or escalate.
- Builder changes rubric or tests: reject the iteration and restore protected surfaces.

## Sources

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), evidence-based evaluator-optimizer pattern.
- [Self-Refine](https://arxiv.org/abs/2303.17651), primary iterative refinement research.
- [[Fresh Context Critic]] and [[Protected Graders]]

## Rollback

Restore the prior artifact revision and retain the failed iteration as evidence.

## Related

- [[Index]]
- [[Blind Comparison and Judge Calibration]]
- [[Feedback Memory]]
- [[Integration Regression and Smoothing]]
