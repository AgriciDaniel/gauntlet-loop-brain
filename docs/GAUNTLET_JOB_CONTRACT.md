# Gauntlet Job Contract

The short user prompt should be expanded into a frozen job contract before any
builder starts. This preserves the one-prompt experience while making the hidden
execution policy inspectable.

The machine-readable contract is defined by
`schemas/gauntlet-job.v1.schema.json`. A validated example lives at
`tests/fixtures/gauntlet-job.json`.

## Required fields

- `goal`: the desired end state, not the implementation plan.
- `reference`: the named artifact or measurement, why it is appropriate, and
  the dimensions a critic can actually observe.
- `authority`: allowed and disallowed actions. Capability does not expand it.
- `budget`: explicit maximum iterations, agents, minutes, tokens, cost, and retries. A zero cost or retry ceiling is valid only when it is stated explicitly.
- `gates`: deterministic, evidence, judge, or human checks, each marked blocking
  or advisory.
- `stop_policy`: plateau, regression, and human-stop behavior.

## Reference test

A valid reference is relevant to the intended audience, inspectable with the
available tools, permissible to use, and better on the dimensions that matter.
Prestige alone is not enough. A reference can guide direction without being a
copy target or a claim that the final artifact reached parity.

## Gate test

At least one gate must be blocking. A run made only from model judges should be
treated as weak evidence. Add deterministic tests, factual source checks, direct
artifact interaction, or human review where the domain permits it.

## Validation

```bash
python scripts/validate_gauntlet_job.py tests/fixtures/gauntlet-job.json --json
```

Validation proves structural completeness only. It does not prove that the
reference is good, the rubric is sound, or the requested action is authorized.
