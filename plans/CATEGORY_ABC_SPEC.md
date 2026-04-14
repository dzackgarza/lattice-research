# ModulesWithForms Category: ABC Contracts

Authoritative specification of the category-level contract for the lattice
redesign.

This file supersedes the earlier `BilinearModules`-first framing. The
canonical top-level category is now `ModulesWithForms(R)`, modeled on
`sage.categories.modules.Modules` and specialized to finitely generated
modules over a PID.

An object of `ModulesWithForms(R)` is a pair `(M, f)` where:

- `R` is a PID,
- `K := Frac(R)`,
- `M` is a finitely generated `R`-module, with free and torsion parts in
  general,
- `f` is either:
  - a bilinear morphism `M \otimes_R M -> S`, or
  - a quadratic morphism `M -> S`,
- `S` is either:
  - a subring of `K` containing `R`, or
  - a quotient of `K`, presently required at minimum to support `K/R`
    and `K/2R`.

Concrete implementations may enforce the currently supported codomain
families by assertions and validation. The public contract is about the
mathematics, not the current backend limits.

The category owns the Sage-style subcategory machinery:

- `Bilinear()`
- `Quadratic()`
- `Free()`
- `Torsion()`
- `NonDegenerate()`
- `Integral()`
- `Rational()`
- `TensorProducts()`
- `CartesianProducts()`
- `DualObjects()`
- `Homsets()`

Downstream categories are intersections of these axioms. For example:

```text
Lattices(R)
    := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()

RationalLattices(R)
    := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()
```

The older names `BilinearModules` and `QuadraticModules`, if retained at
all, are thin aliases for these subcategories. They are not separate
top-level category contracts anymore.


## Form Codomains

The codomain descriptor remains a separate validated object. It records:

- the base PID `R`,
- the fraction field `K = Frac(R)`,
- the actual codomain `S`,
- whether `S` is a subring codomain or a quotient codomain.

The required first-pass codomain strata are:

- `Integral`: `S = R`
- `Rational`: `S = K`
- quotient-valued examples used by discriminant descent:
  - `S = K / R`
  - `S = K / 2R`

These codomain predicates are orthogonal to the free/torsion and
bilinear/quadratic predicates.


## Form ABCs

```python
from abc import ABC, abstractmethod


class Form(ABC):

    @abstractmethod
    def domain(self) -> ModuleWithForm: ...
    """The object (M, f) this form belongs to."""

    @abstractmethod
    def codomain(self) -> FormCodomain: ...
    """The codomain descriptor for the values of the form."""

    @abstractmethod
    def arity(self) -> int: ...
    """1 for quadratic forms, 2 for bilinear forms."""


class BilinearForm(Form):

    def arity(self) -> int:
        return 2

    @abstractmethod
    def gram_matrix(self) -> Matrix: ...
    """Gram matrix with respect to the canonical generators."""

    @abstractmethod
    def evaluate(
        self,
        left: ModuleWithFormElement,
        right: ModuleWithFormElement,
    ) -> object: ...
    """Evaluate the bilinear form."""


class QuadraticForm(Form):

    def arity(self) -> int:
        return 1

    @abstractmethod
    def gram_matrix(self) -> Matrix: ...
    """Quadratic Gram data with respect to the canonical generators."""

    @abstractmethod
    def evaluate(self, element: ModuleWithFormElement) -> object: ...
    """Evaluate the quadratic form."""

    @abstractmethod
    def polar_bilinear_form(self) -> BilinearForm: ...
    """Return the associated polar bilinear form."""
```

Quadratic structure is a refinement, not the default organizing principle.
The common base is meant to support `L`, `L^*`, and `A_L` uniformly with a
bilinear-first public vocabulary. In particular, code may use `v.q()`
uniformly for diagonal evaluation:

- on bilinear objects: `v.q() := b(v, v)`,
- on quadratic objects: `v.q()` is the genuine quadratic value.


## `ModulesWithForms(R)`

```python
class ModulesWithForms(Category_module):
    """Category of finitely generated R-modules equipped with a form."""

    def super_categories(self):
        return [Modules(self.base_ring()).FinitelyPresented()]

    def additional_structure(self):
        return self
```

