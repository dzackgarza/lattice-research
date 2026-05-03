---
trackerStatus:
  type: task
title: Remove raw ConditionSet from public Aut-category surface
---
# Remove raw ConditionSet from public Aut-category surface
Source: pasted backlog 2026-05-02.

Files: plans/category_specs/homsets/autsets.py

Issue: UniversalAutObjectMethods.condition_set() and the from_end_category constructors expose SageConditionSet directly on the public category-spec surface.

Task: replace public condition_set vocabulary with a project-owned subobject/aut-object surface, keep SageConditionSet behind a private helper or implementation bridge, ensure AutCategory().from_end_category(E) returns a project aut/subobject object, and add missing @final markers on the affected concrete aut-object methods.

## Complexity Justification
- Owner: C76
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Remove raw ConditionSet from public Aut-category surface
- Why this specific score:
  - This is a migration-level API boundary change in `autsets.py`, touching public category semantics, object construction paths, and return types. Moving `SageConditionSet` off the public surface while preserving behavior through internal bridges creates both compatibility and correctness risk across dependent category-callers.
  - The task also adds invariants (`@final` on concrete aut-object methods), which increases refactor blast radius beyond a local symbol rename.
- Item-specific evidence:
  - The file names exact touch points (`condition_set`, `from_end_category`, `aut/subobject` surface) and a single authoritative target file, `plans/category_specs/homsets/autsets.py`.
  - Complexity is driven by explicit public/private contract reshaping rather than a single implementation edit.
