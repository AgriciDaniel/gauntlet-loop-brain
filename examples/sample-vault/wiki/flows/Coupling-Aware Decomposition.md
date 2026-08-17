---
type: "flow"
title: "Coupling-Aware Decomposition"
domain: "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
status: "active"
created: "2026-08-17"
updated: "2026-08-17"
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

# Coupling-Aware Decomposition

Turn the contract into work units, then route by dependency and shared-state coupling. Fan-out only after this gate passes.

## Trigger

The job contract is `ready` and has more than one material concern.

## Prerequisites

- Baseline artifact map, protected paths, test topology, and ownership boundaries.
- [[Coupling-Aware Fan-Out]] classification rules.

## Steps

1. Build a dependency graph from artifact surfaces, ordering, shared state, semantics, and validation.
2. Give every unit one outcome, one owner, owned paths, read dependencies, acceptance evidence, and merge contract.
3. Mark each pair `low`, `medium`, `high`, or `unknown` coupling.
4. Route low coupling to parallel builders.
5. Route medium coupling to isolated proposals followed by one integrator.
6. Route high coupling to sequential single-owner passes.
7. Probe unknown coupling with the smallest reversible experiment.
8. Reserve one integration and smoothing unit after every wave.

## Outputs

- Dependency graph, ownership table, wave plan, conflict policy, and per-unit critic packet.
- `routing_state`: `parallel | staged_parallel | sequential | probe_required`.

## Gates

- No overlapping write ownership in one parallel wave.
- No parallel edits to protected graders or shared contracts.
- No wave without an integrator and regression plan.

## Failure Modes

- Hidden coupling appears: pause affected units, preserve work as proposals, reclassify, and assign one owner.
- Parallel local passes conflict: integrated state is `integration_failed`, not average-pass.

## Sources

- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), official system report.
- [Claude of Duty repository](https://github.com/mshumer/Claude-of-Duty), practitioner evidence on coupled visual work.
- [[Coupling-Aware Fan-Out]]

## Rollback

Return affected work to isolated proposals and restore the last integrated baseline.

## Related

- [[Index]]
- [[Builder Critic Evidence Loop]]
- [[Integration Regression and Smoothing]]
- [[Budget Plateau and Human Escalation]]
