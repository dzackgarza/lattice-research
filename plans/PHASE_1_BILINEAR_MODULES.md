# Phase 1: BilinearModule and QuadraticModule Foundation

Build the `BilinearModules(R)` category and parent hierarchy over arbitrary
PID R (primarily R = ZZ). The central design goal: the discriminant form
descent -- from integral lattice L through dual L\* to discriminant group
A\_L with induced QQ/ZZ-valued form -- falls out of the general machinery
rather than being special-cased for free vs torsion modules.

**Depends on:** Phase 0 (Sage patches), especially `QQ/ZZ` and `QQ/2ZZ` as
working codomains, and enriched FGP module operations.

**Canonical sources:**
- `plans/lattice_redesign_corrections_spec.md`
- `plans/lattice_interface_redesign_plan.md` (noun inventory, verb
  attachment, inheritance diagram)
- `plans/CONTRIBUTING.md` (code style, no indirection, no try/except, glue
  not math)
- `tests/lattice_spec/interface_semantics.sage`
- `tests/lattice_spec/interface_extensions.sage`
- `tests/lattice_spec/more_specs.sage`
- `tests/sage_spec/lattice_methods.sage`


## Target File Structure

```
src/lattices/
    __init__.py                          # Re-exports from lattices.py
    lattices.py                          # Lattice class + named constructors, public entry
    categories/
        __init__.py
        bilinear_modules.py              # BilinearModules(R) category
        quadratic_modules.py             # QuadraticModules(R) category
    core/
        __init__.py
        codomains.py                     # FormCodomain, QuotientFormCodomain
        forms.py                         # BilinearForm, QuadraticForm
        abstract.py                      # BilinearModule, QuadraticModule parents
        elements.py                      # All element classes
        free.py                          # FreeBilinearModule, FreeQuadraticModule
        torsion.py                       # TorsionBilinearModule, TorsionQuadraticModule
        rational.py                      # RationalLattice, DualLattice
        discriminant.py                  # DiscriminantGroup, DiscriminantForm
    morphisms/
        __init__.py
        homspaces.py                     # All HomSpace classes
        bilinear.py                      # BilinearModuleMorphism and specializations
        discriminant.py                  # DiscriminantGroup/Form morphisms
    groups/
        __init__.py
        orthogonal.py                    # LatticeOrthogonalGroup, subgroups, etc.
    validation/
        __init__.py
        presentations.py                 # Pydantic models for all constructors
```

The existing `src/lattices/` code is migrated and corrected, not discarded
(`plans/lattice_redesign_corrections_spec.md`, Non-Negotiable Preservation
Rule).


## Implementation Order

Each step depends on the previous steps being stable. The ordering follows
`.serena/memories/lattices/interface/redesign_dependency_order.md`.

Before starting any step, re-read the relevant block of
`plans/lattice_redesign_corrections_spec.md` and
`plans/CONTRIBUTING.md`.


### Step 1: Categories

**Files:** `categories/bilinear_modules.py`, `categories/quadratic_modules.py`

**Existing code:** `categories/bilinear_modules.py` (35 lines) -- minimal
category inheriting `Category_module` with `_Hom_` dispatch.

**Target:** `BilinearModules(R)` as a genuine Sage category, modeled on
`sage.categories.modules.Modules`. This is the foundation everything else
hooks into.

```python
class BilinearModules(Category_module):
    """Category of pairs (M, beta) where M is a f.g. R-module
    and beta: M tensor_R M -> C is a symmetric bilinear form."""

    def super_categories(self):
        return [Modules(self.base_ring())]

    def additional_structure(self):
        return self  # BilinearModules adds structure (the form)

    class ParentMethods:
        def gram_matrix(self): ...
        def bilinear_form(self): ...
        def codomain(self): ...
        def dual(self): ...
        def twist(self, scalar): ...
        def orthogonal_complement(self, elements): ...
        def _Hom_(self, codomain, category=None): ...

    class ElementMethods:
        def bilinear_product_with(self, other): ...
        def q(self): ...
        def norm(self): ...
        def is_isotropic(self): ...

    class MorphismMethods:
        def is_isometry(self): ...

    class Homsets(HomsetsCategory):
        def extra_super_categories(self):
            return [Modules(self.base_category().base_ring())]

        class ParentMethods:
            def element_from_dict(self, mapping): ...
            def element_from_matrix(self, matrix_data): ...
            def natural_map(self): ...
```

