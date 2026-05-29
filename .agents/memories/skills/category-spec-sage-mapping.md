---
title: Category Spec Sage Mapping
status: active
date: 2026-05-29
---
# Category Spec Sage Mapping

Use this skill for Sage-source inventory and mapping work in `category_specs`.

## Required references

Before mapping:

- Read `category_specs/AGENTS.md`.
- Load `category-spec-style` for mathematical ownership and constructor rules.
- Read `mem:skills/category-spec-workflow` for cards, priority, and decisions.

## Mapping workflow

- Read the Sage written docs, source, signature, and local usage before mapping.
- Translate Sage surfaces into project mathematical vocabulary.
- Map each constructor or method to one outcome: existing category surface, named
  project constructor, explicit mathematical rejection, decision card, or research card
  when evidence is missing.
- Preserve old functionality through a documented replacement path.
- Do not admit variadic or option-bag surfaces directly.
- Do not invent software-shaped helper types to avoid naming the mathematics.

## Output routing

- Create `task` or `feature` cards for executable mapping/implementation work.
- Create `decision` cards for unresolved ownership, naming, or admission choices.
- Use `.agents/TODO.md` only for vague findings that still need investigation.
