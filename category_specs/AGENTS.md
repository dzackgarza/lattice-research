# AGENTS.md - category_specs

This file is the mandatory entry point for agents working under `category_specs/`. Keep it small. Canonical category-spec guidance lives in local skills under `.agents/skills/category-spec-*`.

## Directive alignment

Before acting, confirm the user's stated directive, the action you plan, and why the action matches that directive rather than a substituted goal.

## Sage constructor and method frontier gate

Before category-spec Sage inventory or mapping work, open
`[[SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER]]`.

Category-spec inventory or mapping progress exists only when that spec's finite frontier
changes:

```text
Remaining = U - C - R - Q
```

where `U` is the source-grounded universe of Sage constructors, classes, functions, and
methods in the active scope; `C` is classified with owner, hypotheses, codomain, and
project category surface; `R` is rejected as non-mathematical, runtime, display, private,
backend plumbing, or otherwise non-admitted; and `Q` requires a recorded decision.

Do not report progress from row counts, file counts, review prose, current-state
summaries, handoff edits, broad checkpoints, or mapping-doc edits that do not change
that frontier. Subtree `SAGE_INVENTORY.md`, `MAPPING.md`, spec rows, cards, decisions,
and handoffs are evidence and routing surfaces; the frontier spec is the status
authority for what remains.

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
- Refinement is declaration, not validation. It says that an implementation is to be
  regarded as an object of a project category and therefore carries that category's
  contract. It does not interrogate the object, prove satisfaction, reject because
  project methods remain abstract, or instantiate a missing implementation. Smokes
  expose those implementation gaps.
- `ParentMethods` are mathematical object-method obligations, not provider
  implementations or runtime failure hooks. Use Python `abc.abstractmethod` to
  represent abstract spec obligations in the class system; do not replace them with
  generated bodies, `assert False`, `NotImplementedError`, name-specific logic, or
  refinement-time satisfaction checks.
- For ABCMeta/refinement work, use the project-owned category/refinement/constructor
  path, not raw Sage refinement, as the boundary under test. Do not add admission
  control, instantiate inside refinement, or perform MRO surgery when the intended
  relation can be expressed by local dynamic-metaclass composition that delegates
  ordinary behavior to Sage and ABCMeta. If a project abstract requirement has the
  same name as a concrete method already supplied by the Sage parent-class bases, keep
  Sage's MRO as the source of satisfaction; do not let the abstract spec method shadow
  that concrete implementation.
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
- If a category-spec rule is relevant but not in context, load the matching category-spec skill or memory before acting. Do not guess from memory.
- Before reviewing recent category-spec commits, suspicious engineering-shaped patches,
  cache/lookup/cast/hook/QC work, or prior agent output, retrieve the ordinary governing
  memories by topic: `mem:repo-purpose-mathematical-research-machine`,
  `mem:category-spec-rotten-core-indicators`, `mem:mathematical-sanity-check`,
  `mem:analysis-must-be-grounded`, `mem:paperwork-is-a-routing-layer-not-progress`,
  and `mem:corrections-update-the-model-not-the-artifact`.
  If the work touches refinement, provider ordering, constructor refinement,
  abstract methods, ABCMeta, or smoke gaps, also retrieve
  `mem:category-spec-repo-model-corrections`,
  `mem:category-spec-refinement-category-declaration`,
  `mem:category-spec-methods-are-abstract`, and
  `mem:what-category-specs-actually-is`.
  Use `iwe find` with the relevant topic words if the exact memory key is not known.
- Before editing a spec, mapping, method surface, constructor, Hom/End/Aut rule,
  invariant, or predicate, perform the definition-grounding gate from
  `category-spec-style`: locate the exact mathematical definition and hypotheses in
  canonical repo theory, Sage written docs/source, references, spec backups, or an
  approved decision card. Vague migrated cards and old TODO bullets are not enough.
  If the definition is unclear, create or update a decision/source-mining card and
  stop that leaf.
- Constructor mapping has no deferred state. Every source-grounded Sage constructor
  shape recorded in mapping docs maps to a named-parameter category-owned overload or
  spec-layer promotion path. Ungrounded or rejected constructor ideas are absent from
  constructor mappings, provenance, smokes, decisions, and tasks; do not preserve them
  as "not admitted", "deferred", blocked, or gap records.
- Refinement targets one category: the smallest mathematically correct category for
  the object. Do not pass several categories to `refine_category`; inherited
  membership must come from the category hierarchy, not from manually listing
  ancestors at the call site.
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