Subcategories:

```python
class FreeBilinearModules(BilinearModules):
    def super_categories(self):
        return [BilinearModules(self.base_ring())]

class TorsionBilinearModules(BilinearModules):
    def super_categories(self):
        return [BilinearModules(self.base_ring())]
```

Similarly for `QuadraticModules(R)` with `quadratic_form()`, `polar_form()`
in ParentMethods.

**Key decisions:**
- `BilinearModules(R)` returns `Modules(R)` as sole super-category.
- `additional_structure` returns `self`, signaling this adds genuine
  structure beyond being a module. This affects Sage's hom-set construction.
- `_Hom_` in ParentMethods dispatches to the correct HomSpace subclass.
  Uses isinstance checks on a small fixed set -- acceptable per corrections
  spec since the dispatch is between known types.

**Design constraint from corrections spec:** "BilinearModules is a new
category. It has its own elements and morphisms. It is the category of pairs
(M, beta)... So you might as well hook a new category properly, emulating
sage.categories.modules."


### Step 2: FormCodomain

**File:** `core/codomains.py`

**Existing code:** None -- codomains are currently raw `value_ring`
references.

FormCodomain is a lightweight descriptor for the codomain of a
bilinear/quadratic form:

```python
class FormCodomain(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    base_ring: Parent   # R
    codomain: Parent    # C (the Sage object accepting form values)

    @classmethod
    def integral(cls, R) -> FormCodomain:
        """R-valued forms: beta: M tensor M -> R"""
        return cls(base_ring=R, codomain=R)

    @classmethod
    def rational(cls, R) -> FormCodomain:
        """K-valued forms: beta: M tensor M -> K = Frac(R)"""
        return cls(base_ring=R, codomain=R.fraction_field())

    @classmethod
    def torsion_bilinear(cls, R) -> FormCodomain:
        """K/R-valued forms for discriminant bilinear forms"""
        K = R.fraction_field()
        return cls(base_ring=R, codomain=K / R)  # Phase 0 patches

    @classmethod
    def torsion_quadratic(cls, R) -> FormCodomain:
        """K/2R-valued forms for discriminant quadratic forms"""
        K = R.fraction_field()
        return cls(base_ring=R, codomain=K / (2*R))  # Phase 0 patches
```

For R = ZZ:
- `FormCodomain.integral(ZZ)` -- codomain = ZZ
- `FormCodomain.rational(ZZ)` -- codomain = QQ
- `FormCodomain.torsion_bilinear(ZZ)` -- codomain = QQ/ZZ
- `FormCodomain.torsion_quadratic(ZZ)` -- codomain = QQ/2ZZ


### Step 3: Forms

**File:** `core/forms.py`

**Existing code:** Minimal `BilinearForm` (6 lines) delegating to parent.

BilinearForm and QuadraticForm are data objects, NOT Sage Parents. They
store domain, codomain, and Gram matrix:

```python
class BilinearForm:
    def __init__(self, domain, codomain: FormCodomain, gram_matrix: Matrix):
        self._domain = domain
        self._codomain = codomain
        self._gram = gram_matrix

    def domain(self) -> BilinearModule: ...
    def codomain(self) -> FormCodomain: ...
    def gram_matrix(self) -> Matrix: ...

    def evaluate(self, left, right):
        """Compute beta(left, right) in C."""
        raw = left.to_vector() * self._gram * right.to_vector().column()
        return self._codomain.codomain(raw[0])

    def tensor_map(self): ...
```

