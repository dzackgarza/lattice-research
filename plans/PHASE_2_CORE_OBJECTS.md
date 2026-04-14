# Phase 2: Category, Forms, and Core Objects

Build the `BilinearModules(R)` category, form codomain abstraction, and
the core parent/element hierarchy: free and torsion bilinear modules over
arbitrary PID R (primarily R = ZZ). At the end of this phase, one can
construct bilinear modules, create symbolic elements, evaluate forms,
perform direct sums, and check category containment.

**Depends on:** Phase 0 (Sage patches), especially `QQ/ZZ` and `QQ/2ZZ`
as working codomains, enriched FGP module operations, and `+` = direct sum.

**Supersedes:** PHASE_1 Steps 1-7.

**Style guide:** `plans/LATTICE_STYLE_GUIDE.md`.
Every object built here must satisfy: elements are symbolic (not numerical),
containment over equations, categories over classes, operators overloaded,
validation at construction, exact arithmetic only.


## Files

```
src/lattices/
    categories/
        bilinear_modules.py       # BilinearModules(R), FreeBilinearModules, TorsionBilinearModules
        quadratic_modules.py      # QuadraticModules(R)
    core/
        codomains.py              # FormCodomain
        forms.py                  # BilinearForm, QuadraticForm
        abstract.py               # BilinearModule, QuadraticModule (abstract parents)
        elements.py               # Element hierarchy (ElementWrapper-based)
        free.py                   # FreeBilinearModule, FreeQuadraticModule
        torsion.py                # TorsionBilinearModule, TorsionQuadraticModule
    validation/
        presentations.py          # Pydantic validators for all Phase 2 constructors
```


## Implementation Steps


### Step 2.1: BilinearModules(R) Category

**File:** `categories/bilinear_modules.py`

**Existing code:** 35-line minimal category inheriting `Category_module`
with `_Hom_` dispatch.

Model on `sage.categories.modules.Modules`. This is the foundation
everything else hooks into via Sage's category/parent machinery.

**Category/concrete split:** The category defines ONLY the axiomatic
contract -- what any implementation of `BilinearModules` must provide,
expressed as ABCs. Everything implementation-specific (rank for free
modules, signature for lattices, roots for root lattices, internal Sage
objects) lives on concrete subclasses. The full ABC contracts and the
reasoning behind each choice is in `LATTICE_STYLE_GUIDE.md` under
"Category Interface vs. Concrete Implementation".

Key corrections vs. naive design:
- `rank` is NOT in the category -- only free modules have a rank
- `_Hom_` is NOT in the category -- it's a Sage internal hook; our public
  method is `Hom(other)`
- `gram_matrix` is a DERIVED method on the category (from `bilinear_form()`)
  -- not abstract, since it can always be computed as `bilinear_form().gram_matrix()`
- Every abstract method has explicit type annotations

