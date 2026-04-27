# AGENTS.md — category_specs

## Type System Rules

- `__contains__` always takes `Any` as its argument type.
  Never use `object`.
- All types are defined in `types.py`. No type aliases, `TypeAlias` definitions, or
  ad-hoc types anywhere else — not in `TYPE_CHECKING` blocks, not at the top of axiom or
  other files, not inline.
  Import from `types.py`.
- Type names reflect **real mathematical vocabulary**, inspired by the SageMath
  **written docs** (not just type signatures — read the actual mathematics):
  - Objects: `Polynomial`, `RealNumber`, `ComplexNumber`, `RingElement`, `PowerSeries`,
    `Module`, `Ring`, `Set`, `FiniteSet`, `FinitelyGeneratedFreeModule`
  - Categories: `RMod`, `Rings`, `Sets`, `RAlgebras`, etc.
    (semantically named)
  - Morphisms: named after the mathematical morphism, e.g. `RModMorphism`,
    `RModAutomorphism` — never `HomsetElement` or `AutsetElement`
- Every type in `types.py` must be anchored to a real Sage object — `Any` is never
  acceptable. A type only appears in a signature because something in Sage already
  represents it; the written docs identify the vocabulary, and Sage provides the anchor.
  Precision tiers, in increasing preference:
  1. **Minimum**: the relevant SageMath base class (e.g. `sage.structure.parent.Parent`,
     `sage.structure.element.Element`)
  2. **Better**: the relevant SageMath subcategory's `ParentMethods` or `ElementMethods`
     (e.g. `sage.categories.posets.Posets.ParentMethods`)
  3. **Best**: a class from **our own hierarchy** that properly refines the Sage object
     (e.g. `_TotallyOrdered.ParentMethods` for `Poset`)

## Spec Philosophy

The spec's job is to formally declare what objects in a category **are** and **must
have** — not to implement anything.
A subcategory definition should read as a mathematical document: what the subcategory
is, what its supercategories are, what methods an object in it must have, and what
methods Sage already provides.
Almost no software engineering should appear inside subcategory definitions.

**One Source of Truth for Utils**:
All helper functions and glue belong in the top-level `utils.py`.
Subtrees must not define their own `utils.py` for general utility code; any truly
general helper (e.g., category refinement, list partitioning, ABC validation) must live
in the root `utils.py` and be imported by subtrees.
This ensures a single, coherent implementation of all project-wide machinery.

**Completeness**: the spec must fully capture all existing Sage methods on objects in
each subcategory as `@abstract_method` declarations.
Existing Sage objects must pass regression tests with nearly all methods declared
abstract. The only allowed violations are genuine Sage gaps, which are recorded
exclusively in `sage_gaps/` tests.

**Non-trivial implementations are banned inside subcategory definitions.** The only
concrete method bodies permitted are:
- Trivially true/false predicates (e.g. `def is_finite(self) -> bool: return True`)
- One-liners that delegate to another method with no branching or logic (e.g.
  `def __gt__(self, other): return other.__lt__(self)`)

Anything more complex — iteration logic, branching, imports, computations — belongs in
`utils.py` as a helper that the method calls, or must be left as an `@abstract_method`
for implementations to define themselves.
`try/except` is banned everywhere.

## Category Architecture

Each top-level category (`Sets`, `Rings`, `Modules`, etc.)
is defined in its subtree's `__init__.py`. That file defines exactly:

- Private method surface classes: `_XParentMethods`, `_XElementMethods`,
  `_XMorphismMethods`
- The category class itself, which must include:
  - A `__contains__` predicate implemented with `match/case`
  - A `Constructors` inner class (see below)
- Imports of subcategory classes from `subcategories/` to wire them into the hierarchy

**`__init__.py` is the public API document.** Reading it must be sufficient to
understand the full public surface of the category: its method surfaces, its axiomatic
subcategories, its constructions, and its constructors.
Keep it clean — no implementation, no glue.

