---
type: "concept"
title: "Coupling-Aware Fan-Out"
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

# Coupling-Aware Fan-Out

Fan-out is a routing decision, not a quality signal. Parallel work is justified when units have low shared-state, ordering, semantic, and validation coupling. Otherwise use one owner sequentially, or isolate work in separate proposals before integration.

## Coupling Test

For every pair of work units, mark:

- `shared_state`: same files, mutable data, tokens, schemas, or runtime state.
- `ordering`: one result must exist before the other is correct.
- `semantic`: both make decisions about the same user experience or concept.
- `validation`: one unit can invalidate the other's proof.
- `merge_surface`: outputs collide or require subjective reconciliation.

Route as follows:

| Coupling | Route | Ownership |
|---|---|---|
| Low | Parallel | Separate paths and independent acceptance |
| Medium | Staged parallel | Proposals in isolation, one integrator applies |
| High | Sequential | One owner for the coupled concern |
| Unknown | Probe first | Small reversible experiment, then classify |

## Evidence Status

- **Evidence-based for Anthropic's system:** multi-agent research excelled on breadth-first independent directions and used substantially more tokens.
- **Practitioner:** the Claude of Duty postmortem reports that parallel directory ownership increased defects in coupled visual systems, while sequential single-owner passes improved results.
- **Contested:** there is no universal numeric coupling threshold. The matrix is a local operational heuristic.
- **Folklore:** "more agents means better output" has no standing without an equal-budget comparison.

## Sources

- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), official system report.
- [Claude of Duty repository](https://github.com/mshumer/Claude-of-Duty), practitioner postmortem and artifact.

## Related

- [[Index]]
- [[Coupling-Aware Decomposition]]
- [[Integration Regression and Smoothing]]
- [[One Prompt Is Not One Completion]]
- [[wiki/concepts/_index|Concepts Hub]]
