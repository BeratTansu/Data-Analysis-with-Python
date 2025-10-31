#%% Exercise 1
# Problem: Calculate the sum of the list [1, 3, 5, 7, 9] using a for loop.
# Expected output: Sum is 25
from operator import index

print("=== Exercise 1: Sum of [1, 3, 5, 7, 9] ===")
nums = [1, 3, 5, 7, 9]
total = 0
for i in nums:
    total += i
print(f"Sum is {total}")
print()

#%% Exercise 2
# Problem: Count vowels in the string "Programming is fun" using a for loop.
# Expected output (case-insensitive): vowels count = 6  (example)
print("=== Exercise 2: Vowel counter ===")
text = "Programming is fun"
vowels = "aeiou"
count = 0
for ch in text.lower():
    if ch in vowels:
        count += 1
print(f"Text: '{text}'")
print(f"Vowel count: {count}")
print()

#%% Exercise 3
# Problem: Print multiplication table for number 7 from 1 to 10 using a for loop.
# Expected output: "7 x 1 = 7" ... "7 x 10 = 70"
print("=== Exercise 3: Multiplication table for 7 ===")
number = 7

for i in range(1,11):
    print(f"{number} x {i} = {number * i}")
print()

#%% Exercise 4
# Problem: Find the maximum value and its index in the list [23, 45, 12, 67, 34, 89, 15]
# Expected output: Maximum is 89 at index 5
print("=== Exercise 4: Find maximum and index ===")
numbers = [23, 45, 12, 67, 34, 89, 15]

max_val = numbers[0]
max_idx = 0
for idx, val in enumerate(numbers):
    if val > max_val:
        max_val = val
        max_idx = idx
print("Numbers:", numbers)
print(f"Maximum is {max_val} at index {max_idx}")
print()

#%% Exercise 5
# Problem: Build a list of squares for numbers 1 through 10 using a for loop
# Expected output: [1, 4, 9, ..., 100]
print("=== Exercise 5: Build squares list ===")

squares = []
for i in range(1,11):
    squares.append(i*i)
print(f"Squares 1...10: {squares}")
