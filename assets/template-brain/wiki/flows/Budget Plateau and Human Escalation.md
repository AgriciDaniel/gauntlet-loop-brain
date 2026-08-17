---
type: "flow"
title: "Budget Plateau and Human Escalation"
domain: "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
status: "active"
created: "{{date}}"
updated: "{{date}}"
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

# Budget Plateau and Human Escalation

Evaluate stop conditions after every critic and integration event. The loop has no authority to extend its own budget.

## Trigger

An iteration ends, a protected gate fails, a budget threshold is approached, or uncertainty requires authority.

## Prerequisites

- Frozen budgets, plateau window, meaningful-delta rule, human owner, and rollback.

## Steps

1. Update token, cost, wall-clock, retry, regression, and human-attention ledgers.
2. Check terminal conditions in precedence order: safety or authority, hard budget, protected regression, blocked observation, judge disagreement, plateau, acceptance.
3. Compute quality delta only from integrated evidence.
4. If the plateau window fires, set `plateaued` and preserve the best verified artifact.
5. If a human decision is required, provide options, evidence, cost to continue, risk, and rollback.
6. Continue only after an authorized contract revision or when the original contract still permits it.

## Outputs

- Terminal or continuing state with reason and evidence.
- Honest closeout for `accepted`, `plateaued`, `budget_exhausted`, `integration_failed`, `blocked`, `needs_human`, or `aborted`.

## Gates

- Hard caps cannot be traded against quality scores.
- Human approval requirements cannot be self-approved.
- `blocked`, `uncertain`, and unrun checks stay visible.

## Failure Modes

- Runaway retry loop: terminate at cap.
- Metric gain with outcome regression: protect outcome and stop.
- Sunk-cost argument: exclude spent cost from quality verdict, include it in continuation decision.

## Sources

- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), official system report on cost and fit.
- [Specification gaming](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/), official research explainer.
- [[Stop and Escalation Policy]]

## Rollback

Restore the best verified integrated artifact and retain the full iteration ledger.

## Related

- [[Index]]
- [[One-Prompt Job Contract]]
- [[Integration Regression and Smoothing]]
- [[Approval Queue]]