```python
class BilinearModules(Category_module):
    """Category of pairs (M, beta) where M is a f.g. R-module
    and beta: M x M -> C is a symmetric bilinear form."""

    def super_categories(self):
        return [Modules(self.base_ring())]

    def additional_structure(self):
        return self  # Adds the form as genuine extra structure

    class ParentMethods(ABC):
        # === Abstract: every implementation MUST provide these ===
        @abstractmethod
        def bilinear_form(self) -> BilinearForm: ...   # the form object
        @abstractmethod
        def gens(self) -> tuple[BilinearModuleElement, ...]: ...
        @abstractmethod
        def zero(self) -> BilinearModuleElement: ...
        @abstractmethod
        def base_ring(self) -> Ring: ...
        @abstractmethod
        def free_part(self) -> FreeBilinearModule: ...
        @abstractmethod
        def torsion_part(self) -> TorsionBilinearModule: ...
        @abstractmethod
        def Hom(self, other: BilinearModule) -> BilinearModuleHomSpace: ...
        @abstractmethod
        def dual(self) -> BilinearModule: ...
        @abstractmethod
        def twist(self, scalar) -> BilinearModule: ...
        @abstractmethod
        def span(self, elements) -> BilinearModule: ...

        # === Derived: follow from the abstract interface above ===
        def b(self, v, w): return self.bilinear_form().evaluate(v, w)
        def gram_matrix(self): return self.bilinear_form().gram_matrix()
        def End(self): return self.Hom(self)

    class ElementMethods(ABC):
        @abstractmethod
        def parent(self) -> BilinearModule: ...
        @abstractmethod
        def __add__(self, other) -> BilinearModuleElement: ...
        @abstractmethod
        def __neg__(self) -> BilinearModuleElement: ...
        @abstractmethod
        def __rmul__(self, scalar) -> BilinearModuleElement: ...
        @abstractmethod
        def __eq__(self, other) -> bool: ...
        @abstractmethod
        def __hash__(self) -> int: ...
        @abstractmethod
        def to_vector(self) -> Vector: ...

        # === Derived ===
        def __mul__(self, other): return self.parent().b(self, other)
        def q(self): return self.parent().b(self, self)
        def is_isotropic(self): return self.q() == 0
        def span(self): return self.parent().span([self])

    class MorphismMethods(ABC):
        @abstractmethod
        def domain(self) -> BilinearModule: ...
        @abstractmethod
        def codomain(self) -> BilinearModule: ...
        @abstractmethod
        def __call__(self, v: BilinearModuleElement) -> BilinearModuleElement: ...
        @abstractmethod
        def to_matrix(self) -> Matrix: ...
        @abstractmethod
        def kernel(self) -> BilinearModule: ...
        @abstractmethod
        def image(self) -> BilinearModule: ...
        @abstractmethod
        def cokernel(self) -> BilinearModule: ...
        @abstractmethod
        def is_isometry(self) -> bool: ...

        # === Derived ===
        def is_injective(self): return self.kernel() == zero_module(self.domain())
        def is_surjective(self): return self.cokernel() == zero_module(self.codomain())
        def is_bijective(self): return self.is_injective() and self.is_surjective()

    class Homsets(HomsetsCategory):
        def extra_super_categories(self):
            return [Modules(self.base_category().base_ring())]

        class ParentMethods(ABC):
            @abstractmethod
            def domain(self) -> BilinearModule: ...
            @abstractmethod
            def codomain(self) -> BilinearModule: ...
            @abstractmethod
            def element_from_dict(self, mapping) -> BilinearModuleMorphism: ...
            @abstractmethod
            def element_from_matrix(self, M) -> BilinearModuleMorphism: ...
            @abstractmethod
            def element_from_images(self, images) -> BilinearModuleMorphism: ...
            @abstractmethod
            def __contains__(self, f) -> bool: ...
```

**Subcategories:**
- `FreeBilinearModules(BilinearModules)` -- for free underlying module
- `TorsionBilinearModules(BilinearModules)` -- for torsion underlying module

Similarly `QuadraticModules(R)` in `quadratic_modules.py` with
`quadratic_form()` and `polar_form()` in ParentMethods.

**Key decisions:**
- `additional_structure` returns `self` -- signals genuine extra structure
  beyond Modules(R), affects Sage's hom-set construction.
- `_Hom_` dispatches to correct HomSpace subclass (Phase 3 fills these in;
  Phase 2 provides a minimal stub).
- Element `__mul__` must dispatch correctly: `element * element` = bilinear
  product (scalar), `parent * parent` = tensor product (module). These are
  different Python objects so no ambiguity.


### Step 2.2: FormCodomain

**File:** `core/codomains.py`

Lightweight Pydantic-validated descriptor for the codomain of a
bilinear/quadratic form. This determines where form values land.

