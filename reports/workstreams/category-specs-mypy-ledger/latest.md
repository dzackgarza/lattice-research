# Category Specs Mypy Error Ledger

- source_artifact: `reports/workstreams/category-specs-mypy-structural-full/latest.json`
- structural_status: pass
- source_mode: all
- full_structural_mismatches: 0
- full_structural_missing_typeinfos: 0
- full_structural_projected_ancestor_missing_typeinfos: 0
- ordinary_error_count: 1594
- ignored_negative_control_count: 1

## Toolchain

- research_sha: `9796748a07fa9628b2a476c33fbaef465df6a3e0`
- plugin_sha: `c231ac89da769434380dd95e499f5b64680636ae`
- sidecar_sha: `089fb8cfdb5ac413038f12c0717f69428a228297`

## Counts By Owner

- research typing/design: 1154
- mathematical/category-interface question: 311
- missing sidecar ordinary signature: 129

## Counts By Code

- misc: 457
- override: 281
- operator: 242
- arg-type: 194
- attr-defined: 133
- list-item: 133
- assignment: 54
- return-value: 38
- call-arg: 33
- type-var: 10
- call-overload: 8
- return: 5
- abstract: 3
- index: 2
- union-attr: 1

## Counts By Root Area

- rings: 419
- sets: 320
- modules: 263
- algebras: 148
- cat: 130
- posets: 94
- forms: 58
- lattices: 50
- topological_spaces: 50
- homsets: 33
- tensor_algebra_components: 21
- spec_core: 3
- types.py: 3
- utils.py: 2

## Representative Examples

- research typing/design / list-item / utils.py: `category_specs/utils.py:247: error: List item 0 has incompatible type "Category | Sequence[Category]"; expected "Category"  [list-item]`
- research typing/design / arg-type / utils.py: `category_specs/utils.py:249: error: Argument 1 to "_refine_category_" of "Parent" has incompatible type "list[Category] | list[Any] | tuple[Any, ...]"; expected "Category"  [arg-type]`
- missing sidecar ordinary signature / attr-defined / rings: `category_specs/rings/subcategories/_sage_ring_classes.py:5: error: Module "sage.rings.laurent_series_ring" has no attribute "LaurentSeriesRing"; maybe "LaurentSeries" or "LaurentSeriesRing_generic"?  [attr-defined]`
- research typing/design / assignment / cat: `category_specs/cat/base_category_types.py:548: error: Incompatible types in assignment (expression has type "type | None", variable has type "type[Category_singleton]")  [assignment]`
- research typing/design / misc / cat: `category_specs/cat/base_category_types.py:593: error: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"  [misc]`
- research typing/design / override / cat: `category_specs/cat/base_category_types.py:602: error: Argument 1 of "join" is incompatible with supertype "sage.categories.category.Category"; supertype defines the argument type as "list[Category]"  [override]`
- missing sidecar ordinary signature / misc / cat: `category_specs/cat/join_categories.py:38: error: Method "additional_structure" is marked as an override, but no base method was found with this name  [misc]`
- research typing/design / return-value / homsets: `category_specs/homsets/homsets.py:161: error: Incompatible return value type (got "HomCategory", expected "Category")  [return-value]`
- research typing/design / operator / homsets: `category_specs/homsets/homsets.py:183: error: "LazyImport" not callable  [operator]`
- research typing/design / type-var / homsets: `category_specs/homsets/autsets.py:58: error: Value of type variable "_ParentT" of "refine_category" cannot be "UniversalAutObjectMethods"  [type-var]`
- mathematical/category-interface question / return / cat: `category_specs/cat/homsets.py:27: error: Missing return statement  [return]`
- mathematical/category-interface question / misc / sets: `category_specs/sets/homsets.py:70: error: Cannot override final attribute "is_isomorphism" (previously declared in base class "_SetMorphisms")  [misc]`
- mathematical/category-interface question / attr-defined / modules: `category_specs/modules/subcategories/finitely_presented_over_pid.py:66: error: "Category" has no attribute "FinitelyPresented"  [attr-defined]`
- mathematical/category-interface question / call-arg / modules: `category_specs/modules/subcategories/finitely_presented_over_pid.py:117: error: Too many arguments for "Integer"  [call-arg]`
- mathematical/category-interface question / index / sets: `category_specs/sets/subcategories/countable.py:64: error: Invalid index type "Integer" for "type[ParentMethods]"; expected type "int | slice[Any, Any, Any]"  [index]`
- mathematical/category-interface question / abstract / modules: `category_specs/modules/__init__.py:621: error: Cannot instantiate abstract class "_Subobjects" with abstract attribute "as_subobject_of_self"  [abstract]`
- mathematical/category-interface question / call-overload / algebras: `category_specs/algebras/__init__.py:342: error: No overload variant matches argument type "Ring"  [call-overload]`
- mathematical/category-interface question / union-attr / modules: `category_specs/modules/subcategories/with_basis.py:186: error: Item "Sequence[_RModElements]" of "Any | Mapping[Element, _RModElements] | Sequence[_RModElements]" has no attribute "keys"  [union-attr]`
