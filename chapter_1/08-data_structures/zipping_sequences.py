#%% zipping_sequences_blocks.py
# Examples for zip() and related patterns.

#%% 1) Basic zip() and converting to list
print("=== 1) Basic zip() and converting to list ===")
L1 = [1, 2, 3]
L2 = ["first", "second", "third"]
z = zip(L1, L2)
print("zip(L1, L2) ->", z)              # zip object representation
print("list(zip(L1, L2)) ->", list(z))  # convert zip to list of tuples
print()

#%% 2) Iterating zip directly (zip is an iterator)
print("=== 2) Iterating zip directly ===")
for pair in zip([1,2,3], ["a","b","c"]):
    print(pair)
print()

#%% 3) Zipping three sequences (days, weathers, temperatures) - documentation example
print("=== 3) Zipping three sequences (days, weathers, temperatures) ===")
days = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
weathers = "rainy rainy sunny cloudy rainy sunny sunny".split()
temperatures = [10, 12, 12, 9, 8, 11, 11]

for day, weather, temp in zip(days, weathers, temperatures):
    print(f"On {day} it was {weather} and the temperature was {temp} degrees celsius.")
print()

#%% 4) If sequences differ in length, zip stops at the shortest
print("=== 4) zip stops at the shortest sequence ===")
a = [1,2,3,4]
b = ["x","y"]
print("list(zip(a,b)) ->", list(zip(a,b)))   # pairs only while both have items
print()

#%% 5) Using zip for parallel iteration and common patterns
print("=== 5) Common zip patterns ===")
names = ["alice","bob","carol"]
scores = [85, 92, 78]
# parallel iteration
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
# building dict from two lists
score_map = dict(zip(names, scores))
print("score_map ->", score_map)
print()

#%% 6) zip_longest if you need to keep all elements (fills with a value)
print("=== 6) itertools.zip_longest example (keeps longest) ===")
from itertools import zip_longest
a = [1,2,3]
b = ["a","b"]
print("list(zip_longest(a,b, fillvalue=None)) ->", list(zip_longest(a,b, fillvalue=None)))
print()

#%% 7) Unzipping with zip(*zipped)
print("=== 7) Unzipping example ===")
pairs = [(1,'a'), (2,'b'), (3,'c')]
nums, letters = zip(*pairs)
print("nums ->", nums)
print("letters ->", letters)
print()

#%% 8) Exercises (documentation examples included as solved at the end)
print("=== 8) Exercises / examples (solved) ===")
print("See the bottom of this file for the exact documentation snippets reproduced as solved examples.")
print()

#%% 9) Documentation examples (solved) - placed last as requested
print("=== 9) Documentation examples (solved) ===")

# Doc Example 1: L = [1,2,3]; L2 = ["first","second","third"]; print(zip(L1,L2)); print(list(zip(L1,L2)))
print("--- Doc Example 1 ---")
L1 = [1,2,3]
L2 = ["first","second","third"]
print("zip(L1, L2) ->", zip(L1, L2))          # zip object
print("list(zip(L1, L2)) ->", list(zip(L1, L2)))
print()

# Doc Example 2: days/weathers/temperatures example (produces sentence per day)
print("--- Doc Example 2 ---")
days = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
weathers = "rainy rainy sunny cloudy rainy sunny sunny".split()
temperatures = [10, 12, 12, 9, 8, 11, 11]

for day, weather, temp in zip(days, weathers, temperatures):
    # This reproduces the tutorial's example sentences
    print(f"On {day} it was {weather} and the temperature was {temp} degrees celsius.")
print()

# Doc Note: if sequences are unequal, resulting sequence length equals the shortest input
print("--- Doc Note: unequal-length sequences ---")
print("Example: list(zip(range(5), ['a','b'])) ->", list(zip(range(5), ['a','b'])))
print()

def main():
    print("Run cells to explore zip() examples. Documentation snippets are appended at the end as solved examples.")

if __name__ == "__main__":
    main()