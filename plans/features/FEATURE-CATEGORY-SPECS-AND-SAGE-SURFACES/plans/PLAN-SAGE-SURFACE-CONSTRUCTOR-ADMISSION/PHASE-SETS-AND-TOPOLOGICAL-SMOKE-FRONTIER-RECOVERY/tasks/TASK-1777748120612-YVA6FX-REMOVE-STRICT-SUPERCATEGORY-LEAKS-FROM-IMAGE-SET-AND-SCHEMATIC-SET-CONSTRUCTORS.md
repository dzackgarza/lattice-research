---
id: TASK-1777748120612-YVA6FX-REMOVE-STRICT-SUPERCATEGORY-LEAKS-FROM-IMAGE-SET-AND-SCHEMATIC-SET-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
dependsOn: []
title: Remove strict-supercategory leaks from image-set and schematic-set constructors
status: needs-review
priority: critical
description: Remove strict-supercategory leaks from image-set and schematic-set constructors
successCriteria:
- Remove strict-supercategory leaks from image-set and schematic-set constructors is resolved
  according to the body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
- category-specs
- task
- constructors
- sets
- theme-audit-uniformity
---
# Remove strict-supercategory leaks from image-set and schematic-set constructors
Source: pasted backlog 2026-05-02.

Task: remove strict-supercategory leakage from diagram-set/image-set/schematic-set constructors, restrict inputs to the correct base category.

## Complexity Justification
- Owner: C61
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Remove strict-supercategory leaks from image-set and schematic-set constructors
- Why this specific score:
  - This task likely edits multiple constructor categories (`diagram-set`, `image-set`, `schematic-set`) and their inheritance constraints. Tightening category restrictions can break typed and runtime assumptions across callers, so coupling and verification cost are high but still localized to category wiring.
- Item-specific evidence:
  - The task statement directly names supercategory leak removal as the mechanism, implying non-local effect on constructor input validation paths rather than only one function.
  - The explicit owner 61 maps cleanly to this high-but-bounded migration risk.

## Implementation Notes
- Restricted `Sets().Constructors().ImageSubobject(...)` to the documented public inputs
  `f: SetMorphism` and `domain_subset: Subset`, and stopped exposing Sage-only
  `category`, `is_injective`, and `inverse` constructor knobs.
- Removed the public catch-all `Sets().Constructors().RealSet(...)` entry and the
  Sage `normalized` option from the real-line subset constructors. The remaining
  public surface now matches the documented interval, ray, point, and real-line
  constructors in `category_specs/topological_spaces/docs/MAPPING.md`.
- Parent integration review added the non-catch-all
  `Sets().Constructors().RealSetFromIntervals(intervals)` route for finite unions of
  Sage `InternalRealInterval` components, updated the set mapping to name that
  constructor, and updated regression call sites away from removed public option bags.

## Negative Finding: Literal `diagram-set` / `schematic-set` surfaces
- Searched: `npx -y @probelabs/probe search "schematic" . -o plain --max-results 40`; `npx -y @probelabs/probe search "diagram set" . ext:md -o plain --max-results 40`; `npx -y @probelabs/probe search "SchematicSet DiagramSet" category_specs -l python -o plain --max-results 40`
- Found: no current `category_specs` constructor, type, mapping-doc, or code surface named `schematic-set`, `SchematicSet`, `diagram-set`, or `DiagramSet`; the only live constructor leaks in scope were `Sets().Constructors().ImageSubobject(...)` and the real-subset constructor family in `category_specs/sets/__init__.py`
- Conclusion: inference — the migrated task wording appears stale, and the current set/topology constructor leak work is represented by the image-subobject and real-subset constructor surfaces rather than any literal `diagram-set` or `schematic-set` constructor
- Confidence: High
- Gaps: did not inspect unrelated non-`category_specs` mathematical subtrees in depth beyond the broad repo search results because the user limited write ownership to set/topology constructor leak work
