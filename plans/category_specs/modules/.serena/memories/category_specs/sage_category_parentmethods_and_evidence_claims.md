# Sage Category ParentMethods And Method-Provider Mixins

## When This Applies

This applies when working in `plans/category_specs`, especially module/ring category specs that refine existing Sage objects with `_refine_category_`.

## Rule From Transcript Evidence

A prior Codex transcript records the user correcting direct calls such as `SageRings.ParentMethods.foo(self, ...)` / `Sets.ParentMethods.cartesian_product(self, ...)` as the wrong pattern for these specs.

Evidence source: parsed Codex transcript `~/.codex/sessions/2026/04/21/rollout-2026-04-21T14-08-20-019db05e-de7b-7612-a32b-c1da9f786724.jsonl`, section around the discussion beginning with “Honest question: is calling the parentmethods the theoretically most correct solution...”. The key correction was: the spec subcategories must define the relevant upstream Sage categories as supercategories properly. If the Sage categories are in the supercategory graph, Sage's dynamic MRO can see their `ParentMethods` implementations. Compatibility forwarding to `ParentMethods` is a symptom of malformed category joins, not the desired implementation strategy.

## Correct Protocol

- Treat `ParentMethods`, `ElementMethods`, `MorphismMethods`, homset nested classes, and related Sage category nested classes as method-provider/spec surfaces, not public implementation APIs.
- Constructor collectors like `NamedModules` / `NamedRings` are the implementation bridge: call existing Sage constructors, then refine the concrete result into the new category hierarchy.
- For every spec subcategory, define `super_categories()` so the relevant upstream Sage category/subcategory is actually in the category graph. The goal is for Sage's dynamic parent/element/morphism MRO to see upstream implementations naturally.
- If a method is implemented by the concrete Sage class returned by a named constructor, leave the spec method abstract and rely on the concrete class in the refined object's MRO.
- If a method is implemented by an upstream Sage category, include that upstream category as a supercategory rather than adding a forwarding shim.
- If an abstract spec method shadows an upstream Sage implementation after refinement, inspect the refined object's final MRO and category supercategories, then fix category composition.
- Implement method bodies in the spec category only for genuinely new behavior forced by the new mathematical subcategory, not to recover upstream Sage behavior.

## What Not To Do

- Do not implement behavior by calling `SomeCategory.ParentMethods.method(self, ...)`, `SomeCategory.ElementMethods.method(self, ...)`, `.f`, or similar direct method-provider internals.
- Do not use direct `ParentMethods` forwarding as a compatibility bridge for shadowed methods.
- Do not treat cooperative `super()` as an automatic fix; it only works when the desired implementation is actually present in the final refined object's MRO.
- Do not patch individual shadowed methods one by one when the real problem is that the Sage supercategory graph is malformed.
- Do not create fake named-category or fake axiom registrations to force method availability. Use real Sage supercategories and the proper `_base_category_class_and_axiom` mechanism only for literal chained subcategory registration.
- Do not redeclare an upstream Sage category method as a higher-priority abstract spec method unless the upstream category that implements it remains visible in the refined MRO.

## Why

Sage builds dynamic parent, element, morphism, and homset classes from the concrete object's class plus the joined category graph. If the new spec subcategory omits the upstream Sage category that supplies a method, an abstract method in the spec layer can mask the real implementation. Calling `ParentMethods` directly bypasses category composability and breaks future subcategories whose objects did not come from the named Sage constructor path. The correct fix is categorical composition, not method-level forwarding.


## Verification

- Searching the changed spec files should not show direct implementation calls to `.ParentMethods.` except citations/comments explicitly documenting upstream APIs.
- Runtime failures from abstract methods shadowing Sage implementations should be addressed by inspecting the refined object's MRO and category supercategories.
- Runtime verification should inspect the refined object's MRO and category supercategories, not validate direct `ParentMethods` forwarding.