```python
class QuadraticForm:
    def __init__(self, domain, codomain: FormCodomain, gram_matrix: Matrix):
        ...

    def evaluate(self, element):
        v = element.to_vector()
        raw = v * self._gram * v.column()
        return self._codomain.codomain(raw[0])

    def polar_form(self) -> BilinearForm:
        """beta(x,y) = q(x+y) - q(x) - q(y)"""
        ...
```

The critical design: form evaluation coerces the raw scalar product into
the codomain. For integral forms, this is identity. For torsion forms, this
is reduction modulo ZZ (or 2ZZ). The coercion is handled by calling
`self._codomain.codomain(value)`, which uses Phase 0's patched QQ/ZZ
arithmetic.


### Step 4: BilinearModule and QuadraticModule

**File:** `core/abstract.py`

**Existing code:** 298-line `BilinearModule(Parent)` with significant
functionality and many issues flagged in corrections spec.

**Migrate and keep:**
- `Parent.__init__(self, category=BilinearModules(self.base_ring()))`
- `_element_constructor_` / `__call__` for element creation
- `_Hom_` dispatched from category
- `_wrap_element` for rewrapping Sage elements
- Direct sum via `__add__` with block diagonal Gram
- Type promotion via `from_presented_module`

**Remove:**
- `_sage_like()` from public API (keep as `_internal_module`)
- `_ambient`, `_ambient_generators`, `_ambient_submodule` (move to
  subobject mixin if ever needed)
- `rescale` (banned alias for `twist`)
- `getattr`-based `_element_cls` resolution

**Constructor surface:**
- `BilinearModule.from_gram(R, gram_matrix)` -- primary for free modules
- `BilinearModule.from_module_and_gram(module, gram_matrix, codomain)` --
  for torsion/mixed
- `BilinearModule.from_cokernel(morphism)` -- crucial for discriminant
  descent

The `from_gram` / `from_module_and_gram` constructors automatically promote
to the most specific correct subclass:
- Free + integral + nondegenerate + R=ZZ => `Lattice`
- Free + rational + nondegenerate => `RationalLattice`
- Free + R-valued => `FreeBilinearModule`
- Torsion + source lattice data => `DiscriminantGroup`
- Torsion + no source => `TorsionBilinearModule`

**Design constraints from corrections spec:**
- Public nouns NOT naturally embedded in ambient spaces.
- `gens()` is semantically well-defined throughout.
- Membership is parent check: `v in L` means `v.parent() == L`.
- `L.element_from(v)` is the semantic conversion from coordinates to element.
- No `None` sentinels, no optional arguments.
- General verbs live as high in the hierarchy as their semantics allow.


### Step 5: Elements

**File:** `core/elements.py`

**Existing code:** 150-line file with `FreeBilinearModuleElement(ElementWrapper)`
and specialized classes. Fundamentally correct hierarchy.

**Element hierarchy:**
```
BilinearModuleElement(ElementWrapper)
+-- FreeBilinearModuleElement
|   +-- RationalLatticeElement
|   |   +-- LatticeElement
|   |   +-- DualLatticeElement
+-- TorsionBilinearModuleElement
|   +-- DiscriminantGroupElement
+-- QuadraticModuleElement
    +-- FreeQuadraticModuleElement
    +-- TorsionQuadraticModuleElement
        +-- DiscriminantFormElement
```

**Key methods at BilinearModuleElement level:**
- `bilinear_product_with(other)`: Routes through parent's BilinearForm
- `q()` / `norm()`: `self.bilinear_product_with(self)`
- `is_isotropic()`: `self.q() == 0`
- `to_vector()`, `to_coordinates()`

**LatticeElement additions:**
- `inner_product(other)`: Same as `bilinear_product_with` but ZZ-valued
- `divisibility()`: gcd of coordinates
- `is_primitive()`: `self.divisibility() == 1`
- `discriminant_class()`: projection to A\_L (always zero for integral
  elements)
