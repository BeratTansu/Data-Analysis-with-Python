#%% === Introduction to Loops ===
print("=== Loops for Repetitive Tasks ===")
print("Python has two main types of loops:")
print("1. while loop - repeats while condition is True")
print("2. for loop - repeats for each item in a sequence")
print()

#%% === While Loop Basics ===
print("=== While Loop Example ===")

# Basic while loop - like in MOOC.fi example
i = 1
while i*i < 1000:
    print(f"Square of {i} is {i*i}")
    i = i + 1
print("Finished printing all the squares below 1000.")
print()

#%% === While Loop Step by Step ===
print("=== How While Loop Works ===")

# Let's trace through a simpler example
counter = 1
print("Starting while loop with counter = 1")

while counter <= 5:
    print(f"  Loop iteration {counter}")
    print(f"  counter before increment: {counter}")
    counter += 1  # Same as counter = counter + 1
    print(f"  counter after increment: {counter}")
    print(f"  Checking condition: {counter} <= 5? {counter <= 5}")
    print()

print("Loop finished!")
print()

#%% === While Loop - Countdown ===
print("=== Countdown Example ===")

countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blast off! 🚀")
print()

#%% === While Loop - User Input ===
print("=== While Loop with User Input ===")

# Example: Keep asking until user enters 'quit'
# (In practice, you would uncomment this)
"""
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
    print(f"You entered: {user_input}")
print("Goodbye!")
"""
print("(User input example commented out for automatic execution)")
print()

#%% === While Loop - Sum Calculation ===
print("=== Calculating Sum with While Loop ===")

# Calculate sum of numbers 1 to 10
total = 0
number = 1

print("Calculating sum of numbers 1 to 10:")
while number <= 10:
    print(f"Adding {number} to total {total}")
    total += number
    number += 1
    print(f"New total: {total}")

print(f"Final sum: {total}")
print()

#%% === While Loop - Finding Squares (MOOC.fi Style) ===
print("=== Finding All Squares Below a Number ===")

limit = 100
i = 1

print(f"All squares below {limit}:")
while i*i < limit:
    square = i*i
    print(f"{i}² = {square}")
    i += 1

print(f"Next square would be {i}² = {i*i}, which is >= {limit}")
print()

#%% === While Loop Common Patterns ===
print("=== Common While Loop Patterns ===")

print("Pattern 1: Counter-based loop")
count = 0
while count < 3:
    print(f"  Iteration {count + 1}")
    count += 1

print("\nPattern 2: Condition-based loop")
value = 1
while value < 10:
    print(f"  Value: {value}")
    value *= 2  # Double the value each time

print("\nPattern 3: Accumulator pattern")
numbers = [1, 2, 3, 4, 5]
index = 0
total = 0
while index < len(numbers):
    total += numbers[index]
    print(f"  Added {numbers[index]}, total now: {total}")
    index += 1

print()

#%% === Infinite Loop Warning ===
print("=== ⚠️ Infinite Loop Warning ===")
print("ALWAYS make sure your while condition will eventually become False!")
print()
print("BAD Example (would run forever):")
print("x = 1")
print("while x > 0:")
print("    print(x)")
print("    x += 1  # x keeps getting bigger!")
print()
print("GOOD Example:")
print("x = 10")
print("while x > 0:")
print("    print(x)")
print("    x -= 1  # x gets smaller and will reach 0")
print()

#%% === Practice Problems ===
print("=== Practice Exercises ===")

print("Exercise 1: Print even numbers from 2 to 20")
num = 2
while num <= 20:
    if num % 2 == 0:  # Check if even
        print(f"Even number: {num}")
    num += 1

print("\nExercise 2: Calculate factorial of 5")
factorial = 1
n = 5
original_n = n

while n > 0:
    factorial *= n
    print(f"factorial = {factorial}, n = {n}")
    n -= 1

print(f"Factorial of {original_n} is {factorial}")
print()

print("Exercise 3: Find first power of 2 greater than 1000")
power_of_2 = 1
exponent = 0

while power_of_2 <= 1000:
    print(f"2^{exponent} = {power_of_2}")
    exponent += 1
    power_of_2 *= 2

print(f"First power of 2 greater than 1000: 2^{exponent-1} = {power_of_2//2}")

#%% === For Loop Basics ===
print("\n" + "="*50)
print("=== FOR LOOPS ===")
print("="*50)
print("For loops repeat for each item in a sequence")
print("Much cleaner than while loops for many tasks!")
print()

