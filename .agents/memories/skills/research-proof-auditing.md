---
title: Research Proof Auditing
status: active
date: 2026-05-29
---
# Research Proof Auditing

Canonical proof, evidence, fraud-detection, and audit-sufficiency authority for the
research repo.

## Canonical source

Read `mem:skills/research-proof-auditing/proof-auditing` before auditing computation
scripts, formal proofs, proof claims, mathematical argument notes, verification output,
adversarial audit evidence, or acceptance claims.

## Core principle

Assertions with external sources are proof.
Print statements are theater.
A computation that prints success proves nothing.
A computation that asserts a sourced expected value proves the relevant claim when the
asserted predicate is mathematically adequate for the task.

## Argument-shape gate

Mathematical prose must expose the dependency chain.
Reject notes that replace construction with naming, cite authority instead of stating
theorem hypotheses, inflate immediate consequences into literature claims, or use vague
relational language.

## Standardness calibration

Classify "standard" claims: immediate fact (state directly, move burden upstream),
trivial first-principles derivation (write in place), textbook standard theorem (state
theorem and hypotheses), niche research theorem (cite exact theorem + hypotheses),
project-specific claim (construct or compute it).

## Required audit stance

- Check the exact `GOAL.md` obligation before judging evidence.
- Reject substitute computations, sampled evidence, bounded search without a proof of
  exhaustiveness, and prose claims presented as certificates.
- Reject authority chains, conclusion-smuggling names, and "standard" claims that do not
  state the standard theorem, hypotheses, and exact role in the argument.
- Reject public mathematical surfaces that return raw nonmathematical Sage base types.
- Reject mathematical research findings that depend on external or web sources but were
  left only in chat.
- Treat prior session claims, markdown summaries, and agent self-reports as unverified.
- Reject proof computations with zero assertions, self-computed expected values,
  hardcoded boolean verification, print-statement theater, or exception-swallowing
  verification.
- Formal proofs must have precise theorem statements, no `sorry`, and successful project
  build/check evidence.
- Treat reviewer consensus as evidence, not proof.
