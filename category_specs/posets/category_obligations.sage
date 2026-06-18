r"""Mathematical-fact obligations for the poset category subtree.

Each statement instantiates a concrete poset/lattice through the category DSL and asserts a
real computed mathematical value it must recover (extremal elements, cover relations, order
ideals/filters, intervals, height/width certificates, chains/antichains/linear extensions,
complements, atoms/coatoms, meet/join matrices, sublattice and congruence cardinalities). A
statement passes only when the backend computes the value; it is red while the backend is
incomplete. No statement asserts category-graph structure (object-of-Cat membership,
subcategory placement, constructor-output category refinement `obj in C`, abstract-method
ownership) — that is a property of the spec *source*, enforced by the validators in
`category_specs/validators/`. The ~60 `X in Cat()` / `.is_subcategory(...)` / `... in
P.Finite()` / `abstract_method_has_name(...)` meta-assertions that previously dominated this
file were removed here; migrating any structural invariant they encoded into validator
coverage is the separate "framework tests -> validators" workstream (tracked, not silently
dropped).

All expected values below are elementary computed facts about the explicit 4-element diamond
lattice M_2 (bottom 0, atoms 1 and 2, top 3) and the 3-element chain, computed directly by
the SageMath poset/lattice backend; none is a literature-sourced value, so none carries a
Zotero citation.
"""

import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.posets import Posets
from category_specs.utils import assert_category_statements


P = Posets()
PC = P.Constructors()
diamond_covers = {0: [1, 2], 1: [3], 2: [3], 3: []}
diamond_cover_list = [[1, 2], [3], [3], []]

diamond_poset = PC.Poset(upper_covers_dict=diamond_covers)
diamond_lattice = PC.LatticePoset(upper_covers=diamond_cover_list)


CATEGORY_STATEMENTS = (
    (
        "finite diamond poset has the expected top and bottom",
        lambda _: diamond_poset.bottom() == 0
        and diamond_poset.top() == 3
        and diamond_poset.has_bottom()
        and diamond_poset.has_top()
        and diamond_poset.is_bounded(),
    ),
    (
        "finite diamond poset has the expected extremal elements",
        lambda _: diamond_poset.minimal_elements() == [0] and diamond_poset.maximal_elements() == [3],
    ),
    (
        "finite diamond poset exposes cover relations through list and iterator surfaces",
        lambda _: diamond_poset.cover_relations() == [[0, 1], [0, 2], [1, 3], [2, 3]]
        and list(diamond_poset.cover_relations_iterator()) == [[0, 1], [0, 2], [1, 3], [2, 3]],
    ),
    (
        "finite diamond poset exposes reverse comparisons and lower covers",
        lambda _: diamond_poset.ge(3, 1) and diamond_poset.gt(3, 1) and diamond_poset.lower_covers(3) == [1, 2],
    ),
    (
        "finite diamond poset generates order ideals and filters",
        lambda _: diamond_poset.order_ideal([1]) == [0, 1] and diamond_poset.order_filter([1]) == [1, 3],
    ),
    (
        "finite diamond poset intervals distinguish open and closed intervals",
        lambda _: diamond_poset.closed_interval(0, 3) == [0, 1, 2, 3]
        and diamond_poset.interval(0, 3) == [0, 1, 2, 3]
        and diamond_poset.open_interval(0, 3) == [1, 2],
    ),
    (
        "finite diamond poset height and width certificates recover chains and antichains",
        lambda _: diamond_poset.height_certificate() == (3, [0, 1, 3])
        and diamond_poset.width_certificate() == (2, [1, 2]),
    ),
    (
        "finite diamond poset is ranked and semilattice-certified",
        lambda _: diamond_poset.is_ranked()
        and diamond_poset.meet_semilattice_certificate() == (True, None)
        and diamond_poset.join_semilattice_certificate() == (True, None),
    ),
    (
        "finite diamond poset enumerates chains antichains and linear extensions",
        lambda _: [0, 1, 3] in list(diamond_poset.chains())
        and [1, 2] in list(diamond_poset.antichains())
        and [list(extension) for extension in diamond_poset.linear_extensions()] == [[0, 1, 2, 3], [0, 2, 1, 3]],
    ),
    (
        "finite diamond lattice complements pair opposite atoms",
        lambda _: diamond_lattice.complements() == {0: [3], 1: [2], 2: [1], 3: [0]}
        and diamond_lattice.complements(1) == [2],
    ),
    (
        "finite diamond lattice exposes meet and join semilattice extremal elements",
        lambda _: diamond_lattice.atoms() == [1, 2] and diamond_lattice.coatoms() == [1, 2],
    ),
    (
        "finite diamond lattice exposes meet and join operation matrices",
        lambda _: diamond_lattice.meet_matrix()[1, 2] == 0 and diamond_lattice.join_matrix()[1, 2] == 3,
    ),
    (
        "finite diamond lattice exposes meet and join subsemilattice constructors",
        lambda _: diamond_lattice.pseudocomplement(1) == 2
        and diamond_lattice.submeetsemilattice([0, 1, 3]).cardinality() == 3
        and diamond_lattice.subjoinsemilattice([0, 1, 3]).cardinality() == 3,
    ),
    (
        "finite diamond lattice atomic coatomic complemented and distributive certificates are positive",
        lambda _: diamond_lattice.atomic_certificate() == (True, None)
        and diamond_lattice.coatomic_certificate() == (True, None)
        and diamond_lattice.complemented_certificate() == (True, None)
        and diamond_lattice.distributive_certificate() == (True, None),
    ),
    (
        "finite diamond lattice modular and semidistributive surfaces are positive",
        lambda _: diamond_lattice.are_modular_elements([1, 2])
        and diamond_lattice.modular_certificate() == (True, None)
        and diamond_lattice.modular_elements_certificate([1, 2]) == (True, None)
        and diamond_lattice.is_semidistributive(),
    ),
    (
        "finite diamond lattice sublattice and congruence constructions have expected sizes",
        lambda _: diamond_lattice.sublattice([0, 1, 3]).cardinality() == 3
        and diamond_lattice.sublattices_lattice().cardinality() == 13
        and diamond_lattice.congruence_generated_by([[0, 1]]) == SetPartition([[0, 1], [2, 3]])
        and diamond_lattice.congruence_lattice().cardinality() == 4,
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)