#%% === For Loop with List ===
print("=== For Loop with List (MOOC.fi Example) ===")

# MOOC.fi example: sum of numbers
s = 0
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    s = s + i
print("The sum is", s)
print()

#%% === For Loop Step by Step ===
print("=== How For Loop Works ===")

numbers = [1, 2, 3, 4, 5]
total = 0

print(f"List: {numbers}")
print("Step by step:")

for number in numbers:
    print(f"  Current number: {number}")
    print(f"  Total before adding: {total}")
    total += number
    print(f"  Total after adding: {total}")
    print()

print(f"Final total: {total}")
print()

#%% === For Loop with Range ===
print("=== For Loop with Range ===")

print("Using range(5) - numbers from 0 to 4:")
for i in range(5):
    print(f"i = {i}")

print("\nUsing range(1, 6) - numbers from 1 to 5:")
for i in range(1, 6):
    print(f"i = {i}")

print("\nUsing range(0, 10, 2) - even numbers from 0 to 8:")
for i in range(0, 10, 2):
    print(f"i = {i}")
print()

#%% === For Loop with Strings ===
print("=== For Loop with Strings ===")

word = "Python"
print(f"Letters in '{word}':")
for letter in word:
    print(f"  Letter: {letter}")
print()

#%% === Rewriting MOOC.fi Example with Range ===
print("=== Cleaner Version with Range ===")

# Same as MOOC.fi example but cleaner
s = 0
for i in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    s = s + i
    print(f"Added {i}, sum is now {s}")
print("The sum is", s)
print()

#%% === For vs While Comparison ===
print("=== For vs While Comparison ===")

print("WHILE LOOP VERSION:")
i = 1
while i <= 5:
    print(f"Square of {i} is {i*i}")
    i += 1

print("\nFOR LOOP VERSION (much cleaner!):")
for i in range(1, 6):
    print(f"Square of {i} is {i*i}")
print()

#%% === For Loop Patterns ===
print("=== Common For Loop Patterns ===")

print("Pattern 1: Process each item")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\nPattern 2: Accumulate values")
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Total: {total}")

print("\nPattern 3: Count items")
text = "Hello World"
vowel_count = 0
for char in text:
    if char.lower() in "aeiou":
        vowel_count += 1
print(f"Vowels in '{text}': {vowel_count}")

print("\nPattern 4: Build new list")
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num * num)
print(f"Original: {numbers}")
print(f"Squares: {squares}")
print()

#%% === Practical Examples ===
print("=== Practical Examples ===")

print("Example 1: Calculate average")
grades = [85, 92, 78, 96, 88]
total = 0
count = 0
for grade in grades:
    total += grade
    count += 1
average = total / count
print(f"Grades: {grades}")
print(f"Average: {average:.1f}")

print("\nExample 2: Find maximum")
numbers = [23, 45, 12, 67, 34, 89, 15]
maximum = numbers[0]  # Start with first number
for num in numbers:
    if num > maximum:
        maximum = num
print(f"Numbers: {numbers}")
print(f"Maximum: {maximum}")

print("\nExample 3: Multiplication table")
number = 7
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
print()

#%% === Nested Loops ===
print("=== Nested Loops ===")

print("Creating a multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result:2d}", end="  ")
    print()  # New line after each row
print()

#%% === When to Use Which Loop ===
print("=== When to Use Which Loop? ===")
print("USE FOR LOOP when:")
print("  ✅ You know how many times to repeat")
print("  ✅ You're processing items in a list/string")
print("  ✅ You want to repeat a specific number of times")
print()
print("USE WHILE LOOP when:")
print("  ✅ You don't know how many times to repeat")
print("  ✅ You repeat until a condition is met")
print("  ✅ User input scenarios")
print()

#%% === Exercise Solutions ===
print("=== Exercise Solutions ===")

print("Exercise 1: Sum of even numbers from 2 to 20")
total = 0
for num in range(2, 21, 2):  # 2, 4, 6, 8, ..., 20
    total += num
    print(f"Added {num}, total: {total}")
print(f"Sum of even numbers: {total}")

print("\nExercise 2: Countdown using for loop")
for count in range(5, 0, -1):  # 5, 4, 3, 2, 1
    print(f"Countdown: {count}")
print("Blast off! 🚀")

print("\nExercise 3: Character frequency")
text = "programming"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(f"Character frequency in '{text}':")
for char, count in char_count.items():
    print(f"  '{char}': {count}")