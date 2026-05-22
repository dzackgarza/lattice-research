# Category Specs Mypy Error Ledger

- source_artifact: `reports/workstreams/category-specs-mypy-structural-full/latest.json`
- structural_status: pass
- source_mode: all
- full_structural_mismatches: 0
- full_structural_missing_typeinfos: 0
- full_structural_projected_ancestor_missing_typeinfos: 0
- ordinary_error_count: 1611
- ignored_negative_control_count: 1

## Toolchain

- research_sha: `0fb25eec5d84aed9a7e1be655254625a2268b09a`
- plugin_sha: `c231ac89da769434380dd95e499f5b64680636ae`
- sidecar_sha: `62379f8e70b9c8c5d74601325a220f4868d1f69f`

## Counts By Owner

- research typing/design: 1158
- mathematical/category-interface question: 303
- missing sidecar ordinary signature: 150

## Counts By Code

- misc: 478
- override: 280
- operator: 246
- arg-type: 192
- list-item: 132
- attr-defined: 127
- assignment: 54
- return-value: 37
- call-arg: 33
- call-overload: 11
- type-var: 10
- return: 5
- abstract: 3
- index: 2
- union-attr: 1

## Counts By Root Area

- rings: 484
- sets: 303
- modules: 244
- algebras: 152
- cat: 127
- posets: 93
- forms: 54
- lattices: 50
- topological_spaces: 49
- homsets: 33
- tensor_algebra_components: 21
- types.py: 1

## Representative Examples

- missing sidecar ordinary signature / attr-defined / cat: `category_specs/cat/base_category_types.py:35: error: Module "sage.categories.category_types" has no attribute "Category_module"; maybe "Category_ideal"?  [attr-defined]`
- research typing/design / arg-type / cat: `category_specs/cat/base_category_types.py:474: error: Argument 1 to "__init__" of "Parent" has incompatible type "_CatObjectMixin"; expected "Parent"  [arg-type]`
- research typing/design / assignment / cat: `category_specs/cat/base_category_types.py:548: error: Incompatible types in assignment (expression has type "type | None", variable has type "type[Category_singleton]")  [assignment]`
- research typing/design / misc / cat: `category_specs/cat/base_category_types.py:593: error: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"  [misc]`
- research typing/design / override / cat: `category_specs/cat/base_category_types.py:602: error: Argument 1 of "join" is incompatible with supertype "sage.categories.category.Category"; supertype defines the argument type as "list[Category]"  [override]`
- research typing/design / list-item / cat: `category_specs/cat/join_categories.py:34: error: List item 0 has incompatible type "Cat"; expected "Category"  [list-item]`
- missing sidecar ordinary signature / misc / homsets: `category_specs/homsets/homsets.py:153: error: Method "default_super_categories" is marked as an override, but no base method was found with this name  [misc]`
- research typing/design / return-value / homsets: `category_specs/homsets/homsets.py:161: error: Incompatible return value type (got "HomCategory", expected "Category")  [return-value]`
- research typing/design / operator / homsets: `category_specs/homsets/homsets.py:183: error: "LazyImport" not callable  [operator]`
- research typing/design / type-var / homsets: `category_specs/homsets/autsets.py:58: error: Value of type variable "_ParentT" of "refine_category" cannot be "UniversalAutObjectMethods"  [type-var]`
- mathematical/category-interface question / return / cat: `category_specs/cat/homsets.py:27: error: Missing return statement  [return]`
- mathematical/category-interface question / misc / sets: `category_specs/sets/homsets.py:70: error: Cannot override final attribute "is_isomorphism" (previously declared in base class "_SetMorphisms")  [misc]`
- mathematical/category-interface question / attr-defined / modules: `category_specs/modules/subcategories/finitely_presented_over_pid.py:66: error: "Category" has no attribute "FinitelyPresented"  [attr-defined]`
- mathematical/category-interface question / call-arg / modules: `category_specs/modules/subcategories/finitely_presented_over_pid.py:117: error: Too many arguments for "Integer"  [call-arg]`
- mathematical/category-interface question / index / sets: `category_specs/sets/subcategories/countable.py:64: error: Invalid index type "Integer" for "type[ParentMethods]"; expected type "int | slice[Any, Any, Any]"  [index]`
- mathematical/category-interface question / call-overload / sets: `category_specs/sets/subcategories/finite.py:55: error: No overload variant of "int" matches argument type "InfinityElement"  [call-overload]`
- mathematical/category-interface question / abstract / modules: `category_specs/modules/__init__.py:592: error: Cannot instantiate abstract class "_Subobjects" with abstract attribute "as_subobject_of_self"  [abstract]`
- mathematical/category-interface question / union-attr / modules: `category_specs/modules/subcategories/with_basis.py:186: error: Item "Sequence[_RModElements]" of "Any | Mapping[Element, _RModElements] | Sequence[_RModElements]" has no attribute "keys"  [union-attr]`
