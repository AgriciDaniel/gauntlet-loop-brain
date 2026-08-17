---
type: "concept"
title: "Feedback Memory"
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

# Feedback Memory

Feedback memory preserves validated lessons across fresh contexts without carrying builder advocacy into the critic. Store evidence and decisions, not a persuasive narrative about why the current output should pass.

## Iteration Record

Record:

- Iteration ID, artifact hash or revision, role, model or human identity, and timestamp.
- Finding ID, dimension, severity, locator, and supporting evidence.
- Action taken, owner, changed surfaces, and rollback locator.
- Before and after measures, protected gate results, cost, and elapsed time.
- Verdict, uncertainty, unresolved conflicts, and next state.

## Context Boundaries

- Builder receives accepted findings and necessary evidence.
- Fresh critic receives the job contract, candidate, reference packet, rubric, and protected grader results. It does not receive builder reasoning or desired verdict.
- Integrator receives all accepted changes, ownership boundaries, and regression suite.
- Human receives decision-relevant evidence, disagreement, cost, and rollback.

## Local Synthesis

The local `${SECRETARY_ROOT}` system manifests frozen evidence, persists full
prompts, performs deterministic retrieval, and prefers `no data` when support
is absent. The local `${GOGH_ROOT}` vault separates immutable captures, source
and claim ledgers, current snapshots, conflicts, and gaps. These are local
operating patterns, not public evidence that the Gauntlet Loop works. Resolve
the root aliases from the operator's current environment rather than storing a
host-specific home path in a distributable vault.

## Evidence Status

- **Evidence-based:** Reflexion uses an episodic memory buffer of linguistic feedback across trials.
- **Practitioner:** the specific ledger shape and context routing above are governance adaptations.

## Sources

- [Reflexion](https://arxiv.org/abs/2303.11366), primary research.
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), official vendor guidance.
- Local synthesis: `${SECRETARY_ROOT}/docs/evidence-workflow.md` and
  `${GOGH_ROOT}/references/source-map.md`.

## Related

- [[Index]]
- [[Fresh Context Critic]]
- [[Builder Critic Evidence Loop]]
- [[Integration Regression and Smoothing]]
- [[wiki/concepts/_index|Concepts Hub]]
