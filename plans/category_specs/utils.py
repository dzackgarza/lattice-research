from collections.abc import Callable, Iterable, Sequence

from sage.categories.category import Category
from sage.misc.abstract_method import AbstractMethod
from sage.structure.parent import Parent

PROJECT_MODULE_PREFIX = "category_specs."


def partition_list[T](L: list[T], f: Callable[[T], bool]) -> tuple[list[T], list[T]]:
    return [x for x in L if f(x)], [x for x in L if not f(x)]


def partition_set[T](L: set[T], f: Callable[[T], bool]) -> tuple[set[T], set[T]]:
    return {x for x in L if f(x)}, {x for x in L if not f(x)}


def partition_gen[T](L: Iterable[T], f: Callable[[T], bool]) -> tuple[Iterable[T], Iterable[T]]:
    return filter(f, L), filter(lambda x: not f(x), L)


def _is_abstract_method(attr: object) -> bool:
    return isinstance(attr, AbstractMethod)


def _is_project_method_provider(cls: type[object]) -> bool:
    return getattr(cls, "__module__", "").startswith(PROJECT_MODULE_PREFIX)


def _abstract_method_owner(cls: type[object], name: str) -> type[object] | None:
    for base in cls.__mro__:
        attr = base.__dict__.get(name)
        if attr is not None and _is_abstract_method(attr) and _is_project_method_provider(base):
            return base
    return None


def _validate_no_missing_abc_methods(X: Parent) -> None:
    missing = sorted(getattr(type(X), "__abstractmethods__", ()))
    if not missing:
        return

    details = []
    for name in missing:
        owner = _abstract_method_owner(type(X), name)
        if owner is None:
            details.append(name)
        else:
            details.append(f"{name} ({owner.__name__})")

    detail_str = ", ".join(details)
    raise TypeError(f"Can't refine category of {type(X).__name__}: unimplemented abstract methods: {detail_str}")


def refine_category(X: Parent, C: Category | Sequence[Category], test: bool = True) -> Parent:
    X._refine_category_(C)
    _validate_no_missing_abc_methods(X)
    if test:
        X._test_not_implemented_methods()
    return X
