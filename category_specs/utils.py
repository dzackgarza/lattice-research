import logging
import os
from collections.abc import Callable, Sequence
from functools import wraps
from textwrap import dedent
from typing import Any, Protocol, TypeVar, cast, overload

from sage.categories.category import Category
from sage.misc.abstract_method import AbstractMethod
from sage.structure.parent import Parent

PROJECT_MODULE_PREFIX = "category_specs."
CATEGORY_DIAGNOSTIC_LOGGER_NAME = "category_specs.diagnostics"

_FoldParent = TypeVar("_FoldParent", contravariant=True)
_FoldElement = TypeVar("_FoldElement")
_ParentT = TypeVar("_ParentT", bound=Parent)
_CATEGORY_DIAGNOSTICS_ENABLED = False
_CATEGORY_DIAGNOSTIC_LOGGER = logging.getLogger(CATEGORY_DIAGNOSTIC_LOGGER_NAME)
_EMITTED_CATEGORY_DIAGNOSTICS: set[str] = set()


def category_diagnostics_enabled() -> bool:
    r"""Return whether opt-in category diagnostics are enabled."""
    return _CATEGORY_DIAGNOSTICS_ENABLED


def set_category_diagnostics_enabled(enabled: bool) -> None:
    r"""Set the process-local category diagnostics flag."""
    global _CATEGORY_DIAGNOSTICS_ENABLED
    _CATEGORY_DIAGNOSTICS_ENABLED = enabled


def enable_category_diagnostics() -> None:
    r"""Enable opt-in category diagnostic logging for this process."""
    set_category_diagnostics_enabled(True)


def disable_category_diagnostics() -> None:
    r"""Disable category diagnostic logging for this process."""
    set_category_diagnostics_enabled(False)


def category_diagnostic_logger() -> logging.Logger:
    r"""Return the category diagnostic logger."""
    return _CATEGORY_DIAGNOSTIC_LOGGER


def clear_category_diagnostic_history() -> None:
    r"""Clear the once-per-key category diagnostic history."""
    _EMITTED_CATEGORY_DIAGNOSTICS.clear()


def emit_category_diagnostic(
    message: str,
    *,
    key: str | None = None,
    once: bool = True,
) -> None:
    r"""Emit an opt-in category diagnostic warning.

    Diagnostics are disabled by default and logging-only.  They are for
    mathematically valid but non-obvious conventions, not for recovering from
    invalid hypotheses or implementation gaps.
    """
    if not _CATEGORY_DIAGNOSTICS_ENABLED:
        return
    if once and key is not None:
        if key in _EMITTED_CATEGORY_DIAGNOSTICS:
            return
        _EMITTED_CATEGORY_DIAGNOSTICS.add(key)
    _CATEGORY_DIAGNOSTIC_LOGGER.warning(message)


class _FoldableOperation(Protocol[_FoldParent, _FoldElement]):
    @overload
    def __call__(
        self,
        parent: _FoldParent,
        x: _FoldElement,
        y: _FoldElement,
    ) -> _FoldElement: ...

    @overload
    def __call__(
        self,
        parent: _FoldParent,
        elements: Sequence[_FoldElement],
    ) -> _FoldElement: ...


class _MissingFoldArgument: ...


_MISSING_FOLD_ARGUMENT = _MissingFoldArgument()


class _CategoryAxiomRefiner(Protocol):
    def _with_axiom(self, axiom: str) -> Category: ...


def with_axiom(category: object, axiom: str) -> Category:
    r"""Return Sage's dynamic axiom refinement for ``category``."""
    return cast(_CategoryAxiomRefiner, category)._with_axiom(axiom)


def _fold_nonempty_binary_operation[FoldParent, FoldElement](
    operation: Callable[[FoldParent, FoldElement, FoldElement], FoldElement],
    parent: FoldParent,
    elements: Sequence[FoldElement],
) -> FoldElement:
    assert len(elements) >= 1, "foldable binary operation requires a nonempty sequence"
    result = elements[0]
    for element in elements[1:]:
        result = operation(parent, result, element)
    return result