- `span()`, `perp()`, `is_root()`, `reflection()`

**DualLatticeElement additions:**
- Function-call evaluation on lattice elements: `e_star(e)` returns the
  pairing value
- `discriminant_class()`: projection to A\_L (nontrivial for non-integral
  dual elements)

**DiscriminantGroupElement additions:**
- `additive_order()`
- `lift()`: returns element of DualLattice, NOT a raw vector

**Design constraint:** Elements MUST be genuine Sage `ElementWrapper`
instances. This is non-negotiable for `Map.__call__` to work.


### Step 6: Free bilinear modules

**File:** `core/free.py`

**Existing code:** 72-line `FreeBilinearModule(BilinearModule)`.

A free bilinear module is a pair (R^n, Gram matrix). Internally wraps
`FGP_Module(ZZ^n, zero_submodule)`.

**Key methods:**
- `is_R_valued()` / `is_K_valued()`: Check if form codomain is R or K.
- `span(elements)`: Sub-bilinear-module generated by given elements. Returns
  `FreeBilinearModule` with the restricted Gram matrix.
- `orthogonal_complement(submodule)` / `perp`: orthogonal complement
  within `self`.
- `is_primitive(submodule)`, `is_saturated(submodule)`,
  `saturation(submodule)`, `index(submodule)`.


### Step 7: Torsion bilinear modules

**File:** `core/torsion.py`

**Existing code:** 46-line `TorsionBilinearModule(BilinearModule)`.

Default codomain is `FormCodomain.torsion_bilinear(R)`. Form evaluation
coerces into QQ/ZZ. Elements are `TorsionBilinearModuleElement`.

**Constructor:**
- `TorsionBilinearModule.from_invariants_and_gram(invariants, gram)`:
  Direct construction from Smith invariants and a Gram matrix with entries
  in K/R.


### Step 8: HomSpaces and Morphisms

**Files:** `morphisms/homspaces.py`, `morphisms/bilinear.py`

**Existing code:** 107-line `BilinearModuleHomSpace(Homset)`, 123-line
`BilinearModuleMorphism(Morphism)`.

**HomSpace hierarchy:**
```
BilinearModuleHomSpace(Homset)
+-- FreeBilinearModuleHomSpace
|   +-- RationalLatticeHomSpace
|   |   +-- LatticeHomSpace
+-- TorsionBilinearModuleHomSpace
|   +-- DiscriminantGroupHomSpace
|   +-- DiscriminantFormHomSpace
```

**HomSpace methods (at BilinearModuleHomSpace level):**
- `element_from_dict(mapping)`: Construct morphism from generator-image dict
- `element_from_matrix(M)`: Construct morphism from matrix
- `natural_map()`: Natural inclusion/projection between domain and codomain
- `identity()`: Identity morphism when domain == codomain

**Morphism hierarchy:**
```
BilinearModuleMorphism(Morphism)
+-- FreeBilinearModuleMorphism
|   +-- RationalLatticeMorphism
|   |   +-- LatticeMorphism
+-- TorsionBilinearModuleMorphism
|   +-- DiscriminantGroupMorphism
|   +-- DiscriminantFormMorphism
```

**Morphism methods (at BilinearModuleMorphism level):**
- `image()`: BilinearModule with induced form
- `kernel()`: BilinearModule with restricted form
- `cokernel()`: BilinearModule with descended form -- **the critical method**
- `is_isometry()`: Form preservation check (owned by hom-space containment)
- `is_injective()`, `is_surjective()`, `is_isomorphism()`
- `is_primitive()`: `self.cokernel().is_torsionfree()`
- `direct_sum(other)`: Block diagonal morphism

**LatticeMorphism additions:**
- `to_matrix()`, `inverse()`
- `is_involution()`, `order()`
- `is_permutation()`, `is_shear()`
- `as_word_in_generators()`, `as_word_in_reflections()`,
  `reflection_decomposition()`

#### The cokernel method in detail

