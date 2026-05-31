# Category Spec Refinement Is Category Declaration

## Trigger

Read this before editing `refine_category`, constructor refinement, category-spec
smokes, or any code that tries to view a Sage object as an object of a project
subcategory.

## Object Of The Invariant

Refinement is a category-membership declaration. It says that an existing Sage object
is now being viewed inside this repo's category universe as an object of a more
specific project category.

False substitute blocked: treating refinement as a programming repair whose purpose is
to make method search succeed.

## Correct First Question

Before touching refinement code, answer this in ordinary mathematical language:

> Which existing Sage object is being declared to belong to which project category, and
> which parts of the mathematical specification of that category does the Sage object
> already realize?

If the first answer is about method search, cache state, dynamic class mutation,
type-checker appeasement, smoke ordering, hook output, or any other programming
mechanism before it names the category and its mathematical specification, the frame is
already wrong. Concrete examples include `MRO`, `getattr_from_category`,
`_cached_methods`, `cached_method`, Cython, and `can_assign_class`. These are evidence
terms after the category declaration is understood; they are not refinement semantics.

## Purpose Of Refinement

The project spec states the mathematical structure and operations expected of objects
in a category. Existing Sage objects are partial implementations and feasibility
witnesses. Refinement imports the existing Sage object as-is so smokes expose which
parts of the specification are already realized and which parts remain missing.

Within this repo's constructors, all instantiation goes through the project category
layer. It is acceptable, and often expected in the spec phase, that many refined Sage
objects cannot pass full compliance because the ideal spec asks for methods Sage does
not yet implement. That failure is evidence for later implementation, wrapper,
constructor, or spec-gap work; it is not something refinement should hide.

Project specs may and often should declare operations that Sage already implements. The
spec records the mathematical structure in this repo's category universe; the existing
Sage method may realize that part of the specification for a refined object. Do not
delete, weaken, or move a spec method merely because Sage already has a method with the
same name. Conversely, do not add programming machinery merely to force a refined
object to look complete.

## Specification And Implementation

There are two trees of work:

- the spec tree states category definitions, method ownership, and mathematical
  structure;
- the implementation tree closes the gap between existing Sage behavior and the
  mathematical specification.

Refinement sits between them. It imports an existing Sage implementation as partial
evidence for the spec, then smokes reveal the remaining implementation gap. A passing
implementation later may use wrappers, constructors, or backend work. Refinement itself
should not perform that implementation work.

If Sage already implements a method specified by the project category, the refined
object may use that implementation. If the project category has a mathematically forced
concrete method, such as `is_finite()` on finite objects, that method is part of the
project category surface. If no implementation exists, the missing method should remain
visible.

## Caching Is Not Refinement

Caching is a runtime/performance concern of implementation code after objects exist. It
is not part of declaring a category, stating a spec method, or deciding whether a Sage
object belongs to a project subcategory.

Do not preserve cache awareness by giving it a more respectable engineering name. A
source-backed task about Sage internals belongs in a separate implementation note; it
does not become part of the mathematical specification or refinement semantics.

## Frame Rejection

Stop immediately if refinement triage starts from method search, cache state, dynamic
class mutation, type-checker appeasement, smoke ordering, hook output, or any other
programming mechanism instead of the category declaration. The specific historical
terms `MRO`, `getattr_from_category`, `_cached_methods`, `cached_method`, Cython, and
`can_assign_class` matter because they are precise evidence of the wrong layer; they
are not the new vocabulary of refinement.

Before attempting a technical fix, state the refined object, its previous Sage category,
the project subcategory being declared, the spec methods Sage already implements, and
the spec methods still missing. If that cannot be stated, do not edit refinement code.

An invalid fix makes the repo appear more correct by hiding a missing method, weakening
a spec method, deleting an override marker, adding a cast, or improving QC output
without changing the category declaration or the visible spec gap.

## Witness Discipline

A concrete failure such as `ZZ.ideal_monoid()` is a witness, not the task. Do not
overfit refinement guidance to that method, ring, or object. Use it only to ask the
general question: after declaring an existing Sage object to belong to a project
subcategory, does the smoke expose the actual implemented/missing parts of the
mathematical specification, or did the repo hide the gap with programming machinery?

## Verification

A future reviewer should be able to inspect a refined object and answer:

- Which existing Sage object is being declared into which project subcategory?
- Which spec methods belong to that project category?
- Which spec methods are already realized by the existing Sage implementation?
- Which spec methods remain missing and visible?
- Why no method-search or cache mechanism is needed to make that classification true?
