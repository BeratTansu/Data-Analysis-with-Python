# Strings: methods, searching, trimming, joining/splitting and common patterns.
# Examples and small demos for string handling.

# 1) Classification predicates (truthy/False for empty strings)
samples = ["abc123", "ABC", "123", "lower", "UPPER", "  ", "Title Case"]
print("samples:", samples)
print("isalnum:", [s.isalnum() for s in samples])
print("isalpha:", [s.isalpha() for s in samples])
print("isdigit:", [s.isdigit() for s in samples])
print("islower:", [s.islower() for s in samples])
print("isupper:", [s.isupper() for s in samples])
print("isspace:", [s.isspace() for s in samples])
print("istitle:", [s.istitle() for s in samples])
print()

# 2) Case transformations (strings are immutable; methods return new strings)
s = "Hello World"
print("original:", s)
print("lower():", s.lower())
print("upper():", s.upper())
print("capitalize():", s.capitalize())
print("title():", s.title())
print("swapcase():", s.swapcase())
print()

# 3) Searching substrings and membership
text = "mississippi"
print("'issi' in text ->", "issi" in text)
print("'issp' in text ->", "issp" in text)
print("count('ss') ->", text.count("ss"))
print("find('sip') ->", text.find("sip"))     # -1 if not found
print("rfind('si') ->", text.rfind("si"))
print("index('sip') ->", end=" ")
try:
    print(text.index("sip"))                  # raises ValueError if not found
except ValueError as e:
    print("ValueError:", e)
print("startswith('mis') ->", text.startswith("mis"))
print("endswith('ppi') ->", text.endswith("ppi"))
print()

# 4) Replace
s2 = "abc-def--ghi"
print("replace('--','-') ->", s2.replace("--", "-"))
print()

# 5) Trimming and adjusting
raw = "   hello  \n"
print("raw repr ->", repr(raw))
print("strip() ->", repr(raw.strip()))
print("lstrip() ->", repr(raw.lstrip()))
print("rstrip() ->", repr(raw.rstrip()))

# Justify/center
line = "star"
print("ljust(10) ->", repr(line.ljust(10)))
print("rjust(10) ->", repr(line.rjust(10)))
print("center(11) ->", repr(line.center(11)))
print()

# 6) Example: build a little ASCII tree using center and repetition
vals = [1, 3, 5, 7, 9, 1]
print("ASCII tree example:")
width = 9
for i in vals:
    s = "*" * i
    print(s.center(width))
print()

# 7) Joining vs repeated concatenation
L = [str(x) for x in range(30)]
# avoid doing: s = ""; for x in L: s += " " + x  (creates many intermediate strings)
joined = " ".join(L)
print("joined first 60 chars ->", joined[:60])
# demonstrate split
parts = "abc--def--ghi".split("--")
print("split('--') ->", parts)
print()

# 8) Performance note (explanation only)
print("Note: use ''.join(list_of_strings) to concatenate many small strings efficiently.")
print()

# 9) Pitfalls & tips
print("Tips:")
print("- Methods like s.index() raise ValueError if not found; s.find() returns -1.")
print("- Use s.get? (not applicable) — for dicts only; for strings use default logic with find or conditional.")
print("- strip() with argument removes characters in the argument (not substring), e.g. 'xxabxx'.strip('x') -> 'ab'.")
print()

# 10) Documentation examples (solved) - concise reproductions
print("=== Documentation examples (solved) ===")
# classification
s_ex = "abc"
print("s_ex.isalpha() ->", s_ex.isalpha())

# substring membership
print("'issi' in 'mississippi' ->", "issi" in "mississippi")

# center demo (small reproduction)
L_demo = [1, 3, 5, 7, 9, 1]
for i in L_demo:
    print(("*" * i).center(9))

# join/split demo
print("'_'.join(['abc','def','ghi']) ->", "_".join(["abc", "def", "ghi"]))
print("'abc--def--ghi'.split('--') ->", "abc--def--ghi".split("--"))