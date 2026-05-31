# Regression for object-method resolution across category refinement.

from abc import abstractmethod
from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path('/home/dzack/research')
sys.path.insert(0, str(REPO_ROOT))

from sage.all import ZZ as SageZZ
from sage.categories.rings import Rings as SageRings
from category_specs.cat import Category_singleton
from category_specs.rings import Rings


class _IncompleteRingObjects(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def required_regression_operation(self):
            ...


incomplete_refinement = subprocess.run(
    [
        sys.executable,
        '-c',
        """
from abc import abstractmethod
import sys

from sage.all import *

sys.path.insert(0, '/home/dzack/research')

from sage.all import ZZ
from sage.categories.rings import Rings as SageRings
from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


class _IncompleteRingObjects(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def required_regression_operation(self):
            ...


print('reached-incomplete-refinement', flush=True)
refined = refine_category(ZZ, [_IncompleteRingObjects()], test=False)
print('refinement-returned', flush=True)
refined.required_regression_operation()
print('silent-call-returned', flush=True)
""",
    ],
    cwd=REPO_ROOT,
    capture_output=True,
    text=True,
)
assert 'reached-incomplete-refinement' in incomplete_refinement.stdout
assert incomplete_refinement.returncode != 0
assert 'silent-call-returned' not in incomplete_refinement.stdout

incomplete_abstracts = getattr(
    _IncompleteRingObjects().parent_class,
    '__abstractmethods__',
    frozenset(),
)
assert 'required_regression_operation' in incomplete_abstracts

ZZ = Rings().Constructors().ZZ()
ideal_monoid = ZZ.ideal_monoid()

assert ZZ is SageZZ
assert ideal_monoid is not None
assert "Monoid of ideals" in repr(ideal_monoid)

winning_ideal_monoid = next(
    cls.__dict__['ideal_monoid']
    for cls in ZZ.category().parent_class.__mro__
    if 'ideal_monoid' in cls.__dict__
)
assert getattr(winning_ideal_monoid, '__isabstractmethod__', False) is False
assert getattr(winning_ideal_monoid, '__module__', '').startswith('sage.categories')
