# Claim Ledger

Generated 2026-08-17. Source IDs resolve through `references/source-ledger.json`.

Policy: evidence-based means controlled research or authoritative primary data within the source's tested scope. Practitioner means first-party method, artifact, vendor field report, or applied judgment. Contested means a claim is contradicted, unisolated, or missing independent validation. Folklore is retained only to prevent accidental assertion.

Second source policy: causal, comparative, numeric, current-platform, safety,
and production-readiness claims require an independent source family. A row that
rests on only one author, project, or vendor family remains `SINGLE-SOURCE` even
when several pages from that family are listed.

| ID | Material claim | Confidence | Verdict | Sources | Caveat |
|---|---|---|---|---|---|
| C001 | The named Gauntlet Loop combines a lead agent, concrete bar, decomposed work, separate fresh critics, artifact inspection, and repeated refinement. | practitioner | supported as the author's method definition | S001, S003 | Definition does not prove causal superiority. |
| C002 | One initiating prompt can launch many hours, subagents, tool calls, and iterations. | practitioner | supported | S001, S002 | "One prompt" must not be shortened to "one completion" or "one agent". |
| C003 | A concrete reference is more operationally useful than an abstract quality adjective. | practitioner | supported pattern | S001, S006, S010 | The reference must still be relevant, accessible, and representative. |
| C004 | Iterative feedback can outperform one-step generation in some tasks. | evidence-based | supported within studied settings | S008, S009 | Does not imply unlimited or monotonic improvement. |
| C005 | Same-model self-judgment is not reliably sufficient for selecting or improving self-generated outputs. | evidence-based | supported within studied settings | S011, S012 | A fresh or different critic is not automatically correct. |
| C006 | LLM judges can provide scalable pairwise and reference-guided grading. | evidence-based | supported within studied settings | S006, S010 | Model judges are non-deterministic and require calibration for consequential acceptance. |
| C007 | Position, verbosity, self-enhancement, self-preference, familiarity, and reasoning limits can bias LLM judges. | evidence-based | supported | S010, S012 | Exact bias magnitude varies by model and task. |
| C008 | Parallelization is appropriate for independent subtasks and can be harmful when agents need shared context or have many dependencies. | evidence-based | supported by vendor practice and controlled architecture research | S004, S007, S015 | The controlled results remain scoped to the tested tasks, models, and harnesses. |
| C009 | In Claude of Duty's coupled lighting work, sequential single-owner passes beat parallel directory ownership. | practitioner | supported by project postmortem | S002 | Strong project evidence, not a universal law. |
| C010 | Claude of Duty matched or beat modern Call of Duty. | contested | refuted by the project's own assessment | S001, S002 | Every reported blind critic selected Call of Duty. |
| C011 | Claude of Duty's critic scores improved monotonically. | contested | refuted | S002 | Scores moved 3.59, 4.14, 4.05, and 5.05. |
| C012 | The original prompt alone caused the project's result. | contested | unproven | S001, S002, S004, S005 | Model, harness, tools, token budget, orchestration, and stopping are confounded. |
| C013 | Blind A/B with a fresh critic eliminates judge bias. | contested | unsupported | S010, S011, S012 | It reduces some information leakage but not family, familiarity, order, or reasoning bias. |
| C014 | Evaluations should inspect actual outcomes and combine grader types by task. | practitioner | supported vendor practice | S006 | Domain-specific validation remains necessary. |
| C015 | Agent progress can regress, so every round needs protected regression checks. | practitioner | supported project and vendor practice | S002, S006, S008 | Regression frequency is task dependent. |
| C016 | Long-running agents need durable progress artifacts and explicit handoffs across contexts. | practitioner | supported vendor experiment | S005 | Exact harness design can drift. |
| C017 | Multi-agent systems impose significant cost and coordination overhead. | practitioner | supported vendor field data | S004, S007 | Anthropic's token multiples are not universal forecasts. |
| C018 | Literal grader success can diverge from the intended user outcome. | evidence-based | supported mechanism | S013 | Application to generative-agent loops is an analogy that must be tested locally. |
| C019 | Humans should retain control before consequential, high-stakes, or irreversible actions. | practitioner | supported policy and product practice | S014 | Exact controls must match the environment and jurisdiction. |
| C020 | The Gauntlet Loop is broadly market-ready across code, writing, design, and marketing. | contested | unsupported | S001, S004, S006 | Generalization and willingness to pay need domain pilots and controlled comparisons. |
| C021 | Agent count alone is not a reliable quality strategy; task decomposability and coordination architecture materially affect outcomes. | evidence-based | supported within the controlled evaluation | S015 | The reported 180 configurations do not establish a universal routing law or this brain's equal-budget advantage. |

## Claims Deliberately Excluded

- changing repository stars, views, likes, and viral reach
- unverified costs, token totals, agent counts, and duration figures from retellings
- current cross-model parity claims without controlled equal-budget evidence
- claims that procedural generation means training-data independence
- any description of promotional coverage as independent corroboration
