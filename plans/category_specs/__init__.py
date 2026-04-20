"""Category specs for the module redesign.

Importing this package triggers ``refinement.install()`` via ``rings.py``,
which eagerly enrolls the seed base rings and wraps common Sage
constructors.  Subsequent ``Modules(R)`` references lazily refine any
fresh ``R`` into ``ModuleBaseRings`` via ``Modules.__classcall_private__``.
"""

from . import rings  # triggers refinement.install()
from . import sage_modules  # noqa: F401  (ensures Modules is importable)
from . import sage_module_morphism  # noqa: F401
from . import sage_special_modules  # noqa: F401
