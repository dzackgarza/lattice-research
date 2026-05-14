---
id: DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP
trackerStatus:
  type: decision
parents:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
dependsOn: []
title: Mypy error triage — code gaps vs plugin gaps across all remaining error groups
status: decided
tags:
- FEATURE-QC-WARNINGS-ZERO
---
# Mypy error triage — code gaps vs plugin gaps across all remaining error groups

## Summary

Full triage of all remaining mypy errors in `category_specs/` after the
`DECISION-20260513` mechanical cleanup pass. Each error group was investigated by
reading the call sites, the relevant SPEC-MAPPING-*.md canonical sources, and (where
needed) Sage source via DeepWiki. Every error was classified as either a **code gap**
(the spec is wrong and must be fixed in `category_specs/`) or a **plugin gap**
(mypy lacks knowledge of Sage's runtime dispatch and requires either a plugin fix or
an approved `# type: ignore`).

The canonical mapping sources consulted are the SPEC-MAPPING-*.md files under
`plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/`.

---

## Code Gaps — fixable in `category_specs/` without plugin changes

### [no-redef] Constructors class/method name collision (8 files)

**Files:**
`category_specs/sets/__init__.py`,
`category_specs/modules/__init__.py`,
`category_specs/rings/__init__.py`,
`category_specs/algebras/__init__.py`,
`category_specs/posets/__init__.py`,
`category_specs/topological_spaces/__init__.py`,
`category_specs/tensor_algebra_components/__init__.py`,
`category_specs/lattices/__init__.py`

**Pattern in every file:**
```python
class Constructors:          # first definition — the nested helper class
    ...
_Constructors = Constructors  # private alias to preserve reference

@cached_method
@final
def Constructors(self) -> Constructors:   # [no-redef] fires here
    return self.__class__._Constructors(...)
```

mypy sees both `class Constructors` and `def Constructors` as top-level names in the
same class body and fires `[no-redef]` on the method definition.

**Fix:** Rename the nested class body from `class Constructors` to `class
_ConstructorsClass` (or similar private name) in all 8 files. Update the
`_Constructors = Constructors` alias line and any return-type annotations that reference
the nested class by name. The public `@cached_method def Constructors` method is
unchanged — it is the public API surface.

This is a purely mechanical rename. No mathematical content changes.

---

### [no-redef] `Category` import collision in `cat/base_category_types.py:593`

**File:** `category_specs/cat/base_category_types.py`

```python
# line 95-96:
if TYPE_CHECKING:
    from ..types import Category, Hom   # ← introduces 'Category' name

# line 593:
class Category(_CatObjectMixin, SageCategory, Parent):  # [no-redef] fires here
    ...
```

The `TYPE_CHECKING` import at line 96 introduces the name `Category` from `..types`,
which mypy sees as conflicting with the `class Category` definition at line 593 —
the actual concrete class this file exists to define.

**Fix:** Remove `Category` from the `TYPE_CHECKING` import on line 96. The concrete
`class Category` at line 593 is the definition this file exports. Any annotation in
the file that needed `Category` as a forward reference works without the import
because `from __future__ import annotations` is present at line 16.

---

### [no-redef] `forms/__init__.py` redundant `type` declarations (lines 87–98)

**File:** `category_specs/forms/__init__.py`

Four long-named type aliases are declared twice:
- `IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory` at lines 87 and 137
- `...Element` at lines 90 and 140
- `...Morphism` at lines 93 and 143
- `...Object` at lines 96 and 146

Lines 124–135 introduced private shorthand aliases (`_IntegralNondegenerateSymmetricCategory`,
etc.). Lines 137–148 then re-declared the public names using those shorthands. Lines
87–98 (the originals, pointing directly at `_chain.*`) were left in place — a
refactoring artifact.

**Fix:** Delete lines 87–98. The canonical declarations are lines 137–148.

---

### [operator] `_RModHomCategoryObjectMethods` not callable (`modules/homsets.py:63`)

```python
# homsets.py:63 inside _RModHomCategoryObjectMethods.zero_morphism:
return cast(RModMorphism, self(ConstantFunction(self.codomain().zero())))
```

`self(...)` invokes the hom-set parent's element constructor (`Sage Parent.__call__`).
This is a genuine abstract interface of hom-set parents — every hom-set in Sage
accepts a callable and returns the corresponding morphism via `__call__`. The method
is simply absent from `_RModHomCategoryObjectMethods`.

**Fix:** Add `@abstractmethod def __call__(self, f: Any) -> RModMorphism: ...` to
`_RModHomCategoryObjectMethods`. This is a missing abstract interface declaration.
SPEC-MAPPING-MODULES line 152 acknowledges parent `__call__` as part of the
constructor/interop surface admitted under `HomCategory()`.

