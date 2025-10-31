#%% conditionals_basics.py
# Decision making with if / elif / else
# Examples + 5 exercises (with solutions).

#%% === Basic if-else: absolute value ===
print("=== Example: absolute value ===")
x = -5
if x >= 0:
    a = x
else:
    a = -x
print(f"x = {x}, absolute a = {a}")
print()

#%% === if-elif-else: positive/negative/zero ===
print("=== Example: sign of number ===")
c = 0
if c > 0:
    print("c is positive")
elif c < 0:
    print("c is negative")
else:
    print("c is zero")
print()

#%% === Nested/combined conditions: grade example ===
print("=== Example: letter grade from score ===")
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score {score} -> grade {grade}")
print()

#%% === Logical operators and truthiness ===
print("=== Example: age check for ticket discount ===")
age = 17
if age < 18 or age >= 65:
    print("Discount ticket")
else:
    print("Full price ticket")
print()

#%% === Short (ternary) expression ===
print("=== Example: ternary conditional ===")
n = 4
parity = "even" if n % 2 == 0 else "odd"
print(f"{n} is {parity}")
print()

#%% ============================
# Exercises (1..5) with solutions
# Each exercise: problem comment, then solution code (no interactive input).
#%% Exercise 1
# Problem: Given a number, print whether it is even or odd.
print("=== Exercise 1: Even or Odd ===")
num = 23
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
print()

#%% Exercise 2
# Problem: Given three numbers, find and print the maximum using conditionals (no built-ins).
print("=== Exercise 2: Max of three ===")
a, b, c = 12, 7, 12

max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print(f"Numbers: {a}, {b}, {c} -> max is {max_val}")

#%% Exercise 3
# Problem: Check if a given year is a leap year.
# Rule: leap year if divisible by 4, except years divisible by 100 are not leap,
# unless divisible by 400.
print("=== Exercise 3: Leap year check ===")
year = 2000
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
print()

#%% Exercise 4
# Problem: Compute BMI and print category:
# BMI = weight_kg / (height_m ** 2)
# Categories (example): <18.5 underweight, 18.5-24.9 normal, 25-29.9 overweight, >=30 obese
print("=== Exercise 4: BMI category ===")
weight_kg = 82
height_m = 1.78
bmi = weight_kg / (height_m ** 2)
if bmi < 18.5:
    cat = "underweight"
elif bmi < 25:
    cat = "normal weight"
elif bmi < 30:
    cat = "overweight"
else:
    cat = "obese"
print(f"Weight {weight_kg} kg, Height {height_m} m -> BMI {bmi:.1f} -> {cat}")
print()

#%% Exercise 5
# Problem: Simple password strength check (very basic):
# - If length < 6 -> "too short"
# - elif length < 8 -> "weak"
# - elif password has digits and letters -> "good"
# - else -> "medium"
print("=== Exercise 5: Password strength (simple) ===")
password = "abc123XYZ"
pw_len = len(password)
has_digit = any(ch.isdigit() for ch in password)
has_alpha = any(ch.isalpha() for ch in password)

if pw_len < 6:
    strength = "too short"
elif pw_len < 8:
    strength = "weak"
elif has_digit and has_alpha:
    strength = "good"
else:
    strength = "medium"
print(f"Password '{password}' -> {strength}")
print()








