#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml",
# ]
# ///

from __future__ import annotations

import argparse
import collections
import dataclasses
import datetime as dt
import math
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
PLANS_ROOT = ROOT / "plans" / "features"
SCHEMA_ROOT = ROOT / ".nimbalyst" / "trackers"
ACTIVE_ROOT = PLANS_ROOT
COMPLETED_ROOT = PLANS_ROOT / "completed"
FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?", re.S)


@dataclasses.dataclass(frozen=True)
class Card:
    card_id: str
    kind: str
    status: str
    title: str
    path: Path
    parents: tuple[str, ...]
    depends_on: tuple[str, ...]
    priority: str | None
    tags: tuple[str, ...]
    is_completed_tree: bool


@dataclasses.dataclass(frozen=True)
class CommitInfo:
    sha: str
    date: dt.datetime
    subject: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a Markdown report summarizing current planning-card progress "
            "from plans/features and local tracker schemas."
        )
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the report to this path instead of stdout.",
    )
    parser.add_argument(
        "--recent-limit",
        type=int,
        default=15,
        help="Number of recently completed cards to include. Default: 15.",
    )
    return parser.parse_args()


def read_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if match is None:
        raise ValueError(f"{path}: missing YAML frontmatter")
    loaded = yaml.safe_load(match.group(1))
    if loaded is None:
        return {}
    if not isinstance(loaded, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return loaded


def normalize_refs(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        return ()
    refs: list[str] = []
    for item in value:
        if not isinstance(item, str):
            continue
        match = re.fullmatch(r"\[\[([A-Z0-9-]+)\]\]", item)
        refs.append(match.group(1) if match else item)
    return tuple(refs)


def load_status_completion_map() -> dict[str, set[str]]:
    completion_map: dict[str, set[str]] = {}
    for schema_path in sorted(SCHEMA_ROOT.glob("*.yaml")):
        schema = yaml.safe_load(schema_path.read_text(encoding="utf-8")) or {}
        if not isinstance(schema, dict):
            continue
        kind = schema.get("type")
        if not isinstance(kind, str):
            continue
        completed: set[str] = set()
        for field in schema.get("fields", []):
            if not isinstance(field, dict) or field.get("name") != "status":
                continue
            for option in field.get("options", []):
                if not isinstance(option, dict):
                    continue
                value = option.get("value")
                label = str(option.get("label", ""))
                if not isinstance(value, str):
                    continue
                normalized_label = label.casefold()
                if any(
                    token in normalized_label
                    for token in ("done", "complete", "completed", "implemented", "decided", "accepted")
                ):
                    completed.add(value)
        completion_map[kind] = completed
    return completion_map


def infer_kind(path: Path, card_id: str) -> str | None:
    rel = path.relative_to(PLANS_ROOT)
    parts = rel.parts
    if parts and parts[0] == "completed":
        parts = parts[1:]
    if len(parts) == 2 and parts[0] == card_id and parts[1] == f"{card_id}.md":
        return "feature"
    if len(parts) == 3 and parts[1] == "specs":
        return "spec"
    if len(parts) == 3 and parts[1] == "decisions":
        return "decision"
    if len(parts) == 4 and parts[1] == "plans" and parts[2] == card_id:
        return "plan"
    if len(parts) == 5 and parts[1] == "plans" and parts[3] == card_id and parts[4] == f"{card_id}.md":
        return "phase"
    if len(parts) == 6 and parts[1] == "plans" and parts[4] == "tasks":
        return "task"
    return None


def load_cards() -> dict[str, Card]:
    cards: dict[str, Card] = {}
    for path in sorted(PLANS_ROOT.rglob("*.md")):
        frontmatter = read_frontmatter(path)
        card_id = frontmatter.get("id")
        if not isinstance(card_id, str):
            continue
        kind = infer_kind(path, card_id) or str(frontmatter.get("trackerStatus", {}).get("type", "unknown"))
        cards[card_id] = Card(
            card_id=card_id,
            kind=kind,
            status=str(frontmatter.get("status", "unknown")),
            title=str(frontmatter.get("title", card_id)),
            path=path,
            parents=normalize_refs(frontmatter.get("parents")),
            depends_on=normalize_refs(frontmatter.get("dependsOn")),
            priority=(str(frontmatter["priority"]) if "priority" in frontmatter and frontmatter["priority"] is not None else None),
            tags=tuple(frontmatter.get("tags", []) if isinstance(frontmatter.get("tags"), list) else ()),
            is_completed_tree=COMPLETED_ROOT in path.parents,
        )
    return cards


def completion_ratio(done: int, total: int) -> float:
    return 0.0 if total == 0 else done / total


def bar(ratio: float, width: int = 24) -> str:
    filled = min(width, max(0, int(round(ratio * width))))
    return f"[{'#' * filled}{'-' * (width - filled)}] {ratio * 100:5.1f}%"


def summarize_counts(cards: dict[str, Card], completed_statuses: dict[str, set[str]]) -> dict[str, collections.Counter[str]]:
    counts: dict[str, collections.Counter[str]] = {}
    for card in cards.values():
        counts.setdefault(card.kind, collections.Counter())[card.status] += 1
    return counts


def is_complete(card: Card, completed_statuses: dict[str, set[str]]) -> bool:
    return card.status in completed_statuses.get(card.kind, set())


def children_map(cards: dict[str, Card]) -> dict[str, set[str]]:
    child_map: dict[str, set[str]] = collections.defaultdict(set)
    for card in cards.values():
        for parent in card.parents:
            if parent in cards:
                child_map[parent].add(card.card_id)
    return child_map


def descendants(root_id: str, child_map: dict[str, set[str]]) -> set[str]:
    seen: set[str] = set()
    stack = list(child_map.get(root_id, ()))
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        stack.extend(child_map.get(current, ()))
    return seen


def git_commit_for_path(path: Path) -> CommitInfo | None:
    try:
        raw = subprocess.check_output(
            [
                "git",
                "-C",
                str(ROOT),
                "log",
                "-1",
                "--format=%H%x1f%cI%x1f%s",
                "--",
                str(path.relative_to(ROOT)),
            ],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        return None
    if not raw:
        return None
    sha, iso_date, subject = raw.split("\x1f", 2)
    return CommitInfo(
        sha=sha,
        date=dt.datetime.fromisoformat(iso_date.replace("Z", "+00:00")),
        subject=subject,
    )


def recent_completed_cards(
    cards: dict[str, Card],
    completed_statuses: dict[str, set[str]],
    limit: int,
) -> list[tuple[Card, CommitInfo]]:
    results: list[tuple[Card, CommitInfo]] = []
    for card in cards.values():
        if not is_complete(card, completed_statuses):
            continue
        commit = git_commit_for_path(card.path)
        if commit is None:
            continue
        results.append((card, commit))
    results.sort(key=lambda item: item[1].date, reverse=True)
    return results[:limit]


def feature_rollups(
    cards: dict[str, Card],
    completed_statuses: dict[str, set[str]],
    child_map: dict[str, set[str]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for card in cards.values():
        if card.kind != "feature":
            continue
        ids = {card.card_id, *descendants(card.card_id, child_map)}
        relevant = [cards[card_id] for card_id in ids if card_id in cards]
        total = len(relevant)
        done = sum(1 for item in relevant if is_complete(item, completed_statuses))
        blocked = sum(1 for item in relevant if item.status == "blocked")
        in_progress = sum(1 for item in relevant if item.status == "in-progress")
        needs_review = sum(1 for item in relevant if item.status == "needs-review")
        rows.append(
            {
                "card": card,
                "total": total,
                "done": done,
                "blocked": blocked,
                "in_progress": in_progress,
                "needs_review": needs_review,
                "ratio": completion_ratio(done, total),
            }
        )
    rows.sort(key=lambda row: (-row["ratio"], row["card"].title.casefold()))
    return rows


def most_blocked_items(cards: dict[str, Card]) -> list[Card]:
    blocked = [card for card in cards.values() if card.status == "blocked"]
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, None: 4}
    blocked.sort(key=lambda card: (priority_order.get(card.priority, 5), card.kind, card.title.casefold()))
    return blocked[:15]


def high_priority_active(cards: dict[str, Card], completed_statuses: dict[str, set[str]]) -> list[Card]:
    items = [
        card
        for card in cards.values()
        if not is_complete(card, completed_statuses)
        and card.priority in {"critical", "high"}
        and card.status != "blocked"
    ]
    priority_order = {"critical": 0, "high": 1}
    items.sort(key=lambda card: (priority_order.get(card.priority, 2), card.kind, card.title.casefold()))
    return items[:15]


def active_vs_completed_feature_trees(cards: dict[str, Card], completed_statuses: dict[str, set[str]]) -> tuple[int, int]:
    active = 0
    completed = 0
    for card in cards.values():
        if card.kind != "feature":
            continue
        if card.is_completed_tree or is_complete(card, completed_statuses):
            completed += 1
        else:
            active += 1
    return active, completed


def render_report(
    cards: dict[str, Card],
    completed_statuses: dict[str, set[str]],
    recent_limit: int,
) -> str:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    counts = summarize_counts(cards, completed_statuses)
    child_map = children_map(cards)
    rollups = feature_rollups(cards, completed_statuses, child_map)
    recent = recent_completed_cards(cards, completed_statuses, recent_limit)
    blocked = most_blocked_items(cards)
    priority = high_priority_active(cards, completed_statuses)
    active_features, completed_features = active_vs_completed_feature_trees(cards, completed_statuses)

    all_cards = list(cards.values())
    done_cards = sum(1 for card in all_cards if is_complete(card, completed_statuses))
    total_cards = len(all_cards)
    overall_ratio = completion_ratio(done_cards, total_cards)

    lines: list[str] = []
    lines.append("# Planning Progress Report")
    lines.append("")
    lines.append(f"_Generated: {now}_")
    lines.append("")
    lines.append("## Overall")
    lines.append("")
    lines.append(f"- Total cards: **{total_cards}**")
    lines.append(f"- Completed cards: **{done_cards}**")
    lines.append(f"- Overall progress: `{bar(overall_ratio)}`")
    lines.append(f"- Active feature trees: **{active_features}**")
    lines.append(f"- Completed feature trees: **{completed_features}**")
    lines.append("")
    lines.append("## Counts By Type")
    lines.append("")
    lines.append("| Type | Total | Completed | In Progress | Needs Review | Blocked |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: |")
    for kind in sorted(counts):
        counter = counts[kind]
        total = sum(counter.values())
        completed = sum(counter[status] for status in completed_statuses.get(kind, set()))
        lines.append(
            "| "
            + " | ".join(
                [
                    kind,
                    str(total),
                    str(completed),
                    str(counter.get("in-progress", 0)),
                    str(counter.get("needs-review", 0)),
                    str(counter.get("blocked", 0)),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Feature Rollup")
    lines.append("")
    lines.append("| Feature | Progress | Done/Total | In Progress | Needs Review | Blocked |")
    lines.append("| --- | --- | ---: | ---: | ---: | ---: |")
    for row in rollups:
        feature = row["card"]
        lines.append(
            "| "
            + " | ".join(
                [
                    feature.title,
                    f"`{bar(row['ratio'], width=16)}`",
                    f"{row['done']}/{row['total']}",
                    str(row["in_progress"]),
                    str(row["needs_review"]),
                    str(row["blocked"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## High-Priority Active Items")
    lines.append("")
    if not priority:
        lines.append("- None.")
    else:
        for card in priority:
            lines.append(
                f"- `{card.kind}` `{card.card_id}`: {card.title} "
                f"(`{card.priority}`, `{card.status}`)"
            )
    lines.append("")
    lines.append("## Blocked Items")
    lines.append("")
    if not blocked:
        lines.append("- None.")
    else:
        for card in blocked:
            priority_label = card.priority or "unspecified"
            lines.append(
                f"- `{card.kind}` `{card.card_id}`: {card.title} "
                f"(`{priority_label}`)"
            )
    lines.append("")
    lines.append("## Most Recently Completed")
    lines.append("")
    if not recent:
        lines.append("- No completed cards with recorded git history were found.")
    else:
        for card, commit in recent:
            date_text = commit.date.astimezone(dt.timezone.utc).strftime("%Y-%m-%d")
            lines.append(
                f"- {date_text} `{card.kind}` `{card.card_id}`: {card.title} "
                f"(commit `{commit.sha[:7]}`: {commit.subject})"
            )
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(
        "- Completion status is inferred from the local tracker schema labels "
        "such as `Done`, `Complete`, `Implemented`, and `Decided`."
    )
    lines.append(
        "- Recently completed items are cards currently in a completed status, "
        "sorted by the most recent git commit touching that card file."
    )
    lines.append(
        "- Completed feature trees may live under `plans/features/completed/`; "
        "this report includes them in totals."
    )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    cards = load_cards()
    completed_statuses = load_status_completion_map()
    report = render_report(cards, completed_statuses, max(1, args.recent_limit))
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)
        if not report.endswith("\n"):
            sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
