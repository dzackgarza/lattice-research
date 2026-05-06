# Research Project Workflow Reference

## Nimbalyst tracker workspace

All active planning, spec, task, and decision documents for this repo live under root
`plans/` and follow the central planning hierarchy:

```text
plans/features/FEATURE-ID/
├── FEATURE-ID.md
├── specs/SPEC-ID.md
├── decisions/DECISION-ID.md
└── plans/PLAN-ID/
    ├── PLAN-ID.md
    └── PHASE-ID/
        ├── PHASE-ID.md
        └── tasks/TASK-ID.md
```

Use `.agents/current-goal-phase.md` to identify the active staged-program phase. Use
`.agents/retired/` only for short-lived retired legacy cards. Do not create
`nimbalyst-local/tracker` indexes or parallel task inventories. The GUI is the index.

There is no separate backlog. The active tracked cards under `plans/features/` are the
outstanding work set. When work is implemented, resolved, rejected, or superseded, move
the card out of active paths and retire or delete it according to the retired-card
policy.

A plan is not a task container. A plan defines high-level phases and milestones. Each
execution item must exist as its own dedicated tracked file under a phase directory.

## Source order and local choices

Use these sources in order when interpreting or editing planning cards:

- `/home/dzack/ai/planning/AGENTS.md` defines the reusable card framework:
  hierarchy, layer gates, decision-card discipline, generated tags, no-fallback
  validation, and card responsibilities.
- `plans/AGENTS.md` defines this repo's local feature buckets, active root, and
  validation command.
- `.nimbalyst/trackers/*.yaml` defines the installed schema fields and allowed status
  values.
- `GOAL.md` and `.agents/current-goal-phase.md` define the staged mathematical phase
  gate. They do not become active tracker features.

The local schemas intentionally extend the reusable framework in small ways: blocked
statuses on feature/spec cards, priority and owner metadata on plan/phase/task cards,
and complexity on specs/tasks. Do not overwrite local schemas with central copies
unless the user explicitly asks for a schema migration. If the reusable framework and
local schema disagree, the local schema controls valid frontmatter while the reusable
framework controls workflow semantics unless repo policy is stricter.

## Standard tracker types

Accepted planning `trackerStatus.type` values are the registered central schemas in
`.nimbalyst/trackers/*.yaml`: `feature`, `spec`, `plan`, `phase`, `task`, and
`decision`.

Use containment and `dependsOn` as the primary workflow axes. Generated tags come from
feature, plan, and phase ancestry; do not manually maintain status rollups in card
bodies.

## Tracker frontmatter

Use YAML frontmatter and keep metadata in `trackerStatus`, not `trackingStatus`.

```markdown
---
id: TASK-REMOVE-RAW-CONDITIONSET-FROM-AUT-CATEGORY-SURFACE
trackerStatus:
  type: task
parents:
- '[[PHASE-EXAMPLE]]'
dependsOn: []
title: Remove raw ConditionSet from Aut category surface
status: unstarted
priority: medium
description: Replace the public ConditionSet surface with an explicit typed object.
successCriteria:
- Public Aut-category APIs no longer expose raw ConditionSet values.
complexity: 40
---
```

The `trackerStatus.type` value must match a registered schema. Card IDs must match
filename stems. Use `parents` for containment and `dependsOn` for blocking relations.

Metadata fields should stay compact. Put complex explanations, full acceptance
criteria, gates, tables, diagrams, examples, and other structured markdown in the body.

When an active card cannot proceed, set `status: blocked` if its tracker schema
supports that value, record the exact blocker in the body, and link or create the
prerequisite task, research item, or decision. A blocked card remains active until it is
accepted, rejected, or superseded.

## Layer-gated workflow

Build and approve cards top-down. Approval is local to the layer being approved.

- Feature/spec gate: write the feature card and durable spec cards before
  implementation planning. The feature defines the user or research outcome, scope,
  non-goals, contracts, and major links. Specs define stable observable requirements
  and verification obligations that remain true if the implementation plan changes.
- Plan gate: after feature/spec approval, create sibling plan cards under the feature.
  A plan designs milestone phases, sequencing, scope boundaries, validation
  expectations, risks, and expected drill-down shape. It must not become a task index.
- Phase gate: after plan approval, create phase cards under the owning plan. A phase
  converts one milestone into task-card design, resolves local operational decisions,
  records ordering constraints, and defines phase acceptance gates.
