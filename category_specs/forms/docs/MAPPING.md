# Forms Mapping

`FormedModules(R)` is the forms-subtree owner for modules equipped with forms.
It is the named spelling of `Modules(R, dispatch=False).WithForms()`.

## Ownership

| Surface | Owner | Notes |
| --- | --- | --- |
| `Modules(R).WithForms()` | `forms.subcategories.with_forms._WithForms` | Modules keeps the Sage-compatible route; forms owns the class and method surface. |
| `Modules(R).WithForms().Bilinear()` | `forms.subcategories.bilinear._BilinearModules` | Owns bilinear evaluation and generic bilinear predicates. |
| `Modules(R).WithForms().Quadratic()` | `forms.subcategories.quadratic._QuadraticModules` | Owns quadratic evaluation. |
| Symmetric, alternating, nondegenerate, definite, indefinite, integral, rational bilinear axioms | `forms.subcategories.*` | These are formed-module properties, not lattice-only properties. |
| `divisibility(v)` for symmetric bilinear elements | `forms.subcategories.symmetric.SymmetricBilinearModulesCategory.ElementMethods` | The invariant definition is the pairing-image submodule `<b(v, M)>` of the form codomain `S`; for `S = R`, this is an ideal. |
| Form-preserving morphisms between formed modules | `C.HomCategory().Of(M, N)` for `C <= FormedModules(R)` | A candidate map preserves form data exactly when it is contained in the Hom object of the formed-module category. |
| Isometries of formed modules | `C.HomCategory().Of(M, N)` plus generic isomorphism; automorphism case `C.AutCategory().Of(M)` | Form preservation is already Hom containment. The isometry question is invertibility or isomorphism inside that category. |
| Free bilinear modules | `forms.subcategories.free_bilinear._FreeBilinearModules` | First tier where Gram matrices, determinant, and discriminant are universally meaningful. |
| Finite-rank free formed-module chain used by `Lattices(R)` | `forms.chain` | Lattices imports this chain and adds only the named `Lattice` endpoint. |
| Finite torsion quadratic modules | `forms.subcategories.torsion_quadratic_modules._TorsionQuadraticModules` | Modules keeps `TorsionQuadraticModules()` as a compatibility constructor route. |
| `Lattices(R)` | `lattices.chain._Lattices` | Lattice-specific endpoint and lattice construction categories remain in `lattices`. |

## Compatibility Routes

The module and lattice import paths remain valid:

- `category_specs.modules.subcategories.with_forms._WithForms`
- `category_specs.modules.subcategories.bilinear._BilinearModules`
- `category_specs.modules.subcategories.quadratic._QuadraticModules`
- `category_specs.modules.subcategories.torsion_quadratic_modules._TorsionQuadraticModules`
- `category_specs.lattices.subcategories.symmetric._SymmetricBilinearModules`
- analogous lattice paths for alternating, nondegenerate, definite, indefinite,
  integral, rational, and free bilinear categories.

Those files are shims. New specs should import or document formed-module ownership
through `forms`.

## Boundary With Tensor Components

`TensorAlgebraComponents(R)` owns tensor component modules and tensor elements.
A scalar-valued bilinear form may be constructed there as a `(0,2)` tensor. The object
becomes a formed module only when attached as form data to a module category in this
subtree.

## Twisted And Semilinear Form Data

No separate `TwistedForms` category is admitted at this time.

The grounded form-object contract already records the relevant data on the form object:
the tensor-degree source, codomain module, and scalar-action endomorphism `sigma`.
`ModulesWithForms(R)` therefore remains the owner for pairs `(M, f)` with semilinear
form data, while the named forms subcategories own the cases currently admitted by the
mapping:

- bilinear forms use tensor degree `2` and `sigma = id_R`;
- quadratic forms use tensor degree `1` with the current quadratic scalar action;
- alternating, symmetric, integral, rational, finite-torsion, and quotient-valued cases
  refine the existing formed-module chain.

Tensor-component duals remain tensor-component objects until attached as form data to a
module. A future twisted-form subcategory may be admitted only if a concrete public
method or constructor is mathematically wrong without a distinct owner beyond
`FormedModules(R)` plus tensor-component/Hom-category structure.

## Form-Preserving Morphisms And Isometries

For `C <= FormedModules(R)`, the form-preserving maps from `M` to `N` are the elements
of `C.HomCategory().Of(M, N)`. A plain `R`-module morphism belongs to
`Modules(R).HomCategory()` first; it is promoted into the formed-module Hom object only
when it satisfies the defining form-compatibility equation.

Consequences:

- do not introduce a standalone public `is_form_preserving()` predicate as the owner of
  form preservation;
- `is_isometry()` on a formed-module morphism is only a compatibility query for
  isomorphism inside an already form-preserving Hom object;
- `orthogonal_group()` is `C.AutCategory().Of(M)` for the relevant formed-module
  category `C`;
- matrix equations are implementation checks under explicit presentations, not the
  public definition of preservation or isometry.

Metric-space isometries in `TopologicalSpaces().HomCategory()` are a separate surface
and must not be routed through this formed-module owner.

## Symmetric Bilinear Divisibility

For a symmetric bilinear module `(M, b)` with `b: M x M -> S`, the element
divisibility surface is:

`divisibility(v) = < b(v, w) : w in M > <= S`.

This is a submodule of the form codomain `S`. In the scalar-valued case `S = R`, it is
an ideal of `R`. Coordinate gcds, principal generators, or old Sage lattice
presentations are only possible representations after extra hypotheses are recorded;
they are not the mathematical definition and do not create a free-module owner.

## Boundary With Lattices

Lattices are integral, nondegenerate, symmetric, finite-rank free bilinear modules with
the additional named `Lattice` axiom. Formed-module methods such as `b`, `gram_matrix`,
`dual_lattice`, and `orthogonal_group` remain owned by forms. The quotient class map
`L^* -> L^*/L` belongs to `Lattices(R).DualObjects().ElementMethods` because it is
nontrivial on dual-lattice elements and zero on ordinary elements of `L`.
Lattice-specific specializations such as `OverIntegers`, `Even`, `Unimodular`, and
lattice construction categories remain owned by `lattices`.
