---
name: research-proof-auditing
description: Use when auditing computational or formal proofs, checking evidence sufficiency,
  reviewing Sage/GAP/Lean/Aristotle verification, detecting proof fraud, or deciding
  whether a result is accepted.
---

# Research Proof Auditing

This skill is the canonical proof, evidence, fraud-detection, and audit-sufficiency authority for the research repo.

## Canonical source

The source of truth is this skill plus `references/proof-auditing.md`.

Read `references/proof-auditing.md` before auditing computation scripts, formal proofs, proof claims, mathematical verification output, adversarial audit evidence, or acceptance claims.

## Core principle

Assertions with external sources are proof. Print statements are theater.

A computation that prints success proves nothing. A computation that asserts a sourced expected value proves the relevant claim when the asserted predicate is mathematically adequate for the task.

## Required audit stance

- Check the exact `GOAL.md` obligation before judging evidence.
- Reject substitute computations, sampled evidence, bounded search without a proof of exhaustiveness, and prose claims presented as certificates.
- Treat prior session claims, markdown summaries, and agent self-reports as unverified until backed by a passing script or formal proof.
- Require every assertion's expected value to trace to `GOAL.md`, literature, independent computation, or a cited derivation.
- Reject proof computations with zero assertions, self-computed expected values, hardcoded boolean verification, print-statement theater, or exception-swallowing verification.
- Formal proofs must have precise theorem statements, no `sorry`, and successful project build/check evidence.

## Load with

- Load `research-orchestration` when the audit is part of state-machine execution or acceptance.
- Load `research-code-style` when audit findings concern code style, assertions, exceptions, constructors, or mathematical API design.
- Load `research-math-boundary` when audit findings concern the trusted mathematical base, backend ownership, Sage/GAP/Julia routing, or exact computation semantics.
- Load `category-spec-audit` when auditing category-spec plans, cards, smoke work, or implementations.

## Stop conditions

Stop acceptance and route follow-up when the evidence proves a cheaper proxy instead of the requested claim, when exactness is replaced by numerics or sampling, when theorem hypotheses are unchecked, when witnesses are missing, or when the target theorem has drifted.
