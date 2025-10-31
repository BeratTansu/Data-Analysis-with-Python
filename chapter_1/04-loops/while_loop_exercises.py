#%% Exercise 1
# Problem: Print numbers from 1 to 10 (inclusive) using a while loop.
print("=== Exercise 1: Print 1 to 10 ===")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

#%% Exercise 2
# Problem: Print all even numbers from 2 to 20 (inclusive) using a while loop.
print("=== Exercise 2: Even numbers 2 to 20 ===")
i = 2
while i <= 20:
    if i % 2 == 0:
        print(i)
        i += 2
print()

#%% Exercise 3
# Problem: Calculate factorial of 6 using a while loop.
print("=== Exercise 3: Factorial of 6 ===")
n = 6
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial of {n} is {factorial}")
print()

#%% Exercise 4
# Problem: Sum the digits of a positive integer using a while loop.
print("=== Exercise 4: Sum of digits ===")
num = 12345
orig = num
digit_sum = 0
while num > 0:
    digit = num % 10
    digit_sum += digit
    num //= 10
print(f"Sum of digits of {orig} is {digit_sum}")

#%% Exercise 5
# Problem: Find the smallest power of 2 strictly greater than 1000.
print("=== Exercise 5: Smallest power of 2 > 1000 ===")
power = 1
exponent = 0
limit = 1000
while power <= limit:
    power *= 2
    exponent += 1
print(f"First power of 2 greater than {limit} is 2^{exponent} = {power}")
print()
