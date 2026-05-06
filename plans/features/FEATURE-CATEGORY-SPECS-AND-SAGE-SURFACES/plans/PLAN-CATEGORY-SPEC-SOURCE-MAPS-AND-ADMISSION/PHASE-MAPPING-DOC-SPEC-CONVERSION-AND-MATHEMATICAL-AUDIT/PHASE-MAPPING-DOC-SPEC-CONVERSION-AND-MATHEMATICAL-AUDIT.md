---
id: PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
trackerStatus:
  type: phase
parents:
- '[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'
dependsOn: []
title: Mapping doc spec conversion and mathematical audit
status: needs-review
priority: critical
description: Convert every category-spec mapping document into a tracked spec surface
  and audit those specs for Sage-source completeness, mathematical correctness,
  well-typed signatures, and coherent highest-category method placement.
successCriteria:
- Every category_specs subtree mapping document has a feature-owned tracked spec card.
- Each mapping spec records the source MAPPING and SAGE_INVENTORY paths that ground it.
- Completeness review checks Sage written docs and installed Sage source for missing
  constructors, methods, inherited methods, and interop surfaces.
- Mathematical review rejects incoherent ownership, nonmathematical targets, ill-typed
  signatures, and mappings that confuse method definition location with output type.
- Unresolved mathematical choices become decision cards before implementation proceeds.
tasks:
- '[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]'
- '[[TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
---
# Mapping doc spec conversion and mathematical audit

## Summary

This phase makes mapping documents tracked spec surfaces and then reviews them as
mathematical interface specifications. The review must treat every method row as a
claim about where a method is defined, what its full signature is, and why that
signature is mathematically meaningful.

## Audit Standard

- Completeness: compare each mapping spec against Sage written docs, installed Sage
  source, local SAGE_INVENTORY files, and inherited category methods.
- Mathematical correctness: methods are mapped to the highest category where they are
  well-defined; subcategories inherit methods from supercategories; no row may use a
  nonmathematical target or software-shaped placeholder as a public mathematical owner.
- Type correctness: every admitted row states caller category, inputs, hypotheses,
  codomain or return object, and source evidence.
- Review consequence: gaps become tracked specs, tasks, or decision cards, not prose
  TODOs or implementation guesses.

## Review Handoff

Both phase tasks are now in `needs-review`:

- `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]` records the Sage-doc/source
  reconciliation pass.
- `[[TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT]]` records the mathematical
  owner, codomain, and type-signature corrections from the audit pass.

This phase is ready for human/spec review. It is not accepted or closed.
