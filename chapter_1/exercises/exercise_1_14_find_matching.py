#%% exercise_1_14_find_matching.py
# Exercise 1.14 (find matching) - solved

from typing import List

def find_matching(strings: List[str], query: str) -> List[int]:
    """
    Return a list of indices of elements in `strings` that contain `query`
    as a substring. Uses enumerate() to obtain indices.

    Example:
      find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
      -> [0, 1, 3]
    """
    if not query:
        # If query is empty, return indices of all strings (every string contains "")
        return list(range(len(strings)))
    return [i for i, s in enumerate(strings) if query in s]


#%% Demo / quick checks
def _demo():
    examples = [
        (["sensitive", "engine", "rubbish", "comment"], "en", [0, 1, 3]),
        (["apple", "banana", "apricot"], "ap", [0, 2]),
        (["a", "b", "c"], "z", []),
        ([], "x", []),
    ]

    for strings, q, expected in examples:
        out = find_matching(strings, q)
        print(f"find_matching({strings!r}, {q!r}) -> {out} (expected {expected})")
        assert out == expected

    # empty query returns all indices
    assert find_matching(["x","y"], "") == [0,1]

    print("All demo asserts passed.")


if __name__ == "__main__":
    _demo()