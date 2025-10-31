#%% exercise_1_12_distinct_characters.py
# Exercise 1.12 (distinct characters) - solved

from typing import List, Dict

def distinct_characters(strings: List[str]) -> Dict[str, int]:
    """
    Return a dictionary mapping each string in 'strings' to the number
    of distinct characters it contains.

    Example:
      distinct_characters(["check", "look", "try", "pop"])
      -> {"check": 4, "look": 3, "try": 3, "pop": 2}
    """
    # Using set(s) to get distinct characters for each string.
    # If the same string appears multiple times in the input, the dictionary
    # will simply have one entry for that string (as keys are unique).
    return {s: len(set(s)) for s in strings}


#%% Demo / quick checks
def _demo():
    examples = [
        ["check", "look", "try", "pop"],
        ["", "a", "aa", "ab"],
        ["Mississippi", "mississippi"],  # case-sensitive
    ]

    for ex in examples:
        print("input:", ex)
        print("distinct_characters ->", distinct_characters(ex))
        print()

    # sanity asserts (basic)
    assert distinct_characters(["check", "look", "try", "pop"]) == {"check": 4, "look": 3, "try": 3, "pop": 2}
    assert distinct_characters(["", "a", "aa"]) == {"": 0, "a": 1, "aa": 1}
    assert distinct_characters([]) == {}

if __name__ == "__main__":
    _demo()