- Task gate: after the phase breakdown is accepted, create task cards under the
  phase's `tasks/` directory. A task is the executable contract: exact objective,
  allowed scope, dependencies, acceptance checks, and verification command or proof
  artifact.

Do not create tasks first and backfill higher layers. Do not use plans above plans to
simulate feature hierarchy. Do not approve a phase for execution while child tasks
still contain unresolved decisions.

## Decision-card discipline

Unresolved decision language is not durable card content. Phrases such as "decide
whether", "choose an approach", "TBD", "figure out", "investigate and implement", or
"handle appropriately" must be resolved at the current layer or converted into a
feature-level decision card.

Use a decision card only when work cannot continue because the answer does not follow
from approved cards, repo policy, existing contracts, or canonical mathematical
sources. Place it under `plans/features/FEATURE-ID/decisions/`, parent it to the
feature, link blocked cards with `dependsOn`, and mark only the actually blocked cards
`blocked`.

When a decision is made, record the chosen contract in the dependent feature/spec/plan,
phase, or task body. The decision card stores the decision question, constraints,
options, and chosen answer; it does not become an implementation plan.

## Inline items

Avoid inline items in general. Use inline entries only as temporary placeholders while
a broader task is being discovered and a full tracker file is being prepared.

Inline items define a task but provide little context by construction. Any inline item
that is ready to be solved, assigned, or actively worked on must be converted into a
full markdown file under `plans/features/.../tasks/` before execution.

Do not call `create_task` or `tracker_create` for inline items. That creates a
database-only entry with no backing file and produces a duplicate.

## Card responsibilities and progressive disclosure

Use root `plans/` for Nimbalyst-backed planning documents. Plans are strictly human +
LLM collaborative artifacts. To create or materially revise a plan, switch to planning
mode, use the planning tools, iterate with the user until approval, then decompose the
approved plan into tracked phase and task files. Do not enact a chat-only,
harness-local, scratch, or unapproved plan.

Plan placement follows the hierarchy in `plans/AGENTS.md`. Root features own sibling
plans. Plans own phases. Phases own tasks. Specs live under the owning feature's
`specs/` directory, and decisions live under the owning feature's `decisions/`
directory.

The staged program remains explicit in `GOAL.md` and `.agents/current-goal-phase.md`,
while the active planning corpus lives under `plans/features/`.

Write each card for its own level:

- Feature cards own the feature boundary, outcome, scope, non-goals, major contracts,
  and links to specs and plans.
- Spec cards own durable requirements, public contracts, acceptance criteria, and
  verification obligations. They must not depend on phase names, phase order, task
  layout, or current implementation sequencing.
- Plan cards own phase design: phase outcomes, scope boundaries, todo clusters,
  dependencies, validation expectations, risks, and drill-down shape. They may mention
  representative task shapes, but they must not author task cards.
- Phase cards own local task design, task links, ordering constraints, phase
  acceptance gates, and audit checks. They must not manually track child task status,
  owner, completion percentage, or review state.
- Task cards own executable implementation or research work. They must be specific
  enough that an agent can act without deciding product behavior, mathematical
  definitions, architecture, scope, sequencing, or acceptance criteria.

Avoid inline task markers. Use `.agents/TODO.md` only as a scratchpad inbox for
tangential discoveries that need investigation before they can become real cards.
Convert anything executable into a full tracked file with context, source provenance,
boundaries, and acceptance criteria before assignment.

Subtree `AGENTS.md` files may stay small by delegating detailed policy to local skills
and skill-local references. Agents must load those skills when their task matches the
documented trigger.

## Validation and generated planning data

Run `just plan-validate` from the repo root after editing planning cards, local tracker
schemas, `plans/AGENTS.md`, or `.agents/current-goal-phase.md`.

For substantial hierarchy, schema, generated tag, or DAG work, also run the reusable
framework recipe explicitly with absolute repo paths. The reusable justfile executes
from `/home/dzack/ai/planning`, so relative project paths will not resolve correctly.

```bash
just --justfile /home/dzack/ai/planning/justfile validate /home/dzack/research/plans/features /home/dzack/research/.nimbalyst/trackers /home/dzack/research/plans/plan-dag.md
```

The reusable recipe derives structural tags, checks schemas, and regenerates
`plans/plan-dag.md`. If validation or hooks rewrite tags or `plans/plan-dag.md`, inspect
and stage those generated changes deliberately. Do not replace validation failures with
warnings or fallback groups.

