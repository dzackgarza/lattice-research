# Tasks

- Remove raw ConditionSet from public Aut-category surface #task[id:task_1777748120385_rrvdig status:to-do priority:high created:2026-05-02T18:55:20.362Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Files: plans/category_specs/homsets/autsets.py

  Issue: UniversalAutObjectMethods.condition_set() and the from_end_category constructors expose SageConditionSet directly on the public category-spec surface.

  Task: replace public condition_set vocabulary with a project-owned subobject/aut-object surface, keep SageConditionSet behind a private helper or implementation bridge, ensure AutCategory().from_end_category(E) returns a project aut/subobject object, and add missing @final markers on the affected concrete aut-object methods.

- Split boolean and optional return-shape signatures #task[id:task_1777748120440_brc1sx status:to-do priority:medium created:2026-05-02T18:55:20.397Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: split the mixed boolean|None and T|None return-type signatures on Category and Map classes into explicit @overload declarations.

- Remove Sage option bags from number-field and rational-field constructors #task[id:task_1777748120483_nam4mw status:to-do priority:medium created:2026-05-02T18:55:20.432Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: excise Sage option bags from number-field and rational-field constructors, use explicit keyword arguments on the new public surface.

- Split mixed set-constructor input shapes into named alternatives #task[id:task_1777748120529_yqjmy7 status:to-do priority:medium created:2026-05-02T18:55:20.452Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: split the mixed input shapes on set constructors (objects, collection, and single object) into explicit alternatives using @overload.

- Restore binary primitives for module and set product constructors #task[id:task_1777748120565_b5h5vy status:to-do priority:medium created:2026-05-02T18:55:20.480Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: restore the binary-only variants of the module and set product constructors, deprecate the n-ary forms, and add missing @final markers to the concrete implementations.

- Remove strict-supercategory leaks from image-set and schematic-set constructors #task[id:task_1777748120612_yva6fx status:to-do priority:medium created:2026-05-02T18:55:20.517Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: remove strict-supercategory leakage from diagram-set/image-set/schematic-set constructors, restrict inputs to the correct base category.

- Add missing final markers and return annotations on Cat methods #task[id:task_1777748120649_eqpn1a status:to-do priority:medium created:2026-05-02T18:55:20.549Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: add missing @final markers to concrete Cat methods, annotate return types, and excise Sage option bags from the public surface.

- Strip import and LazyImport bloat from ring subcategory constructors #task[id:task_1777748120685_4vx3gb status:to-do priority:medium created:2026-05-02T18:55:20.580Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: strip import and LazyImport bloat from the ring subcategory constructors, fix the public surface to use canonical constructors.

- Move nontrivial algebra construction out of category constructors #task[id:task_1777748120716_zuyahm status:to-do priority:medium created:2026-05-02T18:55:20.616Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: move nontrivial algebra construction (Zmod, Cyclotomic, NumberField, etc.) out of category constructors, restrict to lightweight wrapper logic.

- Fix tensor-component placeholder methods and type leaks #task[id:task_1777748120751_vp7d5v status:to-do priority:medium created:2026-05-02T18:55:20.651Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: fix tensor-component placeholder methods that incorrectly return self or return None, add missing @final markers, and excise Sage option bags from the public surface.

- Clean Sage option bags from public ring constructors #task[id:task_1777748120784_23rowb status:to-do priority:medium created:2026-05-02T18:55:20.684Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: clean Sage option bags from public ring constructors (MatrixSpace, VectorSpace, etc.), use explicit keyword arguments.

- Fix Cat wrapper typing and finality holes #task[id:task_1777748120816_0es9m8 status:to-do priority:medium created:2026-05-02T18:55:20.716Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: fix Cat wrapper typing (explicit type parameters, correct variance), fill finality holes on concrete Cat subclasses, and excise Sage option bags from the public surface.

- Replace assertion-narrowed polynomial and matrix return types #task[id:task_1777748120848_fnu6jv status:to-do priority:medium created:2026-05-02T18:55:20.748Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: replace assertion-narrowed polynomial and matrix return types (via result of isinstance checks) with proper static union types using X|None patterns.

- Audit standard type-package aliases after concrete Cat migration #task[id:task_1777748120881_n0o19f status:to-do priority:medium created:2026-05-02T18:55:20.781Z tags:category-specs,backlog,p0]
  Source: pasted backlog 2026-05-02.

  Task: audit standard type-package aliases (Set, Matrix, etc.) and ensure they point to the new project types after the concrete Cat migration.

- Sample task for testing tracker #task[id:task_19dea4a6ceaDAXC9JSJC5ZI6J5 status:in-progress priority:medium created:2026-05-03]
