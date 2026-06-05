---
id: SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY]]'
title: Control Sage constructor and method frontier
status: in-progress
priority: critical
complexity: 75
requirement: Maintain the canonical set difference for Sage constructors, classes,
  functions, and methods in category-spec scope before inventory or mapping progress
  can be reported.
acceptanceCriteria:
- The file records the active scope, included category families, included Sage source
  roots, and source roots not yet inspected.
- 'Every source-grounded constructor, class, function, or method row belongs to the
  universe `U` and has exactly one frontier status: `unclassified`, `classified`,
  `rejected`, or `decision-needed`.'
- Every inventory or mapping progress claim names the rows moved from `Remaining`
  into `C`, `R`, or `Q`, with source evidence and a commit reference.
- Mapping docs, inventory docs, cards, handoffs, and reports are treated as evidence
  or routing only; they are not completion evidence unless this ledger's set difference
  changes.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Control Sage constructor and method frontier

## Object Preserved

This spec preserves the finite object-level frontier for category-spec Sage inventory
and mapping:

```text
Remaining = U - C - R - Q
```

where `U` is the source-grounded universe of Sage constructors, classes, functions, and
methods in the active scope; `C` is the set classified with owner, hypotheses, codomain,
and project category surface; `R` is rejected as non-mathematical, runtime, display,
private, backend plumbing, or otherwise non-admitted; and `Q` requires a recorded
mathematical, source, or workflow decision.

The false substitute this blocks is reporting row counts, file counts, review prose,
handoff updates, broad checkpoints, or current-state summaries as progress.

## Control Invariant

No category-spec Sage inventory or mapping session may report progress unless it updates
this file's set difference. A substantive commit must identify the `frontierId` values
moved from `Remaining` into `C`, `R`, or `Q`.

Mapping documents, subtree `SAGE_INVENTORY.md` files, task cards, decisions, and
handoffs remain useful evidence and routing surfaces, but this file is the status
authority for what remains.

## Scope

This stub does not assert that any Sage source root has already been enumerated into
the frontier. Unknown counts are not zero.

| Field | Value |
| --- | --- |
| Active scope | Category-spec Sage constructors, classes, functions, and methods for the supporting semantic families below. |
| Included category families | Sets, topological spaces, rings, ideals through ring/module ownership, algebras, modules, Hom/End/Aut, forms, lattices, tensor algebra components, posets, and geometry-facing source rows when they block the category-spec phase. |
| Sage source roots included in this ledger | Not populated. |
| Source roots not yet inspected into this ledger | Not populated. |

## Frontier Sets

Status values are closed. Do not add `pending`, `deferred`, `partial`,
`current-state`, or `best-effort`.

| Set | Row condition | Count |
| --- | --- | --- |
| `U` | Source-grounded row exists in this ledger. | Not populated. |
| `C` | Row status is `classified`. | Not populated. |
| `R` | Row status is `rejected`. | Not populated. |
| `Q` | Row status is `decision-needed`. | Not populated. |
| `Remaining` | Row status is `unclassified`. | Not populated. |

## Required Row Fields

Each row must contain these fields. A future implementation may store them as a
markdown table, CSV, or generated view, but this tracked spec remains the canonical
location or must point to exactly one replacement artifact.

| Field | Required meaning |
| --- | --- |
| `frontierId` | Stable identifier for the Sage surface row. |
| `family` | Supporting family such as `sets`, `rings`, `modules`, `lattices`, or `posets`. |
| `sageSourceRoot` | Sage module, class, package export, written doc, or local source file used to place the row in `U`. |
| `sourceSurfaceKind` | One of `constructor`, `class`, `function`, `parent-method`, `element-method`, `hom-parent-method`, `hom-element-method`, `protocol`, `interop`, or `backend-route`. |
| `constructorOrClass` | Constructor, class, parent, or owning source object that exposes the surface. |
| `methodOrFunction` | Literal method, protocol, function, or export spelling. |
| `objectLevel` | Category object, parent, element, Hom parent, Hom element, constructor namespace, or backend bridge. |
| `status` | Exactly one of `unclassified`, `classified`, `rejected`, or `decision-needed`. |
| `projectOwner` | Minimal project category, construction owner, or explicit `none` for rejected rows. |
| `hypotheses` | Mathematical or source hypotheses needed for the owner and codomain. |
| `codomainOrReturn` | Return object, codomain, or payload class. |
| `evidence` | Source path plus section, line, signature, or stable source citation. |
| `decisionOrBlocker` | Decision card, source-mining card, or empty when classified/rejected. |
| `lastMovedBy` | Commit hash that changed the row's frontier status. |

## Canonical Ledger Rows

No rows are admitted in this stub. The first source-enumeration task must populate `U`
before any classification or mapping progress claim is made.

| frontierId | family | sageSourceRoot | sourceSurfaceKind | constructorOrClass | methodOrFunction | objectLevel | status | projectOwner | hypotheses | codomainOrReturn | evidence | decisionOrBlocker | lastMovedBy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Last Commit Movement

Every substantive inventory or mapping commit must add one row here or update the
corresponding row in a replacement structured artifact named by this spec.

| Commit | Rows moved from `Remaining` to `C` | Rows moved from `Remaining` to `R` | Rows moved from `Remaining` to `Q` | Source files used |
| --- | --- | --- | --- | --- |
