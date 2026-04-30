# Needs Decisions

These are design blockers, not mechanical audit findings. Mechanical compliance issues
should be fixed in code; only items that require a human design choice belong here.

## Sage Construction Re-Exports

Several construction subcategories inherit raw Sage construction bases directly
(`SubobjectsCategory`, `QuotientsCategory`, `CartesianProductsCategory`,
`RegressiveCovariantConstructionCategory`, and related bases). Decide whether these
must be re-exported through `cat/base_category_types.py` before construction files are
considered compliant.

## Collection Signature Ambiguities

Typed finite collection signatures are not themselves design blockers. Shapes such as
`galois_closure() -> Field | tuple[Field, RingMorphism]`,
`list[RingMorphism]`, `tuple[RingElement, ...]`, and
`dict[RingElement, Integer]` are compliant when they transparently state finite
mathematical data. The remaining collection-signature questions are narrower:

- `sets/subcategories/condition.py` has `arguments() -> tuple` and
  `predicates() -> tuple`, with `predicates()` currently returning `arguments()`.
  The set inventory says Sage `ConditionSet.arguments()` exposes the ambient set plus
  predicate/symbolic argument data, while the project constructor takes
  `predicates: Sequence[Callable[[SetElement], bool]]`. Decide whether the project
  surface should split `predicates()` from the raw Sage `arguments()` surface, typed as
  `tuple[Callable[[SetElement], bool], ...]`; and if `arguments()` remains public,
  decide what exact typed product it returns.
- `rings/subcategories/p_adic_ring.py` declares
  `change(..., print_alphabet: dict[str, str] | None = None, ...)`. This is display
  configuration, not finite mathematical data. Decide whether display-only Sage
  options belong in this spec surface, and if they do, whether this argument needs a
  named Sage/project display type or an explicit mapping as localized non-mathematical
  Sage interop.

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

## Algebra Constructor Inventory

`Algebras(R).Constructors()` currently has no admitted concrete constructor entries.
Decide the first Sage-backed algebra constructors to admit before algebra smoke
validation can be meaningful.

## Finitely Presented Module Wiring

`FinitelyPresentedModulesOverPID` must be wired without recursive
`FinitelyPresented().OverPID()` registration. Decide the category path and constructor
ownership before the module constructor surface is considered complete.

## Topological Constructor Inventory

The inheritance path is decided in the mapping docs: topological rings, modules, and
algebras inherit their topological-space surface from `topological_spaces` and their
algebraic surface from their own subtree. The remaining user decision is the
constructor inventory: which Sage topological-space constructor families should be
admitted first, and which named `Constructors()` paths should expose them.

## Poset Constructor Inventory

The poset subtree now has construction-category skeletons, but concrete Sage poset
constructor inventory is still deferred. Decide which Sage poset constructors belong in
`Posets().Constructors()` before smoke validation can be meaningful.