def foldable_operation[FoldParent, FoldElement](
    operation: Callable[[FoldParent, FoldElement, FoldElement], FoldElement],
) -> _FoldableOperation[FoldParent, FoldElement]:
    r"""Decorate a binary method with the standard nonempty-sequence fold."""

    @wraps(operation)
    def folded_operation(
        parent: FoldParent,
        left_or_elements: FoldElement | Sequence[FoldElement],
        right: FoldElement | _MissingFoldArgument = _MISSING_FOLD_ARGUMENT,
    ) -> FoldElement:
        if right is _MISSING_FOLD_ARGUMENT:
            assert isinstance(left_or_elements, Sequence), (
                "sequence overload requires a finite sequence"
            )
            sequence = cast(Sequence[FoldElement], left_or_elements)
            return _fold_nonempty_binary_operation(
                operation,
                parent,
                sequence,
            )
        return operation(
            parent,
            cast(FoldElement, left_or_elements),
            cast(FoldElement, right),
        )

    return cast(_FoldableOperation[FoldParent, FoldElement], folded_operation)


def _is_project_method_provider(cls: type) -> bool:
    return getattr(cls, "__module__", "").startswith(PROJECT_MODULE_PREFIX)


def _abstract_method_owner(cls: type, name: str) -> type | None:
    for base in cls.__mro__:
        attr = base.__dict__.get(name)
        if (
            attr is not None
            and isinstance(attr, AbstractMethod)
            and _is_project_method_provider(base)
        ):
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
    assert not missing, (
        f"Can't refine category of {type(X).__name__}: "
        f"unimplemented abstract methods: {detail_str}"
    )


def _prime_method_cache_before_refinement(
    X: Parent,
    categories: Sequence[Category],
) -> None:
    r"""Pre-populate ``_cached_methods`` for Cython types before category refinement.

    For Cython extension types (where ``__class__`` cannot be reassigned),
    ``_refine_category_`` updates ``_category`` but does not change the class
    or clear ``_cached_methods``.  When the new categories include project-owned
    ``ParentMethods`` stubs, those stubs occupy earlier MRO positions than the
    real Sage implementations in the joined ``parent_class``.  If a method has
    not yet been cached before refinement, a subsequent ``__getattr__`` lookup
    uses the new ``_category.parent_class`` and caches the stub instead of the
    real implementation.

    This function pre-populates ``_cached_methods`` from the *current* (pre-
    refinement) category for every method name defined in project-owned stubs
    within the incoming categories.  Once cached, ``getattr_from_category``
    returns the cached entry regardless of the new ``parent_class`` MRO order.

    Only applied when the type cannot be reassigned (Cython types).  For heap
    types, ``_refine_category_`` replaces ``__class__`` directly, so the MRO
    is controlled by the new class and this pre-priming is not needed.
    """
    from sage.cpython.type import can_assign_class

    if can_assign_class(X):
        return  # Heap type: __class__ replacement makes pre-priming unnecessary.

    cached: dict[str, object] = getattr(X, "_cached_methods", {})

    shadowed_names: set[str] = set()
    for cat in categories:
        try:
            parent_class = cat.parent_class
        except Exception:  # noqa: BLE001
            continue
        for cls in parent_class.__mro__:
            if not _is_project_method_provider(cls):
                continue
            for name, val in vars(cls).items():
                if not name.startswith("_") and callable(val):
                    shadowed_names.add(name)

    for name in shadowed_names:
        if name in cached:
            continue
        try:
            # Attribute access (not call) populates _cached_methods via
            # __getattr__ -> getattr_from_category using the CURRENT _category.
            getattr(X, name)
        except (AttributeError, NotImplementedError, TypeError):
            # Method genuinely absent or not yet available on this object.
            pass


