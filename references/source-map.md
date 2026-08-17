# Source Map

Baseline retrieved 2026-08-17. Source IDs resolve through `references/source-ledger.json`. Canon summaries live under `references/canon/`.

## Evidence Layers

| Layer | Sources | What the layer can establish | What it cannot establish |
|---|---|---|---|
| Origin and method | S001, S003 | What Matt Shumer named the Gauntlet Loop and what the original prompt instructed | That the method caused the result, beat the reference, or transfers unchanged to another domain |
| Artifact and postmortem | S002 | What the public repository contains and what its author reports about scores, defects, performance, and process | Independent reproduction of those measurements or a general law about all multi-agent work |
| Vendor operating patterns | S004, S005, S006, S007, S014 | Field-tested patterns for orchestration, long-running state, evaluation, cost, coordination, and oversight | Controlled proof that one prompt or one vendor harness is superior |
| Controlled architecture routing | S015 | Multi-agent performance depends on task decomposability, tool density, and coordination architecture in the reported evaluation | A universal architecture rule or equal-budget proof for this brain |
| Controlled refinement research | S008, S009 | Iterative feedback and memory can improve results in the reported tasks and models | Unlimited monotonic improvement, current-model parity, or proof of separate-critic superiority |
| Controlled judge research | S010, S011, S012 | LLM judge utility and documented position, self-evaluation, self-preference, and reasoning limits | That fresh context or blind A/B eliminates all judge bias |
| Objective integrity and safety | S013, S014 | Why literal grader success can diverge from intended outcomes, and why humans need control over consequential actions | A complete domain-specific compliance or safety standard |

## Claim-to-Source Crosswalk

| Claim family | Primary support | Corroboration or challenge | Canon |
|---|---|---|---|
| One initiating prompt can launch many governed iterations | S001, S003 | S005 shows why persistent state and handoffs matter | [001](canon/001-how-to-run-a-gauntlet-loop.md), [005](canon/005-effective-harnesses-for-long-running-agents.md) |
| A concrete inspectable reference gives the critic a usable comparison target | S001 | S006 and S010 support reference-based grading, but neither proves the reference is relevant | [001](canon/001-how-to-run-a-gauntlet-loop.md), [006](canon/006-demystifying-evals-for-ai-agents.md), [010](canon/010-judging-llm-as-a-judge-with-mt-bench-and-chatbot-arena.md) |
| Iterative feedback can improve outputs | S008, S009 | S011 shows that self-judgment is not reliably sufficient | [008](canon/008-self-refine-iterative-refinement-with-self-feedback.md), [009](canon/009-reflexion-language-agents-with-verbal-reinforcement-learning.md), [011](canon/011-self-in-correct-llms-struggle-with-discriminating-self-generated.md) |
| Builders should not be sole graders | S010, S011, S012 | S006 requires model graders to be calibrated with humans | [006](canon/006-demystifying-evals-for-ai-agents.md), [010](canon/010-judging-llm-as-a-judge-with-mt-bench-and-chatbot-arena.md), [012](canon/012-self-preference-bias-in-llm-as-a-judge.md) |
| Parallelism is conditional on independence | S004, S007, S015 | S002 reports that sequential ownership beat parallel directory ownership for coupled lighting concerns, while S015 reports controlled parallel gains and sequential penalties | [002](canon/002-claude-of-duty-readme-and-honest-assessment.md), [007](canon/007-how-we-built-our-multi-agent-research-system.md), [015](canon/015-towards-a-science-of-scaling-agent-systems-when-and-why-agent-sy.md) |
| Progress is not guaranteed to be monotonic | S002, S008 | S011 challenges reliable self-discrimination | [002](canon/002-claude-of-duty-readme-and-honest-assessment.md), [008](canon/008-self-refine-iterative-refinement-with-self-feedback.md), [011](canon/011-self-in-correct-llms-struggle-with-discriminating-self-generated.md) |
| Acceptance must use outcomes, regression checks, and appropriate graders | S006 | S010 documents judge biases and S013 documents proxy gaming | [006](canon/006-demystifying-evals-for-ai-agents.md), [010](canon/010-judging-llm-as-a-judge-with-mt-bench-and-chatbot-arena.md), [013](canon/013-specification-gaming-the-flip-side-of-ai-ingenuity.md) |
| Consequential mutations require human authority and bounded access | S014 | S013 explains why literal objectives can produce unintended outcomes | [013](canon/013-specification-gaming-the-flip-side-of-ai-ingenuity.md), [014](canon/014-our-framework-for-developing-safe-and-trustworthy-agents.md) |

## Raw Run Evidence to Capture

External research does not replace run-specific evidence. Each actual loop should preserve:

- operator goal, authority boundary, budget, stopping policy, reference candidates, and protected paths
- chosen reference captures, rights or access notes, and why each reference represents the intended audience and task
- decomposition graph, dependency and coupling decisions, owner assignments, and merge order
- exact builder and critic inputs, artifact versions, screenshots or recordings, tool results, and critic outputs
- deterministic tests, model-judge results, human or domain-expert review, regressions, cost, token, latency, and wall-clock logs
- rejected rounds and score regressions, not just the best round
- final acceptance decision and the person or rule authorized to make it

## Import Strategy

1. Copy immutable captures into `.raw/sources/` and do not follow or rewrite source symlinks.
2. Record path, SHA-256, retrieval date, owner, source type, license or access caveat, and what the capture does and does not prove.
3. Record external evidence in `references/source-ledger.json` and create a concise note under `wiki/sources/`.
4. Link each material claim to one or more source IDs and mark single-source practitioner claims explicitly.
5. Fold the evidence into concepts, flows, decisions, experiments, and deliverables without upgrading its confidence.
6. Recheck fast-moving product claims before integration or release, even when the scheduled refresh date has not arrived.

## Explicit Exclusions

- Repeated press coverage of the same author post is not independent corroboration.
- Repository stars, views, likes, and viral reach are not quality or demand evidence.
- Unverified cost stories, agent counts, token counts, model parity claims, and third-party game claims are excluded from the authoritative ledger.
- The phrases "AAA quality", "utterly perfect", and "one-shot" are instructions or marketing language, not verified outcomes.