This is the SINGLE most critical method. It must:

- Compute the FGP cokernel module
- Descend the bilinear form to the quotient
- Determine the correct codomain for the descended form
- Automatically promote to the correct BilinearModule subclass

```python
def cokernel(self):
    # 1. Compute underlying module cokernel
    quotient_module = self._compute_fgp_cokernel()

    # 2. Determine codomain for induced form
    induced_codomain = self._induced_form_codomain()

    # 3. Compute Gram matrix of descended form
    quotient_gram = self._descend_bilinear_form(quotient_module, induced_codomain)

    # 4. Promote to correct type via BilinearModule.from_module_and_gram
    return BilinearModule.from_module_and_gram(
        quotient_module, quotient_gram, induced_codomain
    )
```

The promotion logic in `from_module_and_gram` detects:
- Is the module free or torsion?
- What is the form codomain?
- Is there source lattice data? (carried through from DualLattice)

This yields the correct subclass (DiscriminantGroup, TorsionBilinearModule,
Lattice, etc.) without hard-coding specific cokernel scenarios.

**Design constraints from corrections spec:**
- Morphisms are NOT containers; no `__contains__` on morphisms.
- `perp` does NOT belong on morphisms.
- Cokernels must construct the correct mathematical object.
- `A_L := coker(L -> L*)` must be modeled correctly.
- Hom-space containment owns isometry testing -- not scattered matrix
  equations.


### Step 9: RationalLattice and DualLattice

**File:** `core/rational.py`

**Existing code:** 126-line file with `RationalLattice(FreeBilinearModule)`
and `DualLattice(RationalLattice)`.

`RationalLattice` is a `FreeBilinearModule` with
`FormCodomain.rational(ZZ)`.

`DualLattice` is a `RationalLattice` with:
- A reference to the source lattice L
- `inclusion_morphism()`: the map iota\_L: L -> L\* with matrix G
- The Gram matrix G^{-1} (the inverse Gram in the dual basis)

**DualLattice construction:**
```python
DualLattice.from_lattice(L):
    # Gram of L* in dual basis is G^{-1}
    dual_gram = L.gram_matrix().inverse()
    # Codomain is QQ (rational-valued form)
    codomain = FormCodomain.rational(ZZ)
    # Store source lattice for discriminant group construction
    return DualLattice(dual_gram, codomain, source_lattice=L)
```

**DualLattice is quotientable by any sublattice**, not just the original
lattice. `L_star.quotient_by(sublattice)` computes the cokernel of the
inclusion.

**DualLatticeElement:**
- Function-call semantics: `e_star(v)` evaluates the functional.
- `discriminant_class()`: projection to A\_L.

#### Spec assertions covered

```python
# From interface_extensions.sage:
E8_2 = E8.twist(2)
assert E8_2.dual() == QQ(1,2) * E8
assert E8_2.discriminant_group() == E8_2.dual() / E8_2

U2_dual = U2.dual()
ep_dual, fp_dual = tuple(U2_dual.basis())
assert ep_dual == ep / 2 and fp_dual == fp / 2
assert ep_dual.discriminant_class() == g1
assert g1.lift() == ep_dual

# From more_specs.sage:
e_star, f_star = U.dual().gens()
assert e_star(e) == 1 and e_star(f) == 0
assert f_star(e) == 0 and f_star(f) == 1
```


### Step 10: Discriminant Group and Discriminant Form

**File:** `core/discriminant.py`

**Existing code:** 230-line `DiscriminantGroup(TorsionBilinearModule, QuadraticModule)`.

This is where the discriminant descent culminates. Given L:

```
L                          Lattice, codomain ZZ
L* = L.dual()              DualLattice, codomain QQ
iota = L*.inclusion()      Morphism L -> L*, matrix G
A_L = iota.cokernel()      DiscriminantGroup, codomain QQ/ZZ
```

