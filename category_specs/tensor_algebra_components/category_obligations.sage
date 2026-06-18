r"""Mathematical-fact obligations for the tensor-algebra-components category subtree.

Each statement instantiates a tensor through the category's constructors and asserts a real
mathematical value it must recover: the tensor type (p, q) the constructor yields, the base
module the constructed tensor lives over, and the multiplication structure constants a
module-element-matrix tensor encodes. A statement passes only when the backend computes the
value; it is red while the backend is incomplete. No statement asserts category-graph
structure (object membership ``X in Cat()``/``in C``, subcategory placement
``is_subcategory(...)``, category-package identity ``... == C``) — that is a property of the
spec *source*, enforced by the validators in ``category_specs/validators/``. Six such
meta-assertions that previously dominated this file (``C in Cat()``, two
``is_subcategory(...)``, the ``Modules(ZZ).TensorProducts().TensorAlgebraComponents() == C``
identity, and the ``tensor_module(...)``/``parent()`` ``in C`` membership checks) were
removed here; migrating any structural invariant they encoded into validator coverage is the
separate "framework tests -> validators" workstream (tracked, not silently dropped).

The asserted values are elementary computed facts about explicitly built tensors
(tensor type, base module, structure constants of a chosen module-element matrix), so they
carry no literature citation.
"""

import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.tensor_algebra_components import TensorAlgebraComponents
from category_specs.utils import assert_category_statements


C = TensorAlgebraComponents(ZZ)
M = FiniteRankFreeModule(ZZ, 2, name="M")
preferred_generators = M.basis("e")
constructors = C.Constructors()


def identity_tensor():
    return constructors.tensor(
        M, (1, 1), components=[[1, 0], [0, 1]], basis=preferred_generators, name="t"
    )


def multiplication_tensor():
    return constructors.tensor(
        M,
        (1, 2),
        module_element_matrix=[
            [
                preferred_generators[0],
                2 * preferred_generators[0] + 3 * preferred_generators[1],
            ],
            [
                5 * preferred_generators[0] + 7 * preferred_generators[1],
                11 * preferred_generators[0] + 13 * preferred_generators[1],
            ],
        ],
        basis=preferred_generators,
        name="mu",
    )


def scalar_matrix_tensor():
    return constructors.tensor(
        M,
        (0, 2),
        matrix=matrix(ZZ, [[2, 1], [1, 3]]),
        basis=preferred_generators,
        name="b",
    )


def legacy_matrix_list_tensor():
    return constructors.tensor(
        M,
        (1, 2),
        matrices=[matrix(ZZ, [[1, 0], [0, 1]]), matrix(ZZ, [[0, 1], [1, 0]])],
        basis=preferred_generators,
        name="mu_legacy",
    )


CATEGORY_STATEMENTS = (
    (
        "components constructor yields a (1,1) tensor over M",
        lambda _: identity_tensor().tensor_type() == (1, 1)
        and identity_tensor().base_module() is M,
    ),
    (
        "the (1,1) component module recovers tensor type (1,1) and base module M",
        lambda _: identity_tensor().parent().tensor_type() == (1, 1)
        and identity_tensor().parent().base_module() is M,
    ),
    (
        "matrix constructor yields a (0,2) tensor over M",
        lambda _: scalar_matrix_tensor().tensor_type() == (0, 2)
        and scalar_matrix_tensor().parent().base_module() is M,
    ),
    (
        "module-element-matrix constructor yields a (1,2) tensor over M",
        lambda _: multiplication_tensor().tensor_type() == (1, 2)
        and multiplication_tensor().parent().base_module() is M,
    ),
    (
        "module-element-matrix tensor recovers its multiplication structure constants",
        lambda _: tuple(multiplication_tensor().structure_constants())
        == (
            matrix(ZZ, [[1, 2], [5, 11]]),
            matrix(ZZ, [[0, 3], [7, 13]]),
        ),
    ),
    (
        "matrix-list constructor yields a (1,2) tensor",
        lambda _: legacy_matrix_list_tensor().tensor_type() == (1, 2),
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)
