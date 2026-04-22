"""Category specs for the module redesign.

Importing this package loads the static category specifications.  Phase 1
records the mathematical hierarchy and abstract method surfaces; later phases
install concrete category interceptors and constructor redefinitions.
"""

from . import (
    modules,  # noqa: F401  (was sage_modules / sage_module_morphism / sage_special_modules)
    rings,  # noqa: F401
)
