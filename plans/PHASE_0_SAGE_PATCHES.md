# Phase 0: Sage Patches

Standalone monkeypatch modules that make existing Sage objects support the
syntax and semantics required by `tests/sage_spec/misc.sage`. These patches
are **prerequisites** for Phase 1: the BilinearModule category cannot work
over general R without them, and discriminant form descent requires QQ/ZZ and
QQ/2ZZ as working codomains.

Phase 0 does NOT touch the existing `src/lattices/` hierarchy. It creates
new files under `src/sage_patches/` that can be imported independently.

Canonical spec: `tests/sage_spec/misc.sage`.


## File Structure

```
src/sage_patches/
    __init__.py              # imports _install.install(); calls it
    ring_quotients.py        # ZZ/n syntax, ring quotient as ZZ-module
    fraction_quotients.py    # QQ/ZZ, QQ/nZZ quotient modules
    module_enrichment.py     # ZZ^n: dual, tensor, base_change, + = direct sum
    module_operations.py     # free_part, torsion_part, generator assignment
    hom_enrichment.py        # Hom spaces: element_from_*, cokernel().projection()
    completions.py           # ZZ.complete(p), ZZ.localize(p)
    _install.py              # Single entry point that applies all patches
```

## Dependency Order

```
ring_quotients          (no internal deps)
fraction_quotients      (depends on ring_quotients)
completions             (no internal deps)
module_enrichment       (depends on ring_quotients, fraction_quotients)
module_operations       (depends on module_enrichment)
hom_enrichment          (depends on module_enrichment, module_operations)
_install                (imports and applies all of the above)
```


## Module-by-Module Design


### `ring_quotients.py` -- ZZ/n syntax and ring quotient identification

#### What Sage provides natively

- `ZZ.quotient(2*ZZ)` returns `IntegerModRing(2)`.
- `ZZ / 2` raises `TypeError` -- `Rings.ParentMethods.__truediv__` blocks it.
- `IntegerModRing(p).is_field()` returns True for primes.
- `IntegerModRing(n) in Modules(ZZ)` returns False.

#### What to build

Monkeypatch `IntegerRing_class.__truediv__` to interpret `ZZ / n` as
`ZZ.quotient(n * ZZ)` when `n` is an integer, and as `ZZ.quotient(I)` when
`n` is a ZZ-ideal.

```python
def _zz_truediv(self, other):
    if other in ZZ:
        return self.quotient(ZZ.ideal(ZZ(other)))
    if isinstance(other, Ideal_generic) and other.ring() is ZZ:
        return self.quotient(other)
    return _original_zz_truediv(self, other)
```

Monkeypatch category containment so `IntegerModRing(n) in Modules(ZZ)` is
True. Z/nZ IS a cyclic ZZ-module; this is mathematically correct. The
cleanest approach: patch `Modules(ZZ).__contains__` to also accept
`IntegerModRing` instances. This avoids deep surgery on Sage's category
caching infrastructure.

#### Spec assertions covered

```python
Z2 = ZZ / (2*ZZ)
Z4 = ZZ / (4*ZZ)
assert Z2 == ZZ/2
assert Z4 == ZZ/4
assert Z2 in Modules(ZZ)
assert Z2 in Modules(Z2)
assert Z2.is_field() and not Z4.is_field()
```


### `fraction_quotients.py` -- QQ/ZZ, QQ/nZZ quotient modules

#### What Sage provides natively

- `QQ / ZZ` might not work natively. Sage has `QmodnZ(1)` for Q/Z, accessed
  via `QQ.quotient_ring(ZZ)` or similar -- needs investigation at
  implementation time.
- `QmodnZ(n)` elements have `.lift()` returning canonical representative.
- `QmodnZ(1)(1/2) == QmodnZ(1)(3/2)` should work.
- `QmodnZ(n)` is in "infinite commutative additive groups" -- NOT in
  `Modules(ZZ)`.

#### What to build

Ensure `QQ / ZZ` and `QQ / (n*ZZ)` produce `QmodnZ(1)` and `QmodnZ(n)`
respectively. This may require patching `QQ.__truediv__` or
`RationalField.__truediv__` to detect when the divisor is ZZ or a ZZ-ideal.

