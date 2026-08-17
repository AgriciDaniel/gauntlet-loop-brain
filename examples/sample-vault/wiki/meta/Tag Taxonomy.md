---
type: "meta"
title: "Tag Taxonomy"
domain: "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
status: "evergreen"
created: "2026-08-17"
updated: "2026-08-17"
tags:
  - "#domain/designing-running-evaluating-and-governing-one-prompt-multi-agen"
  - "#type/meta"
  - "#confidence/practitioner"
confidence: "practitioner"
related:
  - "[[CONVENTIONS]]"
  - "[[Start Here]]"
  - "[[Index]]"
  - "[[Overview]]"
  - "[[Hot]]"
  - "[[Log]]"
  - "[[Dashboard]]"
  - "[[Tag Taxonomy]]"
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

# Tag Taxonomy

Lowercase hierarchical tags govern graph colors, Dataview filters, and note maintenance. Every wiki note carries one domain tag, one type tag, and one confidence tag in frontmatter.

## Domain tags

- `#domain/designing-running-evaluating-and-governing-one-prompt-multi-agen` for designing, running, evaluating, and governing one-prompt multi-agent improvement loops notes. This tag drives the primary graph color group in `.obsidian/graph.json`.

If a generated brain later adds a real subdomain, add the new `#domain/<subdomain>` tag here first, then add graph color coverage, then update the affected notes.

## Type tags

`#type/hot`, `#type/index`, `#type/overview`, `#type/log`, `#type/meta`, `#type/hub`, `#type/flow`, `#type/source`, `#type/concept`, `#type/entity`, `#type/account`, `#type/platform`, `#type/decision`, `#type/deliverable`, `#type/report`, `#type/question`, `#type/gap`, `#type/experiment`

The type tag mirrors the `type` frontmatter field and powers dashboard grouping.

## Confidence tags

`#confidence/evidence-based`, `#confidence/practitioner`, `#confidence/contested`, `#confidence/folklore`

Use the same lowercase value in the `confidence` field. Source-ledger confidence maps as follows:

| Ledger value | Note confidence | Tag |
|---|---|---|
| high | evidence-based | `#confidence/evidence-based` |
| med | practitioner | `#confidence/practitioner` |
| low | contested | `#confidence/contested` |

## Graph discipline

Graph color groups in `.obsidian/graph.json` key on `#domain/*` and `#type/*` tags, not folder paths. When notes look miscolored, fix the frontmatter tag before changing graph settings.

## Related

- [[CONVENTIONS]]
- [[Dashboard]]
- [[Index]]
- [[Start Here]]