```python
class FormCodomain(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    base_ring: Parent   # R
    codomain: Parent    # C (the Sage object accepting form values)

    @classmethod
    def integral(cls, R) -> FormCodomain:
        """R-valued forms: beta: M x M -> R"""
        return cls(base_ring=R, codomain=R)

    @classmethod
    def rational(cls, R) -> FormCodomain:
        """K-valued forms: beta: M x M -> K = Frac(R)"""
        return cls(base_ring=R, codomain=R.fraction_field())

    @classmethod
    def torsion_bilinear(cls, R) -> FormCodomain:
        """K/R-valued forms for discriminant bilinear forms"""
        K = R.fraction_field()
        return cls(base_ring=R, codomain=K / R)

    @classmethod
    def torsion_quadratic(cls, R) -> FormCodomain:
        """K/2R-valued forms for discriminant quadratic forms"""
        K = R.fraction_field()
        return cls(base_ring=R, codomain=K / (2*R))
```

For R = ZZ: integral -> ZZ, rational -> QQ, torsion_bilinear -> QQ/ZZ,
torsion_quadratic -> QQ/2ZZ.

The `codomain` field is a real Sage parent (Phase 0 makes QQ/ZZ work).
Form evaluation coerces into this parent via `codomain(value)`.


### Step 2.3: BilinearForm and QuadraticForm

**File:** `core/forms.py`

Data objects (NOT Sage Parents) storing domain, codomain, and Gram matrix.
The critical design: form evaluation coerces the raw scalar product into
the codomain, so the same code handles integral, rational, and torsion
forms.

```python
class BilinearForm:
    def __init__(self, domain, codomain: FormCodomain, gram_matrix: Matrix):
        ...

    def evaluate(self, left, right):
        """Compute beta(left, right) in C."""
        raw = left.to_vector() * self._gram * right.to_vector().column()
        return self._codomain.codomain(raw[0])
```

QuadraticForm stores a gram matrix and evaluates `q(v) = v^T G v` with
coercion into the quadratic codomain. Its `polar_form()` returns the
associated BilinearForm.


### Step 2.4: BilinearModule Abstract Parent

**File:** `core/abstract.py`

**Existing code:** 298-line `BilinearModule(Parent)` -- migrate and
correct per corrections spec.

The abstract parent for all bilinear modules. Stores a BilinearForm object
(not just a Gram matrix), declares category membership, and provides the
`_element_constructor_` for element creation.

**Constructor surface:**
- `BilinearModule.from_gram(R, gram_matrix)` -- primary for free modules
- `BilinearModule.from_module_and_gram(module, gram_matrix, codomain)` --
  for torsion/mixed
- `BilinearModule.from_cokernel(morphism)` -- Phase 3 fills this in

Automatic promotion: `from_gram` / `from_module_and_gram` detect the most
specific correct subclass and return it (FreeBilinearModule,
TorsionBilinearModule, etc.). This is the only place where type-based
dispatch occurs, and it dispatches on a small fixed set of mathematical
properties (free vs torsion, codomain type), not on Python classes.

**What to migrate from existing code:**
- `Parent.__init__` with correct category
- `_element_constructor_` / `__call__`
- `_wrap_element` for rewrapping Sage elements
- Direct sum via `__add__` (block diagonal Gram)
- `__pow__` for n-fold direct sum

**What to remove:**
- `_sage_like()` from public API (keep as `_internal_module`)
- `_ambient`, `_ambient_generators`, `_ambient_submodule`
- `rescale` (banned)
- `getattr`-based `_element_cls` resolution

**Operators required:**
- `__add__` = direct sum
- `__pow__` = n-fold direct sum (`L^3 == L + L + L`)
- `__mul__` = scalar twist on parent (`n * L` means `{n*v : v in L}`)
- `__truediv__` = quotient (stub; Phase 3 fills in via cokernel)
- `__eq__` = canonical isomorphism (identity-matrix isometry for lattices)
- `__contains__` = parent check (never automatic coercion)
- `__iter__` = lazy enumeration of elements


### Step 2.5: Elements

**File:** `core/elements.py`

**Existing code:** 150-line file with `FreeBilinearModuleElement(ElementWrapper)`.

All elements MUST be genuine Sage `ElementWrapper` instances wrapping the
underlying FGP module element. Non-negotiable for `Map.__call__` to work.

