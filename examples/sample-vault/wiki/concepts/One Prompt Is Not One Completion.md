---
type: "concept"
title: "One Prompt Is Not One Completion"
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

# One Prompt Is Not One Completion

"One prompt" means one initiating job contract. The harness may execute many model calls, agents, tool invocations, context windows, tests, critic rounds, and human decisions. Report both facts.

## Job Envelope

The initiating prompt should bind:

- Goal, audience, deliverable, exclusions, and definition of done.
- Reference packet and dimension rubric.
- Authority boundary, protected paths, external-action policy, and rollback.
- Decomposition policy and coupling routing.
- Builder, critic, integrator, and human roles.
- Evidence requirements and grader precedence.
- Token, cost, time, retry, and concurrency budgets.
- Stop conditions and final typed outcome.

## Honest Accounting

Record prompt count, model calls, agents spawned, tool calls, elapsed time, tokens, cost, human interventions, and final evidence. A single initiating prompt can still represent a large autonomous computation.

## Evidence Status

- **Practitioner:** the Claude of Duty repository exposes a large multi-agent process behind the initiating prompt and reports that its artifact did not reach the stated Call of Duty bar.
- **Evidence-based:** long-running harness guidance treats complex work as incremental progress across sessions rather than a single completion.
- **Contested:** "one-shot" is linguistically defensible for one initiating prompt, but misleading when used to imply one inference or no iteration.

## Sources

- [Claude of Duty repository](https://github.com/mshumer/Claude-of-Duty), first-party artifact and postmortem.
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), official vendor guidance.

## Related

- [[Index]]
- [[One-Prompt Job Contract]]
- [[Feedback Memory]]
- [[Stop and Escalation Policy]]
- [[wiki/concepts/_index|Concepts Hub]]