The module docstring of `__init__.py` must faithfully record the full subcategory
hierarchy as a tree, showing the mathematical relationships between all subcategories
defined in that subtree.

**`SubcategoryMethods`** provides methods available on the category object itself for
navigating to further restricted subcategories (e.g. `Sets().Finite()` returns the
finite sets subcategory).

**Axiomatic subcategories** must be wired to real classes that add genuine spec work.
E.g. `Sets().Finite()` is not just structural — the linked class must declare that
`is_finite()` returns `True`, `is_countable()` returns `True`, `__len__` is defined,
etc.

### Direct implementation categories vs. axiomatic restrictions

Use a direct category class when the category is a genuine implementation target.
For example, a category such as `FinitelyGeneratedFreeModulesOverPID` is a concrete
mathematical and computational class of objects: there is one such category, it may be
reachable by a chain such as `Modules(R).FinitelyGenerated().Free().OverPIDs()` or by a
shortcut, and it is the category whose objects should eventually be implemented by the
corresponding finite-generation/PID free-module machinery.

Use a `with_axiom` restriction when the adjective must be attachable to any existing
subcategory. `Free` is the model case. `Modules(R).Free()` exists for mathematical and
spec reasons even when arbitrary free `R`-modules have little computable structure
without hypotheses on `R`. More importantly, any subcategory `C` of `Modules(R)` must be
allowed to form `C.Free()` to declare "free objects inside `C`". When `C = Modules(R)`,
Sage's `base_category_with_axiom`/`_base_category_class_and_axiom` registration may
return the registered class. For other `C`, the construction primarily records the
mathematical restriction and enforces a consistent method surface; it is not a promise
that the category has a complete implementation.

Do not collapse axiomatic restrictions into implementation categories merely because
some restricted cases are computable. Further restrictions such as finite generation,
basis data, or base-ring hypotheses determine the algorithms.

**Subobject, quotient, and homset categories** must always be wired up, with
mathematically expressive aliases: `Subsets = Subobjects`, `Submodules = Subobjects`,
`Quotients = Quotients`, `Homsets = Homsets`, `Endsets = Endsets`, `Autsets = Autsets`,
etc.

**Subobject types in `types.py`**: types like `Subset`, `Submodule`, `QuotientModule`
must be defined in `types.py` and used explicitly in method signatures to express
mathematical restrictions.
E.g. `intersection(self, other: Subset) -> Subset`, not
`intersection(self, other: Set) -> Set`.

**`Constructors`** is an inner class on the category, not a subcategory.
It organizes all entry points into Sage constructions: each method calls the original
Sage constructor and refines the result into the correct place in the hierarchy.
Accessed as `Sets().Constructors()`, `Rings().Constructors()`,
`Modules(R).Constructors()`. Examples:
- `Rings().Constructors().ZZ()` — wraps Sage's `ZZ` and refines it
- `Modules(R).Constructors().FreeModule(R, 5)` — wraps Sage's `FreeModule` and refines
  it

`Constructors` replaces all previous `NamedSets`, `NamedRings`, `NamedModules`
sub-namespaces uniformly.

**`subcategories/`** is a plain directory (no `__init__.py`) containing one `.py` file
per mathematical subcategory, named using real mathematical vocabulary (e.g.
`finite.py`, `totally_ordered.py`, `free.py`). The parent `__init__.py` imports from
these files directly.
Nothing in `specialized.py`, `named.py`, or any other flat aggregator file.

## Homsets, Endsets, and Autsets

Homsets (`Hom(X, Y)`), Endsets (`End(X) = Hom(X, X)`), and Autsets (`Aut(X) ⊂ End(X)`)
each have their own separate files at both the top level and within each subtree,
following the same organizational principle as other category surfaces.

### File organization

- **Top level**: `homsets/` defines the generic wiring shared across all subtrees —
  base classes, generic `Hom`/`End`/`Aut` dispatch, and the Autset integration layer
  (see below). This is the single place where Autset-as-ConditionSet machinery is
  implemented.
