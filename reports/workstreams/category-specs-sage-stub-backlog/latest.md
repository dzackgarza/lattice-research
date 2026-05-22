# Category Specs Sage Stub Backlog

This backlog is a runtime-verification queue for Sage-stub agents. A row is not
a claim that the sidecar is wrong; it is a Sage-shaped diagnostic that should
be checked against actual Sage behavior before editing `sage-stubs`.

- source_ledger: `reports/workstreams/category-specs-mypy-ledger/latest.json`
- ordinary_error_count: 1611
- stub_candidate_count: 1201
- non_candidate_count: 410

## Toolchain

- research_sha: `0fb25eec5d84aed9a7e1be655254625a2268b09a`
- plugin_sha: `c231ac89da769434380dd95e499f5b64680636ae`
- sidecar_sha: `62379f8e70b9c8c5d74601325a220f4868d1f69f`

## Counts By Failure Kind

- dynamic category attribute missing: 353
- incorrect final/override declaration: 265
- callable LazyImport / lazy factory surface: 206
- generic inheritance/protocol missing: 122
- missing base method in provider stub: 103
- missing sage module member: 43
- missing sage class member: 36
- factory return type too narrow: 32
- constructor signature too narrow: 31
- Sage numeric/operator protocol missing: 10

## Counts By Agent Bundle

- category core and dynamic category constructors: 377
- homsets, morphisms, endsets, autsets: 361
- rings and polynomial-family constructors: 236
- modules, vector spaces, matrix spaces, subobjects: 132
- sets, infinity/cardinality, numeric protocols: 54
- smaller families: algebras/forms/posets/lattices/topological spaces: 41

## Counts By Suggested Sidecar File

- runtime probe must identify Sage module before editing: 1155
- sage/rings/abc.pyi: 24
- sage/rings/padics/generic_nodes.pyi: 6
- sage/combinat/posets/lattices.pyi: 4
- sage/rings/number_field/number_field.pyi: 4
- sage/algebras/clifford_algebra.pyi: 2
- sage/categories/category_types.pyi: 2
- sage/algebras/free_algebra.pyi: 1
- sage/combinat/posets/posets.pyi: 1
- sage/rings/infinity.pyi: 1
- sage/rings/qqbar.pyi: 1

## Representative Rows

- sage-stub-0001 / missing sage module member / high / `category_specs/cat/base_category_types.py:35` / sage/categories/category_types.pyi: Module "sage.categories.category_types" has no attribute "Category_module"; maybe "Category_ideal"?
- sage-stub-0002 / missing sage module member / high / `category_specs/cat/base_category_types.py:36` / sage/categories/category_types.pyi: Module "sage.categories.category_types" has no attribute "Category_over_base"; maybe "Category_over_base_ring"?
- sage-stub-0004 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:475` / runtime probe must identify Sage module before editing: Argument 1 to "_init_category_" of "CategoryObject" has incompatible type "_CatObjectMixin"; expected "CategoryObject"
- sage-stub-0005 / generic inheritance/protocol missing / low / `category_specs/cat/base_category_types.py:495` / runtime probe must identify Sage module before editing: Argument 1 to "Hom" of "Parent" has incompatible type "_CatObjectMixin"; expected "Parent"
- sage-stub-0006 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:511` / runtime probe must identify Sage module before editing: Argument 1 to "_make_named_class_with_cat_subcategory_methods" has incompatible type "_CatObjectMixin"; expected "Category"
- sage-stub-0007 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:548` / runtime probe must identify Sage module before editing: Incompatible types in assignment (expression has type "type | None", variable has type "type[Category_singleton]")
- sage-stub-0008 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:579` / runtime probe must identify Sage module before editing: Incompatible types in assignment (expression has type "type | None", variable has type "type[CategoryWithAxiom_singleton]")
- sage-stub-0009 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:593` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0010 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:593` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0011 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:593` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0012 / incorrect final/override declaration / low / `category_specs/cat/base_category_types.py:602` / runtime probe must identify Sage module before editing: Argument 1 of "join" is incompatible with supertype "sage.categories.category.Category"; supertype defines the argument type as "list[Category]"
- sage-stub-0013 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:604` / runtime probe must identify Sage module before editing: Argument 1 to "join" of "Category" has incompatible type "Iterable[category_specs.cat.base_category_types.Category]"; expected "list[sage.categories.category.Category]"
- sage-stub-0014 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:607` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0015 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:607` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0016 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:607` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0017 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:615` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0018 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:615` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0019 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:615` / runtime probe must identify Sage module before editing: Definition of "__classcall__" in base class "_SingletonClasscallMixin" is incompatible with definition in base class "Category"
- sage-stub-0020 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:615` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0021 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:625` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0022 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:625` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0023 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:625` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0024 / incorrect final/override declaration / low / `category_specs/cat/base_category_types.py:648` / runtime probe must identify Sage module before editing: Argument 1 of "defining_predicate" is incompatible with supertype "sage.categories.category_with_axiom.CategoryWithAxiom"; supertype defines the argument type as "object"
- sage-stub-0025 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:655` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0026 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:655` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0027 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:655` / runtime probe must identify Sage module before editing: Definition of "__classcall__" in base class "_SingletonAxiomClasscallMixin" is incompatible with definition in base class "Category"
- sage-stub-0028 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:655` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0029 / incorrect final/override declaration / low / `category_specs/cat/base_category_types.py:686` / runtime probe must identify Sage module before editing: Argument 1 of "defining_predicate" is incompatible with supertype "sage.categories.category_with_axiom.CategoryWithAxiom"; supertype defines the argument type as "object"
- sage-stub-0030 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:693` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0031 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:693` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0032 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:693` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0033 / incorrect final/override declaration / low / `category_specs/cat/base_category_types.py:718` / runtime probe must identify Sage module before editing: Argument 1 of "defining_predicate" is incompatible with supertype "sage.categories.category_with_axiom.CategoryWithAxiom"; supertype defines the argument type as "object"
- sage-stub-0034 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:725` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0035 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:733` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0036 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:733` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0037 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:733` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0038 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:741` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0039 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:749` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0040 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:749` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0041 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:749` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0042 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:757` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0043 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:757` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0044 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:757` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0045 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:765` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0046 / generic inheritance/protocol missing / low / `category_specs/cat/base_category_types.py:765` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0047 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:765` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0048 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:773` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0049 / generic inheritance/protocol missing / low / `category_specs/cat/base_category_types.py:773` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0050 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:773` / runtime probe must identify Sage module before editing: Definition of "__classcall__" in base class "_SingletonClasscallMixin" is incompatible with definition in base class "Category"
- sage-stub-0051 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:773` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0052 / incorrect final/override declaration / low / `category_specs/cat/base_category_types.py:781` / runtime probe must identify Sage module before editing: Signature of "Endset" incompatible with supertype "sage.categories.homsets.Homsets"
- sage-stub-0053 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:805` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0054 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:805` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0055 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:805` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0056 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:832` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0057 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:832` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0058 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:832` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0059 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:855` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
- sage-stub-0060 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:855` / runtime probe must identify Sage module before editing: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Parent"
- sage-stub-0061 / dynamic category attribute missing / low / `category_specs/cat/base_category_types.py:855` / runtime probe must identify Sage module before editing: Definition of "_make_named_class" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"
