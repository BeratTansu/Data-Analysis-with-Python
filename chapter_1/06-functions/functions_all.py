# functions_all.py
from math import sqrt, log
from typing import Iterable, Tuple, Optional

#%% Double function + docstring demo
def double(x):
    "This function multiplies its argument by two."
    return x * 2

print("=== double() demo ===")
print("double(4) ->", double(4))
print("double(1.5) ->", double(1.5))
print("double('ab') ->", double("ab"))   # works because string * int repeats
print("docstring:", double.__doc__)
print()

#%% sum_of_squares(a, b)
def sum_of_squares(a, b):
    "Computes a**2 + b**2"
    return a**2 + b**2

print("=== sum_of_squares(a, b) demo ===")
print("sum_of_squares(3, 4) ->", sum_of_squares(3, 4))
print()

#%% sum_of_squares_list(lst) - pass a list as single argument
def sum_of_squares_list(lst):
    "Computes the sum of squares of elements in the list given as parameter"
    s = 0.0
    for x in lst:
        s += x**2
    return s

print("=== sum_of_squares_list(lst) demo ===")
print("sum_of_squares_list([-2]) ->", sum_of_squares_list([-2]))
print("sum_of_squares_list([-2, 4, 5]) ->", sum_of_squares_list([-2, 4, 5]))
print()

#%% sum_of_squares_varargs(*t) - arbitrary positional arguments (packing)
def sum_of_squares_varargs(*t):
    "Computes sum of squares of arbitrary number of positional arguments"
    s = 0.0
    for x in t:
        s += x**2
    return s

print("=== sum_of_squares_varargs(*args) demo ===")
print("sum_of_squares_varargs(-2) ->", sum_of_squares_varargs(-2))
print("sum_of_squares_varargs(-2, 4, 5) ->", sum_of_squares_varargs(-2, 4, 5))
print()

#%% unpacking a list into varargs (call-site unpacking)
print("=== unpacking list into varargs demo ===")
lst = [1, 5, 8]
print("List:", lst)
print("Wrong: passing list as single arg -> sum_of_squares_varargs(lst) ->", end=" ")
try:
    print(sum_of_squares_varargs(lst))  # this treats the whole list as one argument
except Exception as e:
    print("Error:", e)
print("Correct: unpack the list with * -> sum_of_squares_varargs(*lst) ->", sum_of_squares_varargs(*lst))
print()

#%% named (keyword) arguments example
def named(a, b, c):
    "Demonstrates named (keyword) arguments"
    print("First:", a, "Second:", b, "Third:", c)

print("=== named() (keyword args) demo ===")
named(5, c=7, b=8)   # mix of positional and named args
print()

#%% default parameter and **kwargs example
def greet(name, greeting="Hi"):
    "Default parameter example"
    return f"{greeting}, {name}!"

def show_info(**kw):
    "Show keyword packing example"
    for k, v in kw.items():
        print(f"{k} = {v}")

print("=== default args and **kwargs demo ===")
print(greet("Ali"))
print(greet("Veli", "Hello"))
show_info(age=25, city="Istanbul")
print()

#%% print sep and end keyword examples
print("=== print sep & end demo ===")
# Note: these two prints will appear on the same line because first print's end is ' |'
print(1, 2, 3, end=' |', sep=' -*- ')
print(" first ", " second ", " third ", end=' |', sep=' -*- ')
print("\n")  # separate from next outputs
print()

#%% length(*t, degree=2) - p-norm example (degree default 2 -> Euclidean)
def length(*t, degree=2):
    """Compute the p-norm of the vector given as arguments.
       degree=2 -> Euclidean norm.
    """
    if len(t) == 0:
        return 0.0
    s = 0.0
    for x in t:
        s += abs(x) ** degree
    return s ** (1.0 / degree)

print("=== length() p-norm demo ===")
print("length(-4, 3) ->", length(-4, 3))                    # default degree=2
print("length(-4, 3, degree=3) ->", length(-4, 3, degree=3))
print()

#%% sqrt and log processing demo (skip non-positive values)
from math import sqrt, log
print("=== sqrt/log processing demo (skip non-positive values) ===")
values = [1, 3, 65, 3, -1, 56, -10, 0]
for x in values:
    if x <= 0:
        # skip zero and negatives because log(x) is invalid and sqrt for negative is invalid (real)
        continue
    print(f"  sqrt({x}) = {sqrt(x):.3f}, log({x}) = {log(x):.4f}")
print()

#%% docstring and help demo (help commented out for non-interactive runs)
print("=== docstring & help demo ===")
print("double.__doc__ ->", double.__doc__)
# To see full interactive help, uncomment the next line when running interactively:
# help(double)
print()

#%% common pitfalls: mutable default arg warning (example)
print("=== mutable default arg warning demo ===")
def append_to_list(value, lst=None):
    """Safe pattern: avoid mutable default arguments by using None and creating inside."""
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print("First call:", append_to_list(1))
print("Second call:", append_to_list(2))
print("If we had used lst=[] as default, calls would share the same list between calls.")
print()