- **Per subtree**: `<subtree>/homsets.py` defines subtree-specific homset categories
  (e.g. `SetHomsets`, `RingHomsets`) and their `ParentMethods`/`ElementMethods`. These
  import and inherit from the top-level `homsets/` base classes.

### Autsets are wired repo-wide

Sage has no native Autset category — it provides `Homsets` and `Endsets` but nothing for
automorphism groups.
**Autsets must be integrated at the top level, once, so that individual subtrees never
reinvent this wiring.**

An Autset is mathematically an Endset with an underlying `ConditionSet` that checks
invertibility: `Aut(X) = {f ∈ End(X) | f is invertible}`. The top-level `homsets/`
subtree must define:

- The `Autset` parent class, constructed from an `Endset` plus an invertibility
  condition.
- Generic `ParentMethods` and `ElementMethods` available on all Autsets regardless of
  the ambient category (e.g. `group_structure`, `inverse`, `composition`).
- Generic `MorphismMethods` on the elements of Autsets (i.e. `Automorphism` methods like
  `inverse`, `order`, `is_involution`).

### What subtrees own vs. what the top level owns

| Concern | Owner | Examples |
| --- | --- | --- |
| Generic Hom/End/Aut construction and dispatch | Top-level `homsets/` | `Aut(X)` builder, ConditionSet integration, `Autset` base class |
| Generic methods on all Autsets | Top-level `homsets/` | `Autset.ParentMethods.group_structure`, `Autset.ElementMethods.inverse` |
| Category-specific Autset properties | Subtree `<subtree>/homsets.py` | `Aut_{Set}(X).ParentMethods.is_transitive`, `Aut_{Ring}(X).ElementMethods.preserves_units` |
| Category-specific Homset/Endset definitions | Subtree `<subtree>/homsets.py` | `SetHomsets`, `RingEndsets`, `RModHomsets` |
| Wiring `Aut` into a subtree's category namespace | Subtree `<subtree>/__init__.py` | `Sets().Aut(X)` delegates to generic `Aut(X)` with the subtree's Endset |

Subtrees focus on **categorical properties**: what methods should `Aut_{Set}(X)` have,
what supercategories and additional structure it carries, how it refines the generic
Autset. They must never reimplement the generic ConditionSet-on-Endset machinery that
produces an Autset from an Endset.

### Morphism, Endomorphism, and Automorphism element types

The element types follow the same naming convention as other morphism types (see Type
System Rules):

- `Morphism` — element of a Homset
- `Endomorphism` — element of an Endset (a `Morphism` where domain = codomain)
- `Automorphism` — element of an Autset (an invertible `Endomorphism`)

These are defined in `types.py` and used in method signatures throughout.
Each subtree's `homsets.py` declares `ElementMethods` for its specific
Homset/Endset/Autset element types, inheriting from the top-level base methods.

## File Tree

```
category_specs/
├── AGENTS.md
├── __init__.py           # imports all subtrees, calls register_all()
├── axioms.py             # ALL axiom definitions and registration — single source of truth
├── types.py              # ALL type aliases — single source of truth
├── utils.py             # shared utilities (refine_category, etc.)
├── homsets/             # generic Hom/End/Aut dispatch, Autset wiring, base classes
│   ├── AGENTS.md
│   ├── __init__.py
│   ├── smoketest.sage
│   ├── docs/
│   └── tests/
├── justfile
└── <subtree>/            # e.g. sets/, rings/, modules/, algebras/, topological_spaces/
    ├── AGENTS.md         # subtree goals and task list
    ├── __init__.py       # defines category, ParentMethods, ElementMethods,
    │                     # MorphismMethods, Constructors; imports from subcategories/
    ├── subcategories/    # one .py file per mathematical subcategory (no __init__.py)
    │   ├── finite.py
    │   ├── constructions/
    │   │   ├── subobjects.py
    │   │   ├── subquotients.py
    │   │   ├── quotients.py
    │   │   └── homsets.py    # subtree-specific Homset/Endset/Autset categories
    │   ├── free.py
    │   └── ...
    ├── smoketest.sage    # exercises every Constructors() entry point
    ├── docs/
    │   ├── TRIAGE.md         # current smoketest failures, grouped by blocker
    │   ├── SAGE_INVENTORY.md # full Sage category surface: classes, methods, on-disk paths
    │   └── MAPPING.md        # decisions mapping Sage categories → our hierarchy, with mathematical justification
    └── tests/
        ├── new_spec/     # tests of the new spec surface (see Testing rules)
        ├── regression/   # per-constructor regression tests
        └── sage_gaps/    # raw Sage gap assertions (see Testing rules)
```

