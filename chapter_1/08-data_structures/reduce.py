# reduce.py
# Examples and patterns for functools.reduce and related alternatives.
# Demonstrates sum/product reductions, initial value behavior, and common pitfalls.

from functools import reduce
import operator
import math
from typing import Iterable, Callable, TypeVar, List

T = TypeVar("T")
S = TypeVar("S")


def sum_with_reduce(values: Iterable[float], start: float = 0) -> float:
    """
    Sum the values using reduce. Equivalent to sum(values, start).
    Using an explicit start avoids TypeError on empty iterables.
    """
    return reduce(lambda a, b: a + b, values, start)


def product_with_reduce(values: Iterable[float], start: float = 1) -> float:
    """
    Compute the product of values using reduce. Equivalent to math.prod(values)
    for Python 3.8+, but reduce demonstrates the folding pattern.
    Using start=1 handles empty iterables (returns 1).
    """
    return reduce(lambda a, b: a * b, values, start)


def fold(values: Iterable[T], fn: Callable[[T, T], T], *, initial: S = None, use_initial: bool = True):
    """
    General reduce wrapper that shows the two common styles:
    - If use_initial is True, the initial value is passed to reduce (safer for empty iterables).
    - If use_initial is False, reduce will use the first element as the initial accumulator
      and raise TypeError on empty iterables.
    """
    if use_initial:
        # Note: mypy typing here is intentionally generic but simple
        return reduce(fn, values, initial)
    else:
        return reduce(fn, values)  # may raise TypeError if values is empty


# Documentation / demo examples
def _demo_examples():
    print("=== Demo: reduce examples ===")

    nums = [1, 2, 3, 4]
    print("nums =", nums)

    # sum via reduce
    s = sum_with_reduce(nums, 0)
    print("sum_with_reduce(nums) ->", s)

    # product via reduce
    p = product_with_reduce(nums, 1)
    print("product_with_reduce(nums) ->", p)

    # difference between giving initial and not:
    empty: List[int] = []
    print("sum_with_reduce([], start=0) ->", sum_with_reduce(empty, 0))
    print("product_with_reduce([], start=1) ->", product_with_reduce(empty, 1))

    try:
        # reduce without initial on empty iterable raises TypeError
        reduce(lambda a, b: a + b, empty)  # type: ignore
    except TypeError as e:
        print("reduce(..., empty) raised TypeError as expected ->", type(e).__name__, "-", e)

    # Using operator functions for clarity and speed
    s2 = reduce(operator.add, nums, 0)
    p2 = reduce(operator.mul, nums, 1)
    print("reduce(operator.add, nums, 0) ->", s2)
    print("reduce(operator.mul, nums, 1) ->", p2)

    # Equivalent modern alternatives
    print("built-in sum(nums) ->", sum(nums))
    try:
        print("math.prod(nums) ->", math.prod(nums))
    except AttributeError:
        # In case Python version <3.8 (math.prod introduced in 3.8)
        print("math.prod not available in this Python version")

    # Show reduction order / associativity note
    l = [2, 3, 4]
    # product reduce corresponds to (((2*3)*4))
    manual = ((2 * 3) * 4)
    print("product manual (((2*3)*4)) ->", manual, "product_with_reduce ->", product_with_reduce(l))

    print("=== end demo ===")


# Small assertions for quick verification
def _demo_asserts():
    assert sum_with_reduce([1, 2, 3], 0) == 6
    assert product_with_reduce([2, 3, 4], 1) == 24
    assert sum_with_reduce([], 0) == 0
    assert product_with_reduce([], 1) == 1
    # operator-based
    assert reduce(operator.add, [1, 2, 3], 0) == 6
    assert reduce(operator.mul, [2, 3, 4], 1) == 24
    # math.prod if available should match
    if hasattr(math, "prod"):
        assert math.prod([2, 3, 4]) == 24

    print("All internal asserts passed.")


if __name__ == "__main__":
    _demo_examples()
    _demo_asserts()