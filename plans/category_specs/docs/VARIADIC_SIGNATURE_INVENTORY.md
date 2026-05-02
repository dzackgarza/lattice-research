# Variadic Signature Inventory

This inventory records the remaining category-spec surfaces that still look
variadic, or that still collapse Sage's finite constructor casework into one
placeholder signature. It is the input for the follow-up scoping pass; it does not
split or rewrite the specs.

Ordinary typed finite collections are not listed merely because they use
`Sequence`, `tuple`, `list`, or `dict`. The audit only records collection
parameters when they stand in for multiple Sage input shapes or raw coordinate
interop that still needs explicit overload review.

## Project Spec Surfaces To Scope

- File: `modules/__init__.py:576`
  Symbol: `Modules(R).Constructors().FreeModule`
  Current signature: `rank_or_basis_keys: Integer | Set | SetFamily | None`,
  `inner_product_matrix: Matrix | Sequence[Sequence[RingElement]] |
  Sequence[RingElement] | None`, plus keyword `rank` and `basis_keys`.
  Why variadic-style: the first parameter still merges rank construction and
  basis-key construction, while the form data accepts matrix and list shapes in
  one slot.
  Source surface to scope next: `modules/docs/SAGE_INVENTORY.md` records
  `FreeModule(R, rank_or_basis_keys, ...)` and its dispatch to ordinary free
  modules, finite-rank free modules, combinatorial free modules, and quadratic
  modules.

- File: `modules/__init__.py:609`
  Symbol: `Modules(R).Constructors().VectorSpace`
  Current signature: `dimension_or_basis_keys: Integer | Set | SetFamily |
  None`, `inner_product_matrix: Matrix | Sequence[Sequence[RingElement]] |
  Sequence[RingElement] | None`, plus keyword `dimension` and `basis_keys`.
  Why variadic-style: this repeats the free-module merged rank/basis-key path
  under field-only vocabulary.
  Source surface to scope next: `modules/docs/SAGE_INVENTORY.md` records
  `VectorSpace(K, dimension_or_basis_keys, ...)` as a field-checking wrapper
  around `FreeModule`.

- File: `modules/__init__.py:633`
  Symbol: `Modules(R).Constructors().FreeQuadraticModule`
  Current signature: `inner_product_matrix: Matrix |
  Sequence[Sequence[RingElement]] | Sequence[RingElement]`.
  Why variadic-style: the form input still accepts several coordinate shapes in
  one parameter instead of named matrix/vector cases.
  Source surface to scope next: `modules/docs/SAGE_INVENTORY.md` records
  `FreeQuadraticModule(R, rank, inner_product_matrix, ...)`.

- File: `modules/__init__.py:723`
  Symbol: `Modules(R).Constructors().FPModule`
  Current signature: `arg0: Algebra | RModule | RModMorphism`,
  `generator_degrees`, `relations`, and `names`.
  Why variadic-style: `arg0` merges the cokernel-of-map construction with the
  algebra-plus-generators presentation construction.
  Source surface to scope next: `modules/docs/SAGE_INVENTORY.md` records
  `FPModule(arg0, generator_degrees=None, relations=(), ...)`.

- File: `modules/__init__.py:754`
  Symbol: `Modules(R).Constructors().IntegerLattice`
  Current signature: `basis: Matrix | Sequence[Sequence[RingElement]]`.
  Why variadic-style: this admits both matrix and nested-list coordinate data in
  the same constructor parameter.
  Source surface to scope next: `modules/docs/SAGE_INVENTORY.md` records
  `IntegerLattice(basis, lll_reduce=True)`.

- File: `modules/__init__.py:765`
  Symbol: `Modules(R).Constructors().TorsionQuadraticForm`
  Current signature: `q: Matrix | Sequence[Sequence[RingElement]]`.
  Why variadic-style: this admits both matrix and nested-list data in one
  constructor parameter.
  Source surface to scope next: `modules/docs/SAGE_INVENTORY.md` records
  `TorsionQuadraticForm(q)`.

- File: `modules/__init__.py:809`
  Symbol: `Modules(R).Constructors().polynomial_ring_as_module`
  Current signature: overload and implementation paths allow
  `n: Integer | tuple[Integer, ...] | None` with
  `var_array: str | Sequence[str] | None`.
  Why variadic-style: the module bridge admits the higher-dimensional
  `var_array` tuple shape even though `rings/docs/MAPPING.md` says that Sage's
  unbounded positional `PolynomialRing(R, 2, 3, 4, var_array=...)` shape is not
  admitted yet.
  Source surface to scope next: `rings/docs/MAPPING.md` and the Sage
  `PolynomialRing` factory casework.