- Axioms are defined and registered **only** in the root `axioms.py`. No subtree defines
  or registers axioms.
- No `specialized.py`, `named.py`, `constructions.py`, or other flat aggregator files.
- `subcategories/` may nest arbitrarily to reflect the mathematical hierarchy.
  A subcategory with many sub-subcategories gets its own subdirectory (e.g.
  `subcategories/free/over_pids/`). A single file suffices when the subcategory is a
  leaf or has few children.
- Construction-style subcategories live under `subcategories/`, split by mathematical
  notion. Use `subcategories/constructions/<notion>.py` for attachable Sage
  construction categories such as subobjects, quotients, subquotients, homsets,
  endsets, and autsets. These classes may extend Sage functorial construction
  classes and use `category_of`; the target organization still places the category
  surface by mathematical notion.
- If a subcategory introduces a genuinely independent and complex method surface (new
  `ParentMethods`, `ElementMethods`, `MorphismMethods`), promote it to its own top-level
  subtree rather than burying it.
  E.g. `lattices/` and `algebras/` are top-level, not nested inside
  `modules/subcategories/`.

## super_categories

`super_categories()` must return a plain list of category instances, e.g.
`[CategoryA(), CategoryB()]`. Never call `Category.join` inside `super_categories()` —
Sage's framework handles the join internally.
`_joined_super_categories` is banned.

Each subcategory must declare **both** its parent in our hierarchy and the corresponding
Sage supercategory (or categories).
This ensures:
- Existing upstream `@abstract_method` declarations and unimplemented methods from Sage
  are surfaced on our objects.
- Objects refined into our subcategory still register as members of the corresponding
  Sage category (e.g. `ZZ in SageRings()` still holds after refinement into our
  `Rings()`).

Example:
```python
def super_categories(self):
    return [Sets().Finite(), SageFiniteSets()]
```

## Refinement

All refinement goes through `utils.refine_category` directly.
No per-subtree `_refine_named_X` wrapper functions (e.g. `_refine_named_set`,
`_refine_named_ring`, `_refine_named_module`). These are banned — they are redundant
indirection over the same call.

## Overall Design

This hierarchy is a **non-destructive staged replacement** for Sage's category system.
The pattern is: intercept existing Sage constructors, call the original implementation,
then refine the result into the new subcategory hierarchy.
Never destructively replace or monkey-patch Sage internals.

## Category Structure

- Every category exposes method surfaces via inner classes: `ParentMethods`,
  `ElementMethods`, `MorphismMethods`. All abstract methods belong in one of these.
- Every category exposes a `Constructors()` sub-namespace
  (e.g. `Sets().Constructors()`, `Rings().Constructors()`,
  `Modules(R).Constructors()`) for all Sage constructor entry points known to that
  category. Constructor wrappers must be collected here, not scattered.
- Every category subtree must properly declare its construction categories:
  `Subobjects`, `Subquotients`, `Quotients`, `Homsets`, `Endsets`, and `Autsets`
  (including all of their elements), even if the implementations are mostly
  trivial. They must be declared explicitly in the subtree's `__init__.py` and
  located in `subcategories/constructions/` to ensure a uniform surface across the
  entire hierarchy.
- Method surface separation is strict: a method belongs in the category whose axioms are
  the minimum required for it to be well-defined.
  Ring-theoretic methods must not appear in `Sets`; module-theoretic methods must not
  appear in `Rings`; etc.

