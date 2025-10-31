#%% exercise_1_6_triple_square.py
# Exercise 1.6 (triple & square)
# This file implements:
#  - two simple functions: triple(x) and square(x)
#  - Part 1: loop 1..10 printing triple and square for each i (each function called exactly once per iteration)
#  - Part 2: same loop but stops (break) when square(i) > triple(i) and **does not print** that last iteration

def triple(x):
    """Return x multiplied by three."""
    return x * 3

def square(x):
    """Return x raised to the power of two."""
    return x ** 2

def main_part1():
    """Part 1:
    Iterate i from 1 to 10 and for each i print triple(i) and square(i).
    Ensure each function is called exactly once per iteration by storing results in local variables.
    Expected lines:
      triple(1)==3 square(1)==1
      triple(2)==6 square(2)==4
      ...
    """
    print("=== Part 1: triple and square for i in 1..10 ===")
    for i in range(1, 11):
        t = triple(i)   # call triple exactly once
        s = square(i)   # call square exactly once
        print(f"triple({i})=={t} square({i})=={s}")
    print()

def main_part2():
    """Part 2:
    Iterate i from 1 to 10, compute t=triple(i) and s=square(i) (each called once),
    and stop iterating (break) when s > t, WITHOUT printing anything for that iteration.
    For the usual numeric values this stops at i=4 (since 4^2=16 > 3*4=12), so printed iterations are 1..3.
    """
    print("=== Part 2: stop when square(i) > triple(i) (do not print that iteration) ===")
    for i in range(1, 11):
        t = triple(i)   # call triple exactly once
        s = square(i)   # call square exactly once
        if s > t:
            # stop before printing this iteration
            break
        print(f"triple({i})=={t} square({i})=={s}")
    print()

def main():
    main_part1()
    main_part2()

if __name__ == "__main__":
    main()