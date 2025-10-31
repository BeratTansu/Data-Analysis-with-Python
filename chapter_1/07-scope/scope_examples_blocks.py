#%% scope_examples_blocks.py
# Scope (Visibility of variables) examples in separate runnable blocks.
# Place this file in chapter_1/07-scope and open in PyCharm/VSCode.
# Run each cell (#%%) independently to see focused output.

#%% 1) LEGB basic lookup order demo
print("=== LEGB lookup order demo ===")
x = "module x (global)"

def outer():
    x = "enclosing x"
    def inner():
        x = "local x"
        print("  inside inner:", x)   # local
    inner()
    print("  inside outer after inner:", x)  # enclosing
outer()
print("  at module level:", x)  # global
print()

#%% 2) Reading global vs local assignment (UnboundLocalError demonstration - caught)
print("=== UnboundLocalError demonstration (caught) ===")
count = 10
def buggy_inc():
    try:
        # The following shows the pattern that causes UnboundLocalError:
        # because an assignment (count += 1) makes `count` local in function scope,
        # reading it before assignment triggers UnboundLocalError.
        print("  trying to print count inside buggy_inc (will error):")
        print(count)   # this would error if an assignment below exists
        count += 1     # makes count local -> UnboundLocalError
    except Exception as e:
        print("  Caught exception:", type(e).__name__, "-", e)

buggy_inc()
print("  module count remains:", count)
print()

#%% 3) Correct patterns: return new value or use global
print("=== Correct: return updated value (no global) ===")
counter = 0
def inc_local(c):
    return c + 1

print("  counter before:", counter)
counter = inc_local(counter)
print("  counter after:", counter)
print()

print("=== Using global keyword to modify module variable ===")
g = 0
def inc_global():
    global g
    g += 1

print("  g before:", g)
inc_global()
print("  g after:", g)
print()

#%% 4) nonlocal and closure counter example
print("=== nonlocal + closure demo ===")
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = make_counter()
print("  c() ->", c())
print("  c() ->", c())
print()

#%% 5) Mutable global objects: mutate vs reassign
print("=== Mutable global demo: mutate vs reassign ===")
L = [0]
def mutate():
    # modifies the global list object (no global declaration needed)
    L.append(1)

def reassign_wrong():
    # creates a local L, does not change the module-level L
    L = [9]   # local assignment - shadows global inside function

def reassign_right():
    global L
    L = L + [2]  # reassign using global to update binding

print("  L initial:", L)
mutate()
print("  after mutate():", L)
reassign_wrong()
print("  after reassign_wrong():", L)
reassign_right()
print("  after reassign_right():", L)
print()

#%% 6) Shadowing builtins (safe demo with cleanup)
print("=== Shadowing builtins demo (temporary) ===")
# Caution: shadowing built-ins is possible and may cause confusing errors.
# We deliberately shadow 'len' to show the effect, then delete the name to restore builtin.
len = 5
try:
    print("  trying to call len([1,2,3]) when len is int ->", len([1,2,3]))
except Exception as e:
    print("  Caught error when built-in shadowed:", type(e).__name__, "-", e)
# cleanup: remove our len binding so builtin len works again
del len
print("  builtin len restored:", len([1,2,3]))
print()

#%% 7) Local assignment inside a function does NOT rebind module/global variable
print("=== Local assignment vs global binding demo (image 10, first example) ===")
i = 2  # module-level (global) variable
def f_local():
    i = 3  # this creates a new local variable i inside f_local
    print("  inside f_local:", i)  # prints 3

f_local()
print("  at module level after f_local:", i)  # prints 2 (global i unchanged)
print()

#%% 8) Rebinding a global variable from inside a function using global
print("=== Rebinding global variable using global keyword (image 10, second example) ===")
i = 2  # reset module-level variable
def f_global():
    global i
    i = 5  # rebinds the module-level name i
    print("  inside f_global:", i)  # prints 5

f_global()
print("  at module level after f_global:", i)  # prints 5 (global i updated)
print()

#%% 9) Nested function assignment without nonlocal (image 11 example)
print("=== Nested function: inner assignment creates local in inner (image 11) ===")
def f_nested_local():
    b = 2  # enclosing variable in f_nested_local
    def g():
        b = 3  # creates new local variable b inside g (does NOT affect enclosing b)
        print("  inside g (local b):", b)  # prints 3
    g()
    print("  after g in f_nested_local (enclosing b):", b)  # prints 2

f_nested_local()
print()

#%% 10) Nested function modifying enclosing variable using nonlocal
print("=== Nested function with nonlocal to modify enclosing variable ===")
def f_nested_nonlocal():
    b = 2  # enclosing variable
    def g():
        nonlocal b
        b = 3  # modifies the enclosing b
        print("  inside g (modified enclosing b):", b)  # prints 3
    g()
    print("  after g in f_nested_nonlocal (enclosing b):", b)  # prints 3 (modified)
f_nested_nonlocal()
print()

#%% 11) Example: avoiding mutable default argument pitfall
print("=== Mutable default argument pitfall and safe pattern ===")
def bad_append(value, lst=[]):
    # bad: default list is shared across calls
    lst.append(value)
    return lst

def safe_append(value, lst=None):
    # good: create new list when None
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print("  bad_append(1):", bad_append(1))
print("  bad_append(2):", bad_append(2), "(same list reused -> pitfall)")
print("  safe_append(1):", safe_append(1))
print("  safe_append(2):", safe_append(2), "(separate lists)")
print()

#%% 12) Exercises (run and try to solve)
print("=== Exercises (try these) ===")
# E1: Fix the following function to increment the module-level `m` without using 'global'.
m = 0
def inc_m(value):
    return value + 1

m = inc_m(m)
print(m)

# E2: Create make_accumulator(initial=0) that returns a function add(value) which updates
#     and returns the running total using nonlocal.
def make_accumulator(initial=0):
    total = initial
    def add(v):
        nonlocal total
        total += v
        return total
    return add

acc = make_accumulator(10)
print("  acc(5) ->", acc(5))  # 15
print("  acc(1) ->", acc(1))  # 16
print()

# E3: Explain in one sentence what LEGB stands for and why nonlocal is needed for closures that mutate.
# Solution: Copilot said: LEGB stands for Local, Enclosing, Global, Builtins
# LEGB stands for Local, Enclosing, Global, Builtins — the order Python looks up names;
# nonlocal is required so an inner function can rebind/modify a variable in its enclosing (outer) function scope,
# because without nonlocal an assignment inside the inner function would create a new local name
# (or cause UnboundLocalError when trying to read-before-assign).

#%% 13) Helpers: small tests (asserts) you can run interactively
print("=== Small asserts (safe to run) ===")
# Test length of list unchanged by reassign_wrong
L_test = [0]
def reassign_wrong_test():
    L_test = [9]
reassign_wrong_test()
assert L_test == [0], "reassign_wrong_test should not mutate outer list"

# Test safe_append
assert safe_append(7, None) == [7]
print("  asserts passed (no output means OK)")
print()

#%% 14) Main reminder
def main():
    print("This module is split into runnable cells. Run individual cells to explore scope behaviours.")

if __name__ == "__main__":
    main()