Patch `QmodnZ` to be recognized as a ZZ-module (same category containment
approach as ring_quotients).

Ensure `QmodnZ(n)` has `base_ring()` returning ZZ (likely needs
monkeypatching).

**Critical for Phase 1:** QQ/ZZ is the codomain for discriminant bilinear
forms, QQ/2ZZ for discriminant quadratic forms. These must work as targets
for form evaluation.

#### Spec assertions covered

```python
R = QQ/ZZ
assert R in Rings
assert R(1/2) == R(3/2)
assert R(3/2).lift() == QQ(1/2)
```

#### Investigation needed at implementation time

- Exact Sage class hierarchy for `QmodnZ`.
- Whether `QQ.__truediv__` already dispatches to `QmodnZ`.
- Whether `QmodnZ` has arithmetic operations (+, *, coercion from QQ)
  sufficient for form evaluation.


### `completions.py` -- ZZ.complete(p), ZZ.localize(p)

#### What Sage provides natively

- `ZZ.completion(5, 20)` returns `Zp(5, prec=20)`.
- `Localization(ZZ, (5,))` returns the localization.
- `Zp(5).fraction_field()` returns `Qp(5)`.
- `ZZ.fraction_field()` returns `QQ`.
- ZZ has NO `.complete()` or `.localize()` method.

#### What to build

```python
# One-liners on IntegerRing_class:
IntegerRing_class.complete = lambda self, p: Zp(p)
IntegerRing_class.localize = lambda self, p: Localization(ZZ, (p,))
```

These are mathematically unambiguous and require no design decisions.

#### Spec assertions covered

```python
S = ZZ.complete(5)
assert S == Zp(5)
assert (ZZ^3).base_change(S) == S^3
assert ZZ.fraction_field() == QQ
assert Zp(5).fraction_field() == Qp(5)

ZZ_L5 = ZZ.localize(5)
assert ZZ_L5 == Localization(ZZ, [5])
assert 1/5 in ZZ_L5 and 1/3 not in ZZ_L5
```


### `module_enrichment.py` -- ZZ^n as enriched FGP module

This is the most substantial patch module.

#### What Sage provides natively

- `ZZ^3` returns `FreeModule_ambient_pid` with `.gens()`, `.rank()`,
  `.Hom()`, `.direct_sum()`.
- Missing: `.dual()`, `.tensor()`, `.base_change()`, `.is_free()`,
  `.is_torsionfree()`, `.is_torsion()`.
- `M + M` means "span inside ambient" for free modules -- NOT direct sum.
- `FGP_Module` (quotient modules) lacks `.direct_sum()`.

#### What to build

Monkeypatch onto `FreeModule_ambient_pid` and/or `FGP_Module_class`:

**Predicate methods:**
- `is_free()`: True for free modules, check invariants for FGP.
- `is_torsionfree()`: True for free modules, check invariants for FGP.
- `is_torsion()`: False for free modules, check invariants for FGP.

**Dual:**
- `dual()` = `self.Hom(ZZ)` (the rank-1 free module as target). For ZZ^n
  this is isomorphic to ZZ^n. The returned object should be a proper
  ZZ-module (hom set in `Modules(ZZ)`).

**Tensor product:**
- `tensor(other)` and `__mul__` on parents: `ZZ^m * ZZ^n` gives
  `ZZ^(m*n)`. For mixed: `(ZZ^n).tensor(ZZ/p)` gives `(ZZ/p)^n`. Use FGP
  module construction with appropriate relations.
- **Parent `*` = tensor, element `*` = bilinear product.** Phase 1 handles
  element `*` via ElementWrapper; this module only patches parent `__mul__`.

**Base change:**
- `base_change(S)` = `self.tensor(S)` where S is a ring viewed as a
  ZZ-module via the structure map.

**Direct sum as `+`:**
- Redefine `__add__` on our enriched modules to mean direct sum, NOT span.
  The spec explicitly rejects the "ambient module" paradigm where `+` means
  span-in-ambient.
- `__pow__` for direct sum powers: `ZZ^3 == ZZ + ZZ + ZZ`.