The cokernel path (Step 8) handles this automatically. But DiscriminantGroup
also needs direct construction:
- `DiscriminantGroup.from_cokernel_data(module, gram, source_lattice)`:
  Constructed by the cokernel promotion logic.
- `DiscriminantGroup.from_invariants_and_gram(invariants, gram)`: Direct
  construction without source lattice (for testing, comparison).

**DiscriminantGroup methods:**
- `gens()`, `zero()`
- `q(element)`: Quadratic form, values in QQ/2ZZ
- `b(left, right)`: Bilinear form, values in QQ/ZZ
- `quadratic_form()`, `bilinear_form()`
- `orthogonal_group()`: DiscriminantOrthogonalGroup
- `isotropic_elements()`, `elements_of_norm(n)`, `value_map()`
- `norm_classes()`
- `is_isometric_to(other)`: Compare quadratic form isometry classes
- `isomorphic_as_groups(other)`: Compare underlying abelian group structure

**DiscriminantForm** is `TorsionQuadraticModule` with the quadratic
refinement. It stores both the bilinear and quadratic forms.

**What to fix from existing code:**
- Remove `_modulus` / `_modulus_qf` private Sage API access. Instead,
  compare normal forms of induced forms for `is_isometric_to`.
- Remove `_lattice` as Optional field. Use two separate constructors.
- Remove `p_rank` as standalone method (it is `is_p_elementary` + rank
  computation, delegated to underlying group).

#### Spec assertions covered

```python
# From interface_extensions.sage:
A_U2 = U2.discriminant_group()
g1, g2 = tuple(A_U2.gens())
assert A_U2.cardinality() == 4
assert g1.additive_order() == 2
assert A_U2.q(g1) == 0
assert A_U2.b(g1, g2) == QQ(1, 2)
assert A_U2.isotropic_elements() == {A_U2.zero(), g1, g2}
assert g1.lift() == ep_dual  # lift returns DualLattice element
```


### Step 11: Lattice

**Files:** `lattices.py` (public entry), `core/integral.py` (if split needed)

**Existing code:** 344-line `Lattice(RationalLattice)` with named
constructors and backend delegation.

`Lattice` is the primary user-facing class. It is a `RationalLattice` with
`FormCodomain.integral(ZZ)` and a cached `IntegralLattice` Sage object for
backend delegation.

**Named constructors:**
- `Z()`, `U()`, `I(p, q)`, `II(p, q)`, `A(n)`, `E(n)`
- `k3()`, `coble_picard()`
- `root_lattice(name)`, `from_string(s)`, `from_gram(G)`

**Key methods:**
- `discriminant_group()`: **Must use the cokernel path:**
  `self.dual().inclusion_morphism().cokernel()`. NOT a direct construction
  bypass.
- `orthogonal_group()`: Returns `LatticeOrthogonalGroup`.
- `dual()`: Returns `DualLattice.from_lattice(self)`.
- `dual_lattice()`: Alias for `dual()`.
- `delta`, `coparity`: Lattice invariants (NOT discriminant group
  invariants).
- `roots()`, `root_sublattice()`, `weyl_group()`, `W()`,
  `coxeter_diagram()`, `eichler_group()`, `E()`.
- `invariant_sublattice(g)`, `coinvariant_sublattice(g)`.
- `primitive_isotropic_vector_orbits()`, `isotropic_vector_orbits()`.

**Syntax sugar:**
- `L + M` = direct sum
- `L ** n` = `sum(n * [L])`
- `n * L` = `L.twist(n)` (but see more\_specs.sage: multiplication is NOT
  twisting; `2*U` means `{2v | v in U}`, which is isometric to `U.twist(4)`)
- `L / M` = `coker(M -> L)` for inclusion M <= L

**What to fix:**
- Remove `inner_product_matrix()`, `rescale()`.
- Route `discriminant_group()` through cokernel path, not direct construction.
- `delta`, `coparity` stay on Lattice, not on DiscriminantGroup.

#### Spec assertions covered

