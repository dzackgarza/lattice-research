# Needs Decisions

These are design blockers, not mechanical audit findings. Mechanical compliance issues
should be fixed in code; only items that require a human design choice belong here.

## Homset Root Boilerplate

`Homsets`, `Endsets`, and `Autsets` behave as root construction categories, but the
top-level rules require every top-level category to expose `SubcategoryMethods` and
`Constructors`. Decide whether these root homset categories must implement the full
boilerplate or receive a documented structural exception.

## Cat Object Hom/End/Aut Notation

`cat/docs/MAPPING.md` describes `A.Hom(B)`, `A.End()`, and `A.Aut()` for category
objects as object-level parents in `Cat()`, while the current Cat-backed wrapper layer
uses zero-argument `Hom`, `End`, and `Aut` as aliases for category-level
`Homsets`, `Endsets`, and `Autsets`. Decide whether the project reserves these names
for object-level Cat homsets, category-level construction categories, or a closed
arity split where only `Hom(codomain)` is object-level.

## Sage Construction Re-Exports

Several construction subcategories inherit raw Sage construction bases directly
(`SubobjectsCategory`, `QuotientsCategory`, `CartesianProductsCategory`,
`RegressiveCovariantConstructionCategory`, and related bases). Decide whether these
must be re-exported through `cat/base_category_types.py` before construction files are
considered compliant.

## Sage Collection Signatures

The static type audit still finds many `list[...]`, `tuple[...]`, `dict[...]`, and
`set[...]` signatures in method surfaces, especially for Sage methods named `list`,
`tuple`, `gens`, `signature`, `basis`, `automorphisms`, and result pairs such as
`galois_closure`. Decide whether specs should preserve Sage-exact collection shapes, or
whether these must be redesigned to mathematical Sage objects such as families, ordered
sets, condition sets, generators, or dedicated result parents before they are compliant.

## Explicit Surface Inventory Completeness

Many subcategory classes define only the methods they refine locally. The local policy
requires each subcategory to explicitly map inherited `ParentMethods`, `ElementMethods`,
`MorphismMethods`, and `SubcategoryMethods` surfaces, including inherited methods with
`...` bodies. Decide whether empty surface classes are an acceptable incremental state,
or whether each subtree must first receive a Sage-doc-backed full inherited method
inventory before further smoke validation.

## Lattices Top-Level Status

`lattices/` has subcategory specs and docs, but lacks the normal top-level subtree
surface (`AGENTS.md`, `__init__.py`, `homsets.py`, `docs/TRIAGE.md`, construction
subcategories, and smoketest). Decide whether `lattices/` is admitted now as a full
top-level category subtree, or whether it remains a staged spec fragment pending a
separate admission pass.

## Lattice Type Anchors

`types.py` currently anchors `Lattice`, `DiscriminantGroup`, and `OrthogonalGroup` to
generic Sage parents/groups. Decide whether those are acceptable temporary anchors or
whether dedicated project category surfaces must exist before lattice signatures can be
considered complete.

## Matrix Algebra Ownership

`rings/matrix_algebras.py` still declares matrix-algebra surface in the rings subtree,
while the algebra docs say algebra-specific surface should live under `Algebras(R)`.
Decide the final ownership split across `rings`, `modules`, and `algebras`.

## Topological Constructors And Inheritance

Topological-space constructors are not admitted yet, and the inheritance path for
topological rings, modules, and algebras is still undecided. Decide the constructor
inventory and whether topological structure is inherited directly from
`TopologicalSpaces()` or through set/ring/module-specific refinements.

## Poset Constructor Inventory

The poset subtree now has construction-category skeletons, but concrete Sage poset
constructor inventory is still deferred. Decide which Sage poset constructors belong in
`Posets().Constructors()` before smoke validation can be meaningful.
