#%% exercise_1_16_transform.py
# Exercise 1.16 (transform)
# Function `transform` that uses split, map and zip as required.

from typing import List
import operator

def transform(s1: str, s2: str) -> List[int]:
    """
    Given two whitespace-separated number strings s1 and s2, convert them
    to integer lists and return a list where each element is the product
    of the integers at the corresponding positions.

    Uses split(), map() and zip().
    Example:
      transform("1 5 3", "2 6 -1") -> [2, 30, -3]
    """
    # split into substrings, convert to ints using map
    nums1 = list(map(int, s1.split()))
    nums2 = list(map(int, s2.split()))
    # multiply pairwise using map with operator.mul and zip semantics via map over two iterables
    return list(map(operator.mul, nums1, nums2))


# Demo / quick checks
def _demo():
    examples = [
        ("1 5 3", "2 6 -1", [2, 30, -3]),
        ("10 0 -2", "3 4 5", [30, 0, -10]),
        ("1", "2", [2]),
        ("", "", []),  # if empty strings, split() -> [], map->[], zip->[] -> []
    ]

    for a, b, expected in examples:
        out = transform(a, b)
        print(f"transform({a!r}, {b!r}) -> {out}   expected: {expected}")
        assert out == expected

    print("All demo checks passed.")


if __name__ == "__main__":
    _demo()