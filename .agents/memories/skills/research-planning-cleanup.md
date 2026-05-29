---
title: Research Planning Cleanup
status: active
date: 2026-05-29
---
# Research Planning Cleanup

Meta-review and cleanup of completed cards.
This skill operates one layer above gate-based per-card review.

## When to Use

Use this skill for:
- Scanning recently completed cards for Jerry-behaviour (paraphrase-as-review, checklist
  theater, evidence-shaped evidence, self-certification).
- Identifying cards where the evidence claims are plausible but the claimed work would
  have been impossible without evidence that is not present.
- Flagging completed cards whose reviewers produced zero findings.
- Cleaning up planning debt: cards that are misclassified, oversized, duplicated, or
  blocking downstream work by sitting in the wrong state.
- Finding systemic patterns.

Do NOT use for:
- Initial gate review of a `needs-agent-review` card.
- Plan approval.
- Proving mathematical correctness.

## Proactive trigger: artifact-heavy drift

Invoke this skill when recent work is mostly: card edits, memory edits, handoff edits,
ledger updates, progress reports, decision-card routing, plan reshuffling.
The cleanup output must reduce or compress process load.

## Inspection Protocol

For each completed card under review:
1. Read the card body, acceptance criteria, and any linked review artifacts.
2. Read the actual git diff or artifact that was produced.
3. Ask: does the artifact prove the card's claim, or does it merely produce output that
   looks like evidence?
4. Ask: could a subagent have produced this output without actually solving the
   mathematical/source problem?
5. If the card claims completion but the evidence is circular, flag it.
6. If a reviewer claimed "verified" or "looks correct" without citing line numbers,
   specific findings, or mathematical facts, flag the review as Jerry.

## Red flags

- A completed card whose body describes work in future tense.
- A completed card whose only evidence is a status update or handoff note.
- A review that says "looks good" or "verified" without a single file path.
- A review that only repeats the card's own description back as findings.
- Three or more completed cards with identical review language.
- Any card where the claimed work would require reading external sources and no source
  references appear in the card, diff, or review.

## Output

A table with card ID, signal, action is preferred.
Do not produce a long prose report.

## Stop conditions

Do not turn planning cleanup into its own paperwork stream.
If the audit produces more than 3 new process artifacts, stop and report the escalation
to the user instead of continuing.
