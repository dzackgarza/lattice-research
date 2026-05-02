
You’re right. Here is the concrete defect backlog I should have produced. I am treating something as a sprint task only when I found an actual file whose current surface appears to violate the guidelines: closed mathematical signatures, no Sage option bags, `@final` on concrete spec methods, strict-supercategory ownership, deep `ConditionSet` integration, and keeping nontrivial implementation out of category specs. The relevant rules are in `plans/category_specs/AGENTS.md`. 

## Concrete sprint tasks

### 1. Remove raw `ConditionSet` from the public Aut-category surface

Files: `plans/category_specs/homsets/autsets.py`.

Current issue: `UniversalAutObjectMethods.condition_set()` publicly exposes a “condition set” view, and `AutCategory.from_end_category`, `AutCategoryConstruction.from_end_category`, and `AutCategoryOf.from_end_category` directly return `SageConditionSet(...)`. The guideline says predicate-defined subsets/subobjects should be public subobjects, with Sage `ConditionSet` only as localized interop backing; raw `ConditionSet` plumbing should not be a category-spec method.  

Sprint task: replace the public `condition_set()` vocabulary with a project-owned subobject/aut object surface, keep `SageConditionSet` behind a private helper or implementation bridge, and make `AutCategory().from_end_category(E)` return an object in the project `AutCategory`/subobject vocabulary. Also add `@final` to the concrete aut-object methods currently lacking it: `condition_set`, `end_category`, `domain`, `codomain`, `identity`, the three `from_end_category` methods, and the `extra_super_categories`/`default_super_categories` implementations where appropriate. 

### 2. Split boolean-return-shape and optional-return-shape signatures

Files: `rings/__init__.py`, `rings/matrix_algebras.py`, `rings/subcategories/number_field.py`, `rings/subcategories/rational_field.py`, and likely the mapped constructor docs for those surfaces.

Current issues include these specific signatures:

`_RingElementMethods.nth_root(..., all: bool = False, ...) -> RingElement | list[RingElement]` and `sqrt(..., all: bool = False, ...) -> RingElement | list[RingElement]` in `rings/__init__.py`. The return type changes with a boolean flag, which is not a closed mathematical signature. 

`_MatrixAlgebras.ParentMethods.echelon_form(..., transformation: bool = False, ...) -> RingElement | tuple[RingElement, RingElement]` in `rings/matrix_algebras.py`. Again, a boolean flag changes the mathematical return shape. 

`_NumberFields.ParentMethods.galois_closure(names: str | None = None, map: bool = False) -> Field | tuple[Field, RingMorphism]`, and the parallel `_QQ.ParentMethods.galois_closure(...)` forwarding method. The `map` flag is Sage factory plumbing; the spec should expose separate mathematical methods, for example `galois_closure()` and `galois_closure_with_embedding()` or a similarly named closed pair.  

`_RingMorphismMethods.image(self, I: Ideal | None = None) -> Ideal` in `rings/__init__.py`, which collapses the image of the morphism and the image of a supplied ideal into one optional-argument method. 

Sprint task: split each of these into closed overloads or named methods. Do not keep optional flags that change the mathematical meaning or return type. Add regression smokes for each old Sage-style call path that is still intentionally supported via a named replacement.

### 3. Remove Sage option bags from number-field and rational-field public specs

Files: `rings/subcategories/number_field.py`, `rings/subcategories/rational_field.py`.

Current issue: the number-field surface still carries Sage implementation/display/proof knobs as public category-spec parameters: `galois_group(type=..., algorithm=..., names=..., gc_numbering=...)`, `class_number(proof=...)`, `class_group(proof=..., names=...)`, `places(all_complex=..., prec=...)`, `roots_of_unity`, `regulator(proof=...)`, `unit_group(proof=...)`, `conductor(check_abelian=...)`, and the order methods with `assume_maximal: bool | None | Literal["non-maximal-non-unique"]`. `_QQ` mirrors these by forwarding through `as_number_field()`.  

