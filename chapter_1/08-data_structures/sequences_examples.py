#%% sequences_examples.py
# Sequences: lists, tuples, strings - runnable blocks
# Run cells (#%%) independently to inspect each example.

#%% 1) Basic list and tuple examples
print("=== 1) Basic list and tuple examples ===")
lst = [2, 100, "hello", 1.0]
tpl = (1, "hello", 1.0)   # a tuple
singleton = (3,)          # single-element tuple must have trailing comma
print("list:", lst)
print("tuple:", tpl)
print("singleton tuple:", singleton)
print("len(list) =", len(lst), "len(tuple) =", len(tpl))
print()

#%% 2) Indexing (0-based) and negative indices
print("=== 2) Indexing and negative indices ===")
s = "abcdefg"
print("s:", s)
print("s[0] ->", s[0])     # 'a'
print("s[2] ->", s[2])     # 'c'
print("s[-1] ->", s[-1])   # last element 'g'
print("lst[1] ->", lst[1]) # 100
print()

#%% 3) Concatenation (+) and repetition (*)
print("=== 3) Concatenation and repetition ===")
print("[1,2] + [3,4] ->", [1,2] + [3,4])
print("'hi' * 3 ->", "hi" * 3)
print("[1] * 4 ->", [1] * 4)
print()

#%% 4) min, max, sum, and caution with heterogeneous types
print("=== 4) min/max/sum examples and caution ===")
numbers = [4, 2, 8, 1]
print("numbers:", numbers)
print("min(numbers) ->", min(numbers))
print("max(numbers) ->", max(numbers))
print("sum(numbers) ->", sum(numbers))
# mixing types causes errors for min/max in Python 3
mixed = [1, "a"]
print("mixed example (showing why mixing types is bad):", mixed)
try:
    print("min(mixed) ->", min(mixed))
except Exception as e:
    print("  min(mixed) raised:", type(e).__name__, "-", e)
print()

#%% 5) Slicing basics: seq[start:stop], stop excluded
print("=== 5) Slicing basics ===")
s = "abcdefg"
print("s:", s)
print("s[1:4] ->", s[1:4])    # indexes 1,2,3 => 'bcd'
print("s[:3] ->", s[:3])      # 'abc'
print("s[3:] ->", s[3:])      # 'defg'
print("s[:] ->", s[:])        # whole string
print()

#%% 6) Slicing with step: seq[start:stop:step]
print("=== 6) Slicing with step ===")
nums = list(range(10))  # [0,1,2,...,9]
print("nums:", nums)
print("nums[::3] ->", nums[::3])   # every 3rd element -> [0, 3, 6, 9]
print("nums[1::2] ->", nums[1::2]) # odd indices
print("nums[::-1] ->", nums[::-1]) # reversed
print("nums[8:2:-2] ->", nums[8:2:-2]) # start at 8 down to >2 step -2
print()

#%% 7) List mutability vs Tuple immutability
print("=== 7) List mutability vs Tuple immutability ===")
a_list = [1, 2, 3]
a_tuple = (1, 2, 3)
print("before:", a_list, a_tuple)
a_list[0] = 100
print("after modifying list[0]:", a_list)
try:
    a_tuple[0] = 100  # will raise TypeError
except Exception as e:
    print("trying to modify tuple[0] raised:", type(e).__name__, "-", e)
print()

#%% 8) Converting between list and tuple
print("=== 8) Converting between list and tuple ===")
t = (1,2,3)
l = list(t)
l.append(4)
t2 = tuple(l)
print("original tuple:", t)
print("converted to list and back:", t2)
print()

#%% 9) Common idiom: unpacking and swapping
print("=== 9) Unpacking and swapping ===")
x, y, z = (10, 20, 30)
print("x,y,z =", x, y, z)
# swapping
x, y = y, x
print("after swap x,y =", x, y)
# single-element tuple unpacking note
one, = (42,)
print("one =", one)
print()

#%% 10) List comprehensions (quick & pythonic)
print("=== 10) List comprehensions ===")
nums = list(range(10))
squares = [n*n for n in nums if n % 2 == 0]  # squares of even numbers
print("nums:", nums)
print("squares of evens:", squares)
# same with tuple comprehension -> generator then tuple()
tup_squares = tuple(n*n for n in nums if n % 2 == 0)
print("tuple of squares:", tup_squares)
print()

#%% 11) Common pitfalls & tips
print("=== 11) Pitfalls & tips ===")
# 1) Beware aliasing (shallow copy)
orig = [[1], [2]]
alias = orig
alias[0].append(99)
print("orig after modifying alias:", orig)  # shows change because alias references same list
# 2) shallow copy vs deepcopy for nested structures
import copy
shallow = orig.copy()
shallow[0].append(777)
print("orig after shallow copy modification:", orig)  # inner list still shared
deep = copy.deepcopy(orig)
deep[0].append(9999)
print("orig after deepcopy modification:", orig)  # orig unchanged by deep changes
print()

#%% 12) Exercises (try these)
print("=== 12) Exercises ===")
# E1: Given lst = [10, 20, 30, 40], print the last two elements using slicing.
lst = [10, 20, 30, 40]
print(lst[-2:])

# E2: Create tuple t = (1,) and show why t[0] = 2 raises an error.
t = (1,)
print(f"t before {t}")
try:
    t[0] = 2
except Exception as e:
    print(f"Assigning to t[0] raised: {type(e).__name__} - {e}")

# E3: Using list comprehension produce [0,2,4,...,18] from range(10).
result = [2 * n for n in range(10)]
print(result)

# E4: Reverse a string s using slicing.
s = "hello"
rev = s[::-1]
print(rev)

# E5: Given nums = list(range(20)), print every 5th element using slicing.
print("Try the exercises above by editing this file or running small snippets in REPL.")
print()

#%% 13) Quick answer templates for exercises (run these to check)
print("=== 13) Exercise quick checks ===")
lst = [10, 20, 30, 40]
print("E1 expected [30, 40] ->", lst[-2:])  # last two elements
try:
    t = (1,)
    t[0] = 2
except Exception as e:
    print("E2: attempting to assign to tuple element raised:", type(e).__name__)
print("E3 ->", [n*2 for n in range(10)])   # [0,2,4,...,18]
s = "hello"
print("E4 reverse 'hello' ->", s[::-1])
nums = list(range(20))
print("E5 every 5th element ->", nums[::5])  # [0,5,10,15]
print()

#%% 14) Main reminder
def main():
    print("Run individual cells to explore sequences. Modify the examples to test edge cases.")

if __name__ == "__main__":
    main()