```python
# From interface_semantics.sage:
assert Lattice.II(0, 8).is_isometric_to(Lattice.E(8))
assert Lattice.II(3, 19).is_isometric_to(Lattice.k3())
assert Lattice.from_string("U(2) + A_1").is_isometric_to(
    Lattice.U().twist(2) + Lattice.A(1)
)

# From interface_extensions.sage:
assert set(U.orthogonal_group()) == {I2, swap, minus_I2, minus_swap}
assert U.roots() == {v, -v}
R_U = U.root_sublattice()
assert R_U == Lattice.root_lattice("A1")
```


### Step 12: Orthogonal Groups

**File:** `groups/orthogonal.py`

**Existing code:** Orthogonal group classes with backend delegation.

**LatticeOrthogonalGroup(Parent):**
- `element_from_matrix(M)`, `from_matrix(M)`, `__call__(M)` (thin router)
- `identity()`, `gens()`
- `special_orthogonal_subgroup()`
- `stabilizer(v_or_submodule)`: Dispatch on argument type
- `stabilizer_of_isotropic_line(v)`
- `centralizer(g)`
- `kernel_of_discriminant_action()`: ker(O(L) -> O(A\_L))
- `isotropic_line_orbits()`, `isotropic_plane_orbits()`,
  `isotropic_flag_orbits(dim)`
- `isotropic_lines_are_equivalent(v, w)`
- `reflection(v)`

**LatticeOrthogonalSubgroup(LatticeOrthogonalGroup):**
- Subgroup inheriting all methods, with restricted `__contains__`.
- Uses `ConditionSet` for lazy membership.

**DiscriminantOrthogonalGroup(Parent):**
- `gens()`, `stabilizer()`

**WeylGroup(LatticeOrthogonalSubgroup):**
- `simple_reflections()`, `coxeter_diagram()`, `is_isomorphic_to()`

**EichlerGroup(LatticeOrthogonalSubgroup):**
- `gens()`, `stabilizer()`, `is_trivial()`, `is_subgroup()`

**Design constraints from corrections spec:**
- Isometry verification belongs in `O(L).__contains__`, not scattered
  matrix equations.
- Stabilizers go on O(L): `L.orthogonal_group().stabilizer(v)`.
- No internal `_definite_orthogonal_group_generators` on public API.


### Step 13: Validation

**File:** `validation/presentations.py`

**Existing code:** 209-line file with Pydantic models.

One Pydantic model per constructor surface:

- `FormCodomainModel`
- `BilinearModulePresentationModel`
- `QuadraticModulePresentationModel`
- `FreeModulePresentationModel`
- `TorsionModulePresentationModel`
- `MorphismFromImagesModel`
- `MorphismFromMatrixModel`
- `LatticeFromGramModel`
- `DiscriminantGroupFromCokernelModel`
- `DiscriminantFormFromRefinementModel`

Validation runs after construction to ensure mathematical validity. No
per-field validation -- one overall `model_validator(mode="after")` that
asserts mathematical properties (e.g. Gram matrix is symmetric, correct
size, entries in correct ring).


## The Discriminant Descent: End-to-End Flow

This is the critical path that validates the entire Phase 1 design.

```python
# 1. Construct lattice
L = Lattice.from_gram(matrix(ZZ, [[2, 1], [1, 2]]))  # A_2

# 2. Dual lattice
L_star = L.dual()
assert isinstance(L_star, DualLattice)
assert L_star.gram_matrix() == L.gram_matrix().inverse()
# form_codomain is FormCodomain.rational(ZZ) -- QQ-valued

# 3. Inclusion morphism
iota = L_star.inclusion_morphism()
assert iota.domain() is L
assert iota.codomain() is L_star
assert iota.to_matrix() == L.gram_matrix()

# 4. Discriminant group as cokernel
A_L = iota.cokernel()
assert isinstance(A_L, DiscriminantGroup)
# form_codomain is FormCodomain.torsion_bilinear(ZZ) -- QQ/ZZ-valued

# 5. Properties
assert A_L.cardinality() == abs(L.gram_matrix().det())  # = 3
assert A_L.invariants() == (3,)

# 6. Bilinear form values in QQ/ZZ
g = A_L.gens()[0]
assert A_L.b(g, g) in QQ/ZZ  # Phase 0 patches

# 7. Quadratic form values in QQ/2ZZ (when L is even)
assert L.is_even()
assert A_L.q(g) in QQ/(2*ZZ)  # Phase 0 patches

# 8. Lift returns DualLattice element
assert g.lift().parent() is L_star
assert g.lift().discriminant_class() == g
```

