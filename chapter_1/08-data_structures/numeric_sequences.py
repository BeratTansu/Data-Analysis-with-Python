#%% numeric_sequences.py
# Examples for generating numerical sequences with range()
# Run each cell (#%%) independently to inspect output.

#%% 1) Basic range and iteration
print("=== 1) Basic range and iteration ===")
L = range(3)   # 0,1,2
for i in L:
    print(i)
print("range object:", L)   # shows representation like range(0, 3)
print()

#%% 2) Converting to list and indexing
print("=== 2) Converting to list and indexing ===")
R = range(10)
print("list(range(10)) ->", list(R))
# indexing works (0-based); negative index supported too
print("R[0] ->", R[0])
print("R[-1] ->", R[-1])   # last element
print()

#%% 3) range(start, stop) and step (like slicing)
print("=== 3) range(start, stop) and step ===")
print("list(range(0,7,2)) ->", list(range(0, 7, 2)))  # [0,2,4,6]
print("list(range(1,10,3)) ->", list(range(1, 10, 3))) # [1,4,7]
print()

#%% 4) Negative step and reversed ranges
print("=== 4) Negative step and reversed ===")
print("list(range(10, 0, -1)) ->", list(range(10, 0, -1)))  # 10..1
print("list(range(5, -1, -2)) ->", list(range(5, -1, -2)))  # 5,3,1
# using reversed on a range
r = range(5)
print("list(reversed(r)) ->", list(reversed(r)))  # [4,3,2,1,0]
print()

#%% 5) Memory & performance note
print("=== 5) Memory & performance note ===")
big = range(10_000_000)
print("range object created for 10_000_000 without allocating a list")
print("len(big) =", len(big))
print("first element:", big[0], "last:", big[-1])
# don't do list(big) unless you really need all elements in memory
print()

#%% 6) Useful patterns: enumerate, zip, stepping with slicing-like semantics
print("=== 6) enumerate, zip, and typical patterns ===")
for idx, val in enumerate(range(3, 9)):
    print("index", idx, "->", val)
# parallel iteration with zip(range(...), some_list)
names = ["alice", "bob", "carol"]
for i, name in zip(range(1, 100), names):   # range longer than names, zip stops with shortest
    print(i, name)
print()

#%% 7) Arithmetic sequences and sum
print("=== 7) Arithmetic sequences and sum ===")
# sum of first n natural numbers:
n = 100
print("sum(range(1, n+1)) =", sum(range(1, n+1)))
# sum with step:
print("sum(range(0, 10, 2)) =", sum(range(0, 10, 2)))
print()

#%% 8) Emulating slicing on range with math (indexing still works)
print("=== 8) Emulating slicing semantics on range ===")
r = range(0, 20, 2)   # 0,2,4,...,18
print("r:", list(r))
# you can get subsequence by converting a slice of indices to values, e.g. r[2:6] -> values at positions 2..5
sub = [r[i] for i in range(2, 6)]
print("values at positions 2..5 of r ->", sub)
# but note: r[2:6] is NOT supported directly as slice on range object; instead do list(r)[2:6] or compute formulaically
print("list(r)[2:6] ->", list(r)[2:6])
print()

#%% 9) Exercises (try these) and solutions
print("=== 9) Exercises and solutions ===")
# E1: Create a list of even numbers from 0 to 18 using range.
print("E1 solution:", list(range(0, 20, 2)))  # [0,2,...,18]

# E2: Print numbers 10 down to 1 using range (inclusive).
print("E2 solution:", list(range(10, 0, -1)))  # [10..1]

# E3: Using range, compute the sum of multiples of 3 under 100.
print("E3 solution:", sum(range(0, 100, 3)))

# E4: Using enumerate and range, print index and square of numbers 0..5.
print("E4 solution:")
for i, val in enumerate(range(6)):
    print(i, val*val)

print()

#%% 10) Quick notes and gotchas
print("=== 10) Quick notes & gotchas ===")
# - range returns a sequence-like object (supports len(), indexing, iteration)
# - range objects are immutable (you can't assign to r[0])
# - Slicing syntax (r[1:5]) does not work directly on range objects in older Python versions;
#   safe approaches: list(r)[1:5] or compute values formulaically.
# - If you need repeated conversion to list, store list(range(...)) to avoid repeated allocations.

def main():
    print("This module shows range() usage. Run cells to experiment.")

if __name__ == "__main__":
    main()