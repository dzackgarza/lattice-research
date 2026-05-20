# AGENTS.md - category_specs

This file is the mandatory entry point for agents working under `category_specs/`. Keep it small. Canonical category-spec guidance lives in local skills under `.agents/skills/category-spec-*`.

## Directive alignment

Before acting, confirm the user's stated directive, the action you plan, and why the action matches that directive rather than a substituted goal.

## Always-active rules

- Obey the repo root `AGENTS.md`; load `research-state-machine` for plan-to-execution routing and acceptance, and load `research-proof-auditing` for proof, evidence, and audit-sufficiency questions.
- The category-spec project exists to specify an ideal mathematical interface inside
  Sage's category/object universe. Current Sage implementation coverage is not the
  adequacy standard: if current Sage already satisfied the ideal interface, this
  project would have no reason to exist. Sage interop is still a design constraint:
  refined Sage objects should remain usable by existing Sage code when
  mathematically appropriate. Sage inventory is implementation evidence and a
  feasibility witness. Inventory and mapping preserve existing Sage functionality
  and help bound the spec to implementable mathematics, while specs must also state
  mathematically required methods that Sage lacks.
- Spec smokes expose gaps between current Sage/refined objects and the ideal spec.
  A smoke failure is normally evidence for an implementation, wrapper, constructor,
  or compliance card; it is not evidence that the spec obligation should be weakened,
  deleted, or moved without a grounded replacement owner.
- Before advancing a category-spec task, phase, or plan, review the staged diff, the
  unstaged diff, and any commits created during the work for spec weakening. Deleted
  abstract methods, removed constructor obligations, narrowed smoke assertions,
  moved obligations without a source-grounded replacement owner, and Sage-gap-driven
  interface shrinkage fail the gate even if smoke output improves.
- Treat spec files, review files, theory notes, TODO files, and durable design artifacts as source material. Do not rewrite, shorten, modernize, or delete them unless the user explicitly asks for that exact edit.
- Use Nimbalyst tracker files for planning, follow-ups, blockers, decisions, deferred compliance findings, smoke triage, and outstanding work. Do not create ad hoc planning, status, audit, or TODO markdown files when a tracked file is the right durable artifact.
- Use only standard registered tracker types. Classify category-spec work with tags and `.agents` paths, not custom `x-work` types.
- Never call `tracker_create` or `create_task` for markdown-backed tracker items.
- Never mark parent work `accepted`, native items `done`, sprint plans `closed`, or
  broader phase/feature acceptance without human approval. Do not translate that rule
  into `needs-human-input` for ordinary category-spec task cards whose routing is
  already determined by source grounding, repo policy, the DAG, or agent-executable
  review.
- If a category-spec rule is relevant but not in context, load the matching category-spec skill before acting. Do not guess from memory.
- Before editing a spec, mapping, method surface, constructor, Hom/End/Aut rule,
  invariant, or predicate, perform the definition-grounding gate from
  `category-spec-style`: locate the exact mathematical definition and hypotheses in
  canonical repo theory, Sage written docs/source, references, spec backups, or an
  approved decision card. Vague migrated cards and old TODO bullets are not enough.
  If the definition is unclear, create or update a decision/source-mining card and
  stop that leaf.
- Do not use `MorphismMethods` in category specs. Morphism behavior belongs on the
  relevant Hom-category element surface, e.g. `C.HomCategory().ElementMethods`, not
  on the object category itself or a nested `MorphismMethods` method-container.
- For domain-specific terms with multiple plausible meanings, keep the meanings
  separate unless a source-backed proof records exactly when they coincide. Do not
  write a spec surface by normalizing to the most familiar interpretation of a word.

## Canonical skills

- Load `category-spec-style` before any task that touches category-spec content or compliance: specs, category surfaces, method surfaces, constructors, morphisms, Hom/End/Aut surfaces, Sage wrappers, type annotations, test files, smoke files, implementations, Sage inventory, or mapping documents.
- For nontrivial edits, loading the skill stub is not enough: keep the canonical
  references named by the matching skills in context before editing. Any change to
  method ownership, inherited method surfaces, `@abstractmethod`/`@override`/`@final`,
  type aliases, construction categories, Hom/End/Aut categories, smokes, specs, or
  mapping rows is nontrivial. If the needed reference is not already in context, stop
  and read it before checkpointing or editing.
- Load `category-spec-subtrees` before editing a specific category subtree or deciding where a method, constructor, Hom/End/Aut rule, or subtree test belongs.
- Load `category-framework-design` and its relevant references before editing or
  reviewing Hom/End/Aut structure, autsets, construction categories, refinement order,
  or constructor interception. For Hom/End/Aut surfaces, `homsets-structural-core.md`
  is mandatory context.
- Load `lattice-redesign` and its relevant references before editing forms, formed
  modules, lattices, lattice morphisms, orthogonal groups, discriminant objects, or
  lattice-backed Hom/End/Aut surfaces. For these edits, `category-abc-spec.md` and
  `lattice-interface-style-guide.md` are mandatory context.
- Load `category-spec-workflow` before any task that touches execution mechanics: tracker item creation or migration, Nimbalyst plans, sprint metadata, tracked work metadata, delegation contracts, subagent instructions, branch/PR policy, smoke triage, validation handoff, stale-document migration, or status changes.
- Load narrower category-spec skills when their descriptions match the task: audit, planning, retirement, Sage mapping, smoke triage, triage, and visuals.

## Removed local docs

`STYLE.md`, `WORKFLOW.md`, and lower nested `AGENTS.md` files have been migrated into skills and should not be recreated as parallel docs. If an older prompt references one of those files, load the corresponding category-spec skill instead.
