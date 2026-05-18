---
id: TASK-MYPY-NAMESPACE-AGNOSTIC-ADMISSION
trackerStatus:
  type: task
parents:
- '[[PHASE-SAGE-SIDE-API]]'
dependsOn:
- '[[TASK-MYPY-PARSER]]'
- '[[TASK-MYPY-INSTANTIATE]]'
title: Rewrite method-container admission to be namespace-agnostic
status: needs-agent-review
priority: high
description: Separate semantic Sage-category validation from `sage.categories.*`
  prefix assumptions so valid third-party category subtrees are admissible.
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Admission does not reject a candidate solely because its source fullname is
  outside `sage.categories.*`
- Random non-Sage `ParentMethods` classes still fail semantic validation
- Repo-local or third-party subtree examples can be parsed and passed to the
  instantiation/projection path
- The task body records the exact failing example that motivated the rewrite
complexity: 24
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-SAGE-SIDE-API
---
# Task: Rewrite Method-Container Admission To Be Namespace-Agnostic

## Summary

Rewrite the introspection admission path so that the plugin distinguishes
between:

1. a source fullname living outside `sage.categories.*`, and
2. a source fullname that truly is not a Sage category method container.

The current implementation conflates those cases.

## Source Provenance

- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: namespace-agnostic admission criteria
- 2026-05-10 investigation in `/home/dzack/research`: confirmed that
  `category_specs.algebras.subcategories.semisimple._SemisimpleAlgebras.ParentMethods`
  is rejected by prefix-based admission

## Context

The plugin is meant for any user who hand-rolls a Sage category subtree, not
only code physically filed under upstream `sage.categories.*`. Today
`parse_method_container_fullname()` and its callers reject non-Sage namespaces
before semantic validation runs. That makes the plugin pass its own fixtures
while failing the actual product contract.

This task owns the rewrite of the parser/admission contract in
`~/sage-mypy-plugin/sage_mypy_category_plugin/introspection.py`.

## Acceptance Criteria

- A valid third-party subtree fullname is eligible for semantic validation even
  when its module path does not start with `sage.categories.`
- Admission still rejects arbitrary unrelated classes whose terminal component
  happens to be `ParentMethods`, `ElementMethods`, `MorphismMethods`, or
  `SubcategoryMethods`
- The rewritten parser/admission logic documents that namespace is not the
  semantic criterion
- The motivating repo-local failing example is preserved in the task or linked
  test fixture so future reviewers can replay it

## Dependencies And Boundaries

- Depends on the existing parser and instantiation tasks because this is a
  corrective rewrite, not a fresh greenfield parser
- This task changes admission semantics only; hook wiring and test coverage live
  in sibling tasks under later phases
- Do not weaken the semantic validation boundary merely to admit more names;
  admissibility still has to come from Sage category semantics

## Work Log

- Created 2026-05-10 after reproducing the bug against repo-local
  `category_specs.*` method-container fullnames.
- Updated 2026-05-10: admission now parses
  `category_specs.algebras.subcategories.semisimple._SemisimpleAlgebras.ParentMethods`
  successfully, keeps namespace out of the decisive rule, and still rejects
  structurally similar unrelated names such as `some.random.ParentMethods`.

## Current Status

Needs agent review. The admission rewrite is implemented in
`~/sage-mypy-plugin/sage_mypy_category_plugin/introspection.py`.