- File: `modules/__init__.py:856`
  Symbol: `Modules(R).Constructors().power_series_ring_as_module`
  Current signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why variadic-style: `arg2` is Sage positional plumbing rather than
  mathematical vocabulary.
  Source surface to scope next: the `PowerSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and the Sage series-ring factory docs/source.

- File: `modules/__init__.py:883`
  Symbol: `Modules(R).Constructors().laurent_series_ring_as_module`
  Current signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why variadic-style: this repeats the unsplit series-ring constructor shape
  while routing the result through module refinement.
  Source surface to scope next: the `LaurentSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and the Sage series-ring factory docs/source.

- File: `modules/__init__.py:910`
  Symbol: `Modules(R).Constructors().puiseux_series_ring_as_module`
  Current signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why variadic-style: this repeats the unsplit series-ring constructor shape
  while routing the result through module refinement.
  Source surface to scope next: the `PuiseuxSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and the Sage series-ring factory docs/source.

- File: `modules/subcategories/constructions/quotients.py:68`
  Symbol: `Modules(R).Quotients().ParentMethods.quotient_module`
  Current signature: `submodule: RModule | Matrix | Sequence[RModuleElement] |
  Sequence[Sequence[RingElement]]`.
  Why variadic-style: the quotient method accepts an existing submodule,
  generator data, matrix data, and nested coordinate data in one parameter.
  Source surface to scope next: `modules/docs/SAGE_INVENTORY.md` records
  quotient modules, `FGP_Module`, and quotient syntax on free modules.

- File: `rings/__init__.py:673`
  Symbol: `Rings().Constructors().NumberField`
  Current signature: `polynomial: Polynomial | Sequence[Polynomial]`, with
  sequence-capable `name`, `names`, `embedding`, `latex_name`, `structure`, and
  `latex_names`.
  Why variadic-style: one constructor still merges simple number fields,
  relative/tower input, and paired sequence metadata.
  Source surface to scope next: `rings/docs/SAGE_INVENTORY.md` records the
  `NumberField`, `QuadraticField`, and `CyclotomicField` constructor family.

- File: `rings/__init__.py:736`
  Symbol: `Rings().Constructors().Zp`
  Current signature: `prec: Integer | tuple[Integer, Integer] | None` plus
  precision-type and print-mode options.
  Why variadic-style: the precision parameter accepts a scalar and a two-entry
  tuple shape without a named distinction.
  Source surface to scope next: the `Zp` p-adic constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage p-adic factory docs/source.

- File: `rings/__init__.py:774`
  Symbol: `Rings().Constructors().Qp`
  Current signature: `prec: Integer | tuple[Integer, Integer] | None` plus
  precision-type and print-mode options.
  Why variadic-style: this repeats the unsplit p-adic precision shape for
  fields.
  Source surface to scope next: the `Qp` p-adic constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage p-adic factory docs/source.

- File: `rings/__init__.py:812`
  Symbol: `Rings().Constructors().Zq`
  Current signature: `q: Integer | tuple[Integer, Integer] |
  Sequence[tuple[Integer, Integer]]`, `prec: Integer | tuple[Integer, Integer] |
  None`, plus p-adic options.
  Why variadic-style: this merges cardinality, prime-power tuple, and sequence
  data in one `q` parameter, and repeats the unsplit precision tuple shape.
  Source surface to scope next: the `Zq` p-adic extension constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage p-adic factory docs/source.

- File: `rings/__init__.py:856`
  Symbol: `Rings().Constructors().Qq`
  Current signature: `q: Integer | tuple[Integer, Integer] |
  Sequence[tuple[Integer, Integer]]`, `prec: Integer | tuple[Integer, Integer] |
  None`, plus p-adic options.
  Why variadic-style: this repeats the unsplit p-adic extension and precision
  tuple shapes for fields.
  Source surface to scope next: the `Qq` p-adic extension constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage p-adic factory docs/source.

- File: `rings/__init__.py:1046`
  Symbol: `Rings().Constructors().PowerSeriesRing`
  Current signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why variadic-style: `arg2` is positional Sage factory plumbing and should be
  replaced by named closed overload cases.
  Source surface to scope next: the `PowerSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage series-ring factory docs/source.

- File: `rings/__init__.py:1074`
  Symbol: `Rings().Constructors().LaurentSeriesRing`
  Current signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why variadic-style: `arg2` is positional Sage factory plumbing and should be
  replaced by named closed overload cases.
  Source surface to scope next: the `LaurentSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage series-ring factory docs/source.

- File: `rings/__init__.py:1102`
  Symbol: `Rings().Constructors().PuiseuxSeriesRing`
  Current signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why variadic-style: `arg2` is positional Sage factory plumbing and should be
  replaced by named closed overload cases.
  Source surface to scope next: the `PuiseuxSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage series-ring factory docs/source.

