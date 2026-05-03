# Retired cards

This directory is a temporary holding area for completed, rejected, or superseded cards
that no longer belong in active task paths.

This is not a permanent archive. Durable history belongs in git commit messages, PRs,
plan history, and canonical decisions/docs.

Use this directory only when a card may still be useful for short-term review,
recovery, or migration context. Delete retired cards when that need ends.

Before moving a card here:

- Record the durable outcome in git, PRs, linked plans, or canonical docs.
- Update linked plans, decisions, and follow-up cards.
- Set a terminal status supported by the tracker schema.
- Add a pointer to the merge commit, PR, replacement card, or decision that now carries
  the durable record.

Do not retire durable decisions that still prevent backsliding. Keep those in
`.agents/decisions/` or promote them into canonical documentation.
