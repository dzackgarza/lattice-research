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
requirement: Maintain the canonical mathematical and constructor set difference for
  Sage surfaces in category-spec scope, with compatibility/runtime/display/backend
  surfaces separated into a non-progress audit lane.
acceptanceCriteria:
- The file records the active scope, included category families, included Sage source
  roots, and source roots not yet inspected.
- 'Every source-grounded row belongs to exactly one lane: `mathematical-api`,
  `constructor-construction`, `codomain-owned-construction`,
  `compatibility-runtime-display-backend`, or `out-of-scope-sage`.'
- Every mathematical progress claim names rows moved from `Remaining_math` into
  `C_math`, `R_math`, or `Q_math`, with source evidence and a commit reference.
- Mapping docs, inventory docs, cards, handoffs, and reports are treated as evidence
  or routing only; they are not completion evidence unless the primary mathematical
  frontier changes.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Control Sage constructor and method frontier

## Object Preserved

This spec preserves the finite object-level frontier for category-spec Sage inventory
and mapping, with the compatibility audit separated from mathematical progress:

```text
Remaining_math = U_math - C_math - R_math - Q_math
Remaining_compat = U_compat - C_compat - R_compat - Q_compat
```

where `U_math` is the source-grounded universe of mathematical API,
constructor/construction, and codomain-owned construction rows; `C_math` is classified
with owner, hypotheses, codomain, and project category surface; `R_math` is rejected from
the mathematical API; and `Q_math` requires a recorded mathematical, source, or workflow
decision.

`U_compat` is the source-grounded universe of compatibility, runtime, display, private,
test-helper, package-export, and backend-plumbing rows. It is audited so these surfaces
do not leak into the mathematical API, but moving a compatibility row is not
mathematical progress unless the row is marked `blocksImplementation`.

The false substitute this blocks is reporting row counts, file counts, review prose,
handoff updates, broad checkpoints, compatibility cleanups, or current-state summaries
as mathematical progress.

## Control Invariant

No category-spec Sage inventory or mapping session may report mathematical progress
unless it updates `Remaining_math`. A substantive mathematical commit must identify the
`frontierId` values moved from `Remaining_math` into `C_math`, `R_math`, or `Q_math`.

Compatibility/runtime/display/backend rows may be recorded in `U_compat`, but they
belong to a low-priority compatibility audit unless they block a named implementation or
spec obligation. A commit that only moves `U_compat` rows must be described as
compatibility audit work, not mathematical frontier progress.

Mapping documents, subtree `SAGE_INVENTORY.md` files, task cards, decisions, and
handoffs remain useful evidence and routing surfaces, but this file is the status
authority for what remains in the primary mathematical frontier.

## Scope

This stub does not assert that any Sage source root has already been enumerated into
the frontier. Unknown counts are not zero.

| Field | Value |
| --- | --- |
| Active scope | Category-spec Sage constructors, classes, functions, and methods for the supporting semantic families below. |
| Included category families | Sets, topological spaces, rings, ideals through ring/module ownership, algebras, modules, Hom/End/Aut, forms, lattices, tensor algebra components, posets, and geometry-facing source rows when they block the category-spec phase. |
| Sage source roots included in this ledger | Not populated. |
| Source roots not yet inspected into this ledger | Not populated. |

## Primary Frontier Sets

Status values are closed. Do not add `pending`, `deferred`, `partial`,
`current-state`, or `best-effort`.

| Set | Row condition | Count |
| --- | --- | --- |
| `U_math` | Source-grounded row exists in this ledger and lane is `mathematical-api`, `constructor-construction`, or `codomain-owned-construction`. | Not populated. |
| `C_math` | Primary-frontier row status is `classified`. | Not populated. |
| `R_math` | Primary-frontier row status is `rejected`. | Not populated. |
| `Q_math` | Primary-frontier row status is `decision-needed`. | Not populated. |
| `Remaining_math` | Primary-frontier row status is `unclassified`. | Not populated. |

## Compatibility Audit Sets

These rows do not control mathematical progress unless `blocksImplementation` is `yes`.

| Set | Row condition | Count |
| --- | --- | --- |
| `U_compat` | Source-grounded row exists and lane is `compatibility-runtime-display-backend`. | Not populated. |
| `C_compat` | Compatibility row is classified as compatibility behavior with no mathematical API owner. | Not populated. |
| `R_compat` | Compatibility row is rejected as irrelevant to the project boundary. | Not populated. |
| `Q_compat` | Compatibility row requires a decision because it blocks implementation or spec migration. | Not populated. |
| `Remaining_compat` | Compatibility row status is `unclassified`. | Not populated. |

Out-of-scope Sage rows may be recorded only long enough to prove why they are outside
the active category-spec boundary. They do not count as either mathematical progress or
compatibility progress.

## Required Row Fields

Each row must contain these fields. A future implementation may store them as a
markdown table, CSV, or generated view, but this tracked spec remains the canonical
location or must point to exactly one replacement artifact.

| Field | Required meaning |
| --- | --- |
| `frontierId` | Stable identifier for the Sage surface row. |
| `family` | Supporting family such as `sets`, `rings`, `modules`, `lattices`, or `posets`. |
| `sageSourceRoot` | Sage module, class, package export, written doc, or local source file used to place the row in `U`. |
| `lane` | Exactly one of `mathematical-api`, `constructor-construction`, `codomain-owned-construction`, `compatibility-runtime-display-backend`, or `out-of-scope-sage`. |
| `sourceSurfaceKind` | One of `constructor`, `class`, `function`, `parent-method`, `element-method`, `hom-parent-method`, `hom-element-method`, `protocol`, `interop`, or `backend-route`. |
| `constructorOrClass` | Constructor, class, parent, or owning source object that exposes the surface. |
| `methodOrFunction` | Literal method, protocol, function, or export spelling. |
| `objectLevel` | Category object, parent, element, Hom parent, Hom element, constructor namespace, or backend bridge. |
| `status` | Exactly one of `unclassified`, `classified`, `rejected`, or `decision-needed`. |
| `projectOwner` | Minimal project category, construction owner, or explicit `none` for rejected rows. |
| `hypotheses` | Mathematical or source hypotheses needed for the owner and codomain. |
| `codomainOrReturn` | Return object, codomain, or payload class. |
| `evidence` | Source path plus section, line, signature, or stable source citation. |
| `blocksImplementation` | `yes` only when a compatibility/runtime/display/backend row blocks a named implementation, smoke, or spec migration. |
| `decisionOrBlocker` | Decision card, source-mining card, or empty when classified/rejected. |
| `lastMovedBy` | Commit hash that changed the row's frontier status. |

## Canonical Ledger Rows

No rows are admitted in this stub. The first source-enumeration task must populate the
primary mathematical universe before any mathematical classification or mapping progress
claim is made.

| frontierId | family | sageSourceRoot | lane | sourceSurfaceKind | constructorOrClass | methodOrFunction | objectLevel | status | projectOwner | hypotheses | codomainOrReturn | evidence | blocksImplementation | decisionOrBlocker | lastMovedBy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Last Commit Movement

Every substantive inventory or mapping commit must add one row here or update the
corresponding row in a replacement structured artifact named by this spec. Only primary
frontier movement is mathematical progress.

| Commit | Rows moved from `Remaining_math` to `C_math` | Rows moved from `Remaining_math` to `R_math` | Rows moved from `Remaining_math` to `Q_math` | Compatibility rows moved | Source files used |
| --- | --- | --- | --- | --- | --- |