Sprint task: decide for each option whether it is mathematical data or Sage interop. Mathematical variants should get named methods; implementation controls such as `algorithm`, `proof`, `names`, `check_abelian`, and Sage sentinel literals should be removed from the category spec or moved behind implementation/mapping docs. The rational-field forwarding methods must then match the cleaned number-field surface, not preserve the old Sage knobs.

### 4. Split mixed set-constructor input shapes

File: `sets/__init__.py`.

Current issue: several set constructor surfaces still merge mathematically different inputs into one union signature. Concrete examples:

`FiniteSetMaps(domain: FiniteSet | Integer, codomain: FiniteSet | Integer | None = None, ...)` merges a finite set with a cardinality shorthand and also uses `codomain=None` for the endomap case. 

`SetPartitions(base_set: Set | Iterable[SetElement] | Integer)`, `SetPartitionsWithBlockCount(...)`, and `SetPartitionsWithBlockSizes(...)` merge an existing base set, an iterable presentation, and a cardinality shorthand. 

`Family(indices: Iterable[SetElement] | Set, function: Callable[...] | None = None, ...)` merges indexed-family construction over a set with iterable-backed construction and optional function behavior. 

Sprint task: split these into named constructor routes, such as finite-map-set from domain/codomain objects, finite-map-set from cardinalities, finite-endomap-set, set partitions of an existing set, set partitions of a finite iterable, set partitions of a cardinality, and family-from-index-set versus family-from-iterable. Preserve old functionality in mapping docs and regression smokes, but remove the shape-collapsing public signatures.

### 5. Fix binary/foldable operation surfaces

Files: `modules/__init__.py`, `sets/__init__.py`.

Current issue: `Modules(R)` declares `direct_sum(self, other: RModule | Sequence[RModule])` and `tensor(self, other: RModule | Sequence[RModule])`. The guidelines say a binary operation must expose the binary primitive and, when meaningful, a separate sequence overload that folds over it. A union of one object and a sequence is exactly the pattern the guideline rules out.  

There is a parallel issue in `Sets._SetObjectMethods.cartesian_product(self, factors: Sequence[Set], ...)`: the object-level surface is aggregate-only, not a binary primitive plus fold. 

Sprint task: define binary primitives such as `direct_sum(self, other: RModule)`, `tensor(self, other: RModule)`, and `cartesian_product_with(self, other: Set)` or the preferred naming convention. Then add a separate sequence method/overload for folding. Remove `RModule | Sequence[RModule]` and aggregate-only binary surfaces.

### 6. Remove strict-supercategory leaks from one-object set subcategories

File: `sets/subcategories/image.py`.

Current issue: `_ImageSets.ParentMethods` restates generic set/subobject obligations: `__eq__`, `__ne__`, `__hash__`, `_element_constructor_`, `ambient`, `lift`, `retract`, `cardinality`, `__iter__`, `__contains__`, `_an_element_`, and `_sympy_`. Image sets may have image-specific structure, but equality, hashing, containment, ambient/lift/retract, cardinality, iteration, and SymPy conversion are not first true at “image sets.” They belong in `Sets()`, `Sets().Subobjects()`, or another strict supercategory.  

Sprint task: delete the duplicated abstract methods from `_ImageSets` unless an image-specific law or refined return type is being added. If any method is absent from the correct supercategory, add it there instead. Then audit the other one-object set subcategories, especially `facade.py` and `primes.py`, for the same pattern.  

### 7. Add missing `@final` and return annotations to concrete methods

Files: `homsets/homsets.py`, `homsets/endsets.py`, `homsets/autsets.py`, `modules/homsets.py`, `modules/__init__.py`, `algebras/__init__.py`, `cat/__init__.py`, `cat/base_category_types.py`, `rings/matrix_algebras.py`, `rings/subcategories/rational_field.py`.

Specific examples found:

`HomCategory.super_categories` and `HomCategoryOf._repr_object_names` are concrete but not `@final`. 

`EndCategory.extra_super_categories`, `EndCategoryConstruction.default_super_categories`, and `EndCategoryOf.extra_super_categories` are concrete but not `@final`. 

Many concrete methods in `homsets/autsets.py` are not `@final`, as noted above. 

