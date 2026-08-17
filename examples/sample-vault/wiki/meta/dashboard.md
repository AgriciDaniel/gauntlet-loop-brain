---
type: "dashboard"
title: "Dashboard"
domain: "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
status: "evergreen"
created: "2026-08-17"
updated: "2026-08-17"
tags:
  - "#domain/designing-running-evaluating-and-governing-one-prompt-multi-agen"
  - "#type/dashboard"
  - "#confidence/practitioner"
confidence: "practitioner"
related:
  - "[[Start Here]]"
  - "[[CONVENTIONS]]"
  - "[[Tag Taxonomy]]"
  - "[[Index]]"
  - "[[Overview]]"
  - "[[Hot]]"
  - "[[Log]]"
  - "[[No controlled equal-budget benchmark yet isolates the Gauntlet prompt from model]]"
  - "[[Which reference set best represents the intended audience and task rather than m]]"
  - "[[Equal-budget comparison one-pass agent, iterative single agent, and governed Gau]]"
  - "[[Dashboard]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Claim Verification Flow]]"
  - "[[Synthesis Workflow]]"
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

# Dashboard

Dataview views over the vault require the Dataview community plugin. Without Dataview, use the linked seed lists and run `python3 scripts/audit_brain.py --json` for the same gate signals.

## Visual Map

![[brain-relationship-map.svg]]

## Notes by status

```dataview
TABLE status, domain, confidence, updated
FROM "wiki"
WHERE type != "meta"
SORT status ASC, updated DESC
```

## Seeds needing substance

```dataview
LIST
FROM "wiki"
WHERE status = "seed"
SORT file.name ASC
```

## Contested and low-confidence claims

```dataview
LIST
FROM "wiki"
WHERE confidence = "contested" OR contains(tags, "#confidence/contested") OR contains(tags, "#confidence/folklore")
SORT updated DESC
```

## Recently updated

```dataview
TABLE updated, status, confidence
FROM "wiki"
SORT updated DESC
LIMIT 15
```

## Seed Evidence Queue

### Gaps

- [[No controlled equal-budget benchmark yet isolates the Gauntlet prompt from model]]
- [[No general method guarantees a model critic can observe dynamic feel, long video]]
- [[Same-model fresh-context criticism reduces shared history but does not guarantee]]
- [[The best production plateau rule across domains remains unverified]]
- [[AI Marketing Hub domain adapters and acceptance metrics have not yet been implem]]
- [[Evidence Coverage Not Yet Verified]]

### Questions

- [[Which reference set best represents the intended audience and task rather than m]]
- [[Which dimensions require deterministic tests, model judges, domain experts, or r]]
- [[How should coupling be measured before fan-out]]
- [[When should a retry use the same critic, a fresh critic, multiple critics, or a]]
- [[What evidence is sufficient for dynamic artifacts such as games, video, and inte]]
- [[What equal-budget baseline would show that the loop adds value beyond more infer]]
- [[What Current Official Source Resolves The Highest Risk Claim]]

### Experiments

- [[Equal-budget comparison one-pass agent, iterative single agent, and governed Gau]]
- [[Blind-order probe run each pairwise judgment in both A-B and B-A order]]
- [[Coupling probe parallel ownership versus sequential single-owner work on the sam]]
- [[Critic independence probe same-context, fresh-context, cross-model, and calibrat]]
- [[Plateau probe quality gain and regression rate across increasing iteration budge]]
- [[AI Marketing Hub pilot one opt-in skill with deterministic gates and no external]]
- [[Source To Claim Spot Check Probe]]

Watch for `> [!gap]`, `> [!question]`, `> [!contradiction]`, `> [!stale]`, and `> [!done]` callouts in seed notes.

## Operating Links

- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Explore Plan Code Commit]]
- [[Multi-Agent Fan-Out Research Flow]]
- [[Context Compaction Routine]]
- [[Synthesis Workflow]]
- [[Reporting Workflow]]
- [[Approval Queue]]
- [[Health Scorecard]]
- [[Action Roadmap]]
