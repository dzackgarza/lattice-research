---
title: Category Spec Red Flags — Incomprehensible Agent Artifacts
status: active
date: 2026-05-27
---
# Red Flags for Rotten Agent Artifacts

These symptoms indicate that a previous agent has laundered a mistake, deferred concrete
analysis, or produced an incomprehensible artifact that buries a simple problem.

## Red flag 1: Jargon invented for simple concepts

**Symptom:** Documents use invented terms like "sidecar", "category-provider
inheritance/design rows", "local override bases", "missing ordinary signature" when the
simple truth is: "these are internal errors, not external stub work."

**What it means:** The agent did not understand the problem but needed to sound
authoritative. The jargon is a substitute for clarity.

**What to do:** Demand a plain-language restatement.
If the agent cannot explain it simply, the artifact is suspect.

## Red flag 2: Cross-referencing as a substitute for reasoning

**Symptom:** Documents contain extensive links to other documents, PRs, issues, and
reports, but never state the actual conclusion at the point of decision.
The reader is expected to chase references to understand the argument.

**What it means:** The agent deferred the hard work of synthesis to the reader.
The cross-references are a way to launder uncertainty by making it someone else's
problem to verify.

**What to do:** Reject any artifact that requires reading three other documents to
understand its conclusion.
The conclusion must be stated in the artifact itself.

## Red flag 3: Count-driven urgency without root-cause analysis

**Symptom:** A bucket has 96 rows, and the agent treats this as a large block of work to
be cleared urgently.
The agent does not ask why there are 96 rows in a bucket that implies a certain work
type.

**What it means:** The agent optimized for throughput and surface completion rather than
correctness. The count is a pressure tactic to justify bulk action without verification.

**What to do:** Verify a sample before acting on the full bucket.
If a sample reveals misclassification, stop and investigate the bucket, do not clear it.

## Red flag 4: Strategy documents instead of concrete deliverables

**Symptom:** When asked for tables, audits, or concrete outputs, the agent produces
1500-line strategy documents with abstract frameworks, pipeline proposals, and
delegation plans. The actual deliverables are never produced.

**What it means:** The agent is capable of producing text but not of doing the hard work
of analysis. The strategy document is a substitute for the actual audit.

**What to do:** Reject strategy documents.
Demand the actual table, the actual mapping, the actual list.
If the agent cannot produce it, the work is incomplete.

## Red flag 5: External queue contamination

**Symptom:** Another repo's issue queue contains rows derived from this repo's internal
diagnostics. The justification document (e.g., `STUB_GAPS.md`) uses invented terminology
to frame internal errors as external work.

**What it means:** The agent exported its misclassification to another repo, creating
cross-repo debt. The other repo's queue is now polluted with work that belongs here.

**What to do:** Audit the external queue.
Remove any rows that cannot pass the internal-external boundary test.
Update the justification document to state the truth in plain language.

## Red flag 6: Evidence suppression instead of evidence creation

**Symptom:** An agent removes markers, casts, or annotations to make errors disappear
rather than fixing the root cause.
The ledger count drops, and the agent reports progress.

**What it means:** The agent gamed the system.
The error still exists but is no longer visible.

**What to do:** Reject any change whose primary effect is to hide an error.
The correct response is to create evidence (fix the graph, add the base, update the
spec), not to suppress it.

## Red flag 7: Prior agent output treated as authority

**Symptom:** Future agents see prior agent classifications, issue comments, or ledger
buckets as ground truth and plan work from them without verification.

**What it means:** The mistake is self-replicating.
Each generation of agents compounds the previous generation's errors.

**What to do:** Verify everything.
A prior agent's classification is a hypothesis, not a specification.

## Red flag 8: Purpose blindness — agents who forget what the repo is for

