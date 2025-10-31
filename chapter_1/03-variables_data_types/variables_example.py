# Variables and Data Types - Complete Example

print("=== Basic Variable Assignment ===")
a = 1
print("a =", a)
print("Type of a:", type(a))

print("\n=== Dynamic Typing Example ===")
# Variable type can change during runtime
a = "some text"  # Now 'a' is a string
print("a =", a)
print("Type of a:", type(a))

print("\n=== Basic Data Types in Python ===")
# int - Integer numbers
i = 5
print("Integer:", i, "- Type:", type(i))

# float - Decimal numbers
f = 1.5
print("Float:", f, "- Type:", type(f))

# bool - Boolean (True/False)
b = i == 4  # This evaluates to False
print(f"Result of the comparison (i==4): {b}")
print("Boolean:", b, "- Type:", type(b))

# complex - Complex numbers
c = 0+2j  # Note: j denotes the imaginary unit
print("Complex multiplication:", c*c)

# str - String (text)
s = "conca" + "tenation"  # String concatenation
print("String:", s, "- Type:", type(s))

print("\n=== Type Conversion Examples ===")
print("int(-2.8):", int(-2.8))           # Float to int
print("float(2):", float(2))             # Int to float
print("int('123'):", int("123"))         # String to int
print("bool(-2), bool(0):", bool(-2), bool(0))  # Numbers to boolean
print("str(234):", str(234))             # Number to string

print("\n=== Bytes Example ===")
# Convert character(s) to bytes
b = "ä".encode("utf-8")
print("Encoded bytes:", b)               # Prints in hexadecimal
print("Bytes as list:", list(b))         # Prints in decimal

# Convert bytes back to character(s)
decoded = bytes.decode(b, "utf-8")
print("Decoded character:", decoded)

print("\n=== Dynamic Typing vs Static Typing ===")
print("Python uses dynamic typing - variable types can change at runtime")
print("C uses static typing - variable types are fixed at compile time")