`additional_structure()` returns `self`, not `None`: a module map between
two objects with forms is not automatically form-preserving.


## `ModulesWithForms.SubcategoryMethods`

This category should reproduce and specialize the Sage machinery exposed by
`sage.categories.modules.Modules`, especially the pattern around
`SubcategoryMethods`, `TensorProducts`, `CartesianProducts`, and
`DualObjects`.

```python
class ModulesWithForms(Category_module):

    class SubcategoryMethods:

        @cached_method
        def base_ring(self):
            ...

        @cached_method
        def Bilinear(self):
            return self._with_axiom("Bilinear")

        @cached_method
        def Quadratic(self):
            return self._with_axiom("Quadratic")

        @cached_method
        def Free(self):
            return self._with_axiom("Free")

        @cached_method
        def Torsion(self):
            return self._with_axiom("Torsion")

        @cached_method
        def NonDegenerate(self):
            return self._with_axiom("NonDegenerate")

        @cached_method
        def Integral(self):
            return self._with_axiom("Integral")

        @cached_method
        def Rational(self):
            return self._with_axiom("Rational")

        @cached_method
        def TensorProducts(self):
            return TensorProductsCategory.category_of(self)

        @cached_method
        def CartesianProducts(self):
            return CartesianProductsCategory.category_of(self)

        @cached_method
        def DualObjects(self):
            return DualObjectsCategory.category_of(self)

        dual = DualObjects
```

Semantics of the main axioms:

- `Bilinear`: the primary form has arity 2.
- `Quadratic`: the primary form has arity 1.
- `Free`: the underlying module is torsion-free and free of finite rank.
- `Torsion`: the underlying module is finite torsion.
- `NonDegenerate`: the associated bilinear pairing has zero radical.
- `Integral`: codomain is exactly `R`.
- `Rational`: codomain is exactly `K = Frac(R)`.

Objects may carry more structure than one axiom records. For example, an
even discriminant form may be implemented as a torsion bilinear object with
an additional quadratic refinement. The category contract should not force a
second top-level hierarchy for that case.


## `ModulesWithForms.ParentMethods`

```python
class ModulesWithForms(Category_module):

    class ParentMethods(ABC):

        @abstractmethod
        def form(self) -> Form: ...
        """The primary form carried by this object."""

        @abstractmethod
        def gens(self) -> tuple[ModuleWithFormElement, ...]: ...
        """Canonical generators."""

        @abstractmethod
        def zero(self) -> ModuleWithFormElement: ...
        """The additive identity."""

        @abstractmethod
        def base_ring(self) -> Ring: ...
        """The PID R."""

        @abstractmethod
        def free_part(self) -> ModuleWithForm: ...
        """The free summand with the restricted/induced form data."""

        @abstractmethod
        def torsion_part(self) -> ModuleWithForm: ...
        """The torsion summand with the restricted/induced form data."""

        @abstractmethod
        def Hom(self, other: ModuleWithForm) -> ModuleWithFormHomSpace: ...
        """The hom space in ModulesWithForms(R)."""

        @abstractmethod
        def dual(self) -> ModuleWithForm: ...
        """The dual object in the appropriate DualObjects subcategory."""

        @abstractmethod
        def span(
            self,
            elements: Iterable[ModuleWithFormElement],
        ) -> ModuleWithForm: ...
        """The subobject generated by the given elements."""

        @abstractmethod
        def cardinality(self) -> CardinalNumber: ...
        """Cardinality of the underlying set."""

        def End(self) -> ModuleWithFormHomSpace:
            return self.Hom(self)
```

The generic contract intentionally stays thin. Arity-specific operations
belong to the `Bilinear()` and `Quadratic()` refinements.


## `ModulesWithForms.ElementMethods`

```python
class ModulesWithForms(Category_module):

    class ElementMethods(ABC):

        @abstractmethod
        def parent(self) -> ModuleWithForm: ...

        @abstractmethod
        def __add__(self, other: ModuleWithFormElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def __neg__(self) -> ModuleWithFormElement: ...

        @abstractmethod
        def _lmul_(self, scalar: RingElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def _rmul_(self, scalar: RingElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def __rmul__(self, scalar: RingElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def __eq__(self, other: object) -> bool: ...

        @abstractmethod
        def __hash__(self) -> int: ...

        @abstractmethod
        def to_vector(self) -> Vector: ...
        """Coordinates with respect to parent().gens()."""

        def span(self) -> ModuleWithForm:
            return self.parent().span([self])
```