`RModuleHomCategory.extra_super_categories`, `RModuleEndCategory.extra_super_categories`, and `RModuleAutCategory.extra_super_categories` lack explicit return annotations. `_RModHomCategoryObjectMethods.zero()` also lacks a return annotation. 

`_RModObjects.tensor_square`, `tensor_power`, and `tensor_module` in `modules/__init__.py` are concrete but have incomplete return typing. 

`Algebras.Constructors.__init__` is concrete and not decorated `@final`. `Algebras.Constructors()` also lacks a return annotation. 

`_MatrixAlgebras.__init__` is concrete and not `@final`. 

Many wrapper `__init__` methods in `cat/base_category_types.py` are concrete and not `@final`, despite the local rule that concrete category-spec methods are final by default.  

Sprint task: add `@final` and precise return annotations to these methods, or document why a method is intentionally an extension hook. This is a mechanical but real compliance defect, not just a lint preference.

### 8. Strip generated/import bloat from ring subcategory files

Files: at least `rings/subcategories/real_double_field.py`, `complex_double_field.py`, `polynomial_ring.py`, `number_field.py`, and `rational_field.py`; search results show the same `LazyImport` pattern across many ring subcategory files.     

Current issue: narrow files such as `real_double_field.py` and `complex_double_field.py` import or lazily import nearly the entire ring subcategory graph, including their own category name, while the actual class only needs the Sage field class and one immediate supercategory. This is category-spec software-engineering bloat and obscures mathematical ownership. The top-level guideline says category specs should read as mathematical declarations and nontrivial glue belongs elsewhere. 

Sprint task: reduce each ring subcategory file to the Sage classes and immediate project supercategories it actually uses. Remove self-`LazyImport` entries and unrelated `_SAGE_*` constants from files that do not use them. Keep broad lazy import registries in a central ring index only if they are genuinely needed there.

### 9. Move nontrivial algebra construction implementation out of the spec file

File: `algebras/__init__.py`.

Current issue: `Algebras.Constructors.from_multiplication_tensor` is not just a spec declaration or trivial glue. It validates tensor type, extracts structure constants, builds a right-multiplication table, calls Sage `FiniteDimensionalAlgebra`, branches on `is_associative()` and `is_unitary()`, and manually assembles category refinements. `_right_multiplication_table` is also a concrete algorithm embedded in the category spec. 

Sprint task: move the table-building and Sage-construction algorithm to an implementation/helper module, probably under an implementation or utility location. Leave the category spec with the mathematical constructor signature and a thin final call into that implementation. This follows the spec-vs-implementation split in the guidelines. 

### 10. Fix tensor-component placeholder and type vocabulary

File: `tensor_algebra_components/__init__.py`; also update `types.py` if needed.

Current issues:

`_TensorAlgebraComponentParentMethods.lift_from_product` is a concrete `@final` method whose body is `assert False`. A concrete final placeholder is not a spec-compliant mathematical method. It should either be abstract, implemented, or recorded as a decision/frontier. 

The local alias `TensorAlgebraComponent = TensorAlgebraComponents` makes the singular object name point to the category class. The module docstring says objects are graded pieces `T_R(M)[p,q]` and elements are tensors, so the alias is likely programmer-shaped or at least misleading relative to the standard type-package rule.  

`from_multidimensional_list` accepts `Sequence[RingElement] | Sequence[Sequence[RingElement]] | Sequence[Sequence[Sequence[RingElement]]]` in one constructor. The variadic inventory says tensor component catch-all public construction was supposed to be removed in favor of named tensor constructors, so this should be checked and split if it is still public API rather than a closed, named case.  

Sprint task: make `lift_from_product` abstract or real; correct the local type package so singular object/type names point to object surfaces, not category classes; and split or justify the multidimensional-list constructor shape.

### 11. Clean Sage option bags from ring constructors

File: `rings/__init__.py`.

Current issue: many public constructor methods expose large Sage option bags rather than mathematical constructor data. Examples include `GF`/`FiniteField` with `impl`, `proof`, `check_prime`, `check_irreducible`, `prefix`, `repr`, `elem_cache`; p-adic constructors with `print_mode`, `print_pos`, `print_sep`, `print_alphabet`, `print_max_terms`, `show_prec`, `label`; and number-field constructors with `check`, `embedding`, `latex_name`, `assume_disc_small`, `maximize_at_primes`, `structure`, and `latex_names`. 

