# Filter function examples and patterns (filter(), lambda, and comprehension equivalents).
# Examples show typical usage, behavior (lazy iterator), and common idioms.
# Documentation screenshot examples are appended at the end as solved examples.

#%% 1) Basic filter with a named predicate
def is_odd(x: int) -> bool:
    """Return True if x is odd."""
    return x % 2 == 1

L = [1, 4, 5, 9, 10]
print("original L ->", L)
filtered = filter(is_odd, L)        # filter returns an iterator
print("filter(is_odd, L) ->", filtered)
print("list(filter(is_odd, L)) ->", list(filter(is_odd, L)))  # consume to view results
print()

#%% 2) Equivalent using list comprehension (more idiomatic in many cases)
squares_of_odd = [i**2 for i in L if is_odd(i)]
print("squares_of_odd (comprehension) ->", squares_of_odd)
# Using filter + map to get same result:
from functools import reduce
mapped = map(lambda x: x**2, filter(is_odd, L))
print("list(map(lambda x: x**2, filter(is_odd, L))) ->", list(mapped))
print()

#%% 3) Using lambda with filter for short one-off predicates
words = ["apple", "", "banana", " ", "cherry"]
non_empty = list(filter(lambda s: s.strip() != "", words))  # filter out empty/whitespace-only strings
print("words ->", words)
print("non_empty ->", non_empty)
print()

#%% 4) filter with None as predicate keeps truthy elements
mixed = [0, 1, "", "hello", [], [1,2], None, True, False]
truthy = list(filter(None, mixed))
print("mixed ->", mixed)
print("filter(None, mixed) keeps truthy ->", truthy)
print()

#%% 5) Laziness and single-pass behavior
it = filter(lambda x: x % 2 == 0, range(6))
print("first consume list(it) ->", list(it))
print("second consume list(it) (exhausted) ->", list(it))
print()

#%% 6) When to use filter vs list comprehensions
print("Notes:")
print("- List comprehensions are often clearer and more idiomatic in Python for simple cases.")
print("- filter can be convenient when you already have a reusable predicate function or when chaining with map.")
print("- filter returns an iterator in Python 3 (lazy evaluation).")
print()

#%% 7) Common patterns: chaining with map or generator expressions
nums = range(10)
# sum of squares of odd numbers (generator expression idiomatic):
sum_squares = sum(x*x for x in nums if x % 2 == 1)
# using filter+map:
sum_squares_filtermap = sum(map(lambda x: x*x, filter(lambda x: x % 2 == 1, nums)))
print("sum squares odd (genexpr) ->", sum_squares)
print("sum squares odd (filter+map) ->", sum_squares_filtermap)
print()

#%% 8) Quick asserts / sanity checks
def _demo_asserts():
    assert list(filter(is_odd, [1,2,3,4,5])) == [1, 3, 5]
    assert [i**2 for i in [1,4,5,9,10] if is_odd(i)] == [1, 25, 81]
    assert list(filter(None, [0,1,"", "ok"])) == [1, "ok"]
    print("internal demo asserts passed.")

if __name__ == "__main__":
    _demo_asserts()

#%% 9) Documentation examples (solved) - placed last as requested
print("=== Documentation examples (solved) ===")

# Doc example: is_odd + filter
def is_odd_doc(x: int) -> bool:
    return x % 2 == 1

L_doc = [1, 4, 5, 9, 10]
print("list(filter(is_odd_doc, L_doc)) ->", list(filter(is_odd_doc, L_doc)))  # [1,5,9]

# Doc example: comprehension equivalent for squares of odd values
print("[i**2 for i in L_doc if is_odd_doc(i)] ->", [i**2 for i in L_doc if is_odd_doc(i)])  # [1,25,81]

print("Note: filter returns an iterator; convert to list() to see elements.")