def refine_category[_ParentT: Parent](
    X: _ParentT,
    C: Category | Sequence[Category],
    test: bool = True,
) -> _ParentT:
    if not isinstance(C, (list, tuple)):
        C = [C]
    _prime_method_cache_before_refinement(X, C)
    X._refine_category_(C)
    _validate_no_missing_abc_methods(X)
    if test:
        X._test_not_implemented_methods()
    return X


def _format_smoke_statement_failure(message: str, exc: Exception) -> str:
    return f"{message}: {type(exc).__name__}: {exc}"


def _run_smoke_statement(message: str, statement: Callable[[Any], bool]) -> str | None:
    try:
        assert statement(None), message
    except Exception as exc:
        return _format_smoke_statement_failure(message, exc)
    return None


def _write_all(fd: int, payload: bytes) -> None:
    view = memoryview(payload)
    while view:
        written = os.write(fd, view)
        view = view[written:]


def _run_smoke_statement_isolated(
    message: str,
    statement: Callable[[Any], bool],
) -> str | None:
    if not hasattr(os, "fork"):
        return _run_smoke_statement(message, statement)

    read_fd, write_fd = os.pipe()
    pid = os.fork()
    if pid == 0:
        os.close(read_fd)
        failure = _run_smoke_statement(message, statement)
        payload = (
            b"" if failure is None else failure.encode("utf-8", "backslashreplace")
        )
        try:
            _write_all(write_fd, payload)
        finally:
            os.close(write_fd)
        os._exit(0 if failure is None else 1)

    os.close(write_fd)
    chunks: list[bytes] = []
    while True:
        chunk = os.read(read_fd, 8192)
        if not chunk:
            break
        chunks.append(chunk)
    os.close(read_fd)
    _, status = os.waitpid(pid, 0)

    failure = b"".join(chunks).decode("utf-8", "replace")
    if os.WIFEXITED(status):
        exit_status = os.WEXITSTATUS(status)
        if exit_status == 0:
            return None
        return (
            failure
            or f"{message}: smoke statement child exited with status {exit_status}"
        )
    if os.WIFSIGNALED(status):
        return (
            f"{message}: smoke statement child terminated "
            f"by signal {os.WTERMSIG(status)}"
        )
    return (
        failure or f"{message}: smoke statement child ended with wait status {status}"
    )


def assert_smoke_statements(
    statements: tuple[tuple[str, Callable[[Any], bool]], ...],
) -> None:
    failures: list[str] = []
    for message, statement in statements:
        # This is the allowed smoke-harness exception pattern: spec smokes are
        # frontier sensors, so one missing method must not hide the rest of the
        # missing surface.  The failures are still reported and made fatal
        # after every labeled statement has run.
        failure = _run_smoke_statement_isolated(message, statement)
        if failure is not None:
            failures.append(failure)

    assert not failures, _format_smoke_failure_message(failures)


def _format_smoke_failure_message(failures: list[str]) -> str:
    reminder = dedent(
        """
        Category-spec smoke failures are gap evidence, not a spec-weakening signal.

        The category-spec project defines an ideal mathematical interface inside
        Sage's category/object universe. Current Sage coverage is not the adequacy
        standard, while Sage interop remains a design constraint where
        mathematically appropriate. A current Sage object missing a spec method
        usually means a wrapper, constructor, implementation, decision, or
        source-mining card is needed.

        Before editing specs, abstract methods, constructor routing, or smoke
        assertions in response to this output, load:
        - category-spec-style
        - category-spec-smoke-triage
        - category-spec-workflow

        Also check repo memory:
        - .agents/memories/category-specs-sage-interop-is-a-design-constraint.md

        Do not delete, weaken, or move a spec obligation because this smoke failed
        unless a source-grounded replacement owner preserves the mathematical surface.
        Before advancing the task, review git diff output and any task-local commits
        for deleted obligations, narrowed smokes, or Sage-gap-driven interface
        shrinkage.
        """
    ).strip()
    return f"{reminder}\n\nSmoke failures:\n" + "\n".join(failures)
