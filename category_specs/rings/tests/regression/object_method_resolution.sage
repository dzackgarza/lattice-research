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


def run_sage_python(source):
    return subprocess.run(
        [
            sys.executable,
            '-c',
            source,
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def run_optimized_sage_python(source):
    return subprocess.run(
        [
            sys.executable,
            '-O',
            '-c',
            source,
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


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

failed_refinement_preserves_category = subprocess.run(
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


original_category = ZZ.category()
try:
    refine_category(ZZ, [_IncompleteRingObjects()], test=False)
except TypeError:
    pass
else:
    raise AssertionError('missing obligation did not fail refinement')
if ZZ.category() is not original_category:
    raise AssertionError('failed refinement mutated the parent category')
print('failed-refinement-preserved-category', flush=True)
""",
    ],
    cwd=REPO_ROOT,
    capture_output=True,
    text=True,
)

parent_class_abstractness_contract = run_sage_python(
    """
from abc import abstractmethod
import inspect
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


C = _IncompleteRingObjects()
standalone_abstracts = getattr(C.parent_class, '__abstractmethods__', frozenset())
if 'required_regression_operation' not in standalone_abstracts:
    raise AssertionError('standalone parent_class lost object-method obligation')
if not inspect.isabstract(C.parent_class):
    raise AssertionError('standalone parent_class is not a Python abstract class')
try:
    C.parent_class()
except TypeError:
    pass
else:
    raise AssertionError('standalone abstract parent_class instantiated')

ZZ._refine_category_([C])
joined_parent_class = ZZ.category().parent_class
joined_abstracts = getattr(joined_parent_class, '__abstractmethods__', frozenset())
if 'required_regression_operation' not in joined_abstracts:
    raise AssertionError('joined parent_class lost object-method obligation')
if not inspect.isabstract(joined_parent_class):
    raise AssertionError('joined parent_class is not a Python abstract class')
try:
    joined_parent_class()
except TypeError:
    pass
else:
    raise AssertionError('joined abstract parent_class instantiated')
print('parent-class-abstractness-contract', sorted(joined_abstracts), flush=True)
"""
)

multiple_missing_join_contract = run_sage_python(
    """
from abc import abstractmethod
import inspect
import sys

from sage.all import *

sys.path.insert(0, '/home/dzack/research')

from sage.all import ZZ
from sage.categories.rings import Rings as SageRings
from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


class _FirstMissingOperation(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def required_regression_operation_a(self):
            ...


class _SecondMissingOperation(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def required_regression_operation_b(self):
            ...


original_category = ZZ.category()
try:
    refine_category(
        ZZ,
        [_FirstMissingOperation(), _SecondMissingOperation()],
        test=False,
    )
except TypeError:
    pass
else:
    raise AssertionError('public refinement accepted multiple missing obligations')
if ZZ.category() is not original_category:
    raise AssertionError('failed multiple-obligation refinement mutated category')

ZZ._refine_category_([_FirstMissingOperation(), _SecondMissingOperation()])
joined_parent_class = ZZ.category().parent_class
abstracts = getattr(joined_parent_class, '__abstractmethods__', frozenset())
expected = {'required_regression_operation_a', 'required_regression_operation_b'}
missing = expected - set(abstracts)
if missing:
    raise AssertionError(f'joined parent_class lost obligations: {sorted(missing)}')
if not inspect.isabstract(joined_parent_class):
    raise AssertionError('multi-obligation joined parent_class is not abstract')
print('multiple-missing-join-contract', sorted(abstracts), flush=True)
"""
)

concrete_parent_type_method_contract = run_sage_python(
    """
from abc import abstractmethod
import sys

from sage.all import *

sys.path.insert(0, '/home/dzack/research')

from sage.all import ZZ
from sage.categories.rings import Rings as SageRings
from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


class _BaseRingRequirement(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def base_ring(self):
            ...


refined = refine_category(ZZ, [_BaseRingRequirement()], test=False)
if refined is not ZZ:
    raise AssertionError('refinement changed the existing Sage parent object')
if refined.base_ring() != ZZ:
    raise AssertionError('concrete parent-type base_ring method was not preserved')
print('concrete-parent-type-method-contract', refined.base_ring(), flush=True)
"""
)

mixed_realized_and_missing_contract = run_sage_python(
    """
from abc import abstractmethod
import sys

from sage.all import *

sys.path.insert(0, '/home/dzack/research')

from sage.all import ZZ
from sage.categories.rings import Rings as SageRings
from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


class _BaseRingAndMissingRequirement(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def base_ring(self):
            ...

        @abstractmethod
        def required_regression_operation(self):
            ...


original_category = ZZ.category()
try:
    refine_category(ZZ, [_BaseRingAndMissingRequirement()], test=False)
except TypeError:
    pass
else:
    raise AssertionError('realized base_ring incorrectly satisfied missing operation')
if ZZ.category() is not original_category:
    raise AssertionError('mixed failed refinement mutated the parent category')
print('mixed-realized-and-missing-contract', flush=True)
"""
)

concrete_category_override_contract = run_sage_python(
    """
from abc import abstractmethod
import inspect
import sys

from sage.all import *

sys.path.insert(0, '/home/dzack/research')

from sage.all import ZZ
from sage.categories.rings import Rings as SageRings
from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


class _AbstractOperation(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def category_specs_contract_probe(self):
            ...


class _ConcreteOperation(Category_singleton):
    def super_categories(self):
        return [_AbstractOperation()]

    def additional_structure(self):
        return None

    class ParentMethods:
        def category_specs_contract_probe(self):
            return ('concrete-category-method', self is ZZ)


refined = refine_category(ZZ, [_ConcreteOperation()], test=False)
if refined.category_specs_contract_probe() != ('concrete-category-method', True):
    raise AssertionError('concrete category method did not satisfy object contract')
joined_parent_class = refined.category().parent_class
abstracts = getattr(joined_parent_class, '__abstractmethods__', frozenset())
if 'category_specs_contract_probe' in abstracts:
    raise AssertionError('concrete override remained abstract in joined parent_class')
if inspect.isabstract(joined_parent_class):
    raise AssertionError('concrete override left joined parent_class abstract')
print('concrete-category-override-contract', flush=True)
"""
)

optimized_failed_refinement_preserves_category = run_optimized_sage_python(
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


original_category = ZZ.category()
try:
    refine_category(ZZ, [_IncompleteRingObjects()], test=False)
except TypeError:
    pass
else:
    raise AssertionError('optimized missing obligation did not fail refinement')
if ZZ.category() is not original_category:
    raise AssertionError('optimized failed refinement mutated the parent category')
print('optimized-failed-refinement-preserved-category', flush=True)
"""
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
if failed_refinement_preserves_category.returncode != 0:
    failures.append('failed refine_category mutated the parent category')
if parent_class_abstractness_contract.returncode != 0:
    failures.append('parent_class abstractness contract failed')
if multiple_missing_join_contract.returncode != 0:
    failures.append('multiple missing obligation join contract failed')
if concrete_parent_type_method_contract.returncode != 0:
    failures.append('concrete parent type method contract failed')
if mixed_realized_and_missing_contract.returncode != 0:
    failures.append('mixed realized-and-missing obligation contract failed')
if concrete_category_override_contract.returncode != 0:
    failures.append('concrete category override contract failed')
if optimized_failed_refinement_preserves_category.returncode != 0:
    failures.append('optimized failed refine_category mutated the parent category')

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
