#%% === What are Statements? ===
print("=== Understanding Statements ===")
print("Statements are commands that have some effect")
print("They DO something, unlike expressions which RETURN something")
print()

#%% === Expression vs Statement Comparison ===
print("=== Expression vs Statement ===")

# EXPRESSIONS (return a value)
result = 5 + 3  # 5 + 3 is an expression (returns 8)
print("Expression: 5 + 3 =", 5 + 3)
print("Expression result stored in variable:", result)

# STATEMENTS (perform an action)
print("This print() is a STATEMENT - it does something (prints text)")
x = 10  # Variable assignment is a STATEMENT
print("x = 10 is a STATEMENT - it assigns value to variable")
print()

#%% === Variable Assignment Statements ===
print("=== Variable Assignment Statements ===")

# Basic assignment
i = 5
print(f"i = {i}")

# Common pattern: increment by 1
i = i + 1  # This is the traditional way
print(f"After i = i + 1: {i}")

# Shorthand for the above (augmented assignment)
i += 1  # Same as i = i + 1
print(f"After i += 1: {i}")

print()
print("Note: Python has NO ++ or -- operators like other languages!")
print("Use += 1 or -= 1 instead")

#%% === Augmented Assignment Operators ===
print("\n=== Augmented Assignment Operators ===")

# Starting values
a = 10
b = 20
c = 3
d = 15
e = 8
f = 100

print("Initial values:")
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}")
print()

# Addition assignment
a += 5  # Same as: a = a + 5
print(f"a += 5  →  a = {a}")

# Subtraction assignment
b -= 3  # Same as: b = b - 3
print(f"b -= 3  →  b = {b}")

# Multiplication assignment
c *= 4  # Same as: c = c * 4
print(f"c *= 4  →  c = {c}")

# Division assignment
d /= 3  # Same as: d = d / 3
print(f"d /= 3  →  d = {d}")

# Integer division assignment
e //= 3  # Same as: e = e // 3
print(f"e //= 3  →  e = {e}")

# Modulus assignment
f %= 7  # Same as: f = f % 7
print(f"f %= 7  →  f = {f}")

# Power assignment
g = 2
g **= 3  # Same as: g = g ** 3
print(f"g **= 3  →  g = {g}")

#%% === String Augmented Assignment ===
print("\n=== String Augmented Assignment ===")

message = "Hello"
print(f"Initial message: '{message}'")

message += " World"  # Same as: message = message + " World"
print(f"After message += ' World': '{message}'")

message *= 2  # Same as: message = message * 2
print(f"After message *= 2: '{message}'")

#%% === List Augmented Assignment ===
print("\n=== List Augmented Assignment ===")

numbers = [1, 2, 3]
print(f"Initial list: {numbers}")

numbers += [4, 5]  # Same as: numbers = numbers + [4, 5]
print(f"After numbers += [4, 5]: {numbers}")

numbers *= 2  # Same as: numbers = numbers * 2
print(f"After numbers *= 2: {numbers}")

#%% === Function Call Statements ===
print("\n=== Function Call Statements ===")

# Function calls can be statements when used for their side effects
print("This print() call is a STATEMENT")

# Importing is also a statement
import math
print("import math is a STATEMENT")

# Method calls can be statements
my_list = [3, 1, 4, 1, 5]
print(f"Original list: {my_list}")
my_list.sort()  # This is a STATEMENT - it modifies the list
print(f"After my_list.sort(): {my_list}")

my_list.append(9)  # Another STATEMENT
print(f"After my_list.append(9): {my_list}")

#%% === Practical Examples ===
print("\n=== Practical Examples ===")

# Counter example
counter = 0
print(f"Counter starts at: {counter}")

counter += 1
print(f"After increment: {counter}")

counter += 5
print(f"After adding 5: {counter}")

counter *= 2
print(f"After doubling: {counter}")

# Accumulator example
total = 0
numbers = [10, 20, 30, 40, 50]

print(f"\nCalculating sum of {numbers}:")
for num in numbers:
    total += num  # Accumulating sum
    print(f"Adding {num}: total = {total}")

print(f"Final total: {total}")

#%% === Advanced Assignment Examples ===
print("\n=== Advanced Assignment Examples ===")

# Multiple assignment (this is also a statement)
x, y, z = 1, 2, 3
print(f"Multiple assignment: x={x}, y={y}, z={z}")

# Swapping variables
print(f"Before swap: x={x}, y={y}")
x, y = y, x  # This is a statement that swaps values
print(f"After swap: x={x}, y={y}")

# Chained assignment
a = b = c = 0  # This is a statement
print(f"Chained assignment: a={a}, b={b}, c={c}")

#%% === Key Differences Summary ===
print("\n=== Key Differences Summary ===")
print("EXPRESSIONS:")
print("  - Return a value")
print("  - Can be used in other expressions")
print("  - Examples: 5 + 3, len(list), x > 5")
print()
print("STATEMENTS:")
print("  - Perform an action")
print("  - Don't return a value (or return None)")
print("  - Examples: x = 5, print('hello'), list.append(item)")
print()
print("AUGMENTED ASSIGNMENT OPERATORS:")
print("  +=  -=  *=  /=  //=  %=  **=")
print("  More concise than: variable = variable operator value")