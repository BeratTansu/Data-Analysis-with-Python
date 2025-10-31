# Examples for break and continue (chapter_1 / 04-loops)
from math import sqrt, log

def example_break_loop_else():
    l = [1, 3, 65, 3, -1, 56, -10]
    print("example_break_loop_else:")
    for x in l:
        if x < 0:
            print("  First negative found:", x)
            break
    else:
        print("  No negative numbers in the list.")
    print()

def example_continue_sqrt_log():
    l = [1, 3, 65, 3, -1, 56, -10]
    print("example_continue_sqrt_log:")
    for x in l:
        if x < 0:
            # skip negative values
            continue
        print(f"  Square root of {x} is {sqrt(x):.3f}")
        print(f"  Natural logarithm of {x} is {log(x):.4f}")
    print()

def example_nested_flag():
    # nested loop - break outer using a flag
    print("example_nested_flag:")
    found = False
    for i in range(1, 6):
        for j in range(1, 6):
            if i * j == 12:   # example condition
                print(f"  Found: i={i}, j={j}")
                found = True
                break  # only breaks inner loop
        if found:
            break  # break outer loop as well
    if not found:
        print("  Condition not met.")
    print()

def example_nested_return():
    # Better: use a function and return to exit both loops
    print("example_nested_return:")
    def find_pair():
        for i in range(1, 6):
            for j in range(1, 6):
                if i * j == 12:
                    return (i, j)
        return None
    res = find_pair()
    print("  Result:", res)
    print()

def example_while_continue_trap():
    print("example_while_continue_trap:")
    i = 0
    while i < 10:
        i += 1  # remember to update loop variable (avoid continue trap)
        if i % 2 == 0:
            continue
        print(" ", i)
    print()

def main():
    example_break_loop_else()
    example_continue_sqrt_log()
    example_nested_flag()
    example_nested_return()
    example_while_continue_trap()

if __name__ == "__main__":
    main()