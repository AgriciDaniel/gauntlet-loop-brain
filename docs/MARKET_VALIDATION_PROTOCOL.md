# Market Validation Protocol

This protocol turns the three unresolved market claims into preregistered tests.
It does not make those claims true. Until completed study records exist, buyer
demand, repeat use, and equal-budget advantage remain unvalidated.

## Claims under test

1. A defined buyer will make a concrete commitment for the governed Gauntlet
   workflow after discussing a recent real project.
2. A buyer who completes a pilot will use the workflow again within the stated
   observation window.
3. On a matched task, the governed workflow improves the preregistered outcome
   against a simpler baseline under equal resource ceilings.

Treat these as separate claims. One cannot stand in for another.

## Authority and ethics

- External interviews, recruiting, messages, incentives, paid pilots, and
  account changes require owner approval before they occur.
- Obtain participant consent for notes and recordings.
- Do not collect credentials, private client artifacts, personal data that is
  not necessary, or confidential work without a written handling agreement.
- Do not promise performance, savings, safety, or market readiness.
- Record refusals, dropouts, negative outcomes, and missing data.
- Freeze the protocol, thresholds, rubrics, and analysis plan before the first
  participant or benchmark run.

## Study A: buyer demand

Choose at least two priority buyer segments before recruitment. Interview at
least five operators in each selected segment. Ask about the most recent
comparable task, current process, actual cost, failure history, approval path,
and evidence burden before showing a proposed product.

The demand outcome is a concrete next action, not positive language. Record one
of the following:

- paid pilot agreed
- written pilot scheduled with owner and date
- installation or evaluation approved by the buyer's decision maker
- follow-up requested without commitment
- declined
- no decision authority

Preregister the minimum commitment rate and minimum number of independent
organizations before recruitment. Do not change the threshold after observing
results. Interest, compliments, waitlist signups, repository stars, and survey
intent do not count as purchase evidence.

## Study B: equal-budget comparison

For every matched task, freeze:

- one real input and one inspectable target
- the same model eligibility, tool access, source packet, and environment
- identical maximum tokens, wall-clock time, financial cost, and human review
  time
- a strong simpler baseline prompt or fixed workflow
- protected deterministic gates
- blinded candidate labels and randomized display order
- the primary acceptance metric and tie rule
- secondary metrics, including regressions, review burden, and cost used

Run at least three trials per condition, as specified in the research plan. The
same unused ceiling is not equal budget if one condition receives extra human
repair, hidden context, or retries. Report actual resource use as well as caps.

An advantage claim needs all preregistered trials, not a selected best run. It
must also survive deterministic blockers. Report wins, ties, losses, effect
sizes where defensible, judge agreement, order sensitivity, and missing data.
Three trials are pilot evidence, not a universal performance claim.

## Study C: retention

Define the observation window before the first pilot. A repeat event must be a
second real use initiated or explicitly scheduled by the buyer, not a researcher
prompt, a support call, or continued work on the first task.

Record:

- eligible pilot completion date
- second-use date or scheduled date
- whether the second use is paid, approved, or exploratory
- buyer segment and organization
- reason for repeat, delay, or refusal
- elapsed days
- support time and operator time required

Preregister the minimum repeat threshold and sample size. Do not call retention
validated while most pilots remain inside the observation window.

## Evidence packet

Each study run must contain:

1. a dated frozen protocol and analysis plan
2. participant or task identifiers that are pseudonymous in public material
3. consent and data-handling record kept outside the public repository
4. raw outcome ledger kept private
5. public aggregate with negative and missing outcomes
6. immutable hashes for inputs, candidates, rubrics, and result files
7. resource accounting for both comparison conditions
8. a named human attestation that the release claim matches the evidence

Use the templates in `examples/market-validation/`. Do not publish the private
participant or artifact ledger.

## Release gate

The repository may be published as an experimental research tool before market
validation, provided every public surface says the claims are unvalidated. It
must not be described as market-ready, proven to outperform a baseline, or
validated for retention until all three studies pass their preregistered rules
and the evidence packet has been independently reviewed.

Experimental publication is an artifact-safety verdict, not a market verdict.
The packaging gate may set `publication_ready: true` only for a named, scanned
artifact set with an owner-selected license, clean commit provenance, and exact
private vulnerability-reporting configuration. Its manifest must still set
`market_ready: false` and all three market-validation fields to false. The
default scaffold remains internal-only. No experimental package can satisfy or
bypass `scripts/audit_brain.py --require market-ready`.
