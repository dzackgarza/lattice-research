---
title: ONBOARDING — READ FIRST
included_by: [index]
---
# ONBOARDING — READ BEFORE ANY ACTION

**Do not read other files, run tools, scan plans, or edit anything until you have read
this entire document.** This is the gate.
Every agent session begins here.

## Completion discipline — the core invariant

Start from the mathematical object.
Route by a priori mathematical ownership.
Treat code as a witness.
Treat artifacts as consequences.
Treat hidden compliance as zero evidence.
Completion means a visible theorem, formula, representation split, or missing-category
obligation.

Hidden reasoning is not evidence.
A code edit, mapping label, prose explanation, or passing report that lacks one of those
four visible outputs is not progress.
If the artifact becomes cleaner while the mathematical owner remains unstated, the edit
is theater.

Separate four layers in every action:

1. **The mathematical object** (set, module, morphism, topological space, etc.)
2. **The expression object** (basis, coordinate chart, matrix representative, etc.)
3. **The implementation** (storage, normalization, backend calls, etc.)
4. **The category obligation** (the highest abstract category where the operation
   belongs)

A type error is a diagnostic, not an editing instruction.
A mapping row must name an owner, give a recovery formula, or declare a missing
category/spec obligation — it is never allowed to defer behind labels like "pending",
"abstract", or "rejected".

If the next move is to adjust a decorator, signature, label, section, report, or prose
explanation before the mathematical owner is visible, the frame is wrong.

See `mem:category-spec-epistemic-foundation` for the full completion discipline:
evidentiary rules, visible obligations, frame-rejection triggers, and mapping-document
purpose.

* * *

## What this project is

This is a **mathematical research repo**, not an engineering project.
The engineering exists only to build reliable mathematical language so that future
lattice/Coble work can state claims, define objects, and write proofs that read like
mathematics.

The test of progress is not completed cards, green checkboxes, or process artifacts.
The test is:

> What mathematical object, operation, claim, interface, or proof path is now closer
> because of this work?

If the answer is only "a card is clearer," "a plan is more detailed," or "handoff
context improved," presume no mathematical progress occurred.

Downstream Coble/lattice goals must NOT be attacked by raw matrix computations.
The repo is in the category-spec phase.
See `mem:repo-purpose-mathematical-research-machine`.

## Current phase

**Category-spec vocabulary.** Building the semantic substrate: sets, modules,
Hom/End/Aut, modules with forms, lattices, morphisms, coercions, backend bridges.
Downstream lattice/Coble work is blocked until this vocabulary exists.

Read `GOAL.md` once, but the phase is tracked in `.agents/current-goal-phase.md`. Do not
attempt downstream Coble research.

## Immediate concrete work

Read `mem:current-goal-handoff` for the most recent next action.
The handoff names **concrete, source-grounded fixes** — read the files it names,
understand the problem, and fix it.
Do not run tools, produce reports, or create process artifacts instead.

## The six most common agent failure modes

Learn these before you act.
Every one of these has happened.
Every one will waste the session if you repeat it.

### 1. Running tools instead of reading code

Error: Producing a mypy report, ledger, structural analysis, or classification before
reading the actual source files that the handoff names.

Rule: Read the code first.
The handoff names specific files and types of errors.
Read those files. If you cannot quote both sides of a conflict from source, you are not
allowed to classify or fix it.
See `mem:analysis-must-be-grounded`.

### 2. Producing process artifacts instead of concrete fixes

Error: Writing strategy documents, issue comments, acceptance criteria, or planning
documents when asked to fix a bug.

Rule: If the handoff says "fix ~25 private-stub annotation bugs," fix the annotations.
Do not write a document about fixing them.
Do not create a card.
Fix the code. See `mem:analysis-must-be-grounded` and
`mem:foundation-serves-research-not-itself`.

### 3. Treating private Sage stubs as types

Error: `_RingObjectMethods`, `_RModObjects`, `_RingHomomorphisms` etc.
appearing in return type annotations.
These are **private method-container stubs** used to organize Sage category definition
files. No object is an instance of `_RingObjectMethods`. No method returns one.

Rule: Any method whose declared return type is a private `_*Methods` or `_*Objects` name
has a **bug in the annotation**. Replace with the public type (`Ring`, `Module`,
`Morphism`, `Set`, etc.). This is mechanical.
No decision, variance analysis, or `# type: ignore` needed.
See `mem:private-stubs-are-not-types`.

### 4. Classifying errors without reading both sides of the conflict

Error: Inventing categories like "variance problem," "Liskov audit," or "interface
design question" before displaying the two conflicting method signatures side by side.

Rule: Before classifying any override/signature error, quote both definitions from the
actual code. The RealSet/topological-space incident involved `is_open(self, U: Subset)`
vs `is_open(self)` — an arity conflict visible in 30 seconds of reading.
An agent spent hours on ledger taxonomy instead.
See `mem:analysis-must-be-grounded` and `mem:mathematics-first-not-engineering-options`.

### 5. Trying to run mypy directly

Error: Running `mypy category_specs/` from the command line instead of through Sage.

Why it's wrong: The code imports Sage — needs `sage -python`. The mypy plugin teaches
mypy about Sage's dynamic category system (`_with_axiom`, dynamic inheritance,
method-container projection).
Running bare mypy fails on every import.

Why the automated structural report recipe is also wrong right now: The plugin CANNOT
produce correct output until the source-level annotation bugs (items 1 and 2 from the
handoff) are fixed. Running the tool before fixing the code is circular.

When to run it: After fixing the source-level errors, use
`just category-specs-mypy-structural-report` which correctly routes through
`sage -python` with the plugin.

### 6. Treating a process problem as a local patch

Error: Finding an embarrassing, fundamental error (e.g., `_QQ` declaring both `_Fields`
and `_NumberFields` as supercategories) and just fixing that one instance.

Rule: The presence of the bug proves the process is broken.
Create inspection tooling so the error is discoverable in the future, then fix the
concrete instance, then add a test that would have caught it.
See `mem:process-before-patches-policy`.

## How to start

1. Read this document. You are doing that now.
2. Read `mem:current-goal-handoff`.
3. Read the files named in the handoff.
4. Fix the bugs.
5. Update the handoff with what the next session should do.

## Critical follow-up memories

Read these when their situation arises:

| Situation | Memory |
| --- | --- |
| Before any surface edit, decorator change, or mapping | `mem:category-spec-epistemic-foundation` |
| Writing, editing, or retrieving a memory | `mem:memory-management-discipline` |
| About to write a return type for a method | `mem:private-stubs-are-not-types` |
| About to classify a mypy override error | `mem:analysis-must-be-grounded` |
| Two methods with the same name collide | `mem:mathematics-first-not-engineering-options` |
| Found an embarrassing category-graph bug | `mem:process-before-patches-policy` |
| About to produce a strategy doc instead of code | `mem:foundation-serves-research-not-itself` |
| Unsure about stub vs. plugin vs. internal work | `mem:category-spec-architectural-boundary` |
| Drifting from mathematical purpose | `mem:repo-purpose-mathematical-research-machine` |
| Writing specs or type annotations | `mem:category-spec-style` (skill) |

## Do not

- Run mypy, structural reports, or ledgers until the source-level bugs are fixed.
- Create cards, issues, or process documents instead of fixing code.
- Delegate concrete fix work to future agents.
- Produce analysis documents when asked for a fix.
- Classify errors without reading both sides of the conflict.
- Use `# type: ignore` or cast-based silencing.
- Write `NotImplementedError` — banned by pre-commit hook.
- Touch downstream Coble/lattice code.
