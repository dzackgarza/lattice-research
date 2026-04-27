# Cat Triage

Source for this pass: `cat/docs/SAGE_INVENTORY.md`, `cat/docs/MAPPING.md`,
installed Sage source under `sage/categories/`, official Sage documentation, and the
local smoke surface `cat/smoketest.sage`.

## Current Alignment

- `Cat()` accepts Sage/project category objects as objects of the category of
  categories.
- `Cat().__contains__` is intentionally object-only: functors are elements of
  `A.Hom(B)`, not objects of `Cat()`.
- `Cat.ParentMethods` is the canonical surface for category-object operations:
  `Hom`, `End`, `Aut`, `leq`, `geq`, `<=`, and `>=`.
- Registration preserves the re-exported Sage base-class mechanism and adapts the
  canonical `Cat.ParentMethods` surface into Sage's category-object method path.
- `A.Hom(B)` and `A.End()` reuse Sage `Hom`/`End` parents in category `Cat()`.
- `A.Aut()` refines `A.End()` through the generic repository-level `Autset`
  construction.
- `CatHomsets` inherits the generic `HomsetsOf` pattern; `_CatEndsets` and
  `_CatAutsets` inherit `GenericEndsets` and `GenericAutsets`.
- Generic homset object methods such as `domain` and `codomain` come from the
  repository-level homset surface. Cat only adds the functor-specific element
  surface.
- The previous `fixed_points()` endofunctor method was removed. Sage provides no
  general computable fixed-point operation for endofunctors.

## Remaining Design Work

- Some subtree category classes already define direct `Hom` methods for their own
  object-level homset constructors. Those direct methods may shadow the Cat-level
  category-object `Hom` at runtime and should be reviewed in a later uniformization
  pass.
- Natural transformations are not modeled. The current Cat morphism surface is Sage
  functors and construction functors.
- The generic Sage functor API does not provide a uniform invertibility certificate.
  Concrete autofunctor membership beyond the generic `Autset` condition remains a
  future refinement.

## Source Note: Sage Generic Autsets

- Searched: installed
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/homsets.py`,
  installed `sage/categories/homset.py`, official Sage documentation pages for
  category and homset machinery, and local `category_specs/homsets/__init__.py`.
- Found: Sage provides `HomsetsCategory`, `HomsetsOf`, `Homsets`, `Homsets.Endset`,
  `Hom(...)`, `End(...)`, and `Homset`. I found no installed generic Sage
  `Autset` category class.
- Conclusion: inference -- project `Autset` vocabulary is an extension over Sage's
  generic homset layer, while `Endset` maps to Sage's existing axiom.
- Confidence: High.
- Gaps: I did not search Sage's full git history or third-party Sage extensions.

## Validation Scope

Run `sage cat/smoketest.sage` after layout and documentation edits are complete.
This smoke is structural. It checks Cat instantiation, category-object membership,
functor homset instantiation, and standard construction navigation. It does not prove
that all other subtrees have completed the later uniformization refactor.
