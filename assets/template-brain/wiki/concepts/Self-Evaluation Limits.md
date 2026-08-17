---
type: "concept"
title: "Self-Evaluation Limits"
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

# Self-Evaluation Limits

Self-evaluation is useful for finding candidate defects, but it is not an independent acceptance layer. Models can preserve their original assumptions, prefer familiar style, mis-rank refinements, or optimize a proxy that they also grade.

## Safe Uses

- Generate a checklist before building.
- Identify suspected defects and propose tests.
- Explain deterministic failures.
- Compare a candidate to explicit reference dimensions.
- Decide what evidence to collect next.

## Unsafe Uses

- Declare its own work production-ready.
- Waive missing tests, inaccessible states, or unsupported claims.
- Replace a human approval or user outcome.
- Convert a persuasive rationale into evidence.
- Keep retrying after repeated uncertain or contradictory verdicts.

## Escalation Rule

After two materially similar self-critic cycles without independent evidence gain, rotate to a fresh critic, cross-model judge, deterministic probe, expert, or human. If no stronger signal is available, report `uncertain` or `blocked`.

## Evidence Status

- **Evidence-based:** SELF-[IN]CORRECT reports that self-refinement judgments are not reliably monotonic.
- **Evidence-based:** the critical survey finds self-correction works best when reliable external feedback is available.
- **Contested:** self-feedback can improve some tasks, as Self-Refine shows. The correct conclusion is bounded use, not blanket rejection.

## Sources

- [SELF-[IN]CORRECT](https://arxiv.org/abs/2404.04298), primary research.
- [When Can LLMs Actually Correct Their Own Mistakes?](https://arxiv.org/abs/2406.01297), primary survey.
- [Self-Refine](https://arxiv.org/abs/2303.17651), primary research and counterweight.

## Related

- [[Index]]
- [[Fresh Context Critic]]
- [[Judge Calibration]]
- [[Protected Graders]]
- [[wiki/concepts/_index|Concepts Hub]]
