---
id: SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY]]'
title: Maintain Sage constructor and method operation map
status: in-progress
priority: critical
complexity: 75
requirement: Maintain the source-backed mathematical operation map for category-spec
  scope. Each admitted row translates Sage behavior into a mathematical operation under
  hypotheses, the weakest category or refinement claimed, witness data, return object,
  and source evidence.
acceptanceCriteria:
- The file records the active scope, included category families, included Sage source
  roots, and source roots not yet inspected.
- Every mathematical row records the Sage method body/docs/examples read, the
  mathematical behavior extracted from them, the hypotheses, weakest category or
  refinement, required witnesses, return object, and source evidence.
- Rows without a mathematical operation are recorded only as nonmathematical
  implementation residue or unresolved mathematical questions.
- Progress claims cite rows whose mathematical assertion was added, corrected, rejected
  as residue, or left as an unresolved mathematical question. Row movement, row counts,
  lane status, and handoff edits are not progress evidence.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Sage Constructor and Method Operation Map

## Object Preserved

This spec preserves the source-backed mathematical operation map for category-spec
inventory and mapping. The map is the mathematical object. A row is complete only when
it states the Sage behavior, the mathematical operation under hypotheses, the weakest
category or refinement claimed, the required witnesses, the return object or codomain,
and the source evidence.

```text
Sage body/docs/examples
  -> mathematical operation O on objects satisfying hypotheses H
  -> weakest owner category C and any refinement membership claimed
  -> witness data or proof obligations required by C
  -> codomain or return object
  -> source evidence
```

Any set-difference notation, lane count, row status, or compatibility audit is a local
navigation aid only. It is not a second mathematical object and cannot be cited as
progress by itself.

The false substitute this blocks is reporting row counts, file counts, review prose,
handoff updates, broad checkpoints, compatibility cleanups, or current-state summaries
as mathematical progress.

## Control Invariant

A category-spec Sage inventory or mapping session reports mathematical progress only
when it adds, corrects, rejects, or records a source-backed mathematical assertion:

```text
method or constructor m implements operation O on objects satisfying H,
belongs to owner category or refinement C, and requires witnesses W.
```

The first question is neither "where does Sage expose this name?" nor "which abstract
category-theory words might apply?" The first question is "what behavior do the Sage
method body, examples, and docs actually implement?" Only after that extraction may the
row introduce the mathematical vocabulary, weakest structure, hypotheses, category
membership, refinement membership, and witness requirements.

Compatibility, runtime, display, private, test-helper, package-export, and backend
plumbing surfaces are not part of the spec unless they change the mathematical
interface or block construction of a required spec object. Otherwise record a one-line
residue classification if useful and move on.

Mapping documents, subtree `SAGE_INVENTORY.md` files, task cards, decisions, and
handoffs remain evidence and routing surfaces. They are not completion evidence unless
they change the operation map itself.

## Scope

Only the constructor/factory batch below has been enumerated into this operation map.
Unknown counts outside that batch are not zero.

| Field | Value |
| --- | --- |
| Active scope | Category-spec mathematical operations, constructors, constructions, and Sage evidence rows for the supporting semantic families below. |
| Included category families | Sets, topological spaces, rings, ideals through ring/module ownership, algebras, modules, Hom/End/Aut, forms, lattices, tensor algebra components, posets, and geometry-facing source rows when they block the category-spec phase. |
| Sage source roots included in this map | `sage/modules/free_quadratic_module.py` free-bilinear and field-quadratic factories; `sage/modules/free_quadratic_module_integer_symmetric.py` integral-lattice constructor cluster; `sage/modules/torsion_quadratic_module.py` torsion quadratic constructors; and the local `category_specs/lattices/__init__.py` constructor collector wrapper. |
| Source roots not yet inspected into this map | Every source root outside the admitted constructor/factory rows in this batch; no non-constructor lattice methods or other category families are populated by this edit. |

## Semantic Extraction Gate

Before any Sage source row is admitted into the operation map, the active scope must
record what the method cluster actually does. A Sage method, constructor, helper,
display hook, backend route, or package export enters the map only after its behavior
has been extracted from source body, examples, or written docs deeply enough to state
the mathematical operation it implements or to classify it as residue.

The extraction step controls the row:

```text
Sage method body/docs/examples
  -> sageBehavior
  -> mathematicalOperation
  -> requiredVocabulary
  -> hypotheses
  -> weakest category/refinement owner
  -> witnesses/proof obligations
  -> source-backed row, residue classification, or unresolved question
```

If a Sage name has no coherent `mathematicalOperation` after semantic extraction, it is
nonmathematical implementation residue, out-of-scope evidence, or an unresolved
mathematical decision. It is not a mathematical row merely because it appears near the
subtree in Sage.

