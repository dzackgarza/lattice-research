---
title: Analysis Must Be Grounded in Real Repo Data — No Inference, No Guesses
date: 2026-05-27
status: active
---
# Rule: Analysis Must Be Grounded in Real Repo Data

## The principle

Any analysis, audit, classification, or fix must be derived from reading the actual
code, the actual reports, and the actual design documents in the repo.
Inference, speculation, and pattern-matching from partial data are not acceptable
substitutes for reading the source.

## The anti-pattern

Agents frequently produce analyses based on:
- **Inference from bucket names:** assuming `missing sidecar ordinary signature` means
  external stub work without reading the actual error messages.
- **Same-name matching:** searching for method names in Sage source and assuming the
  stub is missing them, without checking whether the override chain is internal.
- **Abstract reasoning from incomplete data:** producing a strategy document, a set of
  acceptance criteria, or a vague issue comment instead of the concrete deliverable
  requested.
- **Delegation to future agents:** writing a comment or issue that tells someone else
  what to do, rather than doing the analysis now.

## The requirement

Before producing any analysis or deliverable:

1. **Read the actual repo files.** Not summaries, not cross-references, not other
   agents' interpretations.
   The actual code.
2. **Read the actual design documents.** `AGENTS.md`, `category-spec-style`,
   `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`, etc.
3. **Read the actual reports.**
   `reports/workstreams/category-specs-mypy-ledger/latest.json`,
   `reports/workstreams/category-specs-purge-audit/latest.md`, etc.
4. **Produce the concrete deliverable.** If asked for a table, produce the table with
   real data from the repo.
   If asked for a fix, produce the fixed code.
   If asked for a classification, produce the classified rows with evidence.

## What to never do

- **Never produce a strategy document when asked for a concrete output.** A 1500-line
  comment full of "shoulds" and "coulds" is not an audit.
- **Never defer concrete work to future agents or other repos.** If the task is to
  classify rows, classify them.
  Do not write an issue saying "someone should classify these."
- **Never analyze from the sage-stubs repo when the problem is in the research repo.**
  The `sage-stubs` PR, issue, or gap note is downstream evidence.
  It does not substitute for reading the actual `category_specs` code.
- **Never guess at the graph structure.** Read `super_categories()` returns directly.
  Do not infer what the graph probably looks like.

## The concrete failure

In the vault conversation, the user explicitly asked for a new comment on the issue.
The agent produced a 1500-line draft full of strategy, acceptance criteria, and proposed
tables — but no actual classification of any row, no fixed `super_categories()`, and no
concrete stub inventory.
The user had to say: "....you seem to be suggesting making a comment to DELEGATE and
DEFER that work, when I am telling you to DO that work right NOW."

The agent had access to the repo.
It could have read `category_specs/rings/subcategories/*.py`, built the actual graph,
and produced the actual table.
Instead, it wrote a document about what the table should contain.

## The rule

**If you cannot produce the concrete deliverable, stop and say so.** Do not substitute a
strategy document, an issue comment, or a set of acceptance criteria.
These are not the work.
They are containers for the work.
The user asked for the work.
