
T = TypeVar("T")
def partition_list(L: list[T], f: Callable[T, bool]) -> tuple[list[T], list[T]]:
    return [x for x in L if f(x)], [x for x in L if not f(x)]

def partition_set(L: set[T], f: Callable[T, bool]) -> tuple[set[T], set[T]]:
    return {x for x in L if f(x)}, {x for x in L if not f(x)}

def partition_gen(L: Iterable[T], f: Callable[T, bool]) -> tuple[Iterable[T], Iterable[T]]:
    return filter(f, L), filter(lambda x: not f(x), L)
