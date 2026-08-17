---
type: "flow"
title: "Blind Comparison and Judge Calibration"
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

# Blind Comparison and Judge Calibration

Use pairwise preference only after proving the judge is sufficiently aligned with the real authority for this dimension.

## Trigger

A semantic or subjective rubric dimension cannot be resolved by deterministic evidence alone.

## Prerequisites

- Held-out calibration examples labeled by domain experts, users, or authorized operators.
- Comparable candidate and reference captures.

## Steps

1. Calibrate on accepted, rejected, borderline, and adversarial examples.
2. Measure false passes, false fails, abstention quality, repeat stability, and human agreement.
3. Normalize irrelevant presentation differences.
4. Blind provenance and randomly assign A/B.
5. Require dimension evidence before preference.
6. Repeat as B/A. An order flip becomes `uncertain`.
7. Use multiple independent judges or a human when consequence or disagreement exceeds the declared threshold.
8. Lock verdicts before revealing provenance.

## Outputs

- Calibration receipt and pairwise verdict: `candidate`, `reference`, `tie`, `uncertain`, or `blocked`.
- Dimension findings and order-consistency result.

## Gates

- No uncalibrated judge can own a blocking subjective gate.
- No single blind vote proves parity or production readiness.
- Deterministic and human-required gates remain outside pairwise scoring.

## Failure Modes

- Order flip: rotate or escalate.
- Shared-model self-preference: use cross-family or human review.
- Reference and candidate show different states: recapture before judging.

## Sources

- [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685), primary research.
- [Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2410.21819), primary research.
- [[Judge Calibration]] and [[Blind Comparison Bias]]

## Rollback

Discard the preference verdict, retain the calibration failure, and route to a stronger authority.

## Related

- [[Index]]
- [[Protected Graders]]
- [[Fresh Context Critic]]
- [[Budget Plateau and Human Escalation]]