Some of these may be admissible implementation parameters, but they are not category-spec mathematical vocabulary as written. The variadic inventory says p-adic precision and ring constructor casework were already scoped, so the remaining option bags should not be reintroduced as public mathematical signatures. 

Sprint task: for each constructor family, keep only mathematical constructor inputs on the public method. Move display/proof/algorithm/cache/label options behind implementation defaults, named interop helpers, or mapping docs. Where an option represents a genuine mathematical variant, split it into a named constructor.

### 12. Fix Cat-wrapper typing/finality holes

Files: `cat/__init__.py`, `cat/base_category_types.py`.

Current issue: the cat subtree is the approved Sage category-base touch point, so it can contain more wrapper machinery than ordinary specs. But it still has concrete methods with incomplete signatures: `Cat._make_named_class(self, name, method_provider, cache=False, picklable: bool = True)` has untyped parameters; `Cat.additional_structure(self)` lacks a return annotation; `_make_named_class_with_cat_subcategory_methods` in `base_category_types.py` has untyped `delegate`, `name`, `method_provider`, and `cache`; many wrapper `__init__` methods are concrete and not `@final`.  

Sprint task: type these wrapper signatures explicitly, add `@final` where methods are not extension hooks, and document any hook exceptions. Keep this limited to the cat wrapper boundary, since `cat/AGENTS.md` explicitly says `base_category_types.py` is the only Sage category-base touch point. 

### 13. Reclassify polynomial- and matrix-ring implementation assertions

Files: `rings/subcategories/polynomial_ring.py`, `rings/matrix_algebras.py`.

Current issue: `_PolynomialRings.ParentMethods.completion(self, I: Ideal)` asserts that `I` is principal and generated by an irreducible element before calling `super().completion(p, prec=oo)`. This is a runtime-narrowing implementation embedded in the spec. The signature should express the mathematical input shape directly, or the narrowing should live in implementation code. 

`_MatrixAlgebras.__init__` asserts squareness, and the parent method surface includes optional/flagged construction shapes such as `matrix_space(nrows: Integer | None = None, ncols: Integer | None = None, sparse: bool = False)` and the flagged `echelon_form(... transformation: bool = False ...)`. 

Sprint task: replace assertion-narrowed spec signatures with mathematical signatures: for polynomial completion, use an ideal/generator type or named method that already encodes the required hypothesis; for matrix spaces, split default square-space recovery from rectangular matrix-space construction and split echelon form with transformation from echelon form without transformation.

### 14. Audit standard type-package aliases after the concrete fixes

Files: all category-family `__init__.py` files and `types.py`.

Current issue: `types.py` is meant to import category-local standard packages and then choose conventional aliases. That is a real rule, not just style. The current `types.py` contains a large number of aliases, and at least the tensor-component local package appears suspicious because the local file sets `TensorAlgebraComponent = TensorAlgebraComponents`.  

Sprint task: after fixing local type packages, audit each category family for the standard names `XCategory`, `XObject`, `XElement`, `XMorphism`, `XHomCategory`, `XEndCategory`, `XAutCategory`, `XHom`, `XEnd`, `XAut`, `XEndomorphism`, and `XAutomorphism`. Remove aliases that merely rename private classes or point singular mathematical names at category classes. Keep conventional aliases only in `types.py`, backed by actual Sage/project mathematical objects. 

## What I would put in the sprint

I would make the sprint explicitly defect-driven:

P0: `homsets/autsets.py` raw `ConditionSet`; boolean/return-shape splits in `rings`; missing `@final`/return annotations in hom/end/aut and cat wrappers.

P1: set constructor splits; module binary/foldable operation splits; image-set strict-supercategory cleanup; number-field/rational-field option-bag cleanup.

P2: ring subcategory import-bloat cleanup; algebra implementation extraction; tensor-component placeholder/type-package repair.

P3: final type-package audit and mapping-doc updates for every removed Sage option or renamed constructor.

This is the concrete backlog. The earlier answer should be discarded as too procedural.
