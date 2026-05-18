"""Adapters from constructor-discovery surfaces to spec-core provenance data."""

from __future__ import annotations

from typing import Any

from .constructors import ConstructorRegistry, ConstructorSpec


def constructor_registry_for_category(
    category: object,
    *,
    owner_category: str | None = None,
    id_prefix: str | None = None,
) -> ConstructorRegistry:
    """Return constructor provenance records for one category constructor surface."""
    from category_specs.cat import base_category_types as cat_base

    provider = cat_base._explicit_constructors_provider(category)  # noqa: SLF001
    if provider is None:
        constructors = getattr(category, "Constructors", None)
        if not callable(constructors):
            return ConstructorRegistry()
        provider = type(constructors())

    prefix = id_prefix or cat_base._cat_constructor_prefix(category)  # noqa: SLF001
    owner = owner_category or _category_owner_label(category)
    constructor_names = cat_base._cat_constructor_method_names(  # noqa: SLF001
        prefix, provider
    )
    return ConstructorRegistry(
        constructors=tuple(
            _constructor_spec(
                constructor_id=f"{prefix}.{constructor_name}",
                owner_category=owner,
                method_name=constructor_name,
                provider=provider,
                constructor_name=constructor_name,
                sage_entry_point=(
                    f"{provider.__module__}.{provider.__qualname__}.{constructor_name}"
                ),
                target_category=owner,
                target_refinement_route=(owner,),
            )
            for constructor_name in constructor_names
        )
    )


def cat_constructor_registry() -> ConstructorRegistry:
    """Return provenance records for constructors surfaced through ``Cat``."""
    from category_specs.cat import base_category_types as cat_base

    specs: list[ConstructorSpec] = []
    for prefix, category in sorted(cat_base._CAT_CONSTRUCTOR_OWNERS.items()):  # noqa: SLF001
        provider = cat_base._explicit_constructors_provider(category)  # noqa: SLF001
        if provider is None:
            continue

        owner = _category_owner_label(category)
        for constructor_name in cat_base._cat_constructor_method_names(  # noqa: SLF001
            prefix, provider
        ):
            method_name = f"{prefix}_{constructor_name}"
            specs.append(
                _constructor_spec(
                    constructor_id=f"cat.{prefix}.{constructor_name}",
                    owner_category=owner,
                    method_name=method_name,
                    provider=provider,
                    constructor_name=constructor_name,
                    sage_entry_point=f"Cat.Constructors.{method_name}",
                    target_category=owner,
                    target_refinement_route=(
                        "Cat().Constructors()",
                        f"{owner}.Constructors()",
                    ),
                    description=(
                        f"Forward to {owner}.Constructors().{constructor_name}."
                    ),
                )
            )
    return ConstructorRegistry(constructors=tuple(specs))


def _constructor_spec(
    *,
    constructor_id: str,
    owner_category: str,
    method_name: str,
    provider: type,
    constructor_name: str,
    sage_entry_point: str,
    target_category: str,
    target_refinement_route: tuple[str, ...],
    description: str = "",
) -> ConstructorSpec:
    return ConstructorSpec(
        id=constructor_id,
        owner_category=owner_category,
        method_name=method_name,
        sage_entry_point=sage_entry_point,
        sage_source=f"{provider.__module__}.{provider.__qualname__}.{constructor_name}",
        target_category=target_category,
        target_refinement_route=target_refinement_route,
        description=description,
    )


def _category_owner_label(category: object) -> str:
    from category_specs.cat import base_category_types as cat_base

    category_class = cat_base._static_category_class(category)  # noqa: SLF001
    base_ring = _base_ring_or_none(category)
    if base_ring is None:
        return f"{category_class.__name__}()"
    return f"{category_class.__name__}({base_ring})"


def _base_ring_or_none(category: object) -> Any | None:
    base_getter = getattr(category, "base_ring", None)
    if not callable(base_getter):
        return None
    return base_getter()