**Hierarchy:**
```
BilinearModuleElement(ElementWrapper)
+-- FreeBilinearModuleElement
|   +-- RationalLatticeElement     (Phase 4)
|   |   +-- LatticeElement         (Phase 4)
|   |   +-- DualLatticeElement     (Phase 4)
+-- TorsionBilinearModuleElement
|   +-- DiscriminantGroupElement   (Phase 4)
+-- QuadraticModuleElement
    +-- FreeQuadraticModuleElement
    +-- TorsionQuadraticModuleElement
        +-- DiscriminantFormElement (Phase 4)
```

Phase 2 implements `BilinearModuleElement`, `FreeBilinearModuleElement`,
`TorsionBilinearModuleElement`, and the Quadratic variants. Phase 4
subclasses are stubbed.

**BilinearModuleElement methods:**
- `__mul__(other)` -- bilinear product when other is an element; delegates
  to parent's BilinearForm
- `q()` / `norm()` -- `self * self`
- `is_isotropic()` -- `self.q() == 0`
- `to_vector()` -- extract coordinate vector (explicit basis-dependent
  extraction)
- `to_coordinates()` -- alias
- `span()` -- `self.parent().span([self])`
- `perp()` -- `self.span().perp()`

**FreeBilinearModuleElement additions:**
- `inclusion()` -- morphism `self.span() -> parent` (stub until Phase 3)

**TorsionBilinearModuleElement additions:**
- `additive_order()` -- delegated to underlying FGP element
- `lift()` -- stub until Phase 4 (needs DualLattice)

**Critical style constraint:** `e + f` is a formal symbol in the parent,
not the vector `[1, 1]`. `[1, 0] not in L` must hold.


### Step 2.6: FreeBilinearModule

**File:** `core/free.py`

**Existing code:** 72-line `FreeBilinearModule(BilinearModule)`.

A free bilinear module is `(R^n, Gram matrix)`. Internally wraps
`FGP_Module(ZZ^n, zero_submodule)` from Phase 0 enrichment.

**Key methods:**
- `span(elements)` -- sub-bilinear-module within `self` generated by given
  elements. Computes restricted Gram matrix. Returns `FreeBilinearModule`
  (or degenerate `BilinearModule` if the span is degenerate).
- `perp(submodule)` / `orthogonal_complement(elements)` -- orthogonal
  complement within `self`.
- `is_degenerate()`, `is_nondegenerate()`
- `is_even()`, `is_odd()` (when R = ZZ)
- `determinant()` -- `det(gram_matrix)`
- `signature_pair()` -- `(p, q)` for real forms (exact, via Sylvester)

**Span semantics:** `L.span([e, f])` computes the Gram matrix of the
sub-module generated by `e, f` within `L`. This is the INTERNAL span,
inheriting `L`'s bilinear form. It is NOT the external direct sum `+`.

**Generator assignment:** `L.<e, f> = FreeBilinearModule(...)` works via
Sage's preparser calling `_first_ngens(2)`. Verify this works natively
on the `FGP_Module` wrapper; patch if needed.


### Step 2.7: TorsionBilinearModule

**File:** `core/torsion.py`

**Existing code:** 46-line `TorsionBilinearModule(BilinearModule)`.

Default codomain is `FormCodomain.torsion_bilinear(R)`. Form evaluation
coerces into QQ/ZZ (Phase 0 patches).

**Constructor:**
- `TorsionBilinearModule.from_invariants_and_gram(invariants, gram)` --
  direct construction from Smith invariants and a Gram matrix with entries
  in K/R.

**Methods:**
- `invariants()` -- Smith normal form invariants
- `cardinality()` -- product of invariants
- `is_p_elementary(p)` -- all invariants are p
- `p_rank(p)` -- number of invariant-p summands

**Element methods at TorsionBilinearModuleElement level:**
- `additive_order()` -- order in the underlying group
- `b(g1, g2)` -- bilinear form value in QQ/ZZ (convenience on parent)
- `q(g)` -- quadratic form value in QQ/2ZZ (convenience on parent)


