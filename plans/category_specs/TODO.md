# Category Spec Todo

This list tracks live category-spec work. It is not a decision log; concrete human
choices live in `NEEDS_DECISIONS.md`. Completed items leave this file; git history is
the archive.

## Audit Todo

- [ ] Resolve the remaining q-adic variadic-split concrete-coverage frontier.
  Concrete smoke coverage now exists for the former admitted-name frontiers:
  `Modules(E).Constructors().FPModuleFromCokernelMap` uses the cokernel of the
  identity morphism of a Sage `FreeGradedModule`;
  `Modules(ZZ).Constructors().IntegerLatticeFromOrderElement` uses a
  `CyclotomicField(5)` absolute-order element;
  `Modules(QQ).Quotients().ParentMethods.quotient_by_*` routes through Sage
  quotient subspaces, relation matrices, and relation rows;
  `Algebras(R).ParentMethods.subalgebra` uses `MatrixSpace(QQ, 2).subalgebra`;
  the split algebra ideal names route to Sage `ideal_submodule(..., side=...)` and
  `principal_ideal(..., side=...)` on `MatrixSpace(QQ, 2)`; and
  `Lattices(ZZ).OverIntegers().ParentMethods.short_vectors` /
  `short_vectors_up_to_sign` use `IntegralLattice("A2").short_vectors`.

  Remaining `Rings().Constructors().ZqWithPrecisionCaps` /
  `QqWithPrecisionCaps` frontier:
  - Searched: `rings/docs/MAPPING.md`, `rings/docs/SAGE_INVENTORY.md`,
    `rings/smoketest.sage`, `rings/__init__.py`, Sage
    `sage/rings/padics/factory.py` around `get_key_base`, `Zq`, `Qq`, and
    `pAdicExtension_class`, Sage `sage/rings/padics/generic_nodes.py`, direct Sage
    `Zq(25, prec=4, type="lattice-cap", names="a")`,
    `Zq(25, prec=(4, 8), type="lattice-cap", names="a")`,
    `Qq(25, prec=4, type="lattice-cap", names="a")`, and
    `Qq(25, prec=(4, 8), type="lattice-cap", names="a")`, plus the project
    `Rings().Constructors().ZqWithPrecisionCaps(25, 4, 8, names="a")` and
    `QqWithPrecisionCaps(25, 4, 8, names="a")` runs.
  - Found: Sage `Zp`/`Qp` base constructors canonicalize lattice precision pairs,
    but installed Sage `Zq`/`Qq` extension constructors coerce non-`Integer`
    precision with `prec = Integer(prec)` before calling `ExtensionFactory`. Direct
    Sage pair-precision runs fail with
    `TypeError: unable to coerce <class 'tuple'> to an integer`; scalar
    lattice-precision extension runs also fail before a usable extension parent is
    returned (`Zq`: `TypeError: cannot unpack non-iterable sage.rings.integer.Integer
    object`; `Qq`: `TypeError:
    pAdicLatticeGeneric._element_constructor_() got an unexpected keyword argument
    'absprec'`). `pAdicExtension_class` receives a scalar extension precision and
    dispatches through `ext_table`, not a documented pair-cap extension route.
  - Conclusion: inference — the `ZqWithPrecisionCaps` / `QqWithPrecisionCaps` split
    names remain blocked in the installed Sage path; implementing them concretely
    needs real design/source work around an extension-specific lattice-precision API
    or an upstream fix, not a mechanical wrapper.
  - Confidence: High.
  - Gaps: upstream Sage issue trackers or unreleased Sage branches may contain a fix,
    but the installed Sage source and docs do not expose a working local fixture.
- [ ] Audit for uniformizing opportunities across category trees where several modules
  express the same mathematical construction with different names or shapes.
- [ ] Add mathematical docstrings whenever a spec introduces a new method. The docstring
  should define the method mathematically rather than merely restating its return type.
