---
name: category-spec-audit
description: Use when auditing category-spec cards, specs, smoke work, or implementations
  for mathematical ownership, style compliance, minimal indirection, anti-slop, and
  downstream-poisoning risks.
---

# Category Spec Audit

Use this skill when reviewing category-spec work for compliance and downstream risk.

## Required references

Before auditing:

- Read `category_specs/AGENTS.md`.
- Load `category-spec-style` for mathematical and code/spec compliance.
- Load `category-spec-workflow` for card, priority, decision, visual, and retirement handling.

## Audit focus

- Specced vocabulary exists before implementation proceeds.
- Mathematical ownership is explicit and placed at the most general correct surface.
- Foundations are complete enough to avoid downstream rewrites.
- Complexity is hidden behind mathematical nouns, not ad hoc helper sprawl.
- Indirection is minimal and meaningful.
- Sage interop is mapped, not blindly wrapped.
- Docs and references are current enough to prevent backsliding or confabulation.

## Output routing

- Record defects as `bug` cards when they are concrete failures.
- Record missing work as `task` or `feature` cards.
- Record unresolved mathematical or organizational choices as `decision` cards.
- Add vague or tangential observations to `.agents/TODO.md`.
- Do not create free-form audit reports unless explicitly requested.