## Sage Naming Disambiguation

When importing a Sage category that shares a name with one of ours, alias it as `SageX`:
```python
from sage.categories.sets_cat import Sets as SageSets
from sage.categories.modules import Modules as SageModules
```
Never let Sage and local names collide silently.

## Smoketest and Triage

Each subtree's `smoketest.sage` must:
- Add the repo root to `sys.path` so `category_specs` is importable.
- Import only from this spec hierarchy (not bare Sage globals).
- Define a `smoke_case(label, build)` helper that catches all exceptions, appends
  failures to a `failures` list, and logs a warning — it must never raise.
- Call `smoke_case` for **every** constructor in the subtree's `Constructors()`
  namespace.
  Labels must identify the target spec class and the constructor call.
- End with `assert not failures, "\n".join(failures)` so a failed run exits nonzero.

Each subtree's `docs/TRIAGE.md`:
- Is the canonical record of current `smoketest.sage` failures, grouped by missing
  method or structural blocker.
- Must be updated whenever `smoketest.sage` output changes.
- Is sourced from the smoketest — never edited independently of running it.

Justfile registration:
- Every subtree's `smoketest.sage` must be listed in the `smoke` recipe in the root
  `justfile`.
- `just smoke` runs all smoketests.
  `just test` runs `smoke` first, then all `regression/` and `new_spec/` files.
- Adding a new subtree requires adding its `smoketest.sage` to `smoke` in the justfile.

## Sage Inventory and Mapping

Each subtree maintains a `docs/` folder with three files:

- **`SAGE_INVENTORY.md`**: indexes every Sage class and method relevant to that subtree
  — full class name, method signatures, and on-disk path to the implementation (e.g.
  `$SAGE_ROOT/src/sage/categories/sets_cat.py:142`). The canonical reference for Sage
  internals in that subtree; consult it before searching Sage source directly.

- **`MAPPING.md`**: records, for each Sage category, the mathematical justification for
  how it maps to our hierarchy.
  Must document: what Sage provides, the correct mathematical concept, the
  justification, and the consequence for refinement and regression tests.
  Example: Sage's `EnumeratedSets` → our `Countable` axiom, because countability =
  existence of an enumeration f: X → ℕ; the spec must exhibit such a function; all Sage
  enumerated sets must refine to `Sets().Countable()`.

- **`TRIAGE.md`**: see Smoketest and Triage section.

## Error Handling

- No `try/except` blocks anywhere.
- Use `assert` to enforce preconditions and requirements.
- Any method that is meant to raise an error must remain `abstract`.

## Axiomatic Subcategory Registration

- Each axiom class must declare `_base_category_class_and_axiom` as a **class-level
  attribute** on itself, e.g.:
  ```python
  class _FiniteSets(CategoryWithAxiom):
      _base_category_class_and_axiom = (Sets, "Finite")
  ```
- Never splice `_base_category_class_and_axiom` onto classes at module level after their
  definition. That pattern is banned.

## Method Surface Classes

For top-level categories, `ParentMethods`, `ElementMethods`, and `MorphismMethods` must
be factored into named private classes and assigned, not defined inline.
The names must be mathematically explicit:
- `_SetObjectMethods` (not `ParentMethods`) — methods on objects in `Sets()`
- `_SetElementMethods` (not `ElementMethods`) — methods on elements of sets
- `_SetMorphismMethods` (not `MorphismMethods`) — methods on morphisms between sets

These are then assigned inside the category:
```python
class Sets:
    ParentMethods = _SetObjectMethods
    ElementMethods = _SetElementMethods
    MorphismMethods = _SetMorphismMethods
```

This is self-documenting: the class name explicitly states what the methods are for.

## No Splicing

Never add methods or classes to a category class after its definition (e.g.
`MyCategory.ParentMethods.foo = ...` or `MyCategory.MySubcategory = ...` at module level).
All methods and subcategory attributes must be declared inside the class body.
Splicing fragments documentation and makes the spec impossible to read as a single
coherent document.

