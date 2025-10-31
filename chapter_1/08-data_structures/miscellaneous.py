#%% miscellaneous.py
# Miscellaneous sequences & container operations: membership (in), unpacking, del, iteration.

#%% 1) Membership testing with `in` and `not in`
print("=== 1) Membership testing ===")
print("1 in [1,2] ->", 1 in [1, 2])
d = dict(a=1, b=3)
print("'b' in d ->", 'b' in d)           # membership tests keys for dict
s = set()
print("1 in s ->", 1 in s)
print("'x' in 'text' ->", 'x' in "text")
print()

#%% 2) substring membership for strings
print("=== 2) Substring membership ===")
print("'issi' in 'mississippi' ->", "issi" in "mississippi")
print("'issp' in 'mississippi' ->", "issp" in "mississippi")
print()

#%% 3) Unpacking elements of containers into variables
print("=== 3) Unpacking into variables ===")
first, second = [4, 5]
print("first, second = [4,5] ->", first, second)
a, b, c = "bye"
print("a,b,c = 'bye' ->", a, b, c)
print()

#%% 4) Unpacking dictionary keys (and items)
print("=== 4) Unpacking dict keys & iterating items ===")
d = dict(a=1, b=3)
# Unpacking only uses keys
k1, k2 = d
print("unpacked keys k1,k2 from d ->", k1, k2)
# iterate items to get key & value
for key, value in d.items():
    print(f"For key '{key}' value {value} was stored")
print()

#%% 5) Deleting bindings / removing items with del
print("=== 5) del for variables and containers ===")
s = "hello"
print("s initially ->", s)
del s
try:
    print(s)   # this will raise because s was deleted
except Exception as e:
    print("Accessing deleted variable s raised:", type(e).__name__)
# delete element from list
L = [13, 23, 40, 100]
print("L before del L[1] ->", L)
del L[1]
print("L after del L[1] ->", L)
print()

#%% 6) Deleting dict keys and using pop
print("=== 6) Removing dict entries ===")
d2 = {'x': 10, 'y': 20}
print("d2 before:", d2)
del d2['x']
print("d2 after del d2['x'] ->", d2)
# pop returns value
val = d2.pop('y')
print("pop('y') returned", val, "and d2 ->", d2)
print()

#%% 7) Common patterns & notes
print("=== 7) Notes & common patterns ===")
# - `in` on dict checks keys, use `.values()` or `.items()` if you need to test values/items.
# - unpacking requires matching number of targets or use *rest syntax.
# - del removes a name binding (variable) or deletes an item from a container.
# - prefer d.get(k, default) when a key might be missing to avoid KeyError.
print("Example: 'a' in {'a':1}.keys() ->", 'a' in {'a':1}.keys())
print()

#%% 8) Documentation screenshot examples (solved) - placed last as requested
print("=== 8) Documentation screenshot examples (solved) ===")

# Doc snippet: membership examples
print("--- Doc: membership examples ---")
print("1 in [1,2] ->", 1 in [1,2])
d = dict(a=1, b=3)
print("'b' in d ->", 'b' in d)
s = set()
print("1 in s ->", 1 in s)
print("'x' in 'text' ->", 'x' in "text")
print()

# Doc snippet: substring membership
print("--- Doc: substring membership ---")
print("'issi' in 'mississippi' ->", "issi" in "mississippi")
print("'issp' in 'mississippi' ->", "issp" in "mississippi")
print()

# Doc snippet: unpacking and dict items iteration
print("--- Doc: unpacking & dict.items() ---")
first, second = [4,5]
print("first, second = [4,5] ->", first, second)
a,b,c = "bye"
print("a,b,c = 'bye' ->", a, b, c)
d = dict(a=1, b=3)
for key, value in d.items():
    print(f"For key '{key}' value {value} was stored")
print()

# Doc snippet: del examples
print("--- Doc: del examples ---")
L = [13,23,40,100]
print("L before del L[1] ->", L)
del L[1]
print("L after del L[1] ->", L)
d3 = {2: "value"}
print("dict before del d3[2] ->", d3)
del d3[2]
print("dict after del d3[2] ->", d3)
print()

def main():
    print("This module demonstrates membership, unpacking and del usages. Run cells to experiment.")

if __name__ == "__main__":
    main()