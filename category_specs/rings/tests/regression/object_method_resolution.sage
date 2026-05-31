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


default_incomplete_refinement = subprocess.run(
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
refine_category(ZZ, [_IncompleteRingObjects()])
print('default-refinement-returned', flush=True)
""",
    ],
    cwd=REPO_ROOT,
    capture_output=True,
    text=True,
)

optimized_incomplete_refinement = subprocess.run(
    [
        sys.executable,
        '-O',
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


print('reached-optimized-incomplete-refinement', flush=True)
refined = refine_category(ZZ, [_IncompleteRingObjects()], test=False)
print('optimized-refinement-returned', flush=True)
refined.required_regression_operation()
print('silent-call-returned', flush=True)
""",
    ],
    cwd=REPO_ROOT,
    capture_output=True,
    text=True,
)

joined_abstracts_after_low_level_refinement = subprocess.run(
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


class _IncompleteRingObjects(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def required_regression_operation(self):
            ...


ZZ._refine_category_([_IncompleteRingObjects()])
abstracts = getattr(
    ZZ.category().parent_class,
    '__abstractmethods__',
    frozenset(),
)
print('joined-abstracts', sorted(abstracts), flush=True)
if 'required_regression_operation' not in abstracts:
    raise AssertionError('joined parent_class lost missing ParentMethods obligation')
""",
    ],
    cwd=REPO_ROOT,
    capture_output=True,
    text=True,
)

failures = []
if 'reached-incomplete-refinement' not in default_incomplete_refinement.stdout:
    failures.append('default subprocess did not reach refine_category')
if default_incomplete_refinement.returncode == 0:
    failures.append('default refine_category accepted missing ParentMethods obligation')
if 'default-refinement-returned' in default_incomplete_refinement.stdout:
    failures.append('default refine_category returned after missing obligation')

if (
    'reached-optimized-incomplete-refinement'
    not in optimized_incomplete_refinement.stdout
):
    failures.append('optimized subprocess did not reach refine_category')
if optimized_incomplete_refinement.returncode == 0:
    failures.append('optimized refine/call accepted missing ParentMethods obligation')
if 'optimized-refinement-returned' in optimized_incomplete_refinement.stdout:
    failures.append('optimized refine_category returned after missing obligation')
if 'silent-call-returned' in optimized_incomplete_refinement.stdout:
    failures.append('optimized missing object method call returned silently')

if joined_abstracts_after_low_level_refinement.returncode != 0:
    failures.append(
        'joined parent_class did not retain missing ParentMethods obligation'
    )

assert not failures, '\n'.join(failures)

incomplete_abstracts = getattr(
    _IncompleteRingObjects().parent_class,
    '__abstractmethods__',
    frozenset(),
)
assert 'required_regression_operation' in incomplete_abstracts

class _IdealMonoidRequirement(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def ideal_monoid(self):
            ...


ZZ = refine_category(SageZZ, [_IdealMonoidRequirement()])
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