**The LazyImport Pattern**:
To wire subcategories into a category while avoiding circular imports (e.g., when a
subcategory file needs to import the parent category for registration), use
`sage.misc.lazy_import.LazyImport` at the class level:

```python
class MyCategory(Category):
    # ...
    MySubcategory = LazyImport("category_specs.subtree.subcategories.file", "_MySubcategoryClass")
```

This ensures the subcategory module is only loaded when the attribute is accessed,
breaking the import cycle and keeping the category definition clean and centralized.
All subcategory wiring must follow this pattern instead of module-level assignment or
splicing.

## Method Overrides

- When a subcategory provides a concrete implementation of a method declared
  `@abstract_method` in a parent category, it must be decorated with `@override` (from
  `typing` or `typing_extensions`).
- **Trivial answers are overrides, not exemptions.** When an `@abstract_method` is
  mathematically well-defined for all objects in a parent category, subcategories where
  the answer is trivial must still override with the concrete trivial implementation —
  they must never weaken or remove the abstract requirement.
  E.g. `completion()` is defined for any ring and any ideal; fields override it to
  handle the trivial case (only ideals are 0 and R), rather than being exempted from the
  requirement entirely.

## Method Placement

- All methods must be defined at the **highest category** for which they are universally
  well-defined.
- Do not duplicate method definitions at lower levels if the parent already covers it.

## Testing (sage_gaps)

Files in `sage_gaps/` directories test raw Sage objects directly — no new category
namespace, no `refine_category`. Their sole purpose is to assert that specific methods
are missing or broken in Sage as-is, proving the motivation for the spec.

- Use bare Sage globals (`ZZ`, `QQ`, `GF(...)`, etc.)
  directly here.
- `with raises(...)` / `pytest.raises(...)` constructions are **only** permitted in
  `sage_gaps/` files. They are banned everywhere else.
- Do not import or use any class from this spec hierarchy in `sage_gaps/` tests.

## Testing (new_spec)

Files in `new_spec/` directories test the new category spec, not raw Sage objects.
The objects under test are refined objects exposed on category namespaces.

**Constructor Rule**: Construct test objects through the category namespace entry points
(e.g. `Sets().Constructors().X()`, `Rings().Constructors().X()`,
`Rings().Hom(...)`, etc.).
Never start from bare Sage globals (`ZZ`, `QQ`, `GF(...)`, `PolynomialRing(...)`, etc.)
when the category namespace has the corresponding constructor.
Never call `refine_category(...)` in tests when a category-owned constructor already
exists — the namespace constructor is the implementation surface being tested.

**What to Assert**: Assert properties directly on the refined objects returned by the
spec surface. Do not weaken tests by switching to raw Sage constructors.

**Recording Gaps**: When the current implementation does not satisfy the spec, expose
the failure through the spec surface itself — build the object through the category
namespace, then let the assertion reflect the gap.
Do not bypass the namespace layer and claim the result says something about the new
spec.

## TYPE_CHECKING

`if TYPE_CHECKING:` blocks are only permitted to resolve a concrete circular import.
Never use them as a general mechanism to defer imports or to define type aliases.
If a type can be imported at runtime without a circular dependency, it must be imported
unconditionally at the top of the file.

The priority is that the definition of e.g. `Polynomial`, `RModule`, `Set`, `Matrix`,
`ModuleMorphism`, `RingEndomorphism`, etc. should all be uniform and global.
Use `if TYPE_CHECKING:` where TRULY needed to avoid circularity and help enforce that
uniformity, not as an escape hatch, for defensive hedging, or as an excuse to redefine
basic nouns/verbs hidden away in subcategory files.

## Type Annotations

- Every method argument must have a type annotation.
- Every method must have a well-defined return type annotation.
- Every argument and return type must use a named mathematical type from `types.py`.
  `Any` is forbidden in method signatures (except `__contains__`).