- File: `rings/matrix_algebras.py:84`
  Symbol: `_MatrixAlgebras.ParentMethods.matrix`
  Current signature: `x: Matrix | RingElement | Sequence[RingElement] |
  Sequence[Sequence[RingElement]] | None`.
  Why variadic-style: the element constructor still accepts scalar, flat
  coordinate, nested coordinate, existing-matrix, and empty/default cases in one
  method.
  Source surface to scope next: Sage `MatrixSpace` / `MatrixRing` element
  construction docs/source and the local matrix-ring mapping.

- File: `rings/subcategories/number_field.py:170`
  Symbol: `_NumberFields.ParentMethods.discriminant`
  Current signature: `v: Sequence[RingElement] | None = None`.
  Why variadic-style: optional basis data changes the meaning from field
  discriminant to discriminant of supplied elements.
  Source surface to scope next: Sage number-field discriminant docs/source.

- File: `rings/subcategories/number_field.py:197`
  Symbol: `_NumberFields.ParentMethods.integral_basis`
  Current signature: `v: RingElement | Sequence[RingElement] | None = None`.
  Why variadic-style: one parameter merges default integral basis, one element,
  and a finite element list.
  Source surface to scope next: Sage number-field integral-basis docs/source.

- File: `rings/subcategories/number_field.py:249`
  Symbol: `_NumberFields.ParentMethods.ring_of_integers`
  Current signature: `v: Integer | Sequence[Integer] | None = None`.
  Why variadic-style: one optional parameter merges default construction,
  algorithm/control integer, and sequence data.
  Source surface to scope next: Sage number-field order docs/source.

- File: `rings/subcategories/number_field.py:256`
  Symbol: `_NumberFields.ParentMethods.maximal_order`
  Current signature: `v: Integer | Sequence[Integer] | None = None`.
  Why variadic-style: one optional parameter merges default construction,
  algorithm/control integer, and sequence data.
  Source surface to scope next: Sage maximal-order docs/source.

- File: `rings/subcategories/rational_field.py:190`
  Symbol: `_QQ.ParentMethods.discriminant`
  Current signature: `v: Sequence[RingElement] | None = None`.
  Why variadic-style: this override forwards the unsplit number-field
  discriminant surface through `as_number_field()`.
  Source surface to scope next: scope with `_NumberFields.ParentMethods.discriminant`.

- File: `rings/subcategories/rational_field.py:233`
  Symbol: `_QQ.ParentMethods.integral_basis`
  Current signature: `v: RingElement | Sequence[RingElement] | None = None`.
  Why variadic-style: this override forwards the unsplit number-field
  integral-basis surface through `as_number_field()`.
  Source surface to scope next: scope with `_NumberFields.ParentMethods.integral_basis`.

- File: `rings/subcategories/rational_field.py:317`
  Symbol: `_QQ.ParentMethods.ring_of_integers`
  Current signature: `v: Integer | Sequence[Integer] | None = None`.
  Why variadic-style: this override forwards the unsplit number-field order
  surface through `as_number_field()`.
  Source surface to scope next: scope with `_NumberFields.ParentMethods.ring_of_integers`.

- File: `rings/subcategories/rational_field.py:326`
  Symbol: `_QQ.ParentMethods.maximal_order`
  Current signature: `v: Integer | Sequence[Integer] | None = None`.
  Why variadic-style: this override forwards the unsplit number-field order
  surface through `as_number_field()`.
  Source surface to scope next: scope with `_NumberFields.ParentMethods.maximal_order`.

- File: `tensor_algebra_components/__init__.py:176`
  Symbol: `TensorAlgebraComponents(R).Constructors().from_components`
  Current signature: `components: Matrix | Sequence[RingElement] |
  Sequence[Sequence[RingElement]] | Sequence[Sequence[Sequence[RingElement]]] |
  Sequence[Matrix]`.
  Why variadic-style: this public constructor still accepts all component
  coordinate shapes in one method, even though named tensor constructors already
  exist for matrices, module-element matrices, multidimensional lists, and
  lists of matrices.
  Source surface to scope next: `tensor_algebra_components/docs/SAGE_INVENTORY.md`
  records component assignment `t[:] = ...` and matrix/list interop.

## Private Or Closed Surfaces Reviewed

- File: `posets/__init__.py:249`
  Symbol: `Posets().Constructors()._raw_poset`
  Current signature: `data: Any` plus Sage `Poset` option keywords.
  Why reviewed: it is a private helper that centralizes Sage's variadic
  `Poset(data=None, ...)` dispatch. The public constructors around it are
  already split into named finite cases in `posets/docs/MAPPING.md`.
  Follow-up condition: keep this private; do not expose `data` as a public
  constructor surface.