## Active Lattice Operation Map

The active worker task underneath the current process repair is
`category_specs/lattices` Sage-surface inventory and mapping completion. Its next
substantive artifact is a source-backed mathematical operation map, not another
handoff, memory, review note, local mapping-row patch, Sage-symbol scrape, or a priori
category primer.

### Active Lattice Extraction Questions

This is not a completion claim. It is the required extraction checklist for each Sage
method cluster before owner placement.

For each method cluster, record:

- what inputs, outputs, examples, coercions, and branch cases the Sage body/docs expose
- whether the behavior is a morphism operation, object operation, constructor,
  construction route, representation/presentation datum, algorithmic invariant,
  coercion, display/runtime helper, test helper, or backend choice
- whether the behavior is functorial or depends on a chosen representative,
  presentation, side convention, basis, matrix action, backend algorithm, or display
  convention
- which vocabulary the behavior forces: category, concrete category, Hom/End/Aut,
  preadditive/additive or `R`-linear Hom structure, kernels/cokernels/images/coimages,
  finite generation, finite presentation, finite rank, basis/presentation data,
  bilinear or quadratic form, nondegeneracy, integrality, torsion, quotient
  presentation, discriminant form, or backend/algorithm choice
- what weakest structure and hypotheses make the extracted operation meaningful

The BinaryQF and FreeModuleMorphism cases are the diagnostic examples for the workflow.
A compressed Sage row must split when source behavior splits. Evaluation of a binary
quadratic form at a two-coordinate input, coefficientwise additive operations, Gauss
composition, and left/right matrix actions are different mathematical surfaces.
Likewise, categorical morphism composition/evaluation, additive or exact Hom behavior,
finite-free matrix representation, side-dependent matrix conventions, and
endomorphism-specific spectral algebra cannot be collapsed into one free-module owner
label.

After semantic extraction, the lattice operation map must cover the relevant Sage
category providers, constructors/factories, classes reached through those constructors,
parent and element methods, construction routes, Hom/End/Aut surfaces, and source
surfaces already admitted by the lattice evidence files. Each row must be one of:

- a source-backed mathematical assertion;
- nonmathematical implementation residue;
- an unresolved mathematical question;
- out-of-scope evidence.

The word "touches" is not a scope rule. A Sage surface enters the mathematical operation
map only when it is a mathematical operation, constructor/construction route,
codomain-owned construction, or unresolved mathematical question needed by the
lattice/category foundation. Package imports, random/test helpers, display hooks,
backend options, deprecated aliases, and source implementation branches are discarded
after one-line residue classification unless they change the public mathematical
interface or block construction of a required object.

## Required Row Fields

Each row must contain these fields. A future implementation may store them as a
markdown table, CSV, or generated view, but this tracked spec remains the canonical
location or must point to exactly one replacement artifact.

| Field | Required meaning |
| --- | --- |
| `rowId` | Stable identifier for the Sage surface row. |
| `family` | Supporting family such as `sets`, `rings`, `modules`, `lattices`, or `posets`. |
| `sageSurface` | Constructor, class, parent, element, Hom object, protocol, function, or export spelling. |
| `sageBehavior` | Summary of the behavior actually observed in the Sage body, examples, or written docs: inputs, outputs, branch cases, side effects, and conventions relevant to classification. |
| `mathematicalOperation` | Standard mathematical operation or construction extracted from `sageBehavior`, or `none` for residue/out-of-scope rows. |
| `requiredVocabulary` | Mathematical vocabulary introduced or referenced because `sageBehavior` requires it. |
| `mathematicalSentence` | Complete sentence stating why the operation exists without referring to Sage. |
| `hypotheses` | Mathematical or source hypotheses needed for the operation, owner, and codomain. |
| `ownerCategoryOrRefinement` | Weakest project category, construction owner, or refinement membership claimed. |
| `witnessDataOrProof` | Required witnesses, construction data, proof obligation, or `none` for residue/out-of-scope rows. |
| `codomainOrReturn` | Return object, codomain, or payload class. |
| `sourceEvidence` | Source path plus section, line, signature, or stable source citation. |
| `disposition` | `mathematical-assertion`, `nonmathematical-residue`, `unresolved-question`, or `out-of-scope`. |

## Canonical Operation Rows

The rows currently admitted here are the constructor/factory cluster already visible in
the lattice evidence files: the free bilinear factory route, the field quadratic-space
wrapper route, the three admitted integral-lattice constructors named by the
`constructorNameInventories` lattice collector, and the two torsion quadratic
constructor routes. This is not a completion claim for non-constructor lattice methods
or other category families.

