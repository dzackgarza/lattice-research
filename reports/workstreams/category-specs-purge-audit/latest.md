# Category Specs Purge Audit

This report records the salvage decision for the rejected `origin/main` tail after
`9769adf2`. The acceptance standard is source-grounded mathematical/API
correctness, not downstream ledger reduction.

Accepted salvage is in `1440c8ff`. The old rejected history remains reachable at
`safety/pre-purge-20260525-category-spec-ledger-gaming`.

No post-salvage ledger refresh is committed here. The existing mypy ledger remains
the pre-salvage artifact until the report recipes are rerun from the accepted
source state.

## Accepted Source-Grounded Hunks

| Source commits | Kept in `1440c8ff` | Source basis |
| --- | --- | --- |
| `0e7bd2a` | `PolynomialRings.ParentMethods.completion` imports and passes `infinity` instead of the prelude-only `oo` spelling. | Sage source defines `infinity` in `sage/rings/infinity.py:1730`; polynomial-ring completion accepts infinite precision in `sage/rings/polynomial/polynomial_ring.py:620`. |
| `00af6a4`, `b2c42c7` | Set-family, finite-set, finite-countable, recursive-enumerated, and image-subobject Python protocol methods use `int` for `__len__`/`__hash__`. | Python data model and Sage implementations at `finite_enumerated_sets.py:83`, `family.pyx:753`, `image_set.py:197`, and `recursively_enumerated_set.pyx:550`. |
| `f119142` | Finite-rank free modules restate finite rank as `Integer`, dual as `DualModule`, and use the rank only at Python `range` boundaries. Ordered-basis order routes through the existing `basis_index_set()` helper. | `FiniteRankFreeModule.rank`, `dual`, and finite-rank tensor methods are public Sage methods at `finite_rank_free_module.py:622`, `2675`, `1618`, `2369`, `2759`, `2797`, and `2873`. |
| `ab24a59` | Integral-lattice `LLL` is the no-argument, lattice-returning surface, kept as an abstract spec obligation rather than replaying the rejected final Sage-specific body. The `short_vectors_up_to_sign` call uses a precise Sage lattice cast instead of `Any`. | Sage `FreeQuadraticModule_integer_symmetric.LLL` is no-argument and returns a sublattice at `free_quadratic_module_integer_symmetric.py:1472`. |

## Replayed As Aligned

| Source commit | Local replacement | Disposition |
| --- | --- | --- |
| `4f1b1da` | `dbcc98bb` | Kept. It rejects fake `Morphism.is_invertible` stubbing and keeps invertibility on the local End/Aut mathematical surface. |

## Rejected Commits

| Commit | Disposition |
| --- | --- |
| `eaebf6b` | Rejected. Only removes `@override` from the finite-rank issue-5 family; the source-backed fix belongs in `sage-stubs`. |
| `f015de4` | Rejected report refresh based on rejected finite-rank consumer edits. |
| `0e7bd2a` | Partly mined for `infinity`; override-deletion hunks remain rejected. |
| `64767af` | Rejected. It replaces missing-sidecar pressure with local casts and consumer-side module/countable routing. |
| `00af6a4` | Partly mined for finite-countable `__len__`; override-deletion hunks remain rejected. |
| `2ca825` | Rejected report refresh based on rejected ownership edits. |
| `2ec5341` | Rejected. It removes override evidence and adds an interop cast, without a mathematical owner change. |
| `ccbde8c` | Rejected. It removes module predicate override obligations. |
| `29eb986` | Rejected. RationalField public methods are real Sage surfaces; deleting local override markers is not stub completion. |
| `eeb9dfe` | Rejected report refresh based on rejected ownership edits. |
| `267dd6` | Rejected report refresh; downstream evidence must follow accepted source or stub changes. |
| `fc527e` | Rejected report refresh; downstream evidence must follow accepted source or stub changes. |
| `01190d` | Rejected report refresh; downstream evidence must follow accepted source or stub changes. |
| `f70e2b` | Rejected report refresh; downstream evidence must follow accepted source or stub changes. |
| `384ba0` | Rejected report refresh; downstream evidence must follow accepted source or stub changes. |
| `a2f35e` | Rejected. It handles the named commutative-ring extension and polynomial completion pressure by consumer receiver casts, broad keyword forwarding, and local NotImplemented guards. |
| `9adf1c` | Rejected. It removes `@final` from set providers as a QC accommodation without a source-grounded replacement owner. |
| `b2c42c` | Partly mined for Python dunder protocol returns; `Cardinality`/`SetElement` ontology rewrites remain rejected. |
| `a9cffd` | Rejected. It relaxes formed-module finality instead of recording a source-grounded extension-hook owner. |
| `9b1400` | Rejected. Set-enumeration signature broadening and `SageCategory` return changes are static-model/interop appeasement, not accepted spec design. |
| `46cf7e` | Rejected. It widens `_element_constructor_` to `object` and deletes image subobject obligations for `lift`, `retract`, and `_sympy_`. |
| `0fb6a7` | Rejected. Topological `SageCategory`/cast changes are a static-model lane, not a mathematical spec correction. |
| `6d67ac` | Rejected. Algebra `SageCategory`/cast return changes are a static-model lane, not a mathematical spec correction. |
| `fbffa3` | Rejected. Over-Dedekind rank broadening and predicate-provider deletion weaken the lattice surface. |
| `df5e3b` | Rejected. Poset category return changes and selector finality changes are static-model appeasement. |
| `ab24a5` | Partly mined for integral-lattice LLL/precise cast; lattice Hom base rewrites, Poset broadening, finality removals, and report refreshes remain rejected. |
| `f11914` | Partly mined for finite-rank and ordered-basis corrections; submodule operation deletions, generic free-rank narrowing, and report-count framing remain rejected. |
| `142f8c` | Rejected report refresh based on rejected reductions. |
| `ee9ad7` | Rejected. It adds a broad local cast layer in module constructors to appease current stubs. |
| `1e28e1` | Rejected. Literal `0`/`1` defaults are allowed Sage-style notation; `Integer(0)` rewrites were type appeasement. |
| `7fb186` | Rejected report refresh based on rejected constructor/default changes. |
| `556c6d` | Rejected. Set-leaf cast waves, `SageCategory` return changes, and broad constructor/input domains need a separate source-map decision rather than PR #6 credit. |
| `583980` | Rejected report refresh based on rejected set-leaf reductions. |

## Boundary Ruling

The purge is not a claim that the rejected commits contain no true statements. It
is a claim that their original commit units are not acceptable evidence for
`sage-stubs` issue #5 or category-spec completion. Future mining must enter as a
new source-grounded commit like `1440c8ff`, not by replaying the rejected commits.
