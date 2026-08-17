---
type: "concept"
title: "Stop and Escalation Policy"
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

# Stop and Escalation Policy

The loop stops when the evidence says stop, not when rhetoric says "perfect." Stop conditions are part of the initiating contract and cannot be rewritten by the builder.

## Terminal States

- `accepted`: all required gates pass and required approvals exist.
- `plateaued`: gain is below the declared meaningful delta for the declared window.
- `budget_exhausted`: any hard token, cost, time, or retry cap is reached.
- `integration_failed`: local improvements cannot pass the integrated regression suite.
- `blocked`: required artifact, reference, tool, environment, or evidence is unavailable.
- `needs_human`: authority, taste, risk, or persistent judge disagreement requires a person.
- `aborted`: operator or safety policy stops the run.

## Immediate Escalation

Escalate without further autonomous retries when a protected gate is modified, a grader is gamed, external authorization is missing, rollback is unavailable, evidence is contradictory on a high-risk claim, cost accelerates unexpectedly, or the critic cannot observe the outcome.

## Plateau Rule

Choose the window and minimum delta before the run. A practical default for a pilot is two consecutive integrated iterations with no meaningful aggregate gain, or one regression on a protected gate that the next bounded repair does not reverse. This is a practitioner default, not a research-backed universal threshold.

## Honest Closeout

Report terminal state, best verified artifact, passed and failed gates, unrun checks, reference comparison, regressions, uncertainty, cost, human actions, and rollback locator. Never convert `blocked`, `plateaued`, or `budget_exhausted` into `accepted`.

## Evidence Status

- **Evidence-based:** specification gaming can satisfy literal measures without the intended outcome.
- **Evidence-based:** agent eval guidance distinguishes transcript claims from environment outcomes.
- **Practitioner:** production plateau thresholds remain domain-specific and unverified.

## Sources

- [Specification gaming](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/), official research explainer.
- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), official vendor guidance.

## Related

- [[Index]]
- [[Budget Plateau and Human Escalation]]
- [[Protected Graders]]
- [[One Prompt Is Not One Completion]]
- [[wiki/concepts/_index|Concepts Hub]]
