---
id: SPEC-MAPPING-FORMS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track forms mapping spec
status: needs-review
priority: critical
requirement: Convert category_specs/forms/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  bilinear, quadratic, form-codomain, Hom, End, and Aut signatures.
acceptanceCriteria:
- Source paths category_specs/forms/docs/MAPPING.md and category_specs/forms/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 85
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Track forms mapping spec

Source mapping: `category_specs/forms/docs/MAPPING.md`.

This tracked spec owns review and admission status for the forms mapping document.
