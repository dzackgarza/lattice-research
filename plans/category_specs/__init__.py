"""Category specs for the module redesign.

Importing this package loads the static category specifications.  Phase 1
records the mathematical hierarchy and abstract method surfaces; later phases
install concrete category interceptors and constructor redefinitions.
"""

from . import rings  # noqa: F401
from . import sage_modules  # noqa: F401  (ensures Modules is importable)
from . import sage_module_morphism  # noqa: F401
from . import sage_special_modules  # noqa: F401
