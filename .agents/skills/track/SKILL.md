---
name: track
description: Use when creating tracking items from `/track` commands. The skill maps types to tracker files, writes the markdown item, and confirms the target document.
---

# /track Command

Create a tracking item in the correct tracker document.

## Usage

```
/track [type] [description]
```

Examples:

- `/track bug Login fails on mobile Safari`
- `/track task Update API documentation`
- `/track idea Add dark mode support`
- `/track devblog-post How we built realtime sync`

## Critical Priority: Custom Tracker Discovery First

Before creating any tracker item:

1. Read `.nimbalyst/trackers/*.yaml` for custom definitions.
2. Match custom types before built-in types.
3. Use the YAML fields exactly:
   - `type` becomes the tracker token after `#`
   - `idPrefix` is used in generated IDs
   - statuses come from the YAML `statuses` list

If the user-provided type partially matches a custom type, use the custom
`type` name exactly as defined in YAML.

Example: if `devblog-post.yaml` defines `type: devblog-post`, then `/track dev-blog`
maps to `#devblog-post` and the file goes to
`nimbalyst-local/tracker/devblog-posts.md`, not `plans.md`.

## Built-in Tracker Types

Always available:

- `bugs.md` (`#bug`)
- `tasks.md` (`#task`)
- `ideas.md` (`#idea`)
- `decisions.md` (`#decision`)
- `plans.md` (`#plan`)

Custom tracker files under `.nimbalyst/trackers/*.yaml` add additional types such as:

- `feature-requests.md` (`#feature-request`)
- `tech-debt.md` (`#tech-debt`)
- `devblog-posts.md` (`#devblog-post`)
- plus any custom types declared in the workspace

## Item Format

Add one line entry:

```markdown
- [Brief description] #[type][id:[idPrefix]_[ulid] status:[default-status] priority:medium created:YYYY-MM-DD]
```

- `[type]` and `[idPrefix]` come from YAML or built-in defaults
- `[default-status]` is the YAML first status, or `to-do` for built-ins

## Execution Steps

1. Load custom tracker definitions from `.nimbalyst/trackers/*.yaml`.
2. Parse the requested tracker type, preferring matches in custom types.
3. Resolve `[type]` and `[idPrefix]` from YAML or use built-in defaults.
4. Generate the tracker ID with the resolved `idPrefix`.
5. Set default status from the tracker definition.
6. Infer priority:
   - include `critical`, `urgent`, or `blocking` => `high` or `critical`
   - include `nice to have`, `minor`, or `low` => `low`
   - otherwise `medium`
7. Append to `nimbalyst-local/tracker/[type]s.md` (pluralized type name).
8. Confirm the destination file to the user.

## Hard Constraint

**Do not call `tracker_create`.** Only write the markdown file. The tracker sync
reads markdown and updates the tracker widget; a direct tool call would create
duplicates.
