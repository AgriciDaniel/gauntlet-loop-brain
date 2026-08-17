---
type: "flow"
title: "Gauntlet Fit and Reference Gate"
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

# Gauntlet Fit and Reference Gate

Decide whether a Gauntlet Loop is the right workflow before spending multi-agent budget. The task passes only when the output is observable, a defensible reference exists, and iteration can improve named dimensions.

## Input

- Goal, audience, deliverable, exclusions, authority, risk, budget, and rollback.
- Candidate references with provenance and comparable states.
- Required observation tools and graders.

## Fit Decision

Score each item `yes`, `partial`, `no`, or `unknown`:

1. Can the critic inspect the actual outcome, not only the builder's description?
2. Is at least one reference available, relevant to the intended audience, and legally usable for comparison?
3. Can quality be decomposed into observable dimensions?
4. Can feedback cause a bounded revision?
5. Can required deterministic, expert, user, and approval gates run?
6. Is expected value high enough for the declared compute and human cost?

Route:

- All required items `yes`: `fit`.
- A missing item can be resolved cheaply: `needs_reference` or `needs_probe`.
- Outcome is unobservable, reference is irrelevant, or value is too low: `not_fit`.
- Authority or safety is unresolved: `needs_human`.

## Prerequisites

- Read [[Concrete Reference]], [[Protected Graders]], and [[Stop and Escalation Policy]].
- Capture each reference's URL or file locator, version, retrieval date, audience fit, strengths, known weaknesses, and observation method.

## Steps

1. Reject prestige-only references that do not represent the user's job.
2. Create a reference packet with equivalent states, viewports, data, and prompts.
3. Separate dimensions to emulate from dimensions protected by brand, accessibility, factuality, privacy, performance, and policy.
4. Name grader authority for every dimension.
5. Run one observation probe. If the critic cannot reliably see the state, stop or improve instrumentation.
6. Produce a typed fit decision with confidence and missing evidence.

## Outputs

- `fit_state`: `fit | needs_reference | needs_probe | not_fit | needs_human`.
- Reference packet, comparison dimensions, observation plan, grader authority, budget class, and risks.

## Gates

- No reference, no Gauntlet. Use ordinary planning or deterministic execution instead.
- A reference cannot waive protected graders.
- Dynamic artifacts require evidence of dynamic behavior, not only favorable still images.

## Failure Modes

- Reference mismatch: select a reference set or stop.
- Unobservable outcome: instrument, obtain human evaluation, or return `not_fit`.
- Aspirational bar treated as acceptance: retain the bar for direction and define separate achievable gates.

## Sources

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), evidence-based workflow fit guidance.
- [Gauntlet Loop guide](https://somethingbig.ai/gauntlet-loop), practitioner origin.
- [[Concrete Reference]]

## Rollback

No artifact mutation occurs in this gate. Preserve the fit decision and return to ordinary workflow routing.

## Related

- [[Index]]
- [[One-Prompt Job Contract]]
- [[Judge Calibration]]
- [[Budget Plateau and Human Escalation]]