The point: none of this required special-casing "free lattice discriminant
group" vs "torsion bilinear module". The cokernel of a BilinearModule
morphism automatically produced a TorsionBilinearModule with the correct
descended form, and the promotion logic identified it as a
DiscriminantGroup because the morphism came from the L -> L\* path.


## Key Architectural Decisions

**BilinearModule stores a BilinearForm object, not just a Gram matrix.** The
form knows its codomain. When computing induced forms on subquotients, the
codomain changes (ZZ -> QQ -> QQ/ZZ), tracked through FormCodomain.

**Cokernel promotion is general, not special-cased.** The cokernel of any
BilinearModuleMorphism produces a BilinearModule. Promotion to subclasses
is determined by examining the cokernel module's properties.

**`_Hom_` dispatches from the category.** Sage's `Parent._Hom_` is the
official hook for customizing hom-set construction.

**Elements are genuine Sage ElementWrapper instances.** Non-negotiable for
Sage's `Map.__call__` to work. The wrapped Sage element is the FGP module
element.

**No ambient module assumption.** BilinearModules are defined by (generators,
Gram matrix, codomain). Not subsets of any ambient space.

**General R, specialized at ZZ.** All BilinearModule code is parameterized
by `R = self.base_ring()`. Lattice-specific code references ZZ directly.
The same cokernel code works for any PID R.


## Verification Strategy

### Per-step unit tests

Each step has its own test verifying isolated behavior:
- Categories: BilinearModules(ZZ) is genuine, parents declare membership
- FormCodomain: All four cases construct correctly
- Forms: Evaluation for ZZ-valued and QQ-valued cases
- BilinearModule: Construction, generators, form evaluation, twist, direct sum
- FreeBilinearModule: Over ZZ and QQ, rank, generators
- TorsionBilinearModule: From invariants, form evaluation in QQ/ZZ
- HomSpaces/Morphisms: element\_from\_\*, kernel, image, cokernel
- DualLattice: Inclusion morphism, dual basis, form evaluation
- DiscriminantGroup: Cokernel construction, bilinear/quadratic form values
- Lattice: Named constructors, discriminant\_group via cokernel path

### Spec conformance tests

Run the assertions from each spec file:
- `tests/lattice_spec/interface_semantics.sage` (constructors, elements,
  discriminant forms, isotropic orbits, eigenlattices)
- `tests/lattice_spec/interface_extensions.sage` (dual, discriminant lifts,
  direct sums, O(U), O(U(2)), roots, Weyl, Eichler)
- `tests/lattice_spec/more_specs.sage` (Coble geometry, dual functionals,
  twist semantics, torsion bilinear modules, scalar rescaling)
- `tests/sage_spec/lattice_methods.sage` (U(2) orthogonal group, span, perp,
  stabilizer, dual quotients)

### Integration tests by family

Per `tests/LATTICE_TEST_STYLE.md`:
- A\_n: Gram, det = n+1, signature (n,0), even, scale = 2,
  disc group = Z/(n+1)
- D\_n: Gram, det = 4, signature (n,0), even, disc group depends on n mod 4
- E\_6, E\_7, E\_8: Fixed Gram, specific disc groups
- U: Unimodular hyperbolic, self-dual, trivial disc group
- U(n): det = -n^2, disc group = (Z/n)^2 with specific form
