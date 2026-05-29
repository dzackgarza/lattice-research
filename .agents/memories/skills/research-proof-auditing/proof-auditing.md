---
title: Research Proof Auditing Reference
status: active
date: 2026-05-29
---
# Research Proof Auditing Reference

The canonical detailed proof, evidence, fraud-detection, and audit-sufficiency
reference.

## Core Principle

Assertions with external sources are proof.
Print statements are theater.

## Mathematical Argument Shape

Define the problem before using its answer.
Construct objects, name maps, separate definitions/constructions/immediate
consequences/standard theorems/computed results/unproved claims.
State exact theorem and hypotheses when invoking standard theory.

Treat immediate facts as immediate.
For a Type IV period lattice `T` with rank `r` and signature `(2,r-2)`, `dim D_T = r-2`
is immediate. The nontrivial obligation is constructing the lattice and maps that make
those immediate facts relevant.

## Audit Checklist (Pre-Commit Gate)

### 1. Mathematical Adequacy (Primary Gate)

- Script performs the required computation, not a substitute
- Uses Sage/GAP builtins where they exist
- Every claimed isomorphism has a computation that constructs both sides and verifies
  the relation

### 2. Assertion Quality

- ≥1 assertion per 50 lines of code
- Every assertion's expected value has an external source
- No assertion against self-computed values
- No hardcoded boolean verifications

### 3. Fraud Indicators

Reject: print-statement theater, f-string masquerading, conclusion-by-print, try/except
blocks, bounded enumeration as exhaustiveness, large manually typed matrices, ad-hoc
lattice construction, output files, chat-only source research, status-only card diffs.

### 4. File Structure

- Header states which GOAL.md task it verifies
- Uses foundation library constructors
- No try/except, no raise, no error-path handling

## Verification Standard

Expected value sources in priority order: GOAL.md, literature, independent computation,
mathematical derivation.
Never: same script, previous runs, agent self-reports.

## Zero-Trust Verification

Prior session claims, agent self-reports, and markdown files claiming results without
accompanying scripts are not verification.
A result is UNVERIFIED unless a script asserts the claimed result, runs via `just` and
exits 0, and every assertion traces to an external source.

## Failure Mode Taxonomy

28 identified failure modes including: finite-window search as exhaustive proof,
truncated search as emptiness, sampling as structure, approximate numerics as exact
algebra, print-by-fiat verification, assertion laundering through definitions,
witness-free existential claims, invariant matching as isomorphism, theorem-name
laundering, hypothesis erasure, rational/real shadow replacing integral proof,
output-only verification, and more.

## Formal Proof Auditing (Lean 4 / Aristotle)

Acceptance criteria: theorem statement matches GOAL.md claim, proof uses imported
mathlib theorems, no `sorry` placeholders remain, build succeeds via `just lean-check`.
