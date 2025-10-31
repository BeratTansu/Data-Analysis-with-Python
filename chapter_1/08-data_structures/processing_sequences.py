# Processing sequences: map, filter, reduce and lambda examples
# Examples and short demos for functional-style sequence processing.

from typing import List, Iterable
from functools import reduce
import operator

# 1) map examples (map returns an iterator in Python 3)
def square(x: int) -> int:
    return x * x

nums = [1, 2, 3, 4, 5]
squares_map = map(square, nums)              # map with named function
squares_map_lambda = map(lambda x: x * x, nums)  # map with lambda
squares_comp = [x * x for x in nums]         # equivalent list comprehension

print("map(square, nums) ->", list(squares_map))
print("map(lambda x: x*x, nums) ->", list(squares_map_lambda))
print("list comprehension equivalent ->", squares_comp)
print()

# 2) map with multiple iterables (stops at shortest)
a = [1, 2, 3]
b = [10, 20, 30]
sum_pairs = list(map(lambda x, y: x + y, a, b))
print("map over two iterables (pairwise sum) ->", sum_pairs)
print()

# 3) filter examples (filter returns an iterator)
items = range(10)
evens = filter(lambda x: x % 2 == 0, items)
evens_list = list(evens)
print("filter(lambda x: x%2==0, range(10)) ->", evens_list)
# comprehension equivalent
evens_comp = [x for x in items if x % 2 == 0]
print("comprehension equivalent ->", evens_comp)
print()

# 4) reduce examples (requires functools.reduce)
# Sum of numbers
total = reduce(lambda a, b: a + b, nums, 0)
print("reduce sum ->", total)
# Product of numbers using operator.mul
product = reduce(operator.mul, nums, 1)
print("reduce product ->", product)
print()

# 5) Chaining map/filter/reduce and using generator expressions
# Example: sum of squares of even numbers
sum_squares_even = sum(x * x for x in nums if x % 2 == 0)
# Equivalent using map/filter/reduce:
sum_squares_even_mapfilter = reduce(
    lambda a, b: a + b,
    map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)),
    0,
)
print("sum of squares of even numbers (genexpr) ->", sum_squares_even)
print("sum of squares of even numbers (map+filter+reduce) ->", sum_squares_even_mapfilter)
print()

# 6) When to prefer which
# - Use list comprehensions/generator expressions for most tasks: clearer and idiomatic.
# - Use map/filter when you already have small, reusable functions and want functional style.
# - Use reduce for fold/accumulate patterns that are not expressible with sum/min/max/any/all.
print("notes: prefer comprehensions/generator expressions for readability in Python")
print()

# 7) Small utility wrappers (optional convenience)
def map_list(func, *iters) -> List:
    """Return list(map(func, *iters)) — convenience if you prefer lists directly."""
    return list(map(func, *iters))

def filter_list(func, iterable) -> List:
    """Return list(filter(func, iterable))."""
    return list(filter(func, iterable))

# 8) Documentation screenshot examples (solved) - placed last as requested
print("=== Documentation screenshot examples (solved) ===")

# Example: map demo (apply uppercase to words)
words = ["one", "two", "three"]
print("map(str.upper, words) ->", list(map(str.upper, words)))

# Example: filter demo (keep words with length > 3)
print("filter(len > 3) ->", list(filter(lambda s: len(s) > 3, words)))

# Example: reduce demo (concatenate strings)
concat = reduce(lambda a, b: a + b, words, "")
print("reduce concat ->", concat)

# Example: lambda quick usage
print("lambda example ->", (lambda x, y: x * y)(3, 4))

def _demo():
    # quick sanity checks (non-exhaustive)
    assert map_list(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert filter_list(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    assert reduce(lambda a, b: a + b, [1, 2, 3], 0) == 6
    print("internal demo asserts passed.")

if __name__ == "__main__":
    _demo()