---

### [operator] `ParentMethods` not callable in subobjects (`sets/.../subobjects.py:76`)

```python
# sets/subcategories/constructions/subobjects.py:76 inside ParentMethods.retract:
return self(x)
```

`self(x)` is Sage `Parent.__call__` for element construction — the universal
element-constructor entry point on all Sage parent objects. This is missing from the
base `ParentMethods` mixin. SPEC-MAPPING-SETS line 283 acknowledges element
construction as part of the parent interface.

**Fix:** Add `def __call__(self, x: Any) -> Any: ...` to the base `ParentMethods`
in `category_specs/cat/base_category_types.py` (or the appropriate shared base).
This affects all subclasses of `ParentMethods`.

---

### [operator] `__mul__` missing from `_RingElementMethods` (`rings/__init__.py:347`)

```python
# rings/__init__.py:347 inside _RingElementMethods.is_idempotent:
return self * self == self
```

Multiplication is a fundamental ring element operation. `__mul__` is absent from
`_RingElementMethods`. SPEC-MAPPING-RINGS line 84 confirms ring operations including
multiplication belong in the rings spec.

**Fix:** Add `@abstractmethod def __mul__(self, other: RingElement) -> RingElement: ...`
to `_RingElementMethods`.

---

### [operator] `__gt__`/`__ge__` parameter type too broad (`sets/subcategories/totally_ordered.py:63,68`)

```python
# totally_ordered.py:63,68:
def __gt__(self, other: SetElement) -> bool:
    return cast(bool, other.__lt__(self))   # [operator]: SetElement has no __lt__

def __ge__(self, other: SetElement) -> bool:
    return cast(bool, other.__le__(self))   # [operator]: SetElement has no __le__
```

`other: SetElement` = `Sets.ElementMethods`, which only declares `__eq__` and
`__hash__`. Inside `TotallyOrdered.ElementMethods`, `other` must also be a
`TotallyOrdered.ElementMethods` — the spec itself declares `__lt__` and `__le__`
abstractly on `TotallyOrdered.ElementMethods`, confirming this is the correct type.
SPEC-MAPPING-SETS lines 302 and 478 confirm rich comparison belongs on
`TotallyOrdered` element surfaces.

**Fix:** Change `other: SetElement` to `other: TotallyOrderedElement` (a type alias
for `TotallyOrdered.ElementMethods`, or a forward reference to it) in both `__gt__`
and `__ge__`.

---

### [call-arg] `*_certificate` wrappers call abstract stubs with `certificate=` (11 sites)

**Files:**
`category_specs/posets/subcategories/finite_lattice.py:67,80,93,108,119,128,139`
`category_specs/posets/subcategories/finite.py:135,147,190,205`

Pattern: each `is_atomic_with_certificate`, `height_with_certificate`, etc. is
implemented by calling `self.is_atomic(certificate=True)` — but the abstract stub
for `is_atomic` (per SPEC-MAPPING-POSETS lines 209–222) intentionally has no
`certificate` parameter (the design is to expose the certificate version under a
separate named method, not via an option argument).

The call therefore passes an unexpected keyword argument to the stub.

**Fix:** Each `*_with_certificate` wrapper must call Sage's runtime method directly
rather than the abstract stub. The precedent is `finite.py:165–166`, which already
casts to the Sage parent methods class:
```python
SageFinitePosets.ParentMethods.is_poset_morphism(self, ...)
```
Apply the same pattern: `SageFiniteLattice.ParentMethods.is_atomic(cast(Any, self), certificate=True)`.

---

### [call-arg] `short_vectors_up_to_sign` calls stub with `up_to_sign_flag=` (`lattices/over_integers.py:47`)

```python
# over_integers.py:47 inside short_vectors_up_to_sign:
return self.short_vectors(bound, up_to_sign_flag=True)
```

