---
id: TASK-MAPPING-DOC-COMPLETENESS-RESEARCH
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[SPEC-MAPPING-ALGEBRAS]]'
- '[[SPEC-MAPPING-CAT]]'
- '[[SPEC-MAPPING-FORMS]]'
- '[[SPEC-MAPPING-HOMSETS]]'
- '[[SPEC-MAPPING-LATTICES]]'
- '[[SPEC-MAPPING-MODULES]]'
- '[[SPEC-MAPPING-POSETS]]'
- '[[SPEC-MAPPING-RINGS]]'
- '[[SPEC-MAPPING-SETS]]'
- '[[SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS]]'
- '[[SPEC-MAPPING-TOPOLOGICAL-SPACES]]'
blocks: []
title: Research mapping spec completeness against Sage docs and source
status: needs-review
priority: critical
description: Check every tracked mapping spec against Sage written docs, installed
  Sage source, local SAGE_INVENTORY files, and inherited category methods so missing
  constructors, methods, and interop surfaces become tracked work.
successCriteria:
- Every mapping spec records which Sage docs/source files were checked.
- Missing Sage surfaces are added to the relevant spec or routed to follow-up cards.
- Negative findings use the repo epistemic format and list searched sources.
- Inherited Sage category methods are checked, not only concrete implementation classes.
- No implementation work proceeds from an unreviewed mapping gap.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
commit: '6311873'
---
# Research mapping spec completeness against Sage docs and source

## Summary

Audit every mapping spec for coverage against Sage docs, installed Sage source, and
local inventory docs. This is a research task; it does not implement mappings.

## Execution Evidence

Source-completeness reconciliation has been carried through every tracked mapping spec.
The reconciliation commits are:

- `007c083` reconciles Sets, Rings, and Algebras mapping coverage.
- `7f34f82` aligns coverage ledgers for already reconciled specs.
- `d63abbe` reconciles Modules mapping coverage.
- `6311873` reconciles Lattices mapping coverage.

Validation evidence recorded during the work: `git diff --check` passed for edited
mapping specs, and `just plan-validate` passed with 194 root planning cards.

This card is now ready for review rather than acceptance. Human acceptance remains a
separate gate.