Do not add timestamp metadata such as `created` or `updated` to card frontmatter unless
the installed schema declares those fields. Strict validation treats undeclared metadata
as invalid card data; remove the card fields rather than expanding schemas to admit
accidental metadata.

Recommended local hook behavior: run the reusable validation recipe from pre-commit
when staged planning cards or tracker schemas change, and from post-merge/post-checkout
when the changed paths include `plans/features/`, `plans/AGENTS.md`,
`plans/plan-dag.md`, `.nimbalyst/trackers/`, or `.agents/current-goal-phase.md`. Hooks
should fail on validation errors. If a hook regenerates tags or `plans/plan-dag.md`, it
should leave the changes visible and require deliberate staging.

## Quick card queries

Use these from the repo root for quick status reads. They are suggested ad hoc queries,
not new source-of-truth scripts.

List every card as status, type, id, title, path:

```bash
uvx --with pyyaml python -c 'from pathlib import Path; import re,yaml; rows=[(fm.get("status",""),fm.get("trackerStatus",{}).get("type",""),fm.get("id",""),fm.get("title",""),str(p)) for p in sorted(Path("plans/features").rglob("*.md")) for m in [re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", p.read_text(encoding="utf-8"), re.S)] if m for fm in [yaml.safe_load(m.group(1)) or {}]]; print("\n".join("\t".join(map(str,row)) for row in rows))'
```

List cards with a specific status; change the `status` literal as needed:

```bash
uvx --with pyyaml python -c 'from pathlib import Path; import re,yaml; status="blocked"; rows=[(fm.get("trackerStatus",{}).get("type",""),fm.get("id",""),fm.get("title",""),str(p)) for p in sorted(Path("plans/features").rglob("*.md")) for m in [re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", p.read_text(encoding="utf-8"), re.S)] if m for fm in [yaml.safe_load(m.group(1)) or {}] if fm.get("status")==status]; print("\n".join("\t".join(map(str,row)) for row in rows))'
```

Count cards by type and status:

```bash
uvx --with pyyaml python -c 'from pathlib import Path; import collections,re,yaml; counts=collections.Counter((fm.get("trackerStatus",{}).get("type",""),fm.get("status","")) for p in sorted(Path("plans/features").rglob("*.md")) for m in [re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", p.read_text(encoding="utf-8"), re.S)] if m for fm in [yaml.safe_load(m.group(1)) or {}]); print("\n".join(f"{kind}\t{status}\t{count}" for (kind,status),count in sorted(counts.items())))'
```

List active leaf cards, meaning cards with no child containment references and status
not in a completion status:

```bash
uvx --with pyyaml python -c 'exec("from pathlib import Path\nimport re,yaml\ncomplete={\"complete\",\"done\",\"decided\",\"implemented\"}\nrecords={}\nchildren=set()\ndef ref(v):\n    if isinstance(v,str): vals=[v]\n    elif isinstance(v,list): vals=v\n    else: vals=[]\n    return [x[2:-2] if isinstance(x,str) and x.startswith(\"[[\") and x.endswith(\"]]\") else x for x in vals if isinstance(x,str)]\nfor p in sorted(Path(\"plans/features\").rglob(\"*.md\")):\n    m=re.match(r\"^---\\r?\\n(.*?)\\r?\\n---\\r?\\n?\", p.read_text(encoding=\"utf-8\"), re.S)\n    if not m: continue\n    fm=yaml.safe_load(m.group(1)) or {}\n    cid=fm.get(\"id\")\n    if cid: records[cid]=(p,fm)\nfor cid,(p,fm) in records.items():\n    children.update(parent for parent in ref(fm.get(\"parents\")) if parent in records)\nrows=[]\nfor cid,(p,fm) in records.items():\n    if cid not in children and fm.get(\"status\") not in complete:\n        rows.append((fm.get(\"status\",\"\"),fm.get(\"trackerStatus\",{}).get(\"type\",\"\"),str(fm.get(\"complexity\",\"\")),fm.get(\"priority\",\"\"),cid,fm.get(\"title\",\"\"),str(p)))\nprint(\"\\n\".join(\"\\t\".join(map(str,row)) for row in rows))")'
```

## Visual windows

Use `.agents/visuals/` for optional human-facing windows into complex systems. Visuals
are supporting material only; the operative state remains in tracked feature, spec,
plan, phase, task, and decision files under `plans/features/`.
