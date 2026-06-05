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
requirement: Maintain the canonical mathematically typed constructor and method set
  difference for category-spec scope, with Sage source used as implementation evidence
  and compatibility/runtime/display/backend surfaces separated into a non-progress
  audit lane.
acceptanceCriteria:
- The file records the active scope, included category families, included Sage source
  roots, and source roots not yet inspected.
- The active mathematical theory sheet states the objects, operations, and weakest
  structures that generate `U_math` before Sage source names are classified.
- 'Every Sage-evidenced row belongs to exactly one lane: `mathematical-api`,
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

This spec preserves the finite object-level frontier for category-spec inventory and
mapping. The primary frontier is generated from the mathematical theory sheet first;
Sage source then supplies implementation evidence for those mathematical slots. The
compatibility audit is separated from mathematical progress:

```text
Remaining_math = U_math - C_math - R_math - Q_math
Remaining_compat = U_compat - C_compat - R_compat - Q_compat
```

where `U_math` is the ontology-grounded universe of mathematical API,
constructor/construction, and codomain-owned construction rows; `C_math` is classified
with weakest owner, minimal structure, hypotheses, codomain, and project category
surface; `R_math` is rejected from the mathematical API; and `Q_math` requires a
recorded mathematical, source, or workflow decision.

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

The first question is never "where does Sage expose this name?" The first question is
"what mathematical operation or construction is this, in what standard categorical
language is it defined, and what is the weakest structure that makes it meaningful?"
Sage source may prove that a particular implementation exposes a name; it does not
determine the mathematical owner.

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
| Active scope | Category-spec mathematical operations, constructors, constructions, and Sage evidence rows for the supporting semantic families below. |
| Included category families | Sets, topological spaces, rings, ideals through ring/module ownership, algebras, modules, Hom/End/Aut, forms, lattices, tensor algebra components, posets, and geometry-facing source rows when they block the category-spec phase. |
| Sage source roots included in this ledger | Not populated. |
| Source roots not yet inspected into this ledger | Not populated. |

## Mathematical Ontology Gate

Before any Sage source row is admitted into `U_math`, the active scope must have a short
theory sheet that names the mathematical objects, operations, and minimal structures
being modeled. A Sage method, constructor, helper, display hook, backend route, or
package export can enter the primary frontier only by mapping to one of those
mathematical slots.

The theory sheet controls the primary universe:

```text
theory object + operation + weakest structure
  -> ontologyOperation
  -> U_math row
  -> Sage source evidence
  -> classified / rejected / decision-needed
```

If a Sage name has no coherent `ontologyOperation`, it is compatibility audit,
out-of-scope evidence, or a missing mathematical decision. It is not a mathematical
frontier row merely because it appears near the subtree in Sage.

## Active Lattice Frontier

The active worker task underneath the current process repair is
`category_specs/lattices` Sage-surface inventory and mapping completion. Its next
substantive artifact is an ontology-generated finite mathematical universe, not another
handoff, memory, review note, local mapping-row patch, or Sage-symbol scrape.

### Active Lattice Theory Sheet Stub

This stub is not a completion claim. It is the required controlling vocabulary that
must be populated before Sage source names drive the work.

Objects:

- category, concrete category, preadditive category, additive category, abelian or exact
  category, and `R`-linear category
- module category, quotient module, finite free module, finite free module with chosen
  basis or presentation
- formed module, nondegenerate formed module, integral lattice, rational lattice
- torsion module, discriminant group, torsion quadratic or bilinear module
- Hom, End, and Aut objects and their element surfaces

Operation strata:

- categorical: domain, codomain, identity, composition, isomorphism
- concrete-category: evaluation of a morphism on an element
- preadditive/additive: zero morphism, addition of morphisms, abelian-group Hom object,
  bilinearity of composition
- abelian/exact: kernel, cokernel, image, coimage, exactness, monomorphism and
  epimorphism tests through kernels and cokernels
