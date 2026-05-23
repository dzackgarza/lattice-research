# Category Specs Mypy Error Ledger

- source_artifact: `reports/workstreams/category-specs-mypy-structural-full/latest.json`
- structural_status: pass
- source_mode: all
- full_structural_mismatches: 0
- full_structural_missing_typeinfos: 0
- full_structural_projected_ancestor_missing_typeinfos: 0
- ordinary_error_count: 1791
- ignored_negative_control_count: 1

## Toolchain

- research_sha: `076f669f81694770e28b4bd332e4375aca1a8524`
- plugin_sha: `c231ac89da769434380dd95e499f5b64680636ae`
- sidecar_sha: `72e6cf8b2bf131df5cb44ae1713e304a4a5f7a67`

## Counts By Owner

- research typing/design: 1310
- mathematical/category-interface question: 371
- missing sidecar ordinary signature: 110

## Counts By Code

- misc: 505
- override: 339
- operator: 246
- arg-type: 243
- list-item: 143
- attr-defined: 106
- assignment: 59
- return-value: 42
- abstract: 41
- call-arg: 35
- call-overload: 10
- type-var: 10
- return: 5
- union-attr: 5
- index: 2

## Counts By Root Area

- rings: 470
- sets: 359
- modules: 311
- algebras: 186
- cat: 141
- posets: 90
- lattices: 63
- forms: 61
- topological_spaces: 49
- homsets: 34
- tensor_algebra_components: 25
- constructor_redefinitions.py: 2

## Representative Examples

- research typing/design / arg-type / cat: `category_specs/cat/base_category_types.py:474: error: Argument 1 to "__init__" of "Parent" has incompatible type "_CatObjectMixin"; expected "Parent"  [arg-type]`
- research typing/design / assignment / cat: `category_specs/cat/base_category_types.py:548: error: Incompatible types in assignment (expression has type "type | None", variable has type "type[Category_singleton]")  [assignment]`
- research typing/design / misc / cat: `category_specs/cat/base_category_types.py:593: error: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"  [misc]`
- research typing/design / override / cat: `category_specs/cat/base_category_types.py:602: error: Argument 1 of "join" is incompatible with supertype "sage.categories.category.Category"; supertype defines the argument type as "list[Category]"  [override]`
- research typing/design / list-item / cat: `category_specs/cat/join_categories.py:34: error: List item 0 has incompatible type "Cat"; expected "Category"  [list-item]`
- missing sidecar ordinary signature / misc / homsets: `category_specs/homsets/homsets.py:153: error: Method "default_super_categories" is marked as an override, but no base method was found with this name  [misc]`
- research typing/design / return-value / homsets: `category_specs/homsets/homsets.py:161: error: Incompatible return value type (got "HomCategory", expected "Category")  [return-value]`
- research typing/design / operator / homsets: `category_specs/homsets/homsets.py:183: error: "LazyImport" not callable  [operator]`
- missing sidecar ordinary signature / attr-defined / homsets: `category_specs/homsets/autsets.py:36: error: "Morphism" has no attribute "is_invertible"  [attr-defined]`
- research typing/design / type-var / homsets: `category_specs/homsets/autsets.py:58: error: Value of type variable "_ParentT" of "refine_category" cannot be "UniversalAutObjectMethods"  [type-var]`
- mathematical/category-interface question / return / cat: `category_specs/cat/homsets.py:27: error: Missing return statement  [return]`
- mathematical/category-interface question / misc / sets: `category_specs/sets/homsets.py:70: error: Cannot override final attribute "is_isomorphism" (previously declared in base class "_SetMorphisms")  [misc]`
- mathematical/category-interface question / attr-defined / modules: `category_specs/modules/subcategories/finitely_presented_over_pid.py:66: error: "Category" has no attribute "FinitelyPresented"  [attr-defined]`
- mathematical/category-interface question / call-arg / modules: `category_specs/modules/subcategories/finitely_presented_over_pid.py:117: error: Too many arguments for "Integer"  [call-arg]`
- mathematical/category-interface question / abstract / sets: `category_specs/sets/__init__.py:317: error: Cannot instantiate abstract class "Modules" with abstract attributes "R", "torsion_module" and "zero_module"  [abstract]`
- mathematical/category-interface question / index / sets: `category_specs/sets/subcategories/countable.py:64: error: Invalid index type "Integer" for "type[ParentMethods]"; expected type "int | slice[Any, Any, Any]"  [index]`
- mathematical/category-interface question / call-overload / sets: `category_specs/sets/subcategories/finite.py:55: error: No overload variant of "int" matches argument type "Integer | InfinityElement"  [call-overload]`
- mathematical/category-interface question / union-attr / rings: `category_specs/rings/subcategories/real_precision_field.py:81: error: Item "<subclass of "category_specs.rings.subcategories.real_precision_field._RealPrecisionFields.ParentMethods" and "sage.rings.abc.RealField">" of "<subclass of "category_specs.rings.subcategories.real_precision_field._RealPrecisionFields.ParentMethods" and "sage.rings.abc.RealField"> | <subclass of "category_specs.rings.subcategories.real_precision_field._RealPrecisionFields.ParentMethods" and "sage.rings.abc.RealDoubleField"> | <subclass of "category_specs.rings.subcategories.real_precision_field._RealPrecisionFields.ParentMethods" and "sage.rings.abc.RealIntervalField">" has no attribute "to_prec"  [union-attr]`
