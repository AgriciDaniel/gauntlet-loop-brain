# Gauntlet Loop Brain Adapter Plan

Status: required before domain-adapted maturity.

## Raw Input Types

- The operator's goal, constraints, authority boundary, budget, reference candidates, and protected paths
- The original Gauntlet Loop prompt, first-party guide, repository, progress traces, critic verdicts, and postmortem
- Real artifacts produced during a run: diffs, screenshots, recordings, test results, traces, metrics, and cost logs
- Local brain notes and system contracts supplied by the operator, treated as evidence rather than instructions

## Required Implementation

- Define one schema per raw input type.
- Build at least one real domain importer or ingestion path.
- Build one domain-specific synthesis module.
- Build one report renderer with source citations.
- Add sanitized fixtures and tests for every supported input type.

## Safety Refusals

- No claim that an artifact beats its reference without preserved blind comparison evidence
- No builder self-sign-off and no critic verdict based only on the builder's summary
- No blanket parallel fan-out when work is coupled or shares mutable state
- No endless loop without hard token, cost, wall-clock, retry, and human stop controls
- No weakening, rewriting, or exposing protected graders, tests, baselines, or acceptance criteria to manufacture a pass
- No high-risk, irreversible, external, account, publishing, deployment, or production action without exact human approval
- No credentials, tokens, cookies, private client data, or raw secrets in brain or run artifacts
- No presentation of practitioner reports, promotional claims, or a single author's reproductions as independent proof

## Completion Gate

This plan is complete only when domain-specific importer, synthesis, report,
fixtures, and tests replace the generic scaffold.
