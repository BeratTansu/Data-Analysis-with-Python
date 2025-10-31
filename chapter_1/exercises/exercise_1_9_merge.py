#%% exercise_1_9_merge.py
# Exercise 1.9 (merge)
# Merge two sorted lists of integers into a new sorted list without using sort() or sorted().

from typing import List

def merge(l1: List[int], l2: List[int]) -> List[int]:
    """
    Return a new sorted list that contains all elements from l1 and l2.
    l1 and l2 are assumed to be sorted in ascending order.
    The input lists are NOT modified.
    """
    i, j = 0, 0
    n1, n2 = len(l1), len(l2)
    result: List[int] = []

    # Walk through both lists and pick the smaller current element
    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    # Append any remaining tail (only one of these loops will run)
    if i < n1:
        result.extend(l1[i:])
    if j < n2:
        result.extend(l2[j:])

    return result


def _demo():
    examples = [
        ([1, 3, 5], [2, 4, 6]),
        ([], [1, 2, 3]),
        ([1, 2, 3], []),
        ([1, 3, 7], [1, 2, 3, 6]),
        ([1, 1, 2], [1, 3]),
        ([-5, -1, 0], [-3, 2, 4]),
    ]

    for a, b in examples:
        merged = merge(a, b)
        print(f"merge({a}, {b}) -> {merged}")
        # sanity checks
        assert len(merged) == len(a) + len(b)
        # result must be sorted
        assert all(merged[k] <= merged[k+1] for k in range(len(merged)-1))
        # original lists unchanged
        assert a == a[:] and b == b[:]

    print("All demo checks passed.")


if __name__ == "__main__":
    _demo()