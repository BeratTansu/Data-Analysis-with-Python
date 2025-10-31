# Map and lambda examples: map(...) usage, lambda expressions, and equivalents.
# Examples, small demos, and documentation snippets appended at the end.

from typing import List, Iterable
from functools import reduce
import operator

# 1) map with a named function
def double(x: int) -> int:
    return 2 * x

L = [12, 4, -1]
mapped = map(double, L)  # returns an iterator (map object)
print("map(double, L) ->", mapped)
print("list(map(double, L)) ->", list(map(double, L)))  # convert to list to view contents
print()

# 2) map with lambda (inline anonymous function)
L2 = [2, 3, 5]
print("list(map(lambda x: 2*x + x**2, L2)) ->", list(map(lambda x: 2 * x + x ** 2, L2)))
# Equivalent with list comprehension
print("equivalent comprehension ->", [2 * x + x ** 2 for x in L2])
print()

# 3) Converting strings to numbers using map
s = "12 43 64 6"
parts = s.split()
print("parts:", parts)
nums = list(map(int, parts))  # convert each substring to int
print("list(map(int, parts)) ->", nums)
print("sum(map(int, parts)) ->", sum(map(int, parts)))
print()

# 4) map with multiple iterables (stops at shortest)
a = [1, 2, 3]
b = [10, 20, 30]
print("list(map(lambda x, y: x + y, a, b)) ->", list(map(lambda x, y: x + y, a, b)))
# comprehension equivalent (pairwise)
print("equiv comprehension ->", [x + y for x, y in zip(a, b)])
print()

# 5) map is lazy/one-pass: demonstrate iterator exhaustion
m = map(lambda x: x * x, [1, 2, 3])
print("first consume list(m):", list(m))
print("second consume list(m) (exhausted):", list(m))
print()

# 6) chaining map/filter/reduce briefly
values = [1, 2, 3, 4, 5]
# sum of squares of even numbers using genexpr (idiomatic)
sum_squares_even_gen = sum(x * x for x in values if x % 2 == 0)
# same using map/filter/reduce
sum_squares_even_mapfilter = reduce(
    lambda a, b: a + b,
    map(lambda x: x * x, filter(lambda x: x % 2 == 0, values)),
    0,
)
print("sum squares even (genexpr) ->", sum_squares_even_gen)
print("sum squares even (map+filter+reduce) ->", sum_squares_even_mapfilter)
print()

# 7) Utility wrappers (if you prefer direct lists)
def map_list(func, *iters) -> List:
    """Return list(map(func, *iters))."""
    return list(map(func, *iters))

def filter_list(func, iterable) -> List:
    """Return list(filter(func, iterable))."""
    return list(filter(func, iterable))

# 8) Small practical examples
words = ["one", "two", "three"]
print("list(map(str.upper, words)) ->", list(map(str.upper, words)))
print("list(map(len, words)) ->", list(map(len, words)))
print()

# 9) Documentation screenshot examples (solved) - placed last as requested
print("=== Documentation screenshot examples (solved) ===")

# Doc Example 1: named function + map
def double_for_doc(x):
    return 2 * x
L_doc = [12, 4, -1]
print("list(map(double_for_doc, L_doc)) ->", list(map(double_for_doc, L_doc)))

# Doc Example 2: convert split strings to ints then sum
s_doc = "12 43 64 6"
parts_doc = s_doc.split()
print("parts_doc ->", parts_doc)
print("sum(map(int, parts_doc)) ->", sum(map(int, parts_doc)))

# Doc Example 3: using a lambda inside map for a one-off transform
L_doc2 = [2, 3, 5]
print("list(map(lambda x: 2*x + x**2, L_doc2)) ->", list(map(lambda x: 2 * x + x ** 2, L_doc2)))
print("equivalent comprehension ->", [2 * x + x ** 2 for x in L_doc2])
print()

# Quick asserts / sanity checks
def _demo_checks():
    assert map_list(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert filter_list(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    assert sum(map(int, "1 2 3".split())) == 6
    print("internal demo asserts passed.")

if __name__ == "__main__":
    _demo_checks()