---
name: category-spec-subtrees
description: Use when working inside a specific category_specs subtree and needing local ownership, constructor, hom/end/aut, or test-directory guidance after nested AGENTS files were migrated into skills.
---

# Category Spec Subtrees

This skill is the canonical subtree-ownership guide for `category_specs/`.

## Canonical source

The source of truth is this skill plus `references/subtrees.md`.

Read `references/subtrees.md` before editing a category-specific subtree, moving methods between subtrees, writing subtree-specific tests, or deciding whether a method belongs in generic Cat/Hom/End/Aut infrastructure or a specialized category.

## Core policy

- `category_specs/AGENTS.md` is the only subtree AGENTS entry point.
- Lower nested `AGENTS.md` files were migrated here to avoid many always-loaded mini-manuals.
- Load `category-spec-style` for spec/code compliance and `category-spec-workflow` for cards, status, plans, smoke triage, or delegation.
- Use this skill for local ownership rules: which subtree owns which mathematical surface.
