#%% sorting_sequences.py
# Quick examples for sort() vs sorted(), reverse and key usage.

#%% 1) sort() modifies list in-place
L = [5, 3, 7, 1]
print("original L:", L)
L.sort()
print("after L.sort():", L)   # [1,3,5,7]
print()

#%% 2) sorted() returns a new list, original unchanged
L2 = [6, 1, 7, 3, 6]
print("L2 original:", L2)
print("sorted(L2):", sorted(L2))  # new sorted list
print("L2 after sorted(L2):", L2)  # unchanged
print()

#%% 3) reverse order
L3 = [5, 3, 7, 1]
print("sorted descending:", sorted(L3, reverse=True))
L3.sort(reverse=True)
print("L3 after in-place sort reverse:", L3)
print()

#%% 4) sort with key (case-insensitive & by length)
words = ["apple", "Banana", "cherry", "date"]
print("words:", words)
print("sorted case-insensitive:", sorted(words, key=str.lower))
print("sorted by length:", sorted(words, key=len))
print()

#%% 5) sorting tuples / custom key (by second element)
pairs = [(2, "b"), (1, "aa"), (3, "c"), (1, "b")]
print("pairs:", pairs)
print("sorted by first then second (default):", sorted(pairs))
print("sorted by second element:", sorted(pairs, key=lambda x: x[1]))
print()

#%% 6) stability demo (sort is stable)
data = [(0, 'z'), (1, 'a'), (0, 'y'), (1, 'b')]
print("before:", data)
# sort by first element only - relative order of equal keys is preserved
print("sorted by key=item[0]:", sorted(data, key=lambda x: x[0]))
print()

#%% 7) in-place vs non-mutating patterns (useful idiom)
orig = [3, 1, 2]
sorted_copy = sorted(orig)
orig.sort()  # in-place
print("sorted_copy (non-mutating):", sorted_copy)
print("orig after orig.sort():", orig)
print()

#%% 8) common gotchas: sort on heterogeneous types raises TypeError
mixed = [1, "2", 3]
try:
    sorted(mixed)
except Exception as e:
    print("sorting mixed types raised:", type(e).__name__, "-", e)
print()

#%% 9) Exercises quick (see below for solutions)
# EX1: sort list of dicts by 'age' key: people = [{'name':'a','age':30}, {'name':'b','age':20}]
# EX2: get top 3 largest numbers from a list without modifying original
# EX3: sort strings ignoring accents/case (hint: use locale or .casefold())
print("Exercises: EX1-EX3 (solutions appended in this file)")
print()

#%% 10) Solutions for EX1-EX3 (added into same file as requested)
from typing import List, Dict, Any
import heapq
import unicodedata

def sort_people_by_age(people: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Return a new list of dicts sorted by the 'age' key (ascending).
    Does not modify the original list.
    """
    return sorted(people, key=lambda p: p.get("age", 0))


def top_n_largest(nums: List[float], n: int) -> List[float]:
    """
    Return the top n largest numbers from nums without modifying nums.
    Uses heapq.nlargest for efficiency on large lists.
    If n <= 0 returns [].
    """
    if n <= 0:
        return []
    return heapq.nlargest(n, nums)


def _strip_accents(s: str) -> str:
    """
    Normalize unicode string and remove combining characters (accents).
    """
    normalized = unicodedata.normalize("NFKD", s)
    # Keep only base characters (drop combining marks)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def sort_strings_ignore_accents_case(strings: List[str]) -> List[str]:
    """
    Return a new list of strings sorted in a case-insensitive way and
    ignoring accents (diacritics). Uses .casefold() for stronger case folding.
    """
    return sorted(strings, key=lambda s: _strip_accents(s).casefold())


#%% 11) Demo / quick checks for solutions (run these to verify)
def _demo_solutions():
    print("=== EX1: sort_people_by_age ===")
    people = [{"name": "alice", "age": 30}, {"name": "bob", "age": 20}, {"name": "carol", "age": 25}]
    print("original:", people)
    sorted_people = sort_people_by_age(people)
    print("sorted by age:", sorted_people)
    print("original after sorting (unchanged):", people)
    print()

    print("=== EX2: top_n_largest ===")
    nums = [5, 1, 9, 3, 14, 7]
    print("original:", nums)
    top3 = top_n_largest(nums, 3)
    print("top 3 largest:", top3)
    print("original after top_n_largest (unchanged):", nums)
    print()

    print("=== EX3: sort_strings_ignore_accents_case ===")
    words = ["Ångström", "apple", "Álvaro", "banana", "ångström", "ábaco", "Zoo"]
    print("original:", words)
    sorted_words = sort_strings_ignore_accents_case(words)
    print("sorted ignoring accents and case:", sorted_words)
    print()

# Run demos when module executed directly
if __name__ == "__main__":
    _demo_solutions()