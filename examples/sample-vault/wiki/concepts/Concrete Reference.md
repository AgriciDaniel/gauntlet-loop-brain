---
type: "concept"
title: "Concrete Reference"
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

# Concrete Reference

The reference is an inspectable artifact plus a declared comparison protocol. It turns "make it better" into dimensions a critic can observe, but it is not automatically the right target and does not prove the candidate has reached parity.

## Reference Packet

Record before building:

- Canonical locator, retrieval date, version or snapshot, and usage rights.
- Audience, job-to-be-done, context, and why the reference is relevant.
- Observable dimensions to copy, adapt, or explicitly reject.
- Protected differences such as brand, accessibility, safety, privacy, performance, and platform constraints.
- Evidence capture method: tests, screenshots, traces, recordings, expert review, or user task results.
- Comparison slices that show equivalent states and conditions.

## Selection Gate

Accept the packet only when the reference is available to both critic and operator, represents the intended outcome, and can be compared without hiding material differences. Use a reference set when one artifact is strong on aesthetics but weak on accessibility, evidence, or business fit.

> [!warning] Reference is direction, not authority
> "Ours looks more like the reference" cannot waive tests, policy, factuality, authorization, or human taste. A prestige reference can be the wrong answer for the real audience.

## Confidence

- **Practitioner:** the original Gauntlet guide argues that a concrete bar prevents easy self-approval.
- **Evidence-based:** reference-guided evaluation and external feedback are supported in the evaluator and self-correction literature, but effectiveness depends on task and grader.
- **Contested:** an intentionally unreachable bar may sustain effort, yet it can also create runaway cost or optimize the wrong proxy.
- **Folklore:** superlatives such as "perfect" or "AAA" are not themselves quality mechanisms.

## Sources

- [Gauntlet Loop first-party guide](https://somethingbig.ai/gauntlet-loop), practitioner origin.
- [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685), primary research on reference-guided judging and judge biases.
- [[Source Manifest Guide]] because reference snapshots need provenance.

## Related

- [[Index]]
- [[Gauntlet Fit and Reference Gate]]
- [[Blind Comparison Bias]]
- [[Protected Graders]]
- [[wiki/concepts/_index|Concepts Hub]]
