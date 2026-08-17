---
type: "concept"
title: "Blind Comparison Bias"
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

# Blind Comparison Bias

Blind comparison hides which artifact is the candidate and which is the reference. It reduces provenance cues, but does not remove order, verbosity, style, shared-model, or rubric bias.

## Pairwise Protocol

1. Normalize viewport, task state, prompt, scale, formatting, and evidence window.
2. Randomly assign candidate and reference to A/B.
3. Ask for dimension-level evidence before preference.
4. Repeat with B/A order.
5. Treat conflicting order results as `uncertain`.
6. Keep deterministic results outside the blind preference vote.
7. Reveal provenance only after verdicts are locked.

## Interpretation

- `ours_wins_both_orders`: preference evidence, not parity proof.
- `reference_wins_both_orders`: targeted failure evidence.
- `order_flip`: judge instability, route to calibration or human review.
- `tie_or_abstain`: no decisive preference, inspect dimension evidence.
- `unobservable`: blocked, improve capture instead of scoring.

## Evidence Status

- **Evidence-based:** LLM judge research documents position and self-enhancement biases.
- **Practitioner:** blinding and order reversal are defensible mitigations, not guarantees.
- **Contested:** a separate critic may still share model-family preferences and training-data familiarity.
- **Folklore:** one blind vote cannot establish that an artifact "beats" a market leader.

## Sources

- [Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2410.21819), primary research.
- [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685), primary research.

## Related

- [[Index]]
- [[Blind Comparison and Judge Calibration]]
- [[Fresh Context Critic]]
- [[Judge Calibration]]
- [[wiki/concepts/_index|Concepts Hub]]