**Module quotient:**
- `__truediv__` on modules: `M / (n*M)` produces the FGP quotient. Use
  Sage's existing `FGP_Module(M, n*M)` construction.

**Canonical isomorphisms as equalities:**
- `M/(2*M) == M.tensor(Z2)` -- this requires `__eq__` to recognize
  canonically isomorphic FGP modules. This may be the hardest part. One
  approach: define equality as isomorphism of the underlying FGP presentations
  (same invariants in the same order). Another: defer to Sage's `==` on
  FGP modules and verify it already does the right thing.

#### Spec assertions covered

```python
M = ZZ^3
assert M.base_ring() == ZZ
assert M in Modules(ZZ)
assert M.is_free() and M.is_torsionfree()
assert not M.is_torsion()
assert M.rank() == 3
assert M == ZZ + ZZ + ZZ
assert M.dual() == M.Hom(ZZ)
assert M * M == M.tensor(M)
assert M.tensor(Z2) in Modules(Z2)
assert M/(2*M) == M.tensor(Z2)
assert M.base_change(Z2) == M.tensor(Z2)
```

#### Key design decisions

- **Where to patch:** Monkeypatch methods directly onto
  `FreeModule_ambient_pid` and `FGP_Module_class`. Avoid category-level
  method injection which interacts with Sage's aggressive category caching.
- **`+` redefinition risk:** Redefining `+` on free modules breaks Sage's
  native "span" semantics. Since this codebase explicitly rejects the ambient
  module paradigm and controls all call sites, this is acceptable. If
  isolation is needed, scope the patch to only affect objects that have been
  through our enrichment (e.g. via a marker attribute).


### `module_operations.py` -- free_part, torsion_part, generator assignment

#### What to build

Monkeypatch `FGP_Module_class`:
- `free_part()`: Extract the free summand from Smith normal form
  decomposition. If M has invariants `(0, 0, 3, 5)`, then `free_part()` is
  the sub-module corresponding to invariant-0 generators.
- `torsion_part()`: Extract the torsion summand.

Generator assignment `M.<x,y,z> = ZZ^3`:
- Sage's preparser transforms this to `M = expr; (x,y,z) = M._first_ngens(3)`.
- `ZZ^3` already has `._first_ngens(3)` returning the standard basis.
- Verify this works natively and document. If not, patch `_first_ngens`.

#### Spec assertions covered

```python
F1, F2 = ZZ^2, ZZ^3
T1, T2 = ZZ/5, ZZ/7
M1 = F1 + T1
M2 = F2 + T2
assert M1.free_part() == F1 and M1.torsion_part() == T1
assert M2.free_part() == F2 and M2.torsion_part() == T2

M.<x,y,z> = ZZ^3  # generator assignment
```


### `hom_enrichment.py` -- Hom spaces as modules, morphism construction

#### What Sage provides natively

- `(ZZ^2).Hom(ZZ^2)` returns `FreeModuleHomspace`, already in `Modules(ZZ)`.
- `FGP_Homset_class` for FGP module hom sets.
- Morphisms can be constructed from matrices via `__call__`.
- FGP morphisms have `.kernel()` and some `.cokernel()` support.

#### What to build

**On hom spaces (`FreeModuleHomspace` / `FGP_Homset_class`):**
- `element_from_dict(mapping)`: Given `{gen_i: image_i}`, construct the
  morphism. This resolves the dict to a matrix and delegates to the native
  constructor.
- `element_from_images(images)`: Given a list of images for each generator,
  construct. Sugar for `element_from_dict(dict(zip(domain.gens(), images)))`.
- `element_from_matrix(M)`: Named constructor wrapping the existing
  `__call__` dispatch.
- `element_from_function(f)`: Apply f to each generator, check it defines a
  morphism.
- `natural_map()`: For `Hom(ZZ^m, ZZ^n)` where m >= n, the natural map
  sends e_i to e_i for i <= n and e_i to 0 for i > n.
- `identity()`: The identity morphism (when domain == codomain).

**On morphisms (`FreeModuleMorphism` / `FGP_Morphism`):**
- `to_matrix()`: Alias for `.matrix()` (already exists on free module
  morphisms).
