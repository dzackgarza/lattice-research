# Regression for object-method obligations across project-owned category refinement.

from pathlib import Path
import subprocess
import sys
from textwrap import dedent

REPO_ROOT = Path("/home/dzack/research")


def run_sage_python(source, *, optimized=False):
    command = [sys.executable]
    if optimized:
        command.append("-O")
    command.extend(["-c", dedent(source)])
    return subprocess.run(
        command,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def require_success(label, result):
    if result.returncode != 0:
        raise AssertionError(
            f"{label} failed\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )


REFINEMENT_DECLARATION_SOURCE = """
from abc import abstractmethod
import sys

from sage.all import ZZ
from sage.categories.rings import Rings as SageRings

sys.path.insert(0, '/home/dzack/research')

from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


class _MissingRequirement(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def category_specs_missing_regression_operation(self):
            ...


C = _MissingRequirement()
refined = refine_category(ZZ, [C], test=False)
if refined is not ZZ:
    raise AssertionError('refinement must keep the existing Sage parent object')
if refined not in C:
    raise AssertionError('refinement did not declare the project category')
print('refinement-declaration-returned', flush=True)
"""


for label, optimized in (
    ("default refinement declaration", False),
    ("optimized refinement declaration", True),
):
    require_success(
        label,
        run_sage_python(REFINEMENT_DECLARATION_SOURCE, optimized=optimized),
    )


ABSTRACT_PARENT_CLASS_SOURCE = """
from abc import abstractmethod
import inspect
import sys

from sage.all import ZZ
from sage.categories.rings import Rings as SageRings

sys.path.insert(0, '/home/dzack/research')

from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


class _MissingRequirement(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def category_specs_missing_regression_operation(self):
            ...


C = _MissingRequirement()
refine_category(ZZ, [C], test=False)
joined_parent_class = ZZ.category().parent_class
abstracts = getattr(joined_parent_class, '__abstractmethods__', frozenset())
if 'category_specs_missing_regression_operation' not in abstracts:
    raise AssertionError('joined parent_class did not retain missing obligation')
if not inspect.isabstract(joined_parent_class):
    raise AssertionError('joined parent_class is not abstract')
try:
    joined_parent_class()
except TypeError:
    pass
else:
    raise AssertionError('abstract joined parent_class instantiated')
print('abstract-parent-class-visible', sorted(abstracts), flush=True)
"""


require_success(
    "missing obligations remain visible on joined parent_class",
    run_sage_python(ABSTRACT_PARENT_CLASS_SOURCE),
)


DYNAMIC_ABSTRACT_NAMES_SOURCE = """
from abc import abstractmethod
import inspect
import sys
import uuid

from sage.all import ZZ
from sage.categories.rings import Rings as SageRings

sys.path.insert(0, '/home/dzack/research')

from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


def abstract_method_named(name):
    def requirement(self):
        ...

    requirement.__name__ = name
    return abstractmethod(requirement)


missing_names = {
    f'category_specs_dynamic_missing_{uuid.uuid4().hex}',
    f'category_specs_dynamic_missing_{uuid.uuid4().hex}',
}
DynamicParentMethods = type(
    'ParentMethods',
    (),
    {name: abstract_method_named(name) for name in missing_names},
)


class _DynamicMissingRequirements(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    ParentMethods = DynamicParentMethods


refine_category(ZZ, [_DynamicMissingRequirements()], test=False)
joined_parent_class = ZZ.category().parent_class
abstracts = getattr(joined_parent_class, '__abstractmethods__', frozenset())
if not missing_names <= set(abstracts):
    raise AssertionError(f'dynamic obligations not retained: {sorted(abstracts)}')
if not inspect.isabstract(joined_parent_class):
    raise AssertionError('dynamic missing parent_class is not abstract')
print('dynamic-abstract-names-visible', sorted(missing_names), flush=True)
"""


require_success(
    "dynamic missing obligation names remain visible",
    run_sage_python(DYNAMIC_ABSTRACT_NAMES_SOURCE),
)


CONCRETE_SAGE_METHOD_SOURCE = """
from abc import abstractmethod
import sys

from sage.all import ZZ as SageZZ
from sage.categories.rings import Rings as SageRings

sys.path.insert(0, '/home/dzack/research')

from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


class _IdealMonoidRequirement(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def ideal_monoid(self):
            ...


ZZ = refine_category(SageZZ, [_IdealMonoidRequirement()], test=False)
ideal_monoid = ZZ.ideal_monoid()
if ideal_monoid is None or 'Monoid of ideals' not in repr(ideal_monoid):
    raise AssertionError('Sage ideal_monoid implementation did not win lookup')
refined_type = type(ZZ)
abstracts = getattr(refined_type, '__abstractmethods__', frozenset())
if 'ideal_monoid' in abstracts:
    raise AssertionError('refined parent type left concrete Sage method abstract')
lookup_class = refined_type
if not any('ideal_monoid' in cls.__dict__ for cls in lookup_class.__mro__):
    lookup_class = ZZ.category().parent_class
winning_method = next(
    cls.__dict__['ideal_monoid']
    for cls in lookup_class.__mro__
    if 'ideal_monoid' in cls.__dict__
)
if getattr(winning_method, '__isabstractmethod__', False):
    raise AssertionError('abstract requirement won over concrete Sage method')
if not getattr(winning_method, '__module__', '').startswith('sage.categories'):
    raise AssertionError('winning ideal_monoid method is not Sage-owned')
print('concrete-sage-method-wins', repr(ideal_monoid), flush=True)
"""


require_success(
    "concrete Sage method satisfies matching obligation by lookup",
    run_sage_python(CONCRETE_SAGE_METHOD_SOURCE),
)


CONCRETE_PROJECT_METHOD_SOURCE = """
from abc import abstractmethod
import inspect
import sys

from sage.all import QQ
from sage.categories.rings import Rings as SageRings

sys.path.insert(0, '/home/dzack/research')

from category_specs.cat import Category_singleton
from category_specs.utils import refine_category


class _AbstractProjectRequirement(Category_singleton):
    def super_categories(self):
        return [SageRings()]

    def additional_structure(self):
        return None

    class ParentMethods:
        @abstractmethod
        def category_specs_project_method_probe(self):
            ...


class _ConcreteProjectRequirement(Category_singleton):
    def super_categories(self):
        return [_AbstractProjectRequirement()]

    def additional_structure(self):
        return None

    class ParentMethods:
        def category_specs_project_method_probe(self):
            return ('project-method', self is QQ)


refined = refine_category(QQ, [_ConcreteProjectRequirement()], test=False)
if refined.category_specs_project_method_probe() != ('project-method', True):
    raise AssertionError('concrete project method did not win lookup')
abstracts = getattr(refined.category().parent_class, '__abstractmethods__', frozenset())
if 'category_specs_project_method_probe' in abstracts:
    raise AssertionError('concrete project method remained abstract')
if inspect.isabstract(refined.category().parent_class):
    raise AssertionError('concrete project method left parent_class abstract')
print('concrete-project-method-wins', flush=True)
"""


require_success(
    "concrete project method satisfies matching obligation by lookup",
    run_sage_python(CONCRETE_PROJECT_METHOD_SOURCE),
)
