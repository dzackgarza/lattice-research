"""Constructor discovery and provenance route checks.

This test suite verifies that constructor discovery through ``Cat().Constructors()``
keeps an owner route for the ``Rings`` entry points, not just plain method names.
"""

from __future__ import annotations

import importlib

importlib.import_module("sage.all")
importlib.import_module("category_specs")

from category_specs.cat import Cat
from category_specs.modules import Modules
from category_specs.rings import Rings
from category_specs.spec_core import ConstructorRegistry
from sage.all import QQ


def _constructor_names(collector_type: type) -> list[str]:
    return sorted(
        name
        for name in dir(collector_type)
        if not name.startswith("_")
        and callable(getattr(collector_type, name, None))
        and name[0].isupper()
    )


def test_cat_constructor_forwarders_expose_rings_owner_route() -> None:
    cat_constructors = Cat().Constructors()
    ring_constructors = Rings().Constructors()

    ring_constructor_methods = _constructor_names(type(ring_constructors))
    cat_rings_methods = [
        name
        for name in dir(type(cat_constructors))
        if name.startswith("rings_") and not name.startswith("rings__")
        and callable(getattr(type(cat_constructors), name, None))
    ]

    # Use a focused set so this test stays anchored to a stable surface.
    for constructor_name in ("ZZ", "QQ", "IntegerModRing"):
        expected = f"rings_{constructor_name}"
        assert expected in cat_rings_methods
        forwarder = getattr(type(cat_constructors), expected)

        assert getattr(forwarder, "_cat_constructor_generated_forwarder", False) is True
        assert (
            forwarder.__doc__
            == f"Forward to ``rings.Constructors().{constructor_name}``."
        )
        assert forwarder.__qualname__ == f"Cat.Constructors.{expected}"

    # Round-trip check confirms the route resolves to the owner namespace.
    assert cat_constructors.rings_ZZ() == ring_constructors.ZZ()
    assert cat_constructors.rings_QQ() == ring_constructors.QQ()
    assert (
        cat_constructors.rings_PolynomialRing(ring_constructors.QQ(), name="x")
        == ring_constructors.PolynomialRing(ring_constructors.QQ(), name="x")
    )

    # At least all registered ring constructors are discoverable through Cat.
    assert all(f"rings_{name}" in cat_rings_methods for name in ring_constructor_methods)
    assert "rings_provenance" not in cat_rings_methods


def test_constructor_surfaces_expose_typed_provenance_records() -> None:
    ring_registry = Rings().Constructors().provenance()
    module_registry = Modules(QQ).Constructors().provenance()
    cat_registry = Cat().Constructors().provenance()

    assert isinstance(ring_registry, ConstructorRegistry)
    assert isinstance(module_registry, ConstructorRegistry)
    assert isinstance(cat_registry, ConstructorRegistry)

    ring_zz = ring_registry.constructor("rings.ZZ")
    assert ring_zz.owner_category == "Rings()"
    assert ring_zz.method_name == "ZZ"
    assert ring_zz.sage_entry_point.endswith("Rings._Constructors.ZZ")
    assert ring_zz.target_refinement_route == ("Rings()",)

    polynomial_ring = ring_registry.constructor("rings.PolynomialRing")
    assert polynomial_ring.method_name == "PolynomialRing"
    assert polynomial_ring.sage_source.endswith("Rings._Constructors.PolynomialRing")

    free_module = module_registry.constructor("modules.FreeModule")
    assert free_module.owner_category == f"Modules({QQ})"
    assert free_module.method_name == "FreeModule"
    assert free_module.sage_entry_point.endswith("Modules._Constructors.FreeModule")

    cat_ring_zz = cat_registry.constructor("cat.rings.ZZ")
    assert cat_ring_zz.owner_category == "Rings()"
    assert cat_ring_zz.method_name == "rings_ZZ"
    assert cat_ring_zz.target_refinement_route == (
        "Cat().Constructors()",
        "Rings().Constructors()",
    )
    cat_free_module = cat_registry.constructor("cat.modules_rational_field.FreeModule")
    assert cat_free_module.method_name == "modules_rational_field_FreeModule"
    assert not cat_registry.has_constructor("cat.rings.provenance")
