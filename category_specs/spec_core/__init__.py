"""Typed data kernel for category specification reports."""

from __future__ import annotations

from .constructors import (
    ConstructorRegistry,
    ConstructorSpec,
)
from .constructor_adapters import (
    cat_constructor_registry,
    constructor_registry_for_category,
)
from .inspection import Spec
from .reports import (
    ComputedValue,
    ConstructionWitness,
    SpecCheckResult,
    SpecObligation,
    SpecProvider,
    SpecRegistry,
    SpecReport,
)
