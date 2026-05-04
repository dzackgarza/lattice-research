# AGENTS.md - category_specs

This file is the mandatory entry point for agents working under `category_specs/`. Keep it small. Canonical category-spec guidance lives in local skills under `.agents/skills/category-spec-*`.

## Directive alignment

Before acting, confirm the user's stated directive, the action you plan, and why the action matches that directive rather than a substituted goal.

## Always-active rules

- Obey the repo root `AGENTS.md`; load `research-state-machine` for plan-to-execution routing and acceptance, and load `research-proof-auditing` for proof, evidence, and audit-sufficiency questions.
- Treat spec files, review files, theory notes, TODO files, and durable design artifacts as source material. Do not rewrite, shorten, modernize, or delete them unless the user explicitly asks for that exact edit.
- Use Nimbalyst tracker files for planning, follow-ups, blockers, decisions, deferred compliance findings, smoke triage, and outstanding work. Do not create ad hoc planning, status, audit, or TODO markdown files when a tracked file is the right durable artifact.
- Use only standard registered tracker types. Classify category-spec work with tags and `.agents` paths, not custom `x-work` types.
- Never call `tracker_create` or `create_task` for markdown-backed tracker items.
- Never mark work `accepted`, native items `done`, or sprint plans `closed` without human approval.
- If a category-spec rule is relevant but not in context, load the matching category-spec skill before acting. Do not guess from memory.
- Before editing a spec, mapping, method surface, constructor, Hom/End/Aut rule,
  invariant, or predicate, perform the definition-grounding gate from
  `category-spec-style`: locate the exact mathematical definition and hypotheses in
  canonical repo theory, Sage written docs/source, references, spec backups, or an
  approved decision card. Vague migrated cards and old TODO bullets are not enough.
  If the definition is unclear, create or update a decision/source-mining card and
  stop that leaf.
- For domain-specific terms with multiple plausible meanings, keep the meanings
  separate unless a source-backed proof records exactly when they coincide. Do not
  write a spec surface by normalizing to the most familiar interpretation of a word.

## Canonical skills

- Load `category-spec-style` before any task that touches category-spec content or compliance: specs, category surfaces, method surfaces, constructors, morphisms, Hom/End/Aut surfaces, Sage wrappers, type annotations, test files, smoke files, implementations, Sage inventory, or mapping documents.
- Load `category-spec-subtrees` before editing a specific category subtree or deciding where a method, constructor, Hom/End/Aut rule, or subtree test belongs.
- Load `category-spec-workflow` before any task that touches execution mechanics: tracker item creation or migration, Nimbalyst plans, sprint metadata, tracked work metadata, delegation contracts, subagent instructions, branch/PR policy, smoke triage, validation handoff, stale-document migration, or status changes.
- Load narrower category-spec skills when their descriptions match the task: audit, planning, retirement, Sage mapping, smoke triage, triage, and visuals.

## Removed local docs

`STYLE.md`, `WORKFLOW.md`, and lower nested `AGENTS.md` files have been migrated into skills and should not be recreated as parallel docs. If an older prompt references one of those files, load the corresponding category-spec skill instead.
