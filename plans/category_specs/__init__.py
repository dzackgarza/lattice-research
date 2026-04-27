"""Category specs for the module redesign.

Importing this package loads the static category specifications.  Phase 1
records the mathematical hierarchy and abstract method surfaces; later phases
install concrete category interceptors and constructor redefinitions.
"""

from . import algebras as algebras
from . import cat as cat
from . import homsets as homsets
from . import modules as modules
from . import posets as posets
from . import rings as rings
from . import sets as sets
from . import topological_spaces as topological_spaces
from .axioms import register_all

register_all()
