#%% === What are Expressions? ===
print("=== Understanding Expressions ===")
print("An expression is Python code that results in a value")
print()

#%% === Simple Arithmetic Expressions ===
print("=== Arithmetic Expressions ===")

# Basic math operations
print("1+2 =", 1+2)                    # Addition
print("7/(2+0.1) =", 7/(2+0.1))        # Division with parentheses
print("5*3 =", 5*3)                    # Multiplication
print("10-4 =", 10-4)                  # Subtraction
print("2**3 =", 2**3)                  # Exponentiation (power)
print("15//4 =", 15//4)                # Integer division
print("15%4 =", 15%4)                  # Modulus (remainder)

#%% === Variable Expressions ===
print("\n=== Variable Expressions ===")

a = 5
b = 3
c = 2

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print()

print(f"a + b = {a + b}")
print(f"a * c = {a * c}")
print(f"(a + b) / c = {(a + b) / c}")

#%% === Function Call Expressions ===
print("\n=== Function Call Expressions ===")

import math

# Mathematical functions
print(f"cos(0) = {math.cos(0)}")
print(f"sin(0) = {math.sin(0)}")
print(f"sqrt(16) = {math.sqrt(16)}")
print(f"abs(-5) = {abs(-5)}")
print(f"max(1, 5, 3) = {max(1, 5, 3)}")
print(f"min(1, 5, 3) = {min(1, 5, 3)}")

#%% === List and Indexing Expressions ===
print("\n=== List and Indexing Expressions ===")

mylist = [10, 20, 30, 40, 50]
print(f"mylist = {mylist}")
print(f"mylist[0] = {mylist[0]}")      # First element
print(f"mylist[1] = {mylist[1]}")      # Second element
print(f"mylist[-1] = {mylist[-1]}")    # Last element
print(f"len(mylist) = {len(mylist)}")  # Length of list

#%% === Comparison Expressions ===
print("\n=== Comparison Expressions ===")

x = 10
y = 5

print(f"x = {x}, y = {y}")
print(f"x > y = {x > y}")              # Greater than
print(f"x < y = {x < y}")              # Less than
print(f"x == y = {x == y}")            # Equal to
print(f"x != y = {x != y}")            # Not equal to
print(f"x >= y = {x >= y}")            # Greater than or equal
print(f"x <= y = {x <= y}")            # Less than or equal

#%% === Complex Expressions ===
print("\n=== Complex Expressions ===")

# Combining multiple operations
result1 = (a + b) * c - 1
print(f"(a + b) * c - 1 = ({a} + {b}) * {c} - 1 = {result1}")

# Physics example: kinetic energy = 0.5 * mass * velocity²
mass = 10
velocity = 25
kinetic_energy = 0.5 * mass * velocity**2
print(f"Kinetic Energy = 0.5 * {mass} * {velocity}² = {kinetic_energy}")

#%% === String Expressions ===
print("\n=== String Expressions ===")

first_name = "Berat"
last_name = "Tansu"

# String concatenation expressions
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String methods as expressions
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Length: {len(full_name)}")

#%% === Tuple Expressions ===
print("\n=== Tuple Expressions ===")

coordinates = (1, 2, 3)
print(f"coordinates = {coordinates}")
print(f"x coordinate: {coordinates[0]}")
print(f"y coordinate: {coordinates[1]}")
print(f"z coordinate: {coordinates[2]}")

#%% === Object Attribute Expressions ===
print("\n=== Object Attribute Expressions ===")

# String object attributes and methods
text = "Hello World"
print(f"text = '{text}'")
print(f"text.upper() = '{text.upper()}'")
print(f"text.lower() = '{text.lower()}'")
print(f"text.replace('World', 'Python') = '{text.replace('World', 'Python')}'")

#%% === Boolean Expressions ===
print("\n=== Boolean Expressions ===")

age = 18
has_license = True

print(f"age = {age}")
print(f"has_license = {has_license}")
print(f"age >= 18 = {age >= 18}")
print(f"can_drive = age >= 18 and has_license = {age >= 18 and has_license}")

#%% === Expression Evaluation Order ===
print("\n=== Expression Evaluation Order ===")

# Operator precedence examples
print("2 + 3 * 4 =", 2 + 3 * 4)        # Multiplication first: 2 + 12 = 14
print("(2 + 3) * 4 =", (2 + 3) * 4)    # Parentheses first: 5 * 4 = 20
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)    # Right to left: 2 ** (3 ** 2) = 2 ** 9 = 512
print("(-1)**2 == 1 =", (-1)**2 == 1)  # Parentheses, then power, then comparison