#%% sets.py
# Examples for Python sets (creation, common methods, operators, pitfalls).

#%% 1) Basic set creation and uniqueness property
print("=== 1) Basic creation & uniqueness ===")
s = {1, 1, 1}
print("s = {1,1,1} ->", s)   # {1}
s = set([1, 2, 2, 'a'])
print("set([1,2,2,'a']) ->", s)   # {1, 2, 'a'}
s = set()
print("empty set ->", s)
s.add(7)
print("after s.add(7) ->", s)
print()

#%% 2) Useful example: distinct characters in a string
print("=== 2) Distinct characters example ===")
word = "mississippi"
distinct = set(word)
print(f"There are {len(distinct)} distinct characters in {word!r} ->", distinct)
print()

#%% 3) Non-hashable keys caution
print("=== 3) Hashability caution ===")
try:
    bad = { [1,2] }  # will raise TypeError if executed: lists are unhashable
except TypeError:
    print("Lists are not hashable and cannot be members of a set (example suppressed).")
print()

#%% 4) Non-mutating set methods and checks
print("=== 4) Non-mutating methods & checks ===")
s = set([1,2,3])
t = set([2,8,9])
print("s:", s, "t:", t)
print("s.copy() ->", s.copy())
print("s.issubset(t) ->", s.issubset(t))
print("s.issuperset(t) ->", s.issuperset(t))
print("s.union(t) ->", s.union(t))
print("s.intersection(t) ->", s.intersection(t))
print("s.difference(t) ->", s.difference(t))
print("s.symmetric_difference(t) ->", s.symmetric_difference(t))
print()

#%% 5) Operator forms (|, &, -, ^) produce new sets
print("=== 5) Operator forms ===")
s = set([1,2,7])
t = set([2,8,9])
print("s | t (union) ->", s | t)
print("s & t (intersection) ->", s & t)
print("s - t (difference) ->", s - t)
print("s ^ t (symmetric difference) ->", s ^ t)
print()

#%% 6) Mutating methods (add, clear, discard, pop, remove) and augmented operators
print("=== 6) Mutating methods & augmented assignment ===")
s = {1,2,3}
print("start s:", s)
s.add(4)
print("after s.add(4) ->", s)
s.discard(99)   # no error if missing
print("after s.discard(99) ->", s)
try:
    s.remove(99)   # raises KeyError if missing
except KeyError:
    print("s.remove(99) would raise KeyError (example suppressed)")

popped = s.pop()   # removes and returns an arbitrary element
print("s.pop() returned", popped, "s now ->", s)
s.clear()
print("after s.clear() ->", s)

# augmented assignment forms, mutate in-place
s = {1,2}
t = {2,3}
s |= t   # s.update(t)
print("after s |= t ->", s)
s &= {2}  # keep intersection
print("after s &= {2} ->", s)
s ^= {2,5}  # symmetric difference in-place
print("after s ^= {2,5} ->", s)
print()

#%% 7) Common patterns / use-cases
print("=== 7) Common use-cases ===")
# membership test is fast (average O(1))
nums = [1,2,3,2,1]
unique = set(nums)
print("unique from list", nums, "->", unique)
# set for deduping while preserving order: use dict.fromkeys or OrderedDict or seen set pattern
def dedupe_preserve_order(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

print("dedupe_preserve_order on [1,2,1,3] ->", dedupe_preserve_order([1,2,1,3]))
print()

#%% 8) Pitfalls & notes
print("=== 8) Pitfalls & notes ===")
print("- Sets are unordered containers (no guaranteed element order for membership/popping).")
print("- Elements must be hashable (tuples OK, lists/dicts not).")
print("- Use set operations for membership-heavy code and for mathematical set operations.")
print()

#%% 9) Documentation examples (solved) - placed last as requested
print("=== 9) Documentation examples (solved) ===")

# Doc Example 1: simple set creation and add
print("--- Doc Example 1 ---")
s = {1, 1, 1}
print(s)           # {1}
s = set([1,2,2,'a'])
print(s)           # {1, 2, 'a'}
s = set()
print(s)           # set()
s.add(7)
print(s)           # {7}
print()

# Doc Example 2: distinct characters example (mississippi)
print("--- Doc Example 2 ---")
s = "mississippi"
print(f"There are {len(set(s))} distinct characters in {s!r}")
print()

# Doc Example 3: set methods list (non-mutating) demo and operator examples
print("--- Doc Example 3 ---")
s = set([1,2,7])
t = set([2,8,9])
print("Union:", s | t)
print("Intersection:", s & t)
print("Difference:", s - t)
print("Symmetric difference:", s ^ t)
print()

# Doc Example 4: mutating methods (add, clear, discard, pop, remove) note
print("--- Doc Example 4 ---")
s = {1,2,3}
s.add(4)
print("after s.add(4):", s)
s.discard(5)   # safe if not present
print("after s.discard(5):", s)
# remove would raise if missing: example suppressed
print("s.clear() ->", end=" ")
s.clear()
print(s)
print()

#%% 10) Demo asserts (basic checks)
def _demo_checks():
    # dedupe
    assert dedupe_preserve_order([1,2,1,3]) == [1,2,3]
    # operators
    s = {1,2,7}; t = {2,8,9}
    assert (s | t) == {1,2,7,8,9}
    assert (s & t) == {2}
    assert (s - t) == {1,7}
    assert (s ^ t) == {1,7,8,9}
    # distinct chars
    assert len(set("mississippi")) == 4

if __name__ == "__main__":
    _demo_checks()
    print("All set demos/asserts passed.")