SPEC-MAPPING-LATTICES line 341 explicitly maps Sage's `short_vectors(n,
up_to_sign_flag=True)` to the dedicated method `short_vectors_up_to_sign(n)` — the
design is to eliminate the kwarg from the public spec surface. The abstract stub for
`short_vectors` therefore has no `up_to_sign_flag` parameter.

**Fix:** Same pattern as C1 — call Sage's runtime method directly:
`SageLatticeParentMethods.short_vectors(cast(Any, self), bound, up_to_sign_flag=True)`.

---

### [index] Private interop uses `[:]` without cast (`tensor_algebra_components/__init__.py:102,248,280`)

Three private methods (`structure_constants`, `_from_components`,
`_module_element_coordinates`) use `self[:]` / `tensor[:]` / `element[:]` on
spec-typed objects (`_TensorElementMethods`, `Tensor`, `RModuleElement`). None of
these spec classes declare `__getitem__` or `__setitem__`. SPEC-MAPPING-TENSOR-ALGEBRA-
COMPONENTS explicitly classifies `[:]` component array access as private coordinate
interop that is not part of the public spec surface.

**Fix:** Add `cast(Any, ...)` at each site:
- line 102: `cast(Any, self)[:]`
- line 248: `cast(Any, tensor)[:] = components`
- line 280: `tuple(cast(Any, element)[:])`

No new public API. No plugin changes.

---

### [union-attr] `ModuleBasis` union too broad (`modules/subcategories/with_basis.py:63`)

```python
# with_basis.py:63:
return cast(Sequence[CategoryElement], self.basis().keys())
```

`ModuleBasis` (in `types.py`) is `AbstractFamily | Sequence[RModuleElement]`.
`Sequence` has no `.keys()`, so mypy fires `[union-attr]` on the `Sequence` branch.

SPEC-MAPPING-MODULES confirms `basis().keys()` is an admitted surface, meaning
`basis()` always returns a key-indexed `AbstractFamily`, not a raw `Sequence`.
The `Sequence` branch in the union is a defensive over-broadening.

**Fix:** Narrow `ModuleBasis` in `types.py` from `AbstractFamily | Sequence[RModuleElement]`
to `AbstractFamily` only.

---

### [arg-type] `SubcategoryMethods` passed as `Modules` (`modules/__init__.py:1488`)

```python
# modules/__init__.py:1488 inside SubcategoryMethods.Constructors:
return Modules._Constructors(self)
```

`Modules._Constructors.__init__` expects `category: Modules`. `self` is statically
typed as `SubcategoryMethods`, which has no declared relationship to `Modules`.
At runtime, Sage MRO injection guarantees `self` is always a `Modules` instance.
SPEC-MAPPING-MODULES confirms `SubcategoryMethods.Constructors()` as the subcategory
propagation path.

**Fix:** `cast(Modules, self)` at the call site:
```python
return Modules._Constructors(cast(Modules, self))
```
Minimal, contained, does not require new protocol infrastructure.

---

### [call-overload] `PolynomialRing` all-optional passthrough (`modules/__init__.py:1208`)

```python
# modules/__init__.py:1208 inside polynomial_ring_as_module @final body:
Rings().Constructors().PolynomialRing(
    self.base_ring(), n=n, name=name, names=names,
    var_array=var_array, sparse=sparse, order=order,
    implementation=implementation,
)
```

Each keyword argument is typed `T | None`. No overload of `PolynomialRing`
(defined in `rings/__init__.py:1487–1554`) accepts all parameters simultaneously or
accepts `n: Integer | None` — each overload requires exactly the non-None combination.

**Fix:** Branch on which parameter is non-None before calling, mirroring the overload
structure. Example:
```python
if name is not None:
    return Rings().Constructors().PolynomialRing(self.base_ring(), name=name, ...)
elif names is not None:
    return Rings().Constructors().PolynomialRing(self.base_ring(), names=names, ...)
...
```
This is the pattern the overload declarations already imply.

---

## Plugin Gaps — require plugin tasks or approved `type: ignore`

### [assignment] `_base_category_class_and_axiom` tuple narrowing (`cat/endsets.py:27`)

```
Incompatible types in assignment (expression has type "tuple[type[CatHomCategory], str]",
base class "EndCategoryOf" defined the type as "tuple[type[HomCategoryOf], str]")
```

`CatHomCategory` is a direct subclass of `HomCategoryOf` (confirmed in
`cat/homsets.py:98`: `class CatHomCategory(HomCategoryOf)`). The narrowing of the
tuple's first element is mathematically correct and explicitly specified in
SPEC-MAPPING-CAT (Hom/End/Aut Categories section) and SPEC-MAPPING-HOMSETS lines
244–251. Python tuple types are invariant, so mypy cannot infer this covariance.

This is the same class of false positive as the `[assignment]` errors on
`ParentMethods`/`ElementMethods` refinements (task
`TASK-ADD-LSP-DISABLE-FLAG-FOR-PARENTMETHODS-SURFACES`).

**Resolution:** `# type: ignore[assignment]` on line 27 of `cat/endsets.py` with
reference to this card.

---

### [return-value] Covariant `ParentMethods` return narrowing (5 sites)

