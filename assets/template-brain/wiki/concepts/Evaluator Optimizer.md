---
type: "concept"
title: "Evaluator Optimizer"
domain: "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
status: "active"
created: "{{date}}"
updated: "{{date}}"
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

# Evaluator Optimizer

Evaluator-optimizer alternates an artifact-producing role with an evaluation role until a typed stop condition fires. The useful unit is not "agent talks to itself." It is artifact, evidence, verdict, targeted revision, and regression check.

## Minimum Contract

Each cycle records:

1. Candidate artifact identity and baseline evidence.
2. Rubric dimensions and the authority assigned to each grader.
3. Critic verdict: `pass`, `fail`, `uncertain`, or `blocked`.
4. Findings with locators, severity, expected fix, and proof required.
5. Builder revision tied to selected findings.
6. New evidence plus protected regression results.
7. Cost, elapsed time, retry count, and next state.

## Authority

The optimizer proposes changes. It does not redefine success mid-run. Deterministic tests own machine-checkable invariants, model judges own bounded semantic comparison, domain experts own specialist correctness, users own real task utility, and the human operator owns approvals and exceptions. See [[Protected Graders]].

## When It Fits

Use it when evaluation criteria are clear, feedback can identify actionable differences, and another iteration can plausibly improve the artifact. Skip it when the critic cannot observe the outcome, feedback is non-actionable, or the task is already governed by a deterministic one-pass transformation.

## Evidence Status

- **Evidence-based:** Anthropic explicitly describes evaluator-optimizer and its fit conditions.
- **Evidence-based:** Self-Refine reports improvement from iterative feedback across its tested tasks.
- **Contested:** those results do not prove that separate critics always outperform a single model at equal budget.

## Sources

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), official workflow guidance.
- [Self-Refine](https://arxiv.org/abs/2303.17651), primary research.

## Related

- [[Index]]
- [[Builder Critic Evidence Loop]]
- [[Fresh Context Critic]]
- [[Feedback Memory]]
- [[wiki/concepts/_index|Concepts Hub]]
