---
type: "concept"
title: "How we built our multi-agent research system"
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
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[Claim Verification Flow]]"
  - "[[Index]]"
  - "[[Dashboard]]"
  - "[[CONVENTIONS]]"
  - "[[Tag Taxonomy]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Synthesis Workflow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Best Practices Kernel]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
source_urls:
  - "https://www.anthropic.com/engineering/multi-agent-research-system"
---

# How we built our multi-agent research system

## What It Says

- Anthropic found multi-agent research useful for breadth-first queries with independent directions.
- Anthropic reports that multi-agent systems used about 15 times the tokens of chats in its data.
- Anthropic says domains with shared context or many dependencies are not a good fit for current multi-agent systems.
- Durable execution, retry logic, checkpoints, tracing, clear subagent boundaries, and explicit guardrails were important in production.

## Source

Source: [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system); type vendor; retrieved 2026-08-17; refresh_due 2026-09-17.

> [!gap]
> Ledger confidence is medium/practitioner. Treat this as useful operating evidence, not settled authority, until stronger support is captured.

## Canon Backlink

- Canon ledger entry: [references/canon/007-how-we-built-our-multi-agent-research-system.md](../../../../references/canon/007-how-we-built-our-multi-agent-research-system.md)
- Source ledger: `references/source-ledger.json`

## Related

- [[Claim Verification Flow]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