- `to_dict()`: Convert to `{gen_i: image_i}`.
- `is_primitive()`: `self.cokernel().is_torsionfree()`.
- `base_change(S)`: Tensor the morphism with a ring.
- Ensure `cokernel()` returns an FGP module object, and that the cokernel
  object has a `.projection()` method returning the natural surjection.
  Sage's `FGP_Morphism` may already support this -- investigate at
  implementation time.

**On endomorphism/automorphism:**
- `M.End()` = `M.Hom(M)` -- trivial alias.
- `M.Aut()` -- the group of invertible endomorphisms. For free modules,
  `Aut(ZZ^n)` = `GL(n, ZZ)`. Return a `ConditionSet` or proper group.

#### Spec assertions covered

```python
M1.<g1,g2> = ZZ^2
M2.<h1, h2> = ZZ^2
H = M1.Hom(M2)
assert H in Modules(ZZ)
f = H.element_from_matrix(matrix(ZZ, 2, [0,1,1,0]))
assert f in H
assert f(g1) == h2 and f(g2) == h1
assert f.to_matrix() == matrix(ZZ, 2, [0,1,1,0])
assert f.is_injective() and f.kernel() == Modules(ZZ).zero()
assert f.is_surjective() and f.cokernel() == Modules(ZZ).zero()

g = H.element_from_images([2*h1, 3*h2])
assert g.cokernel() == ZZ/2 + ZZ/3
pi = g.cokernel().projection()
assert pi.is_surjective()

assert M1.End() == M1.Hom(M1)
assert M1.End().identity() in M1.Aut()
assert M1.End() in Monoids
assert M1.Aut() in Groups
```


### `_install.py` -- Single entry point

Each module defines an `install()` function. `_install.py` calls all of them
in dependency order. Calling `import src.sage_patches` installs all patches.

Every monkeypatch must:
- Save the original method (if any) before overwriting.
- Be idempotent (check if already installed).
- Log what it patches (via standard logging).


## Explicitly Out of Scope

- **Tor/Ext functors.** The `Tor` and `Ext` assertions in `misc.sage` are
  labeled TODO and require substantial homological algebra. Defer to a later
  phase.
- **Viewing ZZ/p as multiple algebraic structures simultaneously** (cyclic
  group, abelian group, finitely presented group, FGP module). This requires
  Sage's `Facade` or category-join machinery and is not needed for Phase 1.
- **Number field extensions.** The plan mentions "hopefully extensible to
  number fields", but Phase 0 targets R = ZZ exclusively. The patches should
  not PREVENT generalization (i.e. don't hard-code ZZ where R would work),
  but active support for number fields is deferred.


## Risks

| Risk | Mitigation |
|------|-----------|
| Patching `__truediv__` on ZZ breaks other Sage code | Only intercept integer/ideal arguments; fall through to original for all else |
| Redefining `+` to mean direct sum breaks Sage module arithmetic | This codebase never uses Sage's "span" `+`. If isolation needed, use marker attribute to scope the patch |
| Category containment patches interact with Sage's caching | Patch `__contains__` which is called dynamically, not cached |
| `M/(2*M) == M.tensor(Z2)` requires canonical-isomorphism equality | Investigate Sage's FGP `__eq__` semantics first; may need custom `__eq__` |
| `QmodnZ` arithmetic may be incomplete for form evaluation | Test early; may need additional monkeypatches on `QmodnZ` element arithmetic |


## Verification Strategy

Run `tests/sage_spec/misc.sage` line by line in a Sage session with
`src.sage_patches` imported. Each assertion in that file is a required
behavior. The file is the acceptance test.

Additionally, verify Phase 1 prerequisites:
- `FormCodomain.torsion_bilinear(ZZ)` constructs `QQ/ZZ` successfully.
- `FormCodomain.torsion_quadratic(ZZ)` constructs `QQ/2ZZ` successfully.
- Form evaluation `beta(v, w) mod ZZ` lands in `QQ/ZZ` correctly.
- Cokernel of a free-module morphism produces a torsion FGP module with
  working `invariants()`, `gens()`, and `projection()`.