Uniform diagonal syntax:

- `v.q()` is allowed everywhere.
- In `Bilinear()`, it means `b(v, v)`.
- In `Quadratic()`, it means evaluation of the quadratic form.


## `ModulesWithForms.MorphismMethods`

```python
class ModulesWithForms(Category_module):

    class MorphismMethods(ABC):

        @abstractmethod
        def domain(self) -> ModuleWithForm: ...

        @abstractmethod
        def codomain(self) -> ModuleWithForm: ...

        @abstractmethod
        def __call__(self, v: ModuleWithFormElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def to_matrix(self) -> Matrix: ...
        """Matrix with respect to canonical generators."""

        @abstractmethod
        def kernel(self) -> ModuleWithForm: ...

        @abstractmethod
        def image(self) -> ModuleWithForm: ...

        @abstractmethod
        def cokernel(self) -> ModuleWithForm: ...
        """The actual cokernel object with descended form data."""

        @abstractmethod
        def is_form_preserving(self) -> bool: ...

        def is_injective(self) -> bool:
            ...

        def is_surjective(self) -> bool:
            ...

        def is_bijective(self) -> bool:
            return self.is_injective() and self.is_surjective()
```

Important negative constraints from the corrections:

- morphisms are not containers,
- morphisms do not have `perp`,
- cokernels must construct the correct target object rather than a helper
  invariant package.


## `ModulesWithForms.Homsets.ParentMethods`

```python
class ModulesWithForms(Category_module):

    class Homsets(HomsetsCategory):

        def extra_super_categories(self):
            return [Modules(self.base_category().base_ring())]

        class ParentMethods(ABC):

            @abstractmethod
            def domain(self) -> ModuleWithForm: ...

            @abstractmethod
            def codomain(self) -> ModuleWithForm: ...

            @abstractmethod
            def element_from_dict(
                self,
                mapping: dict[ModuleWithFormElement, ModuleWithFormElement],
            ) -> ModuleWithFormMorphism: ...

            @abstractmethod
            def element_from_matrix(self, matrix_data: Matrix) -> ModuleWithFormMorphism: ...

            @abstractmethod
            def element_from_images(
                self,
                images: Sequence[ModuleWithFormElement],
            ) -> ModuleWithFormMorphism: ...

            @abstractmethod
            def __contains__(self, f: object) -> bool: ...

            def identity(self) -> ModuleWithFormMorphism:
                ...

            def zero(self) -> ModuleWithFormMorphism:
                ...
```

Hom-space containment owns the structural checks. If a specialized homset
represents isometries, its `__contains__` method owns the form-preservation
test.


## Bilinear Refinement

`ModulesWithForms(R).Bilinear()` is the primary working stratum for Phases
0 and 1.

```python
class ModulesWithForms(Category_module):

    class Bilinear(CategoryWithAxiom_over_base_ring):

        class ParentMethods(ABC):

            @abstractmethod
            def bilinear_form(self) -> BilinearForm: ...

            def form(self) -> BilinearForm:
                return self.bilinear_form()

            def b(
                self,
                left: ModuleWithFormElement,
                right: ModuleWithFormElement,
            ) -> object:
                return self.bilinear_form().evaluate(left, right)

            def gram_matrix(self) -> Matrix:
                return self.bilinear_form().gram_matrix()

            @abstractmethod
            def twist(self, scalar: RingElement) -> ModuleWithForm: ...

            @abstractmethod
            def radical(self) -> ModuleWithForm: ...

        class ElementMethods(ABC):

            def b(self, other: ModuleWithFormElement) -> object:
                return self.parent().b(self, other)

            def q(self) -> object:
                return self.parent().b(self, self)

            def is_isotropic(self) -> bool:
                return self.q() == 0

        class MorphismMethods(ABC):

            def is_isometry(self) -> bool:
                return self.is_form_preserving()
```

