---
type: "flow"
title: "One-Prompt Job Contract"
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

# One-Prompt Job Contract

Convert one initiating prompt into a versioned contract that governs many calls and iterations. The contract is frozen before builders start.

## Trigger

[[Gauntlet Fit and Reference Gate]] returns `fit`.

## Prerequisites

- Named goal, reference packet, observation plan, and authority boundary.
- Explicit hard budgets and rollback.

## Steps

1. Assign a `job_id`, contract version, owner, workspace, and baseline revision.
2. State goal, audience, deliverable, exclusions, and non-goals.
3. Attach reference packet and observable comparison dimensions.
4. Declare grader layers and precedence. Name protected gates that no agent may change.
5. Declare allowed tools, writable paths, external-action authority, secrets policy, and rollback locator.
6. Declare coupling policy, maximum concurrency, builder ownership, integrator ownership, and conflict behavior.
7. Set token, cost, wall-clock, iteration, retry, and human-attention caps.
8. Set stop conditions and terminal state schema.
9. Persist the initiating prompt and contract hash before dispatch.

## Outputs

```yaml
job_state: ready
allowed_states: [ready, building, critic_failed, integration_failed, blocked, plateaued, budget_exhausted, needs_human, accepted, aborted]
critic_verdicts: [pass, fail, uncertain, blocked]
```

Also output role envelopes, evidence schema, grader registry, budget ledger, and rollback plan.

## Gates

- Agents may not broaden scope, raise budgets, change protected graders, approve external actions, or self-accept.
- Contract changes require a new version, reason, human owner, and re-baseline.

## Failure Modes

- Ambiguous scope: `needs_human`.
- Missing budget or rollback: `blocked`.
- Reference unavailable after freezing: return to [[Gauntlet Fit and Reference Gate]].

## Sources

- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), official vendor guidance on incremental work and session artifacts.
- [[One Prompt Is Not One Completion]]
- [[Protected Graders]]

## Rollback

Abort dispatch, retain the rejected contract version, and create a corrected version from the unchanged baseline.

## Related

- [[Index]]
- [[Coupling-Aware Decomposition]]
- [[Builder Critic Evidence Loop]]
- [[Budget Plateau and Human Escalation]]