- `R`-linear/module: scalar action, submodule, quotient, tensor product, dual
  `Hom_R(M,R)`, and `R`-linear Hom structure
- finite-free-with-basis/presentation: matrix representative, coordinates, rank,
  determinant, presentation-dependent lift
- formed-module/lattice: form evaluation, Gram matrix, discriminant, dual lattice,
  signature, orthogonal direct-sum and subobject constructions
- torsion/discriminant quadratic: finite quotient form, descended bilinear or quadratic
  form, Brown invariant, genus predicates

Every primary lattice row must name one `ontologyOperation` from this sheet or record a
decision-needed gap in the sheet itself. For example, composition/evaluation cannot be
owned by a free-module morphism row merely because Sage implements them on an inherited
matrix morphism class; module or free-module structure begins only where the row needs
additive, scalar, matrix, kernel/image, presentation, or basis hypotheses.

After the theory sheet exists, the lattice universe must enumerate Sage category
providers, constructors/factories, classes reached through those constructors, parent
and element methods, construction routes, Hom/End/Aut surfaces, and relevant source
surfaces already admitted by the lattice evidence files. The universe must then assign
each row to exactly one lane:

- `mathematical-api`
- `constructor-construction`
- `codomain-owned-construction`
- `compatibility-runtime-display-backend`
- `out-of-scope-sage`

Only the first three lanes form the primary lattice frontier:

```text
Remaining_lattices_math =
  U_lattices_math - C_lattices_math - R_lattices_math - Q_lattices_math
```

Compatibility/runtime/display/private/test-helper/package-export/backend rows form a
separate low-priority audit frontier unless `blocksImplementation` is `yes`.

The word "touches" is not a scope rule. A Sage surface enters the primary lattice
frontier only when it is a mathematical operation, constructor/construction route, or
codomain-owned construction needed by the lattice/category foundation. Package imports,
random/test helpers, display hooks, backend options, deprecated aliases, and source
implementation branches enter the compatibility lane unless they block named
implementation or spec migration work.

## Primary Frontier Sets

Status values are closed. Do not add `pending`, `deferred`, `partial`,
`current-state`, or `best-effort`.

| Set | Row condition | Count |
| --- | --- | --- |
| `U_math` | Ontology-grounded row exists in this ledger, with Sage evidence attached when a Sage surface realizes it, and lane is `mathematical-api`, `constructor-construction`, or `codomain-owned-construction`. | Not populated. |
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
| `ontologyOperation` | Standard mathematical operation or construction from the active theory sheet, or `none` for compatibility/out-of-scope rows. |
| `minimalStructure` | Weakest category, object structure, chosen representation, or hypothesis that makes `ontologyOperation` meaningful. |
| `mathematicalSentence` | Complete sentence stating why the operation exists without referring to Sage. |
| `sageSourceRoot` | Sage module, class, package export, written doc, or local source file used as implementation evidence or compatibility/out-of-scope evidence for the row. |
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
primary mathematical universe from the active theory sheet before any mathematical
classification or mapping progress claim is made. For the current lattice task, that
means populating `U_lattices_math` before claiming progress on
`SPEC-MAPPING-LATTICES`.

| frontierId | family | ontologyOperation | minimalStructure | mathematicalSentence | sageSourceRoot | lane | sourceSurfaceKind | constructorOrClass | methodOrFunction | objectLevel | status | projectOwner | hypotheses | codomainOrReturn | evidence | blocksImplementation | decisionOrBlocker | lastMovedBy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Last Commit Movement

Every substantive inventory or mapping commit must add one row here or update the
corresponding row in a replacement structured artifact named by this spec. Only primary
frontier movement is mathematical progress.

| Commit | Rows moved from `Remaining_math` to `C_math` | Rows moved from `Remaining_math` to `R_math` | Rows moved from `Remaining_math` to `Q_math` | Compatibility rows moved | Source files used |
| --- | --- | --- | --- | --- | --- |
