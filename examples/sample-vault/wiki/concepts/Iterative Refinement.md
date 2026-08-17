---
type: "concept"
title: "Iterative Refinement"
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

# Iterative Refinement

Iterative refinement improves a candidate by converting feedback into bounded changes and re-evaluating the real artifact. A loop is useful only while it produces measurable gain without unacceptable regressions.

## Refinement Unit

Use one ledger row per iteration:

`baseline -> finding -> change -> evidence -> protected regressions -> delta -> state`

The finding must name the failed dimension and locator. The change must be small enough to attribute. The evidence must come from the artifact after the change. Keep rejected findings and regressions visible.

## Control Rules

- Do not rewrite the rubric after seeing a candidate unless a human records a contract revision.
- Prefer one or a small coherent set of findings per retry.
- Re-run all protected gates, not only the grader that motivated the change.
- Compare gain against cost and regression rate.
- Stop when the remaining feedback is contradictory, unobservable, or below the declared minimum meaningful delta.

## Evidence Status

- **Evidence-based:** Self-Refine improved performance across the seven tasks it tested using iterative self-feedback.
- **Evidence-based:** Reflexion shows language agents can use verbal feedback and episodic memory across trials.
- **Contested:** neither result establishes unlimited improvement, universal task coverage, or superiority of Gauntlet orchestration at equal compute.

## Sources

- [Self-Refine](https://arxiv.org/abs/2303.17651), primary research.
- [Reflexion](https://arxiv.org/abs/2303.11366), primary research.
- [When Can LLMs Actually Correct Their Own Mistakes?](https://arxiv.org/abs/2406.01297), primary survey on external-feedback dependence.

## Related

- [[Index]]
- [[Evaluator Optimizer]]
- [[Feedback Memory]]
- [[Self-Evaluation Limits]]
- [[wiki/concepts/_index|Concepts Hub]]
