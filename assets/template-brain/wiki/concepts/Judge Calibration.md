---
type: "concept"
title: "Judge Calibration"
domain: "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
status: "active"
created: "{{date}}"
updated: "{{date}}"
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

# Judge Calibration

Calibration asks whether a judge's verdict tracks the authority the system actually cares about. A fluent critique is not a calibrated measurement.

## Calibration Set

Build a held-out set with accepted, rejected, borderline, and adversarial examples. Obtain labels from the appropriate authority. Run the judge without candidate provenance and measure agreement, false pass rate, false fail rate, abstention quality, order sensitivity, and stability across repeated trials.

## Required Probes

1. Present each pair as A/B and B/A. Flag order-sensitive verdicts.
2. Equalize irrelevant length and formatting where possible.
3. Include examples from the candidate's model family and other families.
4. Include known rubric-gaming outputs and real outcome failures with persuasive transcripts.
5. Recalibrate after model, prompt, rubric, reference, or domain changes.

## Authority Ladder

| Dimension | Primary authority | Model judge role |
|---|---|---|
| Schema, tests, security rule | Deterministic grader | Explain failures, never waive |
| Factual claim | Source evidence or domain expert | Triage and compare support |
| Visual or editorial quality | Calibrated human panel or user evidence | Scalable proxy with abstention |
| Real task success | Environment outcome or user task | Summarize traces |
| Approval, ethics, risk | Authorized human | Surface decision evidence |

## Evidence Status

- **Evidence-based:** MT-Bench research identifies position, verbosity, self-enhancement, and reasoning limits, while showing useful aggregate human agreement in its tested setting.
- **Evidence-based:** Anthropic recommends calibrating subjective model rubrics against expert human judgment.
- **Practitioner:** the thresholds and escalation policy must be set per domain.

## Sources

- [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685), primary research.
- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), official vendor guidance.

## Related

- [[Index]]
- [[Blind Comparison and Judge Calibration]]
- [[Protected Graders]]
- [[Self-Evaluation Limits]]
- [[wiki/concepts/_index|Concepts Hub]]
