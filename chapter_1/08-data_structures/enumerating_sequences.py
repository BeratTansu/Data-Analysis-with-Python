#%% enumerating_sequences.py
# Examples for enumerate() and related patterns.

#%% 1) Basic enumerate usage
print("=== 1) Basic enumerate ===")
L = ["a", "b", "c"]
for i, x in enumerate(L):
    print(i, x)   # prints index and value (0-based)
print()

#%% 2) enumerate with start parameter (1-based indices)
print("=== 2) enumerate with start=1 ===")
for i, x in enumerate(L, start=1):
    print(i, x)   # indices start from 1
print()

#%% 3) Finding occurrences using enumerate (first index of value)
print("=== 3) Finding first occurrence with enumerate ===")
nums = [3, 5, 1, 5, 9]
target = 5
first_index = None
for i, v in enumerate(nums):
    if v == target:
        first_index = i
        break
print("first index of", target, "->", first_index)
print()

#%% 4) Finding nth occurrence (example: second occurrence)
print("=== 4) Finding nth occurrence (second occurrence example) ===")
def find_nth_occurrence(seq, value, n=1):
    count = 0
    for i, v in enumerate(seq):
        if v == value:
            count += 1
            if count == n:
                return i
    return -1  # not found

nums = [1,2,98,5,-1,2,0,5,10]
print("nums:", nums)
print("index of 2nd occurrence of 5 ->", find_nth_occurrence(nums, 5, 2))  # expected 7
print()

#%% 5) enumerate vs zip(range(len(...)), ...)
print("=== 5) enumerate vs zip(range(len(...)), ...) ===")
L = ["x", "y", "z"]
print("enumerate(L) ->", list(enumerate(L)))
print("zip(range(len(L)), L) ->", list(zip(range(len(L)), L)))
print("They produce equivalent pairs; enumerate is more readable.")
print()

#%% 6) Using enumerate in comprehensions (indices of matches)
print("=== 6) Indices of all matches using list comprehension ===")
vals = [0, 1, 2, 1, 3, 1]
indices_of_1 = [i for i, v in enumerate(vals) if v == 1]
print("vals:", vals)
print("indices of 1 ->", indices_of_1)
print()

#%% 7) Parallel iteration with enumerate and another sequence (offset index)
print("=== 7) Parallel iteration example ===")
names = ["alice", "bob", "carol"]
scores = [90, 85, 99]
for rank, (name, score) in enumerate(zip(names, scores), start=1):
    print(rank, name, score)
print()

#%% 8) Performance / semantics notes
print("=== 8) Notes ===")
print("- enumerate returns an iterator of (index, value) tuples.")
print("- Using enumerate avoids manual index bookkeeping and is Pythonic.")
print("- enumerate works with any iterable, not just lists.")
print()

#%% 9) Exercises / practical checks (documentation examples added last)
print("=== 9) Exercises / practical checks ===")
# E1: get indices where value is even
sample = [4,5,6,7,8]
print("even indices in", sample, "->", [i for i, v in enumerate(sample) if v % 2 == 0])
# E2: find 3rd occurrence of a value (use find_nth_occurrence)
print("3rd occurrence of 1 in [1,1,2,1] ->", find_nth_occurrence([1,1,2,1], 1, 3))
print()

#%% 10) Documentation example (solved) - placed last as requested
print("=== 10) Documentation example (solved) ===")
L = [1, 2, 98, 5, -1, 2, 0, 5, 10]
counter = 0
for i, x in enumerate(L):
    if x == 5:
        counter += 1
        if counter == 2:
            break
print("index of second occurrence of 5 ->", i)  # expected 7
print()

def main():
    print("Run cells to explore enumerate examples. Documentation snippet added as solved at the end.")

if __name__ == "__main__":
    main()