This is the layer used for lattices, rational lattices, duals, and the
first-pass treatment of discriminant objects.


## Quadratic Refinement

`ModulesWithForms(R).Quadratic()` is a refinement used when the genuine
quadratic data matters, for example for `K/2R`-valued refinements.

```python
class ModulesWithForms(Category_module):

    class Quadratic(CategoryWithAxiom_over_base_ring):

        class ParentMethods(ABC):

            @abstractmethod
            def quadratic_form(self) -> QuadraticForm: ...

            def form(self) -> QuadraticForm:
                return self.quadratic_form()

            @abstractmethod
            def associated_bilinear_object(self) -> ModuleWithForm: ...
            """The same underlying module equipped with the polar form."""

            def polar_bilinear_form(self) -> BilinearForm:
                return self.quadratic_form().polar_bilinear_form()

        class ElementMethods(ABC):

            def q(self) -> object:
                return self.parent().quadratic_form().evaluate(self)
```

Quadratic objects should not fork the architecture. They sit inside the
same `ModulesWithForms` framework and reuse the same module, morphism,
homset, tensor, Cartesian-product, and dual machinery whenever the
mathematics allows it.


## Tensor Products, Cartesian Products, and Duals

The category must expose Sage-style construction subcategories analogous to
`sage.categories.modules.Modules`.

```python
class ModulesWithForms(Category_module):

    class CartesianProducts(CartesianProductsCategory):

        def extra_super_categories(self):
            return [self.base_category()]

    class TensorProducts(TensorProductsCategory):

        def extra_super_categories(self):
            return [self.base_category()]

        class ParentMethods(ABC):

            @abstractmethod
            def tensor_factors(self) -> tuple[ModuleWithForm, ...]: ...
```

Required semantics:

- `CartesianProducts` model direct products with componentwise module
  structure and product form data.
- `TensorProducts` model tensor products of objects with forms whenever the
  codomain arithmetic supports the induced form; the first required target
  is the bilinear integral/rational stratum.
- `DualObjects()` mirrors the Sage construction but is not required to stay
  inside the same codomain stratum. For example, the dual of an integral
  nondegenerate free bilinear object typically lands in the rational
  bilinear stratum.


## Cokernels and Discriminant Descent

This is the main reason the contract is organized at the
`ModulesWithForms` level rather than around separate lattice and
discriminant hierarchies.

Suppose:

- `(L_2, beta_2)` is a free bilinear object over `R` with codomain `K`,
- `i: L_1 -> L_2` is a morphism in `ModulesWithForms(R).Bilinear()`,
- `beta_2(v, i(L_1)) \subseteq R` for every `v in L_2`.

Then the cokernel `coker(i)` carries a well-defined descended bilinear form
with codomain `K/R`:

```text
beta_bar([v], [w]) := beta_2(v, w) mod R  in K/R.
```

This is the abstract mechanism behind:

```text
L  ->  L^*  ->  A_L = coker(L -> L^*).
```

If additional quadratic data descends, it should be expressed as a
quadratic refinement on the same cokernel object, typically with codomain
`K/2R`.

Implementation note:

- the public object is the actual cokernel of a specific morphism,
- computing it via Smith normal form invariants is acceptable internally,
- presenting only the invariant package is not acceptable as the public
  semantics.


## Named Downstream Categories

These names are ordinary intersections of `ModulesWithForms` axioms:

```text
Lattices(R)
    := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()

RationalLattices(R)
    := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()

DiscriminantBilinearModules(R)
    := ModulesWithForms(R).Bilinear().Torsion()
       with quotient-valued codomain, typically K/R
```

The point is that `L`, `L^*`, and `A_L` live in one framework and differ by
intersecting axioms, not by switching between unrelated object systems.


## Notes on Sage Wiring

- The design should follow the category pattern of
  `sage.categories.modules.Modules`, especially the source around
  `SubcategoryMethods`, `CartesianProducts`, and `TensorProducts`.
- `_Hom_` is an internal Sage hook. The public contract is `M.Hom(N)`.
- Elements must be genuine Sage `Element` or `ElementWrapper` instances.
- Concrete implementations may store Sage, Julia, or other backend objects,
  but those are calculation engines, not the public API.
