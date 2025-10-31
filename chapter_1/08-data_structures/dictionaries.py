#%% dictionaries.py
# Examples and explained snippets for Python dictionaries.

#%% 1) Basic dictionary creation and access
print("=== 1) Basic creation & access ===")
d = {"key1": "value1", "key2": "value2"}
print("d['key1'] ->", d["key1"])
print("d['key2'] ->", d["key2"])
print()

#%% 2) Keys can be different hashable types (tuples ok, lists not)
print("=== 2) Key types & hashability ===")
d2 = {1: "one", "z": 1, (1, 2): "pair"}
print("d2:", d2)
try:
    # lists are not hashable -> using a list as key raises TypeError
    bad = {[1, 2]: "nope"}  # intentional to show TypeError if uncommented
except Exception:
    print("Lists are not hashable and cannot be used as dict keys (example suppressed).")
print()

#%% 3) Alternative constructors
print("=== 3) Alternative constructors ===")
items_list = [("k1", "v1"), ("k2", "v2")]
print("dict(items_list) ->", dict(items_list))
print("dict(k1='v1', k2='v2') ->", dict(k1="v1", k2="v2"))
print()

#%% 4) Assignment with non-existing key adds the key
print("=== 4) Adding keys by assignment ===")
d3 = {}
d3[2] = "value"
print("d3 after d3[2] = 'value' ->", d3)
print()

#%% 5) Non-mutating view methods: copy, items, keys, values, get
print("=== 5) Non-mutating methods & views ===")
d4 = dict(a=1, b=2, c=3)
print("d4:", d4)
print("d4.copy() ->", d4.copy())
print("d4.items() ->", d4.items())
print("d4.keys() ->", d4.keys())
print("d4.values() ->", d4.values())
print("d4.get('a') ->", d4.get("a"))
print("d4.get('nope', 'default') ->", d4.get("nope", "default"))
print()

#%% 6) Mutating methods: clear, update, setdefault, pop, popitem
print("=== 6) Mutating methods ===")
d5 = {"x": 1, "y": 2}
print("start d5:", d5)
d5.update({"z": 3, "x": 10})
print("after update ->", d5)
val = d5.setdefault("k", 99)  # adds key 'k' with 99 if missing
print("after setdefault('k',99) ->", d5, "returned:", val)
p = d5.pop("y")   # removes and returns value for 'y'
print("pop('y') returned", p, "d5 ->", d5)
item = d5.popitem()  # removes and returns an arbitrary (in CPython insertion-order last) pair
print("popitem() returned", item, "d5 ->", d5)
d5.clear()
print("after clear() ->", d5)
print()

#%% 7) Iterating dicts: keys, values, items
print("=== 7) Iteration patterns ===")
d6 = {"name": "alice", "age": 30}
for k in d6:
    print("key:", k)
for k, v in d6.items():
    print("item:", k, v)
print()

#%% 8) Dict comprehensions
print("=== 8) Dict comprehensions ===")
squares = {n: n * n for n in range(5)}
print("squares dict:", squares)
print()

#%% 9) Pitfalls & notes
print("=== 9) Pitfalls & notes ===")
print("- Accessing a missing key with d[key] raises KeyError.")
print("- Use d.get(key, default) to avoid exceptions.")
print("- From Python 3.7 insertion order of keys is preserved (language guarantee from 3.7+).")
print()

#%% 10) Exercises / documentation examples (placed last as requested)
print("=== 10) Documentation examples (solved) ===")

# Doc Example A: basic dict creation & access
print("--- Doc Example A ---")
d = {"key1": "value1", "key2": "value2"}
print(d["key1"])
print(d["key2"])
print()

# Doc Example B: alternative constructors demonstration
print("--- Doc Example B ---")
print("dict([('key1','value1'), ('key2','value2')]) ->", dict([("key1", "value1"), ("key2", "value2")]))
print("dict(key1='value1', key2='value2') ->", dict(key1="value1", key2="value2"))
print()

# Doc Example C: assignment adding a new key
print("--- Doc Example C ---")
d_new = {}
d_new[2] = "value"
print(d_new)   # {2: 'value'}
print()

# Doc Example D: methods lists & values() example
print("--- Doc Example D ---")
d_vals = dict(a=1, b=2, c=3, d=4, e=5)
print("d_vals.values() ->", d_vals.values())  # dict_values([...])
print("list(d_vals.values()) ->", list(d_vals.values()))
print()

# Doc Note: commented example that would raise error
print("--- Doc Note: KeyError example (commented) ---")
print("# d[1]  # This would cause KeyError if uncommented")
print()

#%% 11) Quick demo asserts for exercises
def _demo_checks():
    # A
    dd = {"key1": "value1", "key2": "value2"}
    assert dd["key1"] == "value1" and dd["key2"] == "value2"
    # B
    assert dict([("k1", "v1")]) == {"k1": "v1"}
    # C
    dn = {}
    dn[2] = "value"
    assert dn == {2: "value"}
    # D
    dv = dict(a=1, b=2, c=3, d=4, e=5)
    assert list(dv.values()) == [1, 2, 3, 4, 5]

if __name__ == "__main__":
    _demo_checks()
    print("All dictionary demo asserts passed.")