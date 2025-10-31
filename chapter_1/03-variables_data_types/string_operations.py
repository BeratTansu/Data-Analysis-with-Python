#%% === Creating Strings ===
print("=== String Creation Examples ===")

# Single quotes
name = 'John'
print("Name with single quotes:", name)

# Double quotes
message = "Hello world"
print("Message with double quotes:", message)

# Quotes inside strings
quote = "I don't want to go"
alternative_quote = 'He said "Hello"'
print("Quote:", quote)
print("Alternative quote:", alternative_quote)

#%% === Escape Sequences ===
print("\n=== Escape Sequences ===")

# Newline and tab
print("One\nTwo\nThree\nFour")
print("Name:\tJohn\tAge:\t25")

# Escaped quotes
escaped = "She said \"I don't know\""
print("Escaped quotes:", escaped)

#%% === Multi-line Strings ===
print("\n=== Multi-line Strings ===")

long_text = """A string
spanning over
several lines"""
print(long_text)

poem = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you!'''
print(poem)

#%% === String Concatenation ===
print("\n=== String Concatenation ===")

# Using + operator
first = "first"
second = "second"
print("With +:", first + second)
print("With + and space:", first + " " + second)

# Using join method (more efficient for multiple strings)
words = [first, second, second, first]
print("With join:", " ".join(words))
print("With join (no space):", "".join(words))
print("With join (comma):", ", ".join(words))

#%% === String Formatting ===
print("\n=== String Formatting ===")

name = "Alice"
age = 25
# f-string (modern way)
print(f"My name is {name} and I am {age} years old")

# .format() method
print("My name is {} and I am {} years old".format(name, age))
print("My name is {0} and I am {1} years old. Yes, {0}!".format(name, age))

#%% === String Interpolation Problems ===
print("\n=== Concatenation Problems ===")

# Clumsy concatenation
print(str(1) + " plus " + str(3) + " is equal to " + str(4))

# Better approach with print function
print(1, "plus", 3, "is equal to", 4)

#%% === String Interpolation Methods ===
print("\n=== String Interpolation Examples ===")

# Variables for examples
a, b, result = 1, 3, 4

# 1. Format syntax (older method)
print("%i plus %i is equal to %i" % (a, b, result))

# 2. .format() method (newer method)
print("{} plus {} is equal to {}".format(a, b, result))

# 3. f-strings (modern and preferred)
print(f"{a} plus {b} is equal to {result}")

#%% === Format Specifiers for Numbers ===
print("\n=== Format Specifiers ===")

# Float formatting examples
x, y, z = 1.6, 1.7, 1.8

# Old style with format specifiers
print("%.1f %.2f %.3f" % (x, y, z))

# .format() method with format specifiers
print("{:.1f} {:.2f} {:.3f}".format(x, y, z))

# f-strings with format specifiers
print(f"{x:.1f} {y:.2f} {z:.3f}")

#%% === Format Specifiers Explanation ===
print("\n=== Format Specifier Details ===")

number = 123.456789

# Different decimal places
print(f"Original: {number}")
print(f"1 decimal: {number:.1f}")
print(f"2 decimals: {number:.2f}")
print(f"3 decimals: {number:.3f}")

# Padding with spaces
print(f"Padded: '{number:10.2f}'")  # 10 characters wide, 2 decimals
print(f"Left padded: '{number:>10.2f}'")
print(f"Right padded: '{number:<10.2f}'")

#%% === String Specifiers ===
print("\n=== String Format Specifiers ===")

fruits = ["water", "melon"]

# String concatenation examples
print("%s concatenated with %s produces %s" % ("water", "melon", "watermelon"))
print("{0} concatenated with {1} produces {0}{1}".format("water", "melon"))
print(f"{'water'} concatenated with {'melon'} produces {'water' + 'melon'}")

# More practical example
fruit1, fruit2 = "water", "melon"
combined = fruit1 + fruit2
print(f"{fruit1} concatenated with {fruit2} produces {combined}")

#%% === Format Comparison ===
print("\n=== Format Method Comparison ===")

name = "Alice"
age = 25
score = 95.7

print("=== Old Style (%) ===")
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

print("\n=== .format() Method ===")
print("Name: {}, Age: {}, Score: {:.1f}".format(name, age, score))
print("Name: {0}, Age: {1}, Score: {2:.1f}".format(name, age, score))

print("\n=== f-strings (Recommended) ===")
print(f"Name: {name}, Age: {age}, Score: {score:.1f}")

#%% === Practical Examples ===
print("\n=== Practical Usage Examples ===")

# Shopping list
item = "apples"
quantity = 5
price = 2.50
total = quantity * price

print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Price per item: ${price:.2f}")
print(f"Total cost: ${total:.2f}")

# Progress report
completed = 75
total_tasks = 100
percentage = (completed / total_tasks) * 100

print(f"\nProgress Report:")
print(f"Completed: {completed}/{total_tasks} tasks")
print(f"Progress: {percentage:.1f}%")