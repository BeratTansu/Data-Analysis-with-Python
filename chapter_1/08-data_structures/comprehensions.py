# Compact ways to create data structures: list/dict/set comprehensions and generator expressions.
# Examples and small demos for comprehension patterns and generator usage.
# NOTE: I did not add a "run each cell" comment at the top as requested.

# 1) Simple list comprehensions
squares = [i * i for i in range(10)]
print("squares:", squares)

cubes = [i ** 3 for i in range(1, 11)]
print("cubes 1..10:", cubes)

# with condition
even_squares = [i * i for i in range(20) if i % 2 == 0]
print("even_squares:", even_squares)

# 2) Nested comprehensions (2D -> flattened)
matrix = [[i * 10 + j for j in range(5)] for i in range(3)]
print("matrix rows:", matrix)
flattened = [x for row in matrix for x in row]
print("flattened:", flattened)

# 3) More complicated nested example (from documentation)
numbers = [100 * a + 10 * b + c
           for a in range(10)
           for b in range(10)
           for c in range(10)
           if a <= b <= c]
print("count of numbers where a <= b <= c:", len(numbers))
print("first 20 of numbers:", numbers[:20])

# 4) Generator expression (memory efficient, single-pass)
g = (100 * a + 10 * b + c
     for a in range(10)
     for b in range(10)
     for c in range(10)
     if a <= b <= c)

# consume generator once
total = sum(g)
print("sum of generator elements:", total)
print("sum of generator again (should be 0 because generator is exhausted):", sum(g))

# 5) Dictionary comprehension
d = {k: k ** 2 for k in range(10)}
print("dict comprehension d:", d)

# 6) Set comprehension
s = {i * j for i in range(10) for j in range(10)}
print("set comprehension s (unique products):", sorted(s))

# 7) Conditional expression inside comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print("labels (even/odd):", labels)

# 8) Using comprehensions with functions/calls
def f(x):
    return x * 2

mapped = [f(x) for x in range(6)]
print("mapped via function:", mapped)

# 9) Documentation examples (placed last as requested)
# Example: L = []; for i in range(10): L.append(i**2)  -> list comprehension equivalent:
legacy = []
for i in range(10):
    legacy.append(i ** 2)
print("legacy build:", legacy)
comp_equiv = [i ** 2 for i in range(10)]
print("comprehension equivalent:", comp_equiv)

# Example of a comprehension producing cubes:
cubes_doc = [a ** 3 for a in range(1, 11)]
print("cubes_doc:", cubes_doc)

# Example of set comprehension shown in docs:
set_doc = {i * i for i in range(10)}
print("set_doc:", set_doc)

# Quick notes:
# - Use list comprehensions when you need random access to the whole result.
# - Use generator expressions when you will iterate only once (memory efficient).
# - Nested comprehensions correspond to nested loops; the order of clauses matters.