**Files and lines:**
- `rings/subcategories/field.py:150,152` — `return self` typed as `_Fields.ParentMethods`, expected `_CompleteRings.ParentMethods`
- `rings/subcategories/algebraically_closed_field.py:44` — `return self` typed as `_AlgebraicallyClosedFields.ParentMethods`, expected `_Fields.ParentMethods`
- `rings/subcategories/p_adic_integer_ring.py:51,53` — `return self` typed as `_Zp.ParentMethods`, expected `_CompleteRings.ParentMethods`

All five are `return self` inside `ParentMethods` subclasses that override an
abstract method declared on a parent category's `ParentMethods`. mypy types `self`
as the inner `ParentMethods` class rather than the runtime parent ring object —
because in Sage's dynamic system, `self` inside `ParentMethods` is always the actual
ring parent, not an instance of the nested class. The annotations and mathematics
are correct in all cases:
- A field is its own completion at any place (field.py).
- An algebraically closed field is its own algebraic closure (algebraically_closed_field.py).
- `Z_p` is complete (p_adic_integer_ring.py).

Same root cause as `TASK-ADD-LSP-DISABLE-FLAG-FOR-PARENTMETHODS-SURFACES`.

**Resolution:** `# type: ignore[return-value]` on each `return self` line with
reference to `TASK-ADD-LSP-DISABLE-FLAG-FOR-PARENTMETHODS-SURFACES`.

---

### [operator] `MorphismMethods` not callable (`lattices/.../subobjects.py:45`)

```python
# subobjects.py:45:
return cast("LatticeElement", self.inclusion()(v))
```

`self.inclusion()` returns `LatticesMorphism` = `LatticesCategory.MorphismMethods`.
The inner `MorphismMethods` class has an empty body and no `__call__`. At runtime,
Sage's `Morphism` base provides `__call__` via MRO injection (every Sage morphism is
callable as a function). The spec class correctly models the abstract contract but
mypy cannot see the injected `__call__`.

**Resolution:** New plugin task needed —
`TASK-TEACH-PLUGIN-MORPHISMMETHODS-CALLABLE`. The plugin must recognise that
`MorphismMethods` inner classes have a `__call__` method injected at runtime via
Sage's `Morphism` base. Interim: `# type: ignore[operator]` on line 45.

---

### [operator] `SubcategoryMethods.__contains__` (`algebras/__init__.py:394`)

```python
# algebras/__init__.py:394:
assert algebra in self, ...
```

`self: SubcategoryMethods`. `__contains__` is provided by the ambient category class
at runtime via MRO injection (same mechanism as `ParentMethods`/`ElementMethods`).
SPEC-MAPPING-ALGEBRAS confirms `algebra in category` is a valid predicate.

**Resolution:** Extend `TASK-ADD-LSP-DISABLE-FLAG-FOR-PARENTMETHODS-SURFACES` to
cover `SubcategoryMethods` in addition to `ParentMethods`/`ElementMethods`/
`MorphismMethods`. Interim: `# type: ignore[operator]` on line 394.

---

### [call-arg] `Constructors()` zero-arg — method/class name collision (8 sites)

**Sites:** `sets/__init__.py:190,297,305`, `sets/subcategories/partitioned.py:191,196,256`,
`modules/__init__.py:1124`, `rings/__init__.py:325`

After the rename of the inner class to `_ConstructorsClass` (see code gap fix above),
mypy will resolve `Constructors` as the `@cached_method def Constructors` method.
Calling it as `Constructors()` (zero args, treating it as a constructor) will then
fail because mypy sees the method's return type annotation rather than the class's
`__init__`. This is a consequence of the Sage pattern: the public API is the method,
not the class, but call sites that need a fresh `Constructors` instance currently
call it via `self.Constructors()` — which mypy resolves correctly. Sites that call
`Constructors()` directly (without `self.`) are calling the inner class before the
rename.

**Investigation note:** After the rename, these sites will be resolved if they are
updated to `self.Constructors()`. Some may also reflect the deeper pattern of
`FunctorialConstructionCategory.__classcall__` dispatch (see next item).

**Resolution:** Re-examine each site after the `_ConstructorsClass` rename to
determine which sites resolve naturally and which still need the
`TASK-TEACH-PLUGIN-FUNCTORIAL-CONSTRUCTION-ZERO-ARG` fix.

---

### [call-arg] `FunctorialConstructionCategory` zero-arg construction (10 sites)

**Sites:** `rings/homsets.py:52`, `sets/__init__.py:611`, `modules/__init__.py:593,602,658`,
`tensor_algebra_components/__init__.py:124,154`, `lattices/homsets.py:63`,
`lattices/subcategories/constructions/orthogonal_direct_sums.py:29`,
`modules/subcategories/integer_lattices.py:31`

