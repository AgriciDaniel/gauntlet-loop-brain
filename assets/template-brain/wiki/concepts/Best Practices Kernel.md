---
type: "concept"
title: "Best Practices Kernel"
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
  - "[[Dashboard]]"
  - "[[Tag Taxonomy]]"
  - "[[Source Intake Workflow]]"
  - "[[Synthesis Workflow]]"
  - "[[Claim Verification Flow]]"
  - "[[CONVENTIONS]]"
  - "[[Research Refresh Workflow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Best Practices Kernel]]"
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

# Best Practices Kernel

The kernel is a governed improvement system: define the job, protect the evidence and graders, route work by coupling, iterate with fresh criticism, integrate, and stop honestly. A dramatic quality claim is never a substitute for a gate.

## Operating Order

1. Run [[Gauntlet Fit and Reference Gate]]. Reject tasks whose output cannot be observed or whose reference is unavailable.
2. Freeze the [[One-Prompt Job Contract]]: scope, authority, reference set, rubric, protected paths, budgets, rollback, and expected evidence.
3. Use [[Coupling-Aware Decomposition]]. Parallelize only independent work with separate ownership and merge surfaces.
4. Run [[Builder Critic Evidence Loop]]. Builders change artifacts. Critics receive fresh context and return falsifiable findings.
5. Run [[Blind Comparison and Judge Calibration]]. Reverse A/B order, calibrate model judges, and reserve deterministic or human authority where needed.
6. Run [[Integration Regression and Smoothing]] after every wave. Local wins do not survive unless the integrated artifact passes protected gates.
7. Run [[Budget Plateau and Human Escalation]]. Stop on pass, plateau, regression, uncertainty, budget, or human intervention.

## Evidence Classes

- **Evidence-based:** primary research or official guidance supports the narrow claim.
- **Practitioner:** an author report, repository postmortem, or local operating lesson supports the tactic, but not broad causality.
- **Contested:** credible evidence points in different directions. Keep the conflict visible.
- **Folklore:** repeated prompt advice without a controlled comparison. Never promote it to a gate.

## Non-Negotiable Invariants

- The output state is typed: `not_started`, `building`, `critic_failed`, `integration_failed`, `blocked`, `plateaued`, `budget_exhausted`, `needs_human`, `accepted`, or `aborted`.
- A builder cannot waive its own failing grader.
- A model judge cannot override a deterministic failure, protected policy gate, missing evidence, or human approval requirement.
- A reference directs comparison. It does not prove equivalence.
- Every retry consumes a declared budget and must target named evidence.
- Final reporting states the achieved outcome, remaining gaps, regressions, cost, and unrun checks.

## Why This Kernel Exists

Anthropic describes evaluator-optimizer as useful when evaluation criteria are clear and iterative refinement adds value. Its multi-agent research post says parallelism fits independent breadth-first work and warns about token cost and shared-context dependencies. The Claude of Duty postmortem is practitioner evidence that sequential ownership can beat parallel fan-out for coupled systems. Together these support governed looping, not endless looping.

## Sources

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), official vendor guidance, evidence-based for workflow shapes.
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), official vendor report, evidence-based for its system and practitioner guidance for transfer.
- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), official vendor guidance, evidence-based for layered grader design.
- [Claude of Duty repository](https://github.com/mshumer/Claude-of-Duty), first-party artifact and practitioner postmortem.

Related: [[Index]] | [[One Prompt Is Not One Completion]] | [[Protected Graders]] | [[Stop and Escalation Policy]]
