---
type: "source"
title: "Gauntlet Loop Evidence Baseline"
domain: "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
status: "active"
created: "{{date}}"
updated: "{{date}}"
tags:
  - "#domain/designing-running-evaluating-and-governing-one-prompt-multi-agen"
  - "#type/source"
  - "#confidence/practitioner"
confidence: "practitioner"
related:
  - "[[Index]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[Source Manifest Guide]]"
  - "[[Concrete Reference]]"
  - "[[One Prompt Is Not One Completion]]"
  - "[[Coupling-Aware Fan-Out]]"
  - "[[Protected Graders]]"
  - "[[Stop and Escalation Policy]]"
source_urls:
  - "https://somethingbig.ai/gauntlet-loop"
  - "https://github.com/mshumer/Claude-of-Duty/blob/main/README.md"
  - "https://github.com/mshumer/Claude-of-Duty/blob/main/prompt.md"
  - "https://www.anthropic.com/engineering/building-effective-agents"
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
  - "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"
  - "https://www.anthropic.com/engineering/multi-agent-research-system"
  - "https://arxiv.org/abs/2303.17651"
  - "https://arxiv.org/abs/2303.11366"
  - "https://arxiv.org/abs/2306.05685"
  - "https://arxiv.org/abs/2404.04298"
  - "https://arxiv.org/abs/2410.21819"
  - "https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/"
  - "https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents"
---

# Gauntlet Loop Evidence Baseline

The Gauntlet Loop is a first-party practitioner method that combines a concrete inspectable bar, agent-chosen decomposition, separate builders and critics, direct artifact comparison, and repeated refinement. Controlled research supports iterative feedback in bounded settings and documents material limits in LLM self-evaluation and judging. It does not prove that this prompt is causally superior.

## What Survives Refutation

- One initiating prompt can govern many agent calls and many hours. It is not one completion.
- Concrete reference-based evaluation is more operational than vague quality language when the reference is relevant and inspectable.
- Builders should not be sole graders.
- Parallel work is appropriate only for independent concerns.
- Evaluation must inspect actual outcomes and protect prior guarantees.
- Humans retain authority over consequential actions and ambiguous final acceptance.

## What the Original Project Did Not Show

- It did not beat Call of Duty.
- Its score did not improve every round.
- Its blind critics never selected its frames over Call of Duty.
- Parallel directory ownership did not beat sequential ownership for coupled lighting concerns.
- The initiating prompt was not isolated from model, harness, tools, tokens, or stopping policy.

## Evidence Classes

- S001 to S003: first-party method, artifact, and postmortem. Confidence: practitioner.
- S004 to S007 and S014: vendor engineering, internal evaluation, and policy. Confidence: practitioner.
- S008 to S012: controlled research within stated task and model scopes. Confidence: evidence-based.
- S013: objective-integrity research synthesis and examples. Confidence: evidence-based for the mechanism, applied by analogy to this loop.

Full source metadata, dates, refresh schedule, claims, and caveats live in `references/source-ledger.json`.

Related: [[Source Manifest Guide]] | [[Concrete Reference]] | [[Protected Graders]] | [[Stop and Escalation Policy]]