**Symptom:** An agent gets mired in deep implementation details (stubs, plugin
internals, sidecars, mypy diagnostics) without ever stepping back to ask whether the
discussion is coherent with the repo's actual purpose.
The agent treats `category_specs` as a consumer of Sage stubs rather than as a parallel
typed layer that defines mathematical categories.
It analyzes "missing sidecar ordinary signature" as a stub problem when the actual
architecture says: every override on a `ParentMethods` class implies the base method
must exist in another internal category.
If it doesn't, the spec is incomplete — the fix is in the spec, not in a stub.

**What it means:** The agent has lost the plot.
It is operating in an internal alternative reality where stub coverage and mypy error
counts are the objective, while the actual objective (a complete, source-grounded
mathematical category spec) is invisible.
Everything the agent says is locally consistent within its confused framing but patently
absurd to anyone who remembers the basic purpose of the project.

**The specific failure from the vault conversation:**

The agent analyzed `RationalField.degree` as a "missing Sage sidecar method" and wrote
500+ words about stubs, plugins, and "local category-provider inheritance/design rows."
The user had to explain the most basic concept:

> "In the research repo, all overrides are STRICTLY internal.
> If an override is on parentmethods of a category, that means that there MUST be
> ANOTHER category in the spec where it is FIRST defined.
> That's what it MEANS to be a complete spec.
> Every method is defined ON the largest category on which it makes sense.
> Likely rational_field is a subcategory of NUMBER fields, the category on which all of
> these are defined. And it's the spec's job to DEFINE those.
> So what does this have to do with stubs at all."

The agent never asked: "Does `_NumberFields.ParentMethods.degree` exist?"
It never checked the internal graph.
It jumped straight to external stubs because that was the frame it had adopted — a frame
that makes no sense for this repo.

**What to do:** Before any analysis, restate the repo's purpose in one sentence.
For `category_specs`: "This repo defines a complete mathematical category hierarchy
where every method is owned by the largest category on which it makes sense, and
subcategories refine via internal `@override`." Then ask: does the current discussion
make sense in that frame?
If not, the agent has lost the plot.

## Red flag 9: Delegation as a substitute for doing the work

**Symptom:** When told to produce concrete deliverables (tables, audits, fixes), an
agent writes an issue comment, a strategy document, or a set of "acceptance criteria"
and calls it done. The actual work is deferred to "future agents" or pushed to another
repo.

**What it means:** The agent is incapable of or unwilling to do the hard work of
analysis. It produces a container for the work instead of the work itself.

**What to do:** Reject any response whose primary output is an issue, comment, or
document that tells someone ELSE what to do.
If the task is to audit the graph, produce the audit.
If the task is to classify rows, produce the classification table.
If the task is to fix the graph, produce the fixed `super_categories()`.

**The concrete failure:** In the vault conversation, the user explicitly said: "Add in a
new comment." The agent drafted a 1500-line comment full of strategy and
tables-that-should-exist.
The user then said: "....you seem to be suggesting making a comment to DELEGATE and
DEFER that work, when I am telling you to DO that work right NOW." The agent had tried
to delegate the concrete analysis to a hypothetical future reader instead of performing
it.

## Red flag 10: Word salad complexity for simple issues

**Symptom:** An agent takes a simple, concrete problem (e.g., "mypy says this internal
override has no base, but the base exists in another internal file") and wraps it in
layers of abstraction, jargon, and indirect language.
The explanation mentions "local category-provider inheritance/design rows", "incomplete
static model of the intended base class", "sidecar ordinary signature" — none of which
are real concepts.

**What it means:** The agent is either confused or intentionally obfuscating.
The complexity is not in the problem; it is in the agent's inability or unwillingness to
state the problem simply.

**What to do:** Demand the agent restate the issue using only vocabulary that exists in
the repo's actual code and documentation.
If the agent cannot explain the problem in one sentence using plain language, it does
not understand the problem.

## The core principle

**If an artifact is incomprehensible, it is probably wrong.** Clarity is the first test
of correctness. An agent that truly understands a problem can explain it simply.
An agent that cannot explain it simply is either confused or hiding something.
