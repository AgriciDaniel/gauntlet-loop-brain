---
type: "flow"
title: "Integration Regression and Smoothing"
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

# Integration Regression and Smoothing

Convert local passes into one coherent artifact. Integration is a fresh acceptance event, not the sum of worker verdicts.

## Trigger

One or more work units pass their local critic, or a sequential owner finishes a coupled pass.

## Prerequisites

- One integrator owns the combined surface.
- Baseline and pass-to-pass regression suites are reproducible.

## Steps

1. Integrate one accepted unit at a time in dependency order.
2. Resolve contracts, naming, interfaces, duplicated logic, visual rhythm, tone, and evidence conventions.
3. Re-run all protected deterministic, policy, evidence, accessibility, security, and performance gates.
4. Re-observe the end-to-end artifact in realistic states.
5. Run a fresh critic on the combined artifact and reference packet.
6. Compare integrated metrics and defects to the pre-wave baseline.
7. If any protected gate regresses, set `integration_failed` and repair or roll back.
8. If all gates pass, create a new integrated baseline and continue or stop.

## Outputs

- Integration receipt: included units, conflicts, smoothing changes, full gate results, regressions, artifact identity, and state.

## Gates

- Worker-local passes never override an integrated failure.
- Smoothing cannot silently change the job contract or reference dimensions.
- New failures are attributed and preserved, not averaged away.

## Failure Modes

- Merge conflict or incompatible assumptions: re-route affected concern to one owner.
- Quality improves while performance or accessibility regresses: protected gate blocks acceptance.
- Integrator becomes another builder without fresh review: dispatch a fresh critic.

## Sources

- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), official vendor guidance on outcome, transcript, and regression evaluation.
- [Claude of Duty repository](https://github.com/mshumer/Claude-of-Duty), practitioner evidence on coupled integration.
- [[Protected Graders]]

## Rollback

Restore the last integrated baseline. Keep worker changes as isolated proposals for rework.

## Related

- [[Index]]
- [[Coupling-Aware Decomposition]]
- [[Builder Critic Evidence Loop]]
- [[Budget Plateau and Human Escalation]]