### Step 2.8: Pydantic Validation

**File:** `validation/presentations.py`

**Existing code:** 209-line file with Pydantic models.

Phase 2 validators:
- `FormCodomainModel` -- validates base_ring is a PID, codomain is a ring
- `BilinearModulePresentationModel` -- validates Gram is symmetric, correct
  size, entries in correct ring
- `FreeModulePresentationModel` -- validates gram over R, rank consistency
- `TorsionModulePresentationModel` -- validates invariants are positive
  integers, gram entries in K/R

Each model uses a single `model_validator(mode="after")` that asserts
nontrivial mathematical properties. No per-field validation.


## Explicitly Out of Scope for Phase 2

- **Morphisms and hom spaces** -- Phase 3
- **Cokernel, kernel, image** -- Phase 3
- **Dual lattices, discriminant groups** -- Phase 4
- **Lattice named constructors** (`Lattice.U()`, etc.) -- Phase 4
- **Orthogonal groups** -- Phase 5
- **Tor/Ext functors** -- deferred indefinitely
- **QuadraticModules refinement** -- only stub; full implementation
  alongside discriminant forms in Phase 4


## Functional Checkpoint

Run in a Sage session after completing Phase 2:

```python
import src.sage_patches

from src.lattices.categories.bilinear_modules import BilinearModules
from src.lattices.core.free import FreeBilinearModule
from src.lattices.core.torsion import TorsionBilinearModule
from src.lattices.core.codomains import FormCodomain

# Category exists and is genuine
assert BilinearModules(ZZ) in Categories

# Free bilinear module construction + category containment
L = FreeBilinearModule(ZZ, matrix(ZZ, [[0,1],[1,0]]))
assert L in BilinearModules(ZZ)
assert L in Modules(ZZ)
assert L.gram_matrix() == matrix(ZZ, [[0,1],[1,0]])

# Elements are symbolic, not numerical
L.<e, f> = FreeBilinearModule(ZZ, matrix(ZZ, [[0,1],[1,0]]))
assert e in L and f in L
assert [1, 0] not in L
assert e * f == 1
assert e * e == 0 and f * f == 0
assert e.is_isotropic()
assert e.to_vector() == vector(ZZ, [1, 0])

# FormCodomain machinery
assert L.bilinear_form().codomain() == FormCodomain.integral(ZZ)

# Direct sum via +
M = L + L
assert M.rank() == 4
assert M in BilinearModules(ZZ)
assert M.gram_matrix() == block_diagonal_matrix(
    L.gram_matrix(), L.gram_matrix()
)

# Power via ^
assert (L^3).rank() == 6

# Twist
L2 = L.twist(2)
assert L2.gram_matrix() == 2 * L.gram_matrix()

# Span and perp
S = L.span([e])
assert S in BilinearModules(ZZ)
assert S.is_degenerate()
assert S.perp() == S

# Torsion bilinear modules
T = TorsionBilinearModule.from_invariants_and_gram(
    [2, 2], matrix(QQ, [[0, QQ(1,2)], [QQ(1,2), 0]])
)
assert T in BilinearModules(ZZ)
assert T in TorsionBilinearModules(ZZ)
assert T.bilinear_form().codomain() == FormCodomain.torsion_bilinear(ZZ)
g1, g2 = T.gens()
assert T.b(g1, g2) == QQ(1,2)
assert g1.additive_order() == 2

# Iteration exists (lazy)
first_few = list(itertools.islice(L, 5))
assert L.zero() in first_few
```


## Risks

| Risk | Mitigation |
|------|-----------|
| Element `__mul__` conflicts with Sage's coercion model | Only override on our ElementWrapper subclass; Sage elements use different dispatch |
| `_first_ngens` may not work on wrapped FGP modules | Test early; patch if needed |
| Category caching may interfere with `in BilinearModules(ZZ)` | Use `__contains__` override, not cached category membership |
| Torsion form evaluation depends on Phase 0 QQ/ZZ arithmetic | Verify Phase 0 is complete before starting torsion modules |
