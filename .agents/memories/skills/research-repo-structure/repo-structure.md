---
title: Research Repo Structure Reference
status: active
date: 2026-05-29
---
# Research Repo Structure Reference

## Environment and sacred files

The Sage path is `/home/dzack/miniforge3/envs/sage/bin/sage`. All computation,
validation, and paper builds run through the `justfile`. `GOAL.md` is read-only.
`theory/references/index.md` is append-only.

## Directory organization

Baseline durable roots: `src/`, `tests/`, `notes/`, `theory/`,
`theory/references/literature/`, `paper/`, `reports/`, `lean/`, `tasks/`, `.agents/`,
and `scratch/`.

## Where code goes

`src/` is finalized, permanent, reusable backend and tool code.
`tests/` contains verified mathematical tests run via pytest.
`scratch/` is gitignored.
Lean formalizations go in `lean/`.

## Directory proliferation gate

Routing: verified computation → `tests/`, reusable code → `src/`, exploratory draft →
`scratch/`, mathematical observations → `notes/`, proof sketches → `notes/proofs/`, Lean
→ `lean/`, living paper → `paper/`, reports → `reports/workstreams/`, papers →
`theory/references/literature/`, task artifacts → `tasks/`, theory docs → `theory/`,
operational context → agent memory, change rationale → git commit messages.

There is no `computations/` directory.
There is no `scripts/` root.

## Broken work policy

Broken computations get fixed or deleted.
Never document and preserve them.

## Spec and durable artifact preservation

Spec files, review files, theory notes, TODO files, and other durable design artifacts
are source material.
Autonomous agents must never modify spec files.
A spec that disagrees with code is not stale implementation debris — it may define the
migration target.

## Debris handling

Do not delete or remove any file unless you can directly prove it was created by a
subagent, or the user explicitly authorizes the deletion.
Before cleanup that touches multiple files, list what will be removed and wait for user
confirmation.

## Runtime caches

All repo workflows run through `just`. Expensive deterministic backend computations may
use the repo cache configured by `.envrc`. Treat cache as local generated state, not
source.