- File: `sets/subcategories/finite_set_maps.py:75`
  Symbol: `_FiniteSetMapsSets.ParentMethods._element_constructor_`
  Current signature: closed implementation signature
  `data: FiniteSetMap | Callable[[SetElement], SetElement] |
  Sequence[SetElement]` after three explicit overload declarations.
  Why reviewed: the final abstract signature is broad, but the overloads
  enumerate the admissible cases. This is the AGENTS.md closed-overload pattern,
  not an unscoped variadic public constructor.
  Follow-up condition: do not replace the overloads with a catch-all body.

- File: `sets/__init__.py:513`
  Symbol: `Sets().Constructors().RealSet`
  Current signature: `intervals: Sequence[RealInterval]`.
  Why reviewed: it routes to Sage `RealSet(*tuple(intervals))`, but the public
  input is a typed finite union of interval objects. The catch-all
  `RealSet(*args)` is already rejected in `topological_spaces/docs/MAPPING.md`.
  Follow-up condition: keep arbitrary symbolic/manifold `RealSet(...)` inputs
  out of this constructor.

## Inventoried Sage Variadics Still Relevant To Scoping

- File: `algebras/docs/SAGE_INVENTORY.md`
  Sage surface: `sage.categories.algebra_functor.AlgebrasCategory(category, *args)`.
  Current mapping status: source-category algebra construction maps through
  `Algebras(R).Constructors().free_algebra_from_*`.
  Scoping need: source-category subtrees must expose only the admitted
  `S.free_algebra(R)` methods when those categories exist.

- File: `algebras/docs/SAGE_INVENTORY.md`
  Sage surface: `Sets.ParentMethods.algebra(base_ring, category=None, **kwds)`.
  Current mapping status: plain sets route to `S.free_module(R)`; structured
  source categories route to explicit free-algebra constructors.
  Scoping need: no project API should expose the Sage `category=` or `**kwds`
  path.

- File: `algebras/docs/SAGE_INVENTORY.md`
  Sage surface: `CombinatorialFreeModule(..., **kwds)`.
  Current mapping status: constructor ownership lives in
  `Modules(R).Constructors().CombinatorialFreeModule`.
  Scoping need: decide whether any `**kwds` behavior has mathematical content
  beyond the already named basis-key, element-class, category, prefix, and names
  parameters.

- File: `algebras/docs/SAGE_INVENTORY.md`
  Sage surfaces: `subalgebra(gens, category=None, *args, **opts)`,
  `ideal_submodule(gens, side='left', category=None, *args, **opts)`, and
  `principal_ideal(a, side='left', *args, **opts)`.
  Current mapping status: algebra subobjects and algebra ideals are mapped, but
  the extra Sage option bags have not been split.
  Scoping need: read the finite-dimensional algebra source and split any
  mathematically meaningful options from implementation plumbing.

- File: `lattices/docs/SAGE_INVENTORY.md`
  Sage surface: `short_vectors(self, n, **kwargs)`.
  Current mapping status: inventoried only.
  Scoping need: read the Sage lattice implementation and document the finite
  keyword cases before adding or rejecting a public lattice/vector-enumeration
  spec surface.

- File: `posets/docs/SAGE_INVENTORY.md`
  Sage surfaces: `MeetSemilattice(data=None, *args, **options)`,
  `JoinSemilattice(data=None, *args, **options)`, and
  `LatticePoset(data=None, *args, **options)`.
  Current mapping status: already split into named constructor families in
  `posets/docs/MAPPING.md`.
  Scoping need: preserve regression coverage for each old Sage constructor
  shape when the split constructor pass runs.

- File: `sets/docs/MAPPING.md`
  Sage surface: `EnumeratedSetFromIterator(f, args=..., kwds=...)`.
  Current mapping status: public constructor admits a nullary
  `iterator_factory` and omits arbitrary callable plumbing.
  Scoping need: preserve old functionality through wrapper factories in
  migration docs or regression tests without exposing `args`/`kwds`.

- File: `sets/docs/MAPPING.md`
  Sage surface:
  `Sets.ParentMethods._element_constructor_from_element_class(*args, **keywords)`.
  Current mapping status: omitted as Sage element-class forwarding.
  Scoping need: keep it out of category specs unless a concrete mathematical
  element constructor is named.

- File: `topological_spaces/docs/SAGE_INVENTORY.md`
  Sage surfaces: `RealSet(*args)` and named `RealSet` constructors with
  `**kwds`.
  Current mapping status: mapped to named `Sets().Constructors()` real-line
  subset constructors, with manifold-producing keyword paths rejected from the
  pure topological-space subtree.
  Scoping need: keep the named interval/ray constructors as the only admitted
  pure real-subset paths and avoid reintroducing a catch-all `RealSet(...)`.
