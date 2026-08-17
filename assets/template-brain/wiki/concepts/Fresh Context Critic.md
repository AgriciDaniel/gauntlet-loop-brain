---
type: "concept"
title: "Fresh Context Critic"
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

# Fresh Context Critic

Fresh context reduces anchoring on the builder's plan, effort, and explanations. It is an independence control, not proof of correctness.

## Critic Input Packet

Provide only:

- Frozen [[One-Prompt Job Contract]].
- Candidate artifact and reproducible observation instructions.
- [[Concrete Reference]] packet with provenance removed from A/B labels.
- Rubric, protected grader results, and allowed verdict schema.
- Prior unresolved findings only when needed to test a claimed repair.

Withhold builder identity, rationale, sunk cost, preferred verdict, and unsupported summaries. Give the critic read-only access wherever feasible.

## Critic Output

Require `pass`, `fail`, `uncertain`, or `blocked`; dimension-level findings; concrete evidence; regression risks; and the smallest proof that could reverse each verdict. A critic that cannot observe the required state returns `blocked`, not a guessed score.

## Rotation Policy

- Same critic: useful for continuity when a narrowly specified defect is retested.
- Fresh critic: default after substantive revision or suspected anchoring.
- Cross-model or expert: use when the same model family may share blind spots.
- Human: required for taste, policy, authorization, consequential uncertainty, or unresolved disagreement.

## Evidence Status

- **Evidence-based:** long-running harness research shows the value of explicit artifacts between fresh sessions.
- **Evidence-based:** judge research documents position, verbosity, and self-enhancement biases.
- **Contested:** no cited controlled study here proves that fresh context alone eliminates self-preference.

## Sources

- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), official vendor guidance.
- [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685), primary research.
- [Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2410.21819), primary research.

## Related

- [[Index]]
- [[Blind Comparison Bias]]
- [[Judge Calibration]]
- [[Feedback Memory]]
- [[wiki/concepts/_index|Concepts Hub]]
