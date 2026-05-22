# Category Specs Mypy Error Ledger

- source_artifact: `reports/workstreams/category-specs-mypy-structural-full/latest.json`
- structural_status: pass
- source_mode: all
- full_structural_mismatches: 0
- full_structural_missing_typeinfos: 0
- full_structural_projected_ancestor_missing_typeinfos: 0
- ordinary_error_count: 1574
- ignored_negative_control_count: 1

## Toolchain

- research_sha: `493749063d2d4cc11d983d34de562854cac10683`
- plugin_sha: `c231ac89da769434380dd95e499f5b64680636ae`
- sidecar_sha: `e74d1f9f3fe55ded04147ecc9cc7f3a3944a9e5f`

## Counts By Owner

- research typing/design: 1157
- mathematical/category-interface question: 314
- missing sidecar ordinary signature: 103

## Counts By Code

- misc: 457
- override: 282
- operator: 246
- arg-type: 194
- list-item: 132
- attr-defined: 107
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

- rings: 418
- sets: 306
- modules: 263
- algebras: 147
- cat: 130
- posets: 94
- forms: 58
- lattices: 50
- topological_spaces: 50
- homsets: 33
- tensor_algebra_components: 21
- spec_core: 3
- types.py: 1

## Representative Examples

- missing sidecar ordinary signature / attr-defined / rings: `category_specs/rings/subcategories/_sage_ring_classes.py:9: error: Module "sage.rings.polynomial.polynomial_ring" has no attribute "PolynomialRing_generic"; maybe "PolynomialRing_general"?  [attr-defined]`
- research typing/design / arg-type / spec_core: `category_specs/spec_core/constructor_adapters.py:20: error: Argument 1 to "_explicit_constructors_provider" has incompatible type "object"; expected "Category"  [arg-type]`
- research typing/design / assignment / cat: `category_specs/cat/base_category_types.py:548: error: Incompatible types in assignment (expression has type "type | None", variable has type "type[Category_singleton]")  [assignment]`
- research typing/design / misc / cat: `category_specs/cat/base_category_types.py:593: error: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"  [misc]`
- research typing/design / override / cat: `category_specs/cat/base_category_types.py:602: error: Argument 1 of "join" is incompatible with supertype "sage.categories.category.Category"; supertype defines the argument type as "list[Category]"  [override]`
- research typing/design / list-item / cat: `category_specs/cat/join_categories.py:34: error: List item 0 has incompatible type "Cat"; expected "Category"  [list-item]`
- missing sidecar ordinary signature / misc / cat: `category_specs/cat/join_categories.py:38: error: Method "additional_structure" is marked as an override, but no base method was found with this name  [misc]`
- research typing/design / return-value / homsets: `category_specs/homsets/homsets.py:161: error: Incompatible return value type (got "HomCategory", expected "Category")  [return-value]`
- research typing/design / operator / homsets: `category_specs/homsets/homsets.py:183: error: "LazyImport" not callable  [operator]`
- research typing/design / type-var / homsets: `category_specs/homsets/autsets.py:58: error: Value of type variable "_ParentT" of "refine_category" cannot be "UniversalAutObjectMethods"  [type-var]`
- mathematical/category-interface question / return / cat: `category_specs/cat/homsets.py:27: error: Missing return statement  [return]`
- mathematical/category-interface question / misc / sets: `category_specs/sets/homsets.py:70: error: Cannot override final attribute "is_isomorphism" (previously declared in base class "_SetMorphisms")  [misc]`
- mathematical/category-interface question / attr-defined / modules: `category_specs/modules/subcategories/finitely_presented_over_pid.py:66: error: "Category" has no attribute "FinitelyPresented"  [attr-defined]`
- mathematical/category-interface question / call-arg / modules: `category_specs/modules/subcategories/finitely_presented_over_pid.py:117: error: Too many arguments for "Integer"  [call-arg]`
- mathematical/category-interface question / index / sets: `category_specs/sets/subcategories/countable.py:64: error: Invalid index type "Integer" for "type[ParentMethods]"; expected type "int | slice[Any, Any, Any]"  [index]`
- mathematical/category-interface question / call-overload / sets: `category_specs/sets/subcategories/finite.py:55: error: No overload variant of "int" matches argument type "InfinityElement"  [call-overload]`
- mathematical/category-interface question / abstract / modules: `category_specs/modules/__init__.py:621: error: Cannot instantiate abstract class "_Subobjects" with abstract attribute "as_subobject_of_self"  [abstract]`
- mathematical/category-interface question / union-attr / modules: `category_specs/modules/subcategories/with_basis.py:186: error: Item "Sequence[_RModElements]" of "Any | Mapping[Element, _RModElements] | Sequence[_RModElements]" has no attribute "keys"  [union-attr]`