| rowId | family | sageSurface | sageBehavior | mathematicalOperation | hypotheses | ownerCategoryOrRefinement | witnessDataOrProof | codomainOrReturn | sourceEvidence | disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `forms.constructor.free-quadratic-module` | `forms` | `FreeQuadraticModule` | Coerces rank, canonicalizes an `n x n` inner-product matrix over a commutative base ring, caches by presentation data, and dispatches to field, PID, integral-domain, or generic backends. The form matrix is not required to be symmetric, nondegenerate, integral, or definite. | Finite-rank free module over a commutative ring equipped with a bilinear form matrix. | `base_ring` is commutative; `rank` is a nonnegative integer; the matrix coerces to an `n x n` matrix over `base_ring`; `inner_product_ring` is not supplied. | `Modules(R).Free().FiniteRank().WithForms().Bilinear().Constructors().FreeQuadraticModule`; lattice membership requires additional symmetric, integral, nondegenerate, finite-rank free witnesses. | Chosen finite free presentation and bilinear form matrix. | Free bilinear module over `R`. | Sage source `sage/modules/free_quadratic_module.py:86-187`; official Sage docs `free_quadratic_module.html`; mapping row `SPEC-MAPPING-LATTICES:196`; inventory row `category_specs/lattices/docs/SAGE_INVENTORY.md:15`. | `mathematical-assertion` |
| `forms.constructor.quadratic-space` | `forms` | `QuadraticSpace` / `InnerProductSpace` | Checks that `K` is a field and `sparse` is boolean, then delegates to `FreeQuadraticModule(K, rank=dimension, inner_product_matrix=..., sparse=sparse)`. | Field-valued finite-dimensional free bilinear module, i.e. a quadratic space in Sage's naming. | `K` is a field; `dimension` is a nonnegative integer; the matrix coerces to a `dimension x dimension` matrix over `K`; `sparse` is storage data. | `Modules(K).Free().FiniteRank().WithForms().Bilinear().OverField().Constructors().QuadraticSpace`; not `Lattices(R)` without an integral presentation and lattice witnesses. | Chosen finite-dimensional free presentation over `K` and bilinear form matrix. | Field-valued free bilinear module. | Sage source `sage/modules/free_quadratic_module.py:190-223`; official Sage docs `free_quadratic_module.html`; mapping row `SPEC-MAPPING-LATTICES:197`; inventory rows `category_specs/lattices/docs/SAGE_INVENTORY.md:16-17`. | `mathematical-assertion` |
| `lattices.constructor.integral-lattice` | `lattices` | `IntegralLattice` | Accepts a symmetric rational matrix, integer rank identity form, Cartan/root descriptor, or `"U"`/`"H"`; optional basis data presents a generated sublattice in the ambient quadratic space. | Integral lattice construction from a finite Gram, Euclidean-rank, root-system, or hyperbolic-plane presentation with optional selected basis. | Descriptor is a symmetric matrix, integer rank, Cartan/root descriptor, or `"U"`/`"H"`; the effective Gram presentation is symmetric, integral, and nondegenerate over `ZZ`; optional basis rows or module elements belong to the ambient quadratic space. | `Lattices(ZZ).Constructors().IntegralLattice`. | Finite-rank free abelian presentation, nondegenerate symmetric integral bilinear form, and optional selected generator data. | `Lattice`. | Sage source `sage/modules/free_quadratic_module_integer_symmetric.py:73-259,625-669`; local wrapper `category_specs/lattices/__init__.py:105-174`; mapping row `SPEC-MAPPING-LATTICES:204`. | `mathematical-assertion` |
| `lattices.constructor.integral-lattice-direct-sum` | `lattices` | `IntegralLatticeDirectSum` | Verifies inputs are Sage integral lattices, forms a block-diagonal ambient form, block-embeds selected bases, and optionally returns homomorphisms from each summand into the block presentation. | Orthogonal direct sum of a finite family of integral lattices with canonical summand inclusions. | Inputs are a finite list of integral lattices over `ZZ`; `return_embeddings` selects the structure-map payload. | `Lattices(ZZ).OrthogonalDirectSums()` via `Lattices(ZZ).Constructors().IntegralLatticeDirectSum`. | Finite family of integral lattices, block-diagonal form, selected basis presentation, and optional canonical summand inclusions. | `Lattice` or `(Lattice, Sequence[LatticeMorphism])`. | Sage source `sage/modules/free_quadratic_module_integer_symmetric.py:262-369`; local wrapper `category_specs/lattices/__init__.py:188-237`; mapping row `SPEC-MAPPING-LATTICES:205`. | `mathematical-assertion` |
| `lattices.constructor.integral-lattice-gluing` | `lattices` | `IntegralLatticeGluing` | Forms the orthogonal direct sum with embeddings, coerces glue components through discriminant groups, adjoins rational lifts, and optionally recomputes summand embeddings into the glued lattice. | Gluing or overlattice construction from discriminant-group glue data on a finite family of integral lattices. | Inputs are a finite list of integral lattices over `ZZ`; every glue row has one component per lattice; each component coerces into the corresponding discriminant group; `return_embeddings` selects the structure-map payload. | `Lattices(ZZ).Overlattices()` via `Lattices(ZZ).Constructors().IntegralLatticeGluing`. | Orthogonal direct sum, discriminant-group elements, rational lifts, overlattice generators, and optional summand embeddings. | `Lattice` or `(Lattice, Sequence[LatticeMorphism])`. | Sage source `sage/modules/free_quadratic_module_integer_symmetric.py:372-616`; local wrapper `category_specs/lattices/__init__.py:240-271`; mapping row `SPEC-MAPPING-LATTICES:206`. | `mathematical-assertion` |
| `forms.constructor.torsion-quadratic-form` | `forms` | `TorsionQuadraticForm` | Coerces a square symmetric rational matrix, clears denominators, uses Smith form, builds a free quadratic `ZZ` cover, forms denominator relations, and returns a torsion quadratic module. | Finite torsion quadratic module constructed from symmetric rational Gram data. | `q` is a square symmetric rational matrix; quotient codomain is `QQ/ZZ` or `QQ/2ZZ`; no lattice input is present. | `Modules(ZZ).WithForms().Quadratic().Torsion().Constructors().TorsionQuadraticForm`; lattice discriminant-group ownership requires explicit metric-dual descent. | Symmetric rational Gram presentation and Smith-denominator quotient data. | `TorsionQuadraticModule`. | Sage source `sage/modules/torsion_quadratic_module.py:35-87`; official Sage docs `torsion_quadratic_module.html`; mapping row `SPEC-MAPPING-LATTICES:208`; inventory row `category_specs/lattices/docs/SAGE_INVENTORY.md:559`. | `mathematical-assertion` |
| `forms.constructor.torsion-quadratic-module` | `forms` | `TorsionQuadraticModule` | Constructs the finite quotient `V/W` where `V` is a symmetric free quadratic module over `ZZ` and `W` is a same-rank submodule; checking enforces equal rank, `ZZ` base, symmetric cover form, and generator data. | Finite torsion formed-module quotient construction with bilinear and quadratic quotient-valued forms. | `V` is a symmetric free quadratic module over `ZZ`; `W <= V` has the same rank; optional `gens` generate `V/W`; codomain moduli satisfy the required divisibility conditions. | `Modules(ZZ).WithForms().Quadratic().Torsion().Constructors().from_quotient`, with `Lattices(ZZ).DiscriminantGroups()` only for the specialization `coker(L -> L^#)` with descended lattice form. | Same-rank quotient presentation, selected quotient generators when supplied, and quotient-valued bilinear/quadratic form codomains. | `TorsionQuadraticModule`. | Sage source `sage/modules/torsion_quadratic_module.py:188-277`; official Sage docs `torsion_quadratic_module.html`; mapping rows `SPEC-MAPPING-LATTICES:209-210`; inventory rows `category_specs/lattices/docs/SAGE_INVENTORY.md:561-570`. | `mathematical-assertion` |

## Source Evidence Commits

Every substantive inventory or mapping commit must add or correct a source-backed row
here or in exactly one replacement structured artifact named by this spec. The commit
record is provenance for the mathematical assertions, not a second progress ledger.

| Commit | Operation rows added or corrected | Source files used |
| --- | --- | --- |
| `325d8915` | `forms.constructor.free-quadratic-module`; `forms.constructor.quadratic-space`; `forms.constructor.torsion-quadratic-form`; `forms.constructor.torsion-quadratic-module` | `sage/modules/free_quadratic_module.py`; `sage/modules/torsion_quadratic_module.py`; official Sage docs; `category_specs/lattices/docs/SAGE_INVENTORY.md`; `SPEC-MAPPING-LATTICES.md` |
| `a24824cd` | `lattices.constructor.integral-lattice`; `lattices.constructor.integral-lattice-direct-sum`; `lattices.constructor.integral-lattice-gluing` | `sage/modules/free_quadratic_module_integer_symmetric.py`; `category_specs/lattices/__init__.py`; `category_specs/lattices/docs/SAGE_INVENTORY.md`; `SPEC-MAPPING-LATTICES.md` |
