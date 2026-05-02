---
description: Track bugs, tasks, ideas, and other work items
---

# /track Command

Create a tracking item in the appropriate tracking document.

## Usage

```
/track [type] [description]
```

**Examples:**
- `/track bug Login fails on mobile Safari`
- `/track task Update API documentation`
- `/track idea Add dark mode support`
- `/track devblog-post How we built realtime sync`

## CRITICAL: Discover Custom Tracker Types First

Before creating a tracker item, **always check for custom tracker types** defined in the workspace:

1. Look for YAML files in `.nimbalyst/trackers/*.yaml` in the workspace root
2. Each YAML file defines a custom tracker type with a `type:` field (e.g., `type: devblog-post`)
3. The `type` field in the YAML is what goes after `#` in the tracker syntax (e.g., `#devblog-post[...]`)
4. The `idPrefix` field determines the ID prefix (e.g., `dev` produces IDs like `dev_abc123`)
5. Custom types have their own status options - use those, not the built-in ones

**If the user's requested type matches a custom tracker (even partially), use the custom type name exactly as defined in the YAML.**

For example, if `.nimbalyst/trackers/devblog-post.yaml` exists with `type: devblog-post`, then:
- `/track dev-blog Something` should use `#devblog-post`, NOT `#plan` or `#blog`
- The file goes in `nimbalyst-local/tracker/devblog-posts.md`, NOT `plans.md`

## Built-in Tracker Types

These are always available:
- **bugs.md**: Issues and defects (`#bug`)
- **tasks.md**: Work items and todos (`#task`)
- **ideas.md**: Concepts to explore (`#idea`)
- **decisions.md**: Important decisions (`#decision`)
- **plans.md**: Plans and features (`#plan`)

## Custom Tracker Types

Defined in `.nimbalyst/trackers/*.yaml`. Common custom types:
- **feature-requests.md**: User requests (`#feature-request`)
- **tech-debt.md**: Technical debt (`#tech-debt`)
- **devblog-posts.md**: Dev blog posts (`#devblog-post`)
- Any other type defined in the workspace's YAML files

## Item Format

Use the mode declared by `.nimbalyst/trackers/[type].yaml` when a YAML definition
exists.

For `modes.fullDocument: true`, create one markdown file per item under
`nimbalyst-local/tracker/[type]s/` with `trackingStatus` frontmatter:

```markdown
---
trackingStatus:
  itemId: [idPrefix]_[ulid]
  title: Brief description
  type: [type]
  status: [default-status]
  priority: medium
  assignee: null
  tags:
    - relevant-tag
  created: YYYY-MM-DD
  updated: YYYY-MM-DDTHH:MM:SS.000Z
---
```

Full-document task bodies must include the real task content, not only a title. Use at
least: `Summary`, `Source Provenance`, `Context`, `Acceptance Criteria`,
`Dependencies And Boundaries`, and `Work Log`. Keep
`nimbalyst-local/tracker/[type]s.md` as an index for full-document trackers; do not add
duplicate inline tracker tags there.

For inline-only trackers, use:

```markdown
- [Brief description] #[type][id:[idPrefix]_[ulid] status:[default-status] priority:medium created:YYYY-MM-DD]
```

The `[type]` and `[idPrefix]` come from the tracker YAML definition. The `[default-status]` comes from the first status option in the YAML, or `to-do` for built-in types.

## Execution Steps

1. **Check `.nimbalyst/trackers/*.yaml`** for custom tracker types that match the user's request
2. Parse the type from the command - match against custom types first, then built-in types
3. Use the correct `type` name and `idPrefix` from the YAML definition
4. Generate a unique ID using the prefix from the YAML (e.g., `dev_` for devblog-post)
5. Use the correct default status from the YAML definition
6. Determine priority from description keywords:
   - "critical", "urgent", "blocking" -> high/critical
   - "nice to have", "minor", "low" -> low
   - Otherwise -> medium
7. If the tracker has `modes.fullDocument: true`, write the full task file under
   `nimbalyst-local/tracker/[type]s/` and update the aggregate file only as an index.
8. If the tracker is inline-only, add to `nimbalyst-local/tracker/[type]s.md`
   (pluralize the type name)
9. Confirm where the item was tracked

## Migration Requirements

When converting existing docs into tracker items, preserve source paths, original
headings or lines, execution context, acceptance criteria, and boundaries in the
per-item body. Do not collapse a real task into a one-line tracker row when the tracker
supports full documents.

## CRITICAL: Do NOT Call tracker_create

**Never call the `tracker_create` MCP tool when executing /track.** The markdown file you write is automatically synced to the tracker widget via frontmatter/inline parsing. Calling `tracker_create` in addition to writing the markdown file creates a duplicate entry -- one from the file sync and one from the database insert. Only write the markdown file; the tracker system handles the rest.

## Best Practices

- Always check for custom tracker types before falling back to built-in ones
- Be specific in descriptions
- Include context when helpful
- Use the exact type name from the YAML definition
- Set priorities appropriately