Calls like `HomCategoryOf(self.base_category())`, `Subobjects(category)`,
`CartesianProducts(category)`, `TensorProducts(category)` where mypy fires
"Too few arguments". These are all `FunctorialConstructionCategory` subclasses
(parallel to `CategoryWithAxiom`). At runtime, `FunctorialConstructionCategory.__classcall__`
intercepts construction and routes arguments — `base_category` / `category` are
handled internally.

**Resolution:** New plugin task: `TASK-TEACH-PLUGIN-FUNCTORIAL-CONSTRUCTION-ZERO-ARG`.
The plugin must recognise that `FunctorialConstructionCategory` subclasses
(Subobjects, Quotients, CartesianProducts, TensorProducts, HomCategory, etc.) have
valid zero- or single-argument public constructors regardless of `__init__` declarations.
This is the direct parallel of `TASK-TEACH-PLUGIN-CATEGORY-WITH-AXIOM-ZERO-ARG-CONSTRUCTION`
for the `FunctorialConstructionCategory` hierarchy.

---

### [call-arg] `dispatch=False` via `__classcall_private__` (2 sites)

**Sites:** `lattices/__init__.py:223`, `forms/__init__.py:160`

Both call `Modules(base_ring, dispatch=False)`. The `dispatch` parameter is declared
on `Modules.__classcall_private__` (line 490–491 of `modules/__init__.py`):
```python
@classcall_private
def __classcall_private__(cls, base_ring: Ring, dispatch: bool = True) -> ...:
```
mypy does not understand `@classcall_private` and does not propagate its parameters
to the public constructor signature, so `dispatch=False` is rejected as an unexpected
keyword argument. SPEC-MAPPING-LATTICES line 250 confirms `Modules(R, dispatch=False)`
is the canonical form for obtaining undecorated module categories.

**Resolution:** New plugin task: `TASK-TEACH-PLUGIN-CLASSCALL-PRIVATE-KWARGS`. The
plugin must recognise that `__classcall_private__` parameters are valid public
constructor keyword arguments.

---

## Decision

All classifications above are **decided** as of 2026-05-14 based on:
1. Direct inspection of call sites and error messages
2. Canonical SPEC-MAPPING-*.md sources
3. DeepWiki Sage source verification where needed

**Code gaps** (15 distinct fixes, ~40 error sites): must be fixed in `category_specs/`
without any `# type: ignore`.

**Plugin gaps with approved interim suppression** (7 groups, ~26 error sites):
each requires either a filed plugin task or an extension of an existing task, plus
an approved `# type: ignore` with reference to this card until the plugin fix lands.

Approved interim suppressions under this card:
- `# type: ignore[assignment]` — `cat/endsets.py:27`
- `# type: ignore[return-value]` — `rings/subcategories/field.py:150,152`, `algebraically_closed_field.py:44`, `p_adic_integer_ring.py:51,53`
- `# type: ignore[operator]` — `lattices/.../subobjects.py:45`, `algebras/__init__.py:394`

All other plugin-gap sites (`Constructors` zero-arg, FunctorialConstruction zero-arg,
`dispatch=` kwarg) must be re-examined after the corresponding plugin tasks are filed
and the `_ConstructorsClass` rename is completed.

## Work Log

- 2026-05-14: Full triage performed via 5 parallel investigation agents.
  All 14 error clusters classified. Decision recorded.

## Affected Files (code gap fixes required)

- `category_specs/sets/__init__.py`
- `category_specs/modules/__init__.py`
- `category_specs/rings/__init__.py`
- `category_specs/algebras/__init__.py`
- `category_specs/posets/__init__.py`
- `category_specs/topological_spaces/__init__.py`
- `category_specs/tensor_algebra_components/__init__.py`
- `category_specs/lattices/__init__.py`
- `category_specs/cat/base_category_types.py`
- `category_specs/forms/__init__.py`
- `category_specs/modules/homsets.py`
- `category_specs/sets/subcategories/constructions/subobjects.py`
- `category_specs/rings/__init__.py`
- `category_specs/sets/subcategories/totally_ordered.py`
- `category_specs/posets/subcategories/finite_lattice.py`
- `category_specs/posets/subcategories/finite.py`
- `category_specs/lattices/subcategories/over_integers.py`
- `category_specs/tensor_algebra_components/__init__.py`
- `category_specs/modules/subcategories/with_basis.py`
- `category_specs/modules/subcategories/integer_lattices.py